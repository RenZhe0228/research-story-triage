# Soil Carbon And Soil Microbiome Profile

Use this profile for soil carbon cycling, soil microbial ecology, metagenomics, MAGs, CAZyme, KEGG, METABOLIC, microbial necromass, priming, microbial carbon use efficiency, SOC stability, carbon fractions, NMR carbon chemistry, enzymes, land-use change, forest/agricultural systems, regional soil carbon simulation, carbon sink assessment, and carbon sequestration enhancement technologies.

## Core Distinctions

- Distinguish SOC stock from SOC concentration.
- Distinguish labile C from recalcitrant C.
- Distinguish chemical recalcitrance from mineral protection.
- Distinguish microbial biomass from microbial necromass.
- Distinguish microbial CUE from genomic or stoichiometric proxies.
- Distinguish gene abundance from expression.
- Distinguish MAG functional potential from realized activity.
- Distinguish a carbon stability metric from actual carbon persistence.
- Distinguish carbon sequestration potential from a verified carbon sink.
- Distinguish site-level association from regional prediction.
- Distinguish incubation potential from field-scale process rate.

## Data Type To Defensible Claim Boundary

| Data type | Defensible claim | Needs before stronger claim | Do not claim |
| --- | --- | --- | --- |
| SOC concentration | SOC concentration differs among samples or treatments. | Bulk density, depth interval, coarse fragment correction, and equivalent soil mass or stock calculation. | Carbon sequestration or carbon sink. |
| SOC stock | SOC stock differs within the measured depth and boundary. | Temporal baseline, persistence, uncertainty, and additionality for sink claims. | Permanent sequestration without duration and uncertainty. |
| Carbon fractions | Fraction distribution or pool proxy differs. | Turnover or persistence evidence for stability claims. | Actual long-term persistence from fraction label alone. |
| NMR carbon chemistry | Chemical composition or aromatic/O-alkyl patterns differ. | Mineral association, turnover, or incubation/field persistence evidence. | Chemical recalcitrance equals ecosystem persistence. |
| Soil enzyme activity | Potential extracellular enzyme activity under assay conditions differs. | Field process rates or flux measurements for ecosystem process claims. | Decomposition rate or SOC loss in the field. |
| MAGs | Genomes encode functional potential and module organization. | Abundance weighting, expression, protein, enzyme, isotope, or process data. | MAGs drive SOC sequestration or active carbon metabolism. |
| CAZyme/KEGG/METABOLIC annotations | Annotated genes/pathways indicate potential capacity. | Expression/activity/flux/process validation. | Active decomposition, flux, or ecosystem function. |
| Microbial biomass | Living microbial pool size differs. | Turnover, necromass, CUE, or process measurements. | Necromass formation or carbon stabilization. |
| Microbial necromass markers | Necromass proxy differs. | Marker validation, soil matrix context, turnover, and contribution to SOC stock. | Complete microbial contribution to stable SOC. |
| CUE proxies | Proxy suggests possible allocation pattern. | Direct CUE method or convergent physiological evidence. | Actual microbial carbon use efficiency. |
| Incubation data | Potential mineralization, priming, or treatment response under lab conditions. | Field validation and scaling assumptions. | Field-scale annual carbon balance. |
| Field survey | Associations across sites or gradients. | Experimental, temporal, or causal identification design. | Drivers, controls, or mechanisms. |
| Machine-learning prediction | Predictors improve estimated performance under validation scheme. | Leakage-free independent validation and interpretability caution. | Predictor importance proves biological control. |
| Regional model | Estimated spatial pattern or scenario under assumptions. | Calibration, independent validation, uncertainty propagation, representativeness. | Proven regional sequestration without uncertainty. |

## Preferred Story Types

### 1. Genome-Resolved Functional Organization

- Minimum data: high-quality MAGs, annotation quality control, module definition, taxonomic placement, abundance or prevalence if claiming ecological relevance.
- Common fatal flaws: treating MAG potential as activity; ignoring MAG completeness/contamination; no abundance weighting.
- Acceptable language: "MAGs encode potential for complex carbon degradation"; "functional modules show redundancy and specialization."
- Unacceptable language: "MAGs drive carbon sequestration"; "METABOLIC-C proves active metabolism."
- Recommended figures: MAG quality/tree, module heatmap, taxon-module architecture, redundancy/specialization, environmental association.
- Validation: abundance weighting, metatranscriptomics, enzyme assays, isotope tracing, or process measurements.

