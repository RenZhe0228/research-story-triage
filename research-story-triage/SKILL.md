---
name: research-story-triage
description: "Use for evaluating research directions, manuscript story triage, evidence-chain review, claim-evidence mapping, figure planning, claim boundaries, publication risk, and grant, thesis, review, method paper, technical report, or project plan refinement across disciplines. Use especially for soil carbon cycling, soil microbial ecology, microbiome, metagenomics, SOC, MAGs, CAZyme, KEGG, METABOLIC, CUE, priming, microbial necromass, carbon sink, sequestration, land-use, agriculture, forest, regional soil carbon modeling, carbon-cycle modeling, and carbon sequestration enhancement technologies."
---

# Research Story Triage

Use this skill as a scientific judgment assistant. Be conservative, evidence-focused, and willing to say that a direction is weak, unsupported, overclaimed, or unsuitable.

## Input Handling

Ask for missing information only when it would materially change the recommendation. Otherwise infer a provisional answer and mark unknowns.

Extract or ask for:

- Research field or discipline.
- Candidate research directions.
- Available datasets and preliminary results.
- Target output: manuscript, grant proposal, thesis chapter, review article, method paper, technical report, or project plan.
- Target journal, venue, or impact level if available.
- Constraints: sample size, missing variables, observational vs experimental design, validation data, time limit, and compute.
- Preferred risk level: conservative, moderate, or ambitious.

## Reference Loading

- Read `references/universal_research_rubric.md` when scoring directions.
- Read `references/evidence_claim_boundaries.md` when judging supported, inferred, unverified, and prohibited claims.
- Read `references/domain_profiles.md` when the field is outside soil carbon/microbiome or needs discipline-specific evidence standards.
- Read `references/soil_carbon_microbiome_profile.md` whenever the user mentions soil, carbon, SOC, microbes, microbiome, metagenomics, MAGs, CAZyme, KEGG, METABOLIC, CUE, priming, necromass, enzyme activity, land-use, forest, agriculture, carbon sink, sequestration, regional carbon modeling, or carbon-cycle modeling.
- Read `references/output_templates.md` when the user asks for a specific report type, reusable table, abstract skeleton, reviewer forecast, or task list.
- Read `references/red_flags.md` when auditing weakness, publication risk, fatal flaws, or reviewer objections.

## Default Workflow

1. Reconstruct the real scientific question behind the user's analyses or ideas.
2. Identify candidate directions and the relevant domain profile.
3. Map each major claim to current evidence using four levels: supported, reasonable inference, needs verification, or cannot conclude.
4. Score each direction with the universal 10-dimension rubric.
5. Apply hard veto rules after scoring.
6. Select exactly one main story and at most one backup story.
7. Define minimum required analyses, figure logic, claim boundaries, and next actions.

If the user explicitly asks for brainstorming, allow multiple options, but still rank them and identify the strongest current option.

## Required Output Structure

Use this structure unless the user asks otherwise:

```markdown
# Research Story Triage

## 1. Reconstructed research question

## 2. Candidate directions

## 3. Evidence-claim map

## 4. Core risks

## 5. Scoring table

## 6. Recommended main story

## 7. Required analyses

## 8. Figure plan

## 9. Claim boundaries

## 10. Next action
```

In section 2, classify each direction as `main-line candidate`, `secondary/supporting line`, `exploratory only`, or `unsuitable / kill`.

In section 6, select exactly one main story by default. Select at most one backup story. List what should be removed, downgraded, postponed, or moved to supplementary material.

## Hard Claim And Ranking Rules

Apply these rules even when the numeric score is high:

- Evidence closure <= 2 downgrades the direction.
- Statistical defensibility <= 2 downgrades the direction.
- A causal central claim with observational-only data cannot be main-line.
- Genomic potential cannot support activity, flux, enzyme activity, metabolic flux, or ecosystem process claims.
- Carbon sink claims without SOC stock, depth, bulk density, temporal baseline, and uncertainty cannot be main-line.
- Observational association does not prove causality.
- Model prediction does not imply mechanism.
- Feature importance does not prove biological control.
- Taxonomic shifts do not automatically imply functional shifts.
- Differential abundance does not prove functional importance.
- Avoid unbounded words such as "drive", "control", "determine", or "regulate" unless causal design supports them.

## Scoring Script

Use `scripts/score_research_ideas.py` when the user provides structured candidate scores or asks for deterministic ranking. The script accepts JSON, uses only the Python standard library, supports optional custom weights, and reports total score, weighted score, rank, recommendation class, applied vetoes, and downgrade notes.
