# Output Templates

Use these templates when the user asks for a specific deliverable. Preserve conservative claim boundaries.

## Usage Examples Inside Skill Package

Example prompts:

```text
I have three possible manuscript directions. Help me choose the strongest one.
```

```text
Evaluate whether this soil carbon microbiome story is strong enough for a manuscript.
```

```text
Turn these preliminary results into a claim-evidence map and figure plan.
```

```text
I have SOC, pH, climate, MAG, CAZyme, and METABOLIC results. What is the defensible main story?
```

```text
Review this abstract and mark unsupported claims.
```

## 1. Idea Triage Report

```markdown
# Research Story Triage

## 1. Reconstructed research question
[One or two sentences.]

## 2. Candidate directions
| Direction | Classification | Rationale |
| --- | --- | --- |

## 3. Evidence-claim map
| Claim | Evidence | Level | Boundary |
| --- | --- | --- | --- |

## 4. Core risks
[Methodological, statistical, conceptual, publication risks.]

## 5. Scoring table
| Direction | Q clarity | Novelty | Evidence | Method | Stats | Causality | Mechanism | Figures | Fit | Feasible | Class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 6. Recommended main story
[Exactly one main story, at most one backup, and what to remove.]

## 7. Required analyses
[Minimum defensible analyses.]

## 8. Figure plan
[4-7 figures and what each must prove.]

## 9. Claim boundaries
[May say, may cautiously infer, must not say.]

## 10. Next action
[Short practical plan.]
```

## 2. Manuscript Results Architecture

```markdown
1. Establish the system, dataset, and scientific contrast.
2. Show the primary pattern or response.
3. Test whether the evidence supports the central claim.
4. Add mechanism only if directly supported or clearly framed as inference.
5. Validate, benchmark, or bound the result.
6. End with the defensible implication, not the largest possible claim.
```

## 3. Figure Plan

```markdown
| Figure | Role | What it must prove | Required data | Claim boundary |
| --- | --- | --- | --- | --- |
| Fig. 1 | Study system and question | The contrast is clear and data are sufficient. |  |  |
| Fig. 2 | Primary result | The main pattern exists. |  |  |
| Fig. 3 | Evidence closure | The central claim is directly tested. |  |  |
| Fig. 4 | Mechanistic or explanatory layer | Mechanism is supported or bounded. |  |  |
| Fig. 5 | Validation/robustness | Result is not an artifact. |  |  |
| Fig. 6 | Synthesis or implication | The final claim is proportional. |  |  |
```

## 4. Claim-Evidence Table

```markdown
| Proposed claim | Current evidence | Evidence level | Allowed wording | Required verification |
| --- | --- | --- | --- | --- |
```

Evidence levels: supported by current evidence, reasonable inference, needs verification, cannot be concluded.

## 5. Fatal Flaw Checklist

```markdown
- [ ] Central question is testable.
- [ ] Central claim is directly supported.
- [ ] Sample size and replication match the analysis.
- [ ] Causal wording is justified or removed.
- [ ] Validation is independent or leakage-free.
- [ ] Figure sequence proves one coherent story.
- [ ] Title and abstract do not exceed evidence.
```

## 6. Reviewer Objection Forecast

```markdown
| Likely objection | Why it matters | Severity | Preemptive fix |
| --- | --- | --- | --- |
```

## 7. Minimal Analysis Plan

```markdown
1. Define the central claim in one sentence.
2. Identify the smallest analysis that directly tests it.
3. Add covariates or controls required to avoid obvious confounding.
4. Add validation or sensitivity checks.
5. Remove analyses that do not support the main story.
```

## 8. Conservative Abstract Skeleton

```markdown
[Context]. However, [specific uncertainty] remains unresolved. Here we used [data/design] to test whether [bounded question]. We found that [directly supported result]. [Reasonable inference with cautious wording]. These results suggest [bounded implication] and identify [specific next verification need].
```

## 9. Ambitious But Bounded Abstract Skeleton

```markdown
[Field-level problem]. A key barrier is [specific gap]. We integrate [data streams] to evaluate [central question]. Our results show [strongest supported result], while [mechanistic or predictive claim] is supported only as [evidence level]. This framework provides [contribution] without claiming [unsupported stronger conclusion].
```

## 10. Codex Analysis Task List

```markdown
- Reconstruct the scientific question.
- Extract candidate directions.
- Build a claim-evidence table.
- Score each direction with the universal rubric.
- Apply veto rules.
- Select one main story and one optional backup.
- Draft required analyses.
- Draft a 4-7 figure plan.
- Rewrite claim boundaries.
- List the next three actions.
```

## Behavioral Smoke Test

Prompt:

```text
Use $research-story-triage. I have SOC concentration, pH, climate variables, metagenomic MAGs, CAZyme annotations, KEGG modules, and METABOLIC outputs from forest and agricultural soils across 24 sites. I want to claim that MAGs drive soil carbon sequestration and that land-use change increased the regional carbon sink. There are no bulk density data, no depth-resolved SOC stock, no temporal baseline, no metatranscriptomics, and no enzyme assays. Possible stories: MAG carbon degradation modules, taxonomy-function decoupling, microbial predictors of SOC chemistry, and regional carbon sink enhancement. What is the defensible main story?
```

Pass criteria:

- Output includes all 10 required sections.
- Exactly one main story is selected by default.
- "MAGs drive soil carbon sequestration" is marked cannot be concluded.
- Regional carbon sink enhancement is not main-line because SOC stock, depth, bulk density, temporal baseline, and uncertainty are missing.
- The likely main story is bounded toward genome-resolved functional organization, taxonomy-function decoupling, or microbial predictors of SOC chemistry, depending on the detailed evidence.