### 2. Taxonomy-Function Decoupling

- Minimum data: taxonomy, functional potential, gradient or treatment, appropriate compositional analysis.
- Common fatal flaws: overinterpreting annotation noise; no test showing different turnover rates.
- Acceptable language: "taxonomic turnover exceeds functional-potential turnover."
- Unacceptable language: "community function is unchanged" without activity or process data.
- Recommended figures: beta diversity contrast, functional distance, gradient response, module stability, bounded interpretation.
- Validation: activity or process data if claiming realized function.

### 3. Soil Carbon Chemistry Linkage

- Minimum data: SOC chemistry or fractions, microbial traits or functional potential, covariates such as pH, texture, climate, vegetation or land-use.
- Common fatal flaws: one weak correlation as mechanism; no confounder control.
- Acceptable language: "microbial trait proxies are associated with SOC chemistry."
- Unacceptable language: "microbial traits control SOC stability."
- Recommended figures: soil chemistry overview, microbial feature architecture, association models, covariate controls, claim-boundary schematic.
- Validation: independent sites, abundance/activity data, enzyme/process assays, or temporal support.

### 4. Carbon Stability Prediction

- Minimum data: stability metric, predictors, leakage-free validation, baseline model, uncertainty.
- Common fatal flaws: feature importance as mechanism; same-site leakage; unclear stability endpoint.
- Acceptable language: "trait-informed models improve prediction under cross-validation."
- Unacceptable language: "the model proves microbial control of SOC stability."
- Recommended figures: endpoint definition, model design, performance comparison, feature contribution, uncertainty.
- Validation: independent validation, sensitivity analysis, ablation, leakage audit.

### 5. Carbon Sink Assessment

- Minimum data: SOC stock, depth, bulk density, temporal baseline, land-use/management boundary, uncertainty.
- Common fatal flaws: SOC concentration only; no baseline; no depth; no uncertainty.
- Acceptable language: "SOC stock increased in the measured depth interval under the sampled conditions."
- Unacceptable language: "carbon sink increased" without stock, persistence, baseline, and uncertainty.
- Recommended figures: sampling boundary, stock calculation, temporal or management contrast, uncertainty, sink-boundary assessment.
- Validation: repeated measurements, equivalent soil mass, persistence, additionality, leakage risk.

### 6. Carbon Enhancement Technology Evaluation

- Minimum data: treatment design, SOC stock or relevant carbon endpoint, baseline, duration, depth, uncertainty, side effects.
- Common fatal flaws: short-term concentration changes as sequestration; no permanence or leakage boundary.
- Acceptable language: "the practice shows sequestration potential under these conditions."
- Unacceptable language: "the treatment increases carbon sink" without full stock and persistence evidence.
- Recommended figures: technology/practice, treatment response, carbon stock/fractions, tradeoffs, implementation boundary.
- Validation: multi-year field data, stock accounting, additionality, permanence, leakage, uncertainty.

### 7. Regional Carbon-Cycle Modeling

- Minimum data: representative soil carbon data, spatial predictors, model validation, uncertainty propagation.
- Common fatal flaws: site-level association extrapolated without representativeness; no independent validation.
- Acceptable language: "regional SOC stock was estimated under the model assumptions."
- Unacceptable language: "regional sequestration is proven" without uncertainty and temporal evidence.
- Recommended figures: data coverage, model workflow, validation, regional map, uncertainty map, scenario comparison.
- Validation: independent validation, sensitivity analysis, spatial uncertainty, boundary definition.

## Claim Boundary Examples

Acceptable:

- "MAGs encode genomic potential for complex carbon degradation."
- "Functional redundancy differs among carbon-related modules."
- "Microbial trait proxies are associated with soil carbon chemistry."
- "This relationship is exploratory and requires abundance weighting or activity data."
- "The model improves prediction under cross-validation, but does not prove mechanism."

Not acceptable:

- "MAGs drive soil carbon sequestration."
- "METABOLIC-C proves active carbon metabolism."
- "CAZyme abundance proves decomposition rate."
- "Microbial traits control SOC stability."
- "The treatment increases carbon sink without SOC stock and persistence evidence."
- "Regional carbon sequestration is proven without uncertainty propagation."
