Process-ID: 4.3
Parent-Process: 05
Type: subprocess

# 4.3 Consult Experts

## Relation to the BPMN Extension Process

This document details subprocess 4.3 of
`05_validate_and_evaluate_extension.md`.

This subprocess is executed during the validation and evaluation phase of the BPMN extension.

Parent subprocess:
- 05_validate_and_evaluate_extension.md

Parent activity:
- 4.3 Consult experts

Input:
- BPMN extension developed
- Extension specification [Developed]

Output:
- BPMN extension validated by experts

Next step:
- Return to step 4.4 of
  `05_validate_and_evaluate_extension.md`

Related process:
- 00_bpmn_extension_process_overview.md

## Objective

Collect expert feedback about the BPMN extension proposal in order to identify problems, inconsistencies, missing constructs, modelling issues and improvement opportunities before the formal evaluation.

The expected final outcome is:

- BPMN extension validated by experts.

## Participants

- Extender
- Experts in BPMN extensions
- Experts in the domain/application area

## Inputs

- BPMN extension developed.
- Extension specification [Developed].
- List of experts in BPMN extensions.
- Checklist for verification of problems.
- Models or scenarios used to apply the BPMN extension.

## Supporting Artifacts Used in this Subprocess

The following artifacts are created, updated or consulted:

- Extension specification [Developed]
- Application area
- Practical aspects
- List of experts in BPMN extensions
- Feedback given
- BPMN extension validated by experts

## Instructions

### 4.1 Use the BPMN Extension Proposed to Model a System

Apply the developed BPMN extension to model a representative system, process, or scenario.

Use this activity to verify whether the extension can be used in practice.

During modelling, observe:

- whether all proposed constructs can be used;
- whether the concrete syntax is understandable;
- whether the extension concepts are clear;
- whether the metamodel and validation rules are sufficient;
- whether the extension supports the intended modelling need;
- whether any construct is missing, redundant, ambiguous, or hard to use;
- whether the extension creates conflicts with BPMN semantics.

Decision: **Were corrections/improvements identified?**

- **Yes**: apply corrections or improvements from usage and continue to step 4.2.
- **No**: continue to expert consultation in step 4.3.

### 4.2 Apply Corrections/Improvements From the Usage

Apply the corrections and improvements identified while modelling a system with the BPMN extension.

Corrections may include:

- adjusting concept definitions;
- changing concrete syntax;
- refining metamodel elements;
- updating validation rules;
- removing unnecessary constructs;
- adding missing constraints;
- improving examples;
- correcting conflicts with BPMN constructs.

After applying the corrections, update the **Extension specification [Developed]** and continue to expert consultation.

### 4.3 Consult Experts

Consult BPMN extension experts to review the developed extension.

Send the experts:

- Extension specification [Developed];
- modelled system or example models;
- list of corrections/improvements already applied from usage;
- checklist for verification of problems;
- specific questions about completeness, consistency, conflicts, and suitability.

Ask experts to verify:

- whether the extension is complete;
- whether it is consistent with BPMN;
- whether the concrete syntax is adequate;
- whether validation rules are sufficient;
- whether there are semantic conflicts;
- whether the extension should be improved before evaluation.

Decision: **Are there corrections/improvements suggested?**

- **Yes**: apply the corrections/improvements from the experts and continue to step 4.4.
- **No**: decide whether the extension should be evaluated and continue toward step 4.5 or step 4.7.

### 4.4 Apply the Corrections/Improvements From the Experts

Apply the corrections and improvements suggested by BPMN extension experts.

Use the **checklist for verification of problems** to ensure that each expert recommendation is evaluated and addressed.

For each suggestion, register:

- expert source;
- issue or improvement suggested;
- affected extension construct;
- decision taken;
- change applied;
- justification if the suggestion is not applied.

Update the developed specification before deciding whether to evaluate the extension.

Decision: **Evaluate the extension?**

- **Yes**: continue to step 4.5.
- **No**: continue to step 4.7 and generate the validated/evaluated specification with the current evidence.

### 4.5 Evaluate the BPMN Extension

Evaluate the BPMN extension using the selected evaluation method.

The evaluation may include:

- expert review;
- modelling experiment;
- case study;
- comparison with standard BPMN;
- comparison with related BPMN extensions;
- quality assessment;
- usability assessment;
- completeness, consistency, and conflict analysis.

During evaluation, verify:

- whether the extension satisfies its purpose;
- whether it improves modelling expressiveness;
- whether it remains compatible with BPMN;
- whether users can understand and apply it;
- whether the extension specification is sufficiently complete;
- whether the extension introduces modelling problems.

Decision: **Are there improvements of the BPMN extensions defined?**

- **Yes**: apply the improvements from the evaluation and continue to step 4.6.
- **No**: continue to step 4.7.

### 4.6 Apply the Improvements From the Evaluation

Apply all improvements identified during evaluation.

Improvements may include:

- revising extension concepts;
- changing concrete syntax;
- improving validation rules;
- updating examples;
- refining the metamodel;
- improving tool support;
- clarifying documentation;
- resolving problems found during evaluation.

After applying the improvements, update the extension specification and continue to step 4.7.

### 4.7 Generate Extension Specification [Validated/Evaluated]

Generate the final specification for this process.

The specification must include:

- original developed extension specification;
- models or scenarios used to validate the extension;
- corrections/improvements from usage;
- expert consultation results;
- corrections/improvements from experts;
- evaluation method;
- evaluation results;
- improvements from evaluation;
- final checklist for verification of problems;
- evidence that the extension is validated/evaluated.

The output of this step is **Extension specification [Validated/evaluated]**.

When this output is complete, the process ends with **BPMN extension evaluated**.

## Guidance for BPMN-BOT

When supporting this subprocess, BPMN-BOT should help answer questions such as:

1. Which BPMN extension experts should be consulted?
2. Which domain experts should be consulted?
3. What information should be sent to experts?
4. Which practical aspects should be analysed?
5. How should expert feedback be documented?
6. How should conflicting expert opinions be handled?
7. Which recommendations should be incorporated into the extension?
8. Has the BPMN extension been sufficiently validated by experts?

## Decision Summary

Use the following decision rules:

- If usage identifies corrections or improvements, apply them before expert consultation.
- If experts suggest corrections or improvements, apply or justify each decision before evaluation.
- If the extension should be evaluated, perform the evaluation and incorporate the resulting improvements.
- If evaluation identifies no improvements, proceed to the validated/evaluated specification.
- The BPMN extension is considered evaluated only after the validated/evaluated specification is generated.

## Expected Outputs

- System or scenario modelled with the BPMN extension.
- Corrections/improvements from usage.
- List of experts in BPMN extensions.
- Expert consultation results.
- Checklist for verification of problems.
- Corrections/improvements from experts.
- Evaluation results.
- Improvements from evaluation.
- Extension specification [Validated/evaluated].
- Final decision that the BPMN extension is evaluated.
