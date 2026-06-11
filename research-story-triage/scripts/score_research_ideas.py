#!/usr/bin/env python3
"""Score and rank research story candidates using the research-story-triage rubric.

Input JSON example:
{
  "candidates": [
    {
      "name": "Microbial predictors of SOC chemistry",
      "scores": {"question_clarity": 4, "novelty_boundary": 3, ...},
      "metadata": {
        "design": "observational",
        "central_claim_type": "associational",
        "claim_basis": ["genomic_potential"],
        "claim_targets": ["SOC chemistry"]
      }
    }
  ],
  "weights": {"evidence_closure": 1.5}
}
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


DIMENSIONS = [
    "question_clarity",
    "novelty_boundary",
    "evidence_closure",
    "method_fit",
    "statistical_defensibility",
    "causality_risk",
    "mechanistic_depth",
    "figure_continuity",
    "publication_fit",
    "execution_feasibility",
]

CLASSES = [
    "main-line candidate",
    "secondary/supporting line",
    "exploratory only",
    "unsuitable / kill",
]

DEFAULT_WEIGHTS = {dimension: 1.0 for dimension in DIMENSIONS}
CARBON_SINK_REQUIRED = ["soc_stock", "depth", "bulk_density", "baseline", "uncertainty"]


def load_json(path: str) -> Any:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Input file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}")


def as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y"}
    return bool(value)


def normalize_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip().lower() for item in value]
    return [str(value).strip().lower()]


def merged_metadata(candidate: Dict[str, Any]) -> Dict[str, Any]:
    metadata = {}
    if isinstance(candidate.get("metadata"), dict):
        metadata.update(candidate["metadata"])
    for key, value in candidate.items():
        if key not in {"name", "scores", "metadata"}:
            metadata.setdefault(key, value)
    return metadata


def validate_scores(candidate: Dict[str, Any]) -> Dict[str, float]:
    name = str(candidate.get("name", "<unnamed>"))
    scores = candidate.get("scores")
    if not isinstance(scores, dict):
        raise SystemExit(f"Candidate '{name}' must contain a scores object")

    normalized: Dict[str, float] = {}
    missing = [dimension for dimension in DIMENSIONS if dimension not in scores]
    if missing:
        raise SystemExit(f"Candidate '{name}' is missing scores: {', '.join(missing)}")

    for dimension in DIMENSIONS:
        value = scores[dimension]
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise SystemExit(f"Candidate '{name}' score '{dimension}' must be numeric")
        if value < 1 or value > 5:
            raise SystemExit(f"Candidate '{name}' score '{dimension}' must be between 1 and 5")
        normalized[dimension] = float(value)
    return normalized


def normalize_weights(raw_weights: Any) -> Dict[str, float]:
    weights = dict(DEFAULT_WEIGHTS)
    if raw_weights is None:
        return weights
    if not isinstance(raw_weights, dict):
        raise SystemExit("Weights must be a JSON object")
    for dimension, value in raw_weights.items():
        if dimension not in DIMENSIONS:
            raise SystemExit(f"Unknown weight dimension: {dimension}")
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
            raise SystemExit(f"Weight for '{dimension}' must be a positive number")
        weights[dimension] = float(value)
    return weights


def class_from_score(weighted_average: float) -> str:
    if weighted_average >= 4.0:
        return CLASSES[0]
    if weighted_average >= 3.2:
        return CLASSES[1]
    if weighted_average >= 2.4:
        return CLASSES[2]
    return CLASSES[3]


def downgrade(recommendation: str, steps: int = 1) -> str:
    index = CLASSES.index(recommendation)
    return CLASSES[min(index + steps, len(CLASSES) - 1)]


def cap_at(recommendation: str, cap: str) -> str:
    return CLASSES[max(CLASSES.index(recommendation), CLASSES.index(cap))]


def contains_any(values: Iterable[str], needles: Iterable[str]) -> bool:
    haystack = " | ".join(values).lower()
    return any(needle in haystack for needle in needles)


def is_observational_only(metadata: Dict[str, Any]) -> bool:
    if as_bool(metadata.get("observational_only")):
        return True
    design = " ".join(normalize_list(metadata.get("design")))
    return "observational" in design and not any(term in design for term in ["experiment", "random", "perturb"])


def has_causal_central_claim(metadata: Dict[str, Any]) -> bool:
    if as_bool(metadata.get("causal_central_claim")):
        return True
    claim_type = " ".join(normalize_list(metadata.get("central_claim_type")))
    central_claim = " ".join(normalize_list(metadata.get("central_claim")))
    return "causal" in claim_type or contains_any([central_claim], ["drive", "control", "determine", "regulate"])


def uses_genomic_potential_for_activity(metadata: Dict[str, Any]) -> bool:
    if as_bool(metadata.get("genomic_potential_claims_activity")):
        return True
    basis = normalize_list(metadata.get("claim_basis")) + normalize_list(metadata.get("evidence_basis"))
    targets = normalize_list(metadata.get("claim_targets")) + normalize_list(metadata.get("claimed_outcomes"))
    genomic_basis = contains_any(basis, ["genomic potential", "mags", "mag", "cazyme", "kegg", "metabolic"])
    active_target = contains_any(targets, ["activity", "flux", "process", "enzyme", "ecosystem", "rate", "metabolism"])
    return genomic_basis and active_target


def carbon_sink_missing(metadata: Dict[str, Any]) -> Tuple[bool, List[str]]:
    claim_text = " ".join(
        normalize_list(metadata.get("central_claim"))
        + normalize_list(metadata.get("claim_type"))
        + normalize_list(metadata.get("claim_targets"))
    )
    is_claim = as_bool(metadata.get("carbon_sink_claim")) or contains_any(
        [claim_text], ["carbon sink", "sequestration", "carbon sequestration"]
    )
    if not is_claim:
        return False, []

    evidence = metadata.get("carbon_sink_evidence", {})
    if not isinstance(evidence, dict):
        evidence = {}
    aliases = {
        "baseline": ["baseline", "temporal_baseline", "time_baseline"],
        "soc_stock": ["soc_stock", "stock", "carbon_stock"],
        "depth": ["depth", "depth_interval", "soil_depth"],
        "bulk_density": ["bulk_density", "bd"],
        "uncertainty": ["uncertainty", "uncertainty_propagation", "confidence_interval"],
    }
    missing = []
    for required in CARBON_SINK_REQUIRED:
        keys = aliases[required]
        present = any(as_bool(evidence.get(key)) or as_bool(metadata.get(key)) for key in keys)
        if not present:
            missing.append(required)
    return bool(missing), missing


def apply_vetoes(scores: Dict[str, float], metadata: Dict[str, Any], recommendation: str) -> Tuple[str, List[str], List[str]]:
    vetoes: List[str] = []
    notes: List[str] = []

    if scores["evidence_closure"] <= 2:
        recommendation = downgrade(recommendation)
        vetoes.append("evidence_closure_le_2")
        notes.append("Evidence closure <= 2 downgraded the direction.")

    if scores["statistical_defensibility"] <= 2:
        recommendation = downgrade(recommendation)
        vetoes.append("statistical_defensibility_le_2")
        notes.append("Statistical defensibility <= 2 downgraded the direction.")

    if has_causal_central_claim(metadata) and is_observational_only(metadata):
        capped = cap_at(recommendation, "secondary/supporting line")
        if capped != recommendation:
            notes.append("Causal central claim with observational-only data cannot be main-line.")
        recommendation = capped
        vetoes.append("causal_claim_observational_only")

    if uses_genomic_potential_for_activity(metadata):
        capped = cap_at(recommendation, "secondary/supporting line")
        if capped != recommendation:
            notes.append("Genomic potential cannot support activity, flux, or ecosystem process claims.")
        recommendation = capped
        vetoes.append("genomic_potential_activity_or_process_claim")

    missing_carbon, missing_fields = carbon_sink_missing(metadata)
    if missing_carbon:
        capped = cap_at(recommendation, "secondary/supporting line")
        if capped != recommendation:
            notes.append("Carbon sink claim lacks required stock/depth/bulk density/baseline/uncertainty evidence.")
        recommendation = capped
        vetoes.append("carbon_sink_missing_" + "_".join(missing_fields))

    return recommendation, vetoes, notes


def score_candidate(candidate: Dict[str, Any], weights: Dict[str, float]) -> Dict[str, Any]:
    name = str(candidate.get("name", "<unnamed>"))
    scores = validate_scores(candidate)
    total_score = sum(scores.values())
    weight_total = sum(weights.values())
    weighted_score = sum(scores[dimension] * weights[dimension] for dimension in DIMENSIONS) / weight_total
    initial_class = class_from_score(weighted_score)
    final_class, vetoes, notes = apply_vetoes(scores, merged_metadata(candidate), initial_class)

    return {
        "name": name,
        "total_score": round(total_score, 3),
        "weighted_score": round(weighted_score, 3),
        "initial_recommendation_class": initial_class,
        "recommendation_class": final_class,
        "applied_vetoes": vetoes,
        "downgrade_notes": notes,
        "scores": scores,
    }


def load_candidates(data: Any) -> List[Dict[str, Any]]:
    if isinstance(data, list):
        candidates = data
    elif isinstance(data, dict):
        candidates = data.get("candidates", data.get("directions"))
    else:
        candidates = None
    if not isinstance(candidates, list) or not candidates:
        raise SystemExit("Input must contain a non-empty 'candidates' or 'directions' list")
    for candidate in candidates:
        if not isinstance(candidate, dict):
            raise SystemExit("Each candidate must be a JSON object")
    return candidates


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score research story candidates.")
    parser.add_argument("input_json", help="Path to candidate JSON file")
    parser.add_argument("--weights", help="Optional path to weights JSON file")
    args = parser.parse_args(argv)

    data = load_json(args.input_json)
    input_weights = data.get("weights") if isinstance(data, dict) else None
    weights = normalize_weights(input_weights)
    if args.weights:
        weights.update(normalize_weights(load_json(args.weights)))

    results = [score_candidate(candidate, weights) for candidate in load_candidates(data)]
    results.sort(key=lambda item: (CLASSES.index(item["recommendation_class"]), -item["weighted_score"], item["name"]))
    for index, result in enumerate(results, start=1):
        result["rank"] = index

    output = {
        "rubric_dimensions": DIMENSIONS,
        "weights": weights,
        "results": results,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        raise SystemExit(1)
