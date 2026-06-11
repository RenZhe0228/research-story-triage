# Research Story Triage

Cross-disciplinary research story triage skill for evaluating scientific questions, evidence chains, figure logic, and claim boundaries, with a specialized profile for soil carbon cycling and soil microbiome research.

## What This Skill Does

`research-story-triage` helps researchers turn vague ideas, preliminary results, datasets, and manuscript fragments into a disciplined assessment of:

- The actual scientific question.
- Whether the evidence chain supports the claim.
- Which claims are supported, inferred, unverified, or not allowed.
- Which direction should become the main manuscript story.
- Which analyses, figures, and validations are required next.
- What should be killed, downgraded, or moved to supplementary material.

It is designed as a scientific judgment assistant, not a writing assistant first.

## Who It Is For

Use it for researchers, graduate students, PIs, and analysts who need to choose among competing research directions, audit manuscript logic, plan figures, prepare grant or thesis chapters, or avoid overclaiming.

The skill is general across disciplines and includes a specialized profile for soil carbon cycling, soil microbial ecology, metagenomics, MAGs, CAZyme, KEGG, METABOLIC, microbial necromass, CUE, priming, SOC stability, regional soil carbon modeling, carbon sink assessment, and carbon sequestration enhancement technologies.

## How To Use

Upload or install the `research-story-triage` skill folder or `research-story-triage.zip`, then invoke:

```text
Use $research-story-triage to evaluate these candidate research directions.
```

For deterministic ranking from pre-scored candidates, run:

```bash
python research-story-triage/scripts/score_research_ideas.py candidates.json
```

Custom weights are optional:

```bash
python research-story-triage/scripts/score_research_ideas.py candidates.json --weights weights.json
```

## Example Prompts

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

## Output Example

The default response contains ten sections:

1. Reconstructed research question
2. Candidate directions
3. Evidence-claim map
4. Core risks
5. Scoring table
6. Recommended main story
7. Required analyses
8. Figure plan
9. Claim boundaries
10. Next action

The skill selects exactly one main story by default, with at most one backup story. Brainstorming requests may produce multiple options, but they are still ranked and the strongest option is identified.

## Limitations

- The skill does not replace domain expert review.
- The scoring script ranks user-provided scores; it does not infer scores from raw manuscripts.
- Bibliographic novelty claims still require literature review.
- Causal, mechanistic, and carbon sink claims are deliberately conservative.
- Soil carbon sequestration claims require SOC stock, depth, bulk density, temporal baseline, persistence, and uncertainty.

## GitHub Description

Cross-disciplinary research story triage skill for evaluating scientific questions, evidence chains, figure logic, and claim boundaries, with a specialized profile for soil carbon cycling and soil microbiome research.

## 支持作者

如果这个 Skill 对你有帮助，欢迎 Star，也欢迎打赏支持后续更新。

| 微信打赏 | 支付宝打赏 |
|---|---|
| <img src="./assets/wechat-reward.jpg" width="220" alt="微信收款码"> | <img src="./assets/alipay-reward.jpg" width="220" alt="支付宝收款码"> |
