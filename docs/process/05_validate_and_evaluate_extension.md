Process-ID: 4
Parent-Process: 0
Type: process

# 4. Validate and Evaluate the BPMN Extension

## Relation to the BPMN Extension Process

This document details subprocess 4 of the BPMN Extension Process.

This subprocess is executed after the BPMN extension has been developed.

Previous subprocess:
- `03_develop_bpmn_extension.md`

Input:
- BPMN extension developed.
- Extension specification [Developed].

Output:
- Extension specification [Validated/evaluated].
- BPMN extension evaluated.

Next subprocess:
- `07_publicise_bpmn_extension.md`

Related process:
- `00_bpmn_extension_process_overview.md`

Use this process to validate and evaluate the BPMN extension through practical usage, expert review and evaluation activities.

## Objective

Validate and evaluate the BPMN extension through practical usage, expert feedback and formal evaluation activities.

The expected final outcome is:

- **Extension specification [Validated/evaluated]**
- **BPMN extension evaluated**

## Validation and Evaluation Strategy

This subprocess validates the BPMN extension through three complementary activities:

1. Practical usage of the extension in realistic modelling scenarios.

2. Review by BPMN extension experts and, when applicable,
   domain experts.

3. Formal evaluation through experiments, case studies
   or surveys.

The BPMN-BOT should guide the Extender through all
validation activities and register every identified
improvement.

## Participants

- Extender
- BPMN extension experts
- Domain experts, when required
- Evaluation participants, when applicable

## Inputs

- BPMN extension developed.
- Extension specification [Developed].
- Modelling tool for the extension, when available.
- Example models or case studies.

## Supporting Artifacts Used in this Subprocess

The following artifacts are created, updated or consulted:

- Extension specification [Developed]
- List of experts in BPMN extensions
- Checklist for verification of problems
- Usage Example
- Expert Review Results
- Evaluation results
- Identified improvements
- Extension specification [Validated/evaluated]

## Instructions

### 4.1 Use the BPMN Extension Proposed to Model a System

Apply the BPMN extension to one or more realistic modelling scenarios.

The BPMN-BOT should encourage the use of non-trivial and real-world examples.

Document:

- modelling steps;
- modelling decisions;
- identified limitations;
- usability observations;
- improvement opportunities.

Decision:

Were corrections/improvements identified?

- Yes → continue to step 4.2.
- No → continue to step 4.3.

### 4.2 Apply Corrections/Improvements From Usage

Apply corrections identified during practical usage.

The BPMN-BOT should update the extension specification and record:

- corrected concepts;
- corrected syntax;
- corrected metamodel elements;
- identified issues.

After corrections are applied, continue to step 4.3.

### 4.3 Consult Experts

Submit the BPMN extension for expert review.

Experts may include:

- BPMN extension experts;
- BPMN practitioners;
- domain specialists;
- researchers from related application areas.

Collect:

- comments;
- suggestions;
- criticisms;
- improvement proposals.

Decision:

Are there corrections/improvements suggested?

- Yes → continue to step 4.4.
- No → continue to evaluation decision.

### 4.4 Apply Corrections/Improvements From Experts

Apply expert recommendations.

The BPMN-BOT should ensure that modifications do not introduce:

- inconsistencies;
- incompleteness;
- conflicts.

After corrections are applied, continue to the evaluation decision.

### Evaluation Decision

Evaluate the extension?

- Yes → continue to step 4.5.
- No → continue to step 4.7.

### 4.5 Evaluate the BPMN Extension

Evaluation may be performed using:

- Controlled Experiment;
- Case Study;
- Survey.

The BPMN-BOT should help select the most suitable method according to:

- available participants;
- research objectives;
- available time;
- extension maturity.

Record:

- evaluation method;
- participants;
- results;
- identified strengths;
- identified weaknesses.

Decision:

Are there improvements of the BPMN extension defined?

- Yes → continue to step 4.6.
- No → continue to step 4.7.

### 4.6 Apply Improvements From Evaluation

Apply the improvements identified during evaluation.

Update:

- extension concepts;
- metamodel;
- syntax;
- documentation;
- examples.

After improvements are applied, continue to step 4.7.

### 4.7 Generate Extension Specification [Validated/Evaluated]

Generate the final validated version of the BPMN extension specification.

Include:

- usage examples;
- expert feedback;
- evaluation results;
- applied improvements;
- final observations.

Output:

- Extension Specification [Validated/Evaluated]
- BPMN Extension Evaluated



## BPMN-BOT Validation States

| State | Process Step | Bot Action | Artifact Updated |
|---------|---------|---------|---------|
| `4.1_use_extension` | Use BPMN extension to model a system | Collect modelling examples and observations | Usage Example |
| `4.2_apply_usage_corrections` | Apply improvements from usage | Record corrections and update extension | Extension Specification [Developed] |
| `4.3_consult_experts` | Consult experts | Collect expert feedback | Expert Review Results |
| `4.4_apply_expert_corrections` | Apply expert suggestions | Update extension after review | Extension Specification [Developed] |
| `4.5_evaluate_extension` | Evaluate BPMN extension | Guide evaluation planning and execution | Evaluation Results |
| `4.6_apply_evaluation_improvements` | Apply improvements from evaluation | Update extension after evaluation | Extension Specification [Developed] |
| `4.7_generate_validated_specification` | Generate final validated specification | Produce validated artefact | Extension Specification [Validated/Evaluated] |

## Guidance for BPMN-BOT

When supporting this subprocess, BPMN-BOT should act as a validation facilitator.

The BPMN-BOT should:

- guide the Extender through the execution of real modelling examples;
- record modelling observations and identified limitations;
- register corrections discovered during practical usage;
- collect and organise expert feedback;
- distinguish between expert suggestions and evaluation findings;
- help select an evaluation strategy (experiment, case study or survey);
- register evaluation results;
- identify improvement opportunities;
- update the Extension Specification [Validated/Evaluated];
- indicate the current validation stage and the next expected activity.

The BPMN-BOT should help answer questions such as:

1. Which modelling scenarios should be used?
2. Were limitations identified during usage?
3. Which experts should be consulted?
4. Which expert recommendations should be incorporated?
5. Is an evaluation feasible within the project constraints?
6. Which evaluation method is most appropriate?
7. What improvements were identified?
8. Is the extension ready to be considered validated?
9. What information must be included in the validated specification?

## Decision Summary

Use the following decision rules:

- If practical usage identifies issues, apply corrections.
- If experts suggest improvements, apply them.
- If evaluation is feasible, perform an evaluation.
- If evaluation identifies improvements, apply them.
- Generate the validated specification only after all identified improvements have been addressed.

## Expected Outputs

- Usage Example
- Expert Review Results
- Evaluation Results
- Identified Improvements
- Extension Specification [Validated/Evaluated]
- BPMN Extension Evaluated

## Transition to the Next Subprocess

After this subprocess is completed, continue to:

`05_check_new_constructs.md`

Any new concepts identified during validation and evaluation should be recorded and considered in the next iteration of the BPMN extension process.