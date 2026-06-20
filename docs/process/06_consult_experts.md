Process-ID: 4.3
Parent-Process: 4
Type: subprocess

# 4.3 Consult Experts

## Relation to the BPMN Extension Process

This document details subprocess 4.3 of
`05_validate_and_evaluate_extension.md`.

This subprocess is executed during the validation and evaluation phase of the BPMN extension.

Parent subprocess:
- 04_validate_and_evaluate_extension.md

Parent activity:
- 4.3 Consult experts

Input:
- BPMN extension developed
- Extension specification [Developed]

Output:
- BPMN extension validated by experts

Next step:
- Return to step 4.4 of
  `04_validate_and_evaluate_extension.md`

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

### 4.3.1 Consult Experts in BPMN Extensions

Identify BPMN extension experts.

Use:

- artifact_list_of_bpmn_extension_experts.md

Send:

- Extension Specification [Developed]
- example models
- identified issues
- specific questions

Collect:

- recommendations
- corrections
- observations

### 4.3.2 Consult Experts in Domain/Application Area

Only execute this path when the extension is related to a specific domain or application area.

Examples:

- Security
- Healthcare
- IoT
- Robotics

Use:

- references identified during subprocess 1

Collect:

- missing concepts
- domain inconsistencies
- terminology corrections
- practical observations

### 4.3.3 BPMN Experts Analyse the Extension

Experts analyse:

- construct definitions
- BPMN integration
- syntax
- metamodel
- validation rules

Output:

- BPMN expert feedback

### 4.3.4 Domain Experts Analyse the Extension

Experts analyse:

- domain correctness
- concept completeness
- practical applicability

Output:

- domain expert feedback

### 4.3.5 Receive Feedback from BPMN Experts

Review all received feedback.

Record:

- expert
- recommendation
- impacted construct
- action taken

### 4.3.6 Receive Feedback from Domain Experts

Review all received feedback.

Record:

- expert
- recommendation
- impacted concept
- action taken

## Guidance for BPMN-BOT

The BPMN-BOT should act as a facilitator for expert review.

The BPMN-BOT should:

- identify the appropriate expert type;
- determine whether domain experts are required;
- prepare information to be sent to experts;
- organise received feedback;
- distinguish BPMN feedback from domain feedback;
- register expert recommendations;
- identify impacted constructs;
- prepare feedback summaries for subprocess 4.

## Decision Summary

Use the following decision rules:

- If the extension targets a specific application domain, consult domain experts.
- BPMN extension experts should always be consulted when available.
- All expert recommendations should be documented.
- Expert feedback should be analysed before continuing to subprocess 4.4.
- Lack of expert response should not block the process.

## Expected Outputs

- BPMN expert feedback.
- Domain expert feedback.
- Expert consultation records.
- List of recommendations.
- Identified corrections and improvements.
- BPMN extension validated by experts.