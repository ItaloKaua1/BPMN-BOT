Artifact-Type: process-output

Artifact-ID: extension-specification-validated-evaluated

Produced-By:

* 05_validate_and_evaluate_extension.md

Used-By:

* 06_consult_experts.md
* 07_publicise_bpmn_extension.md

Related-Process:

* 00_bpmn_extension_process_overview.md

# Artifact: Extension Specification [Validated and Evaluated]

## Purpose

This artifact records the validation and evaluation results of a BPMN extension.

It is produced during:

`05_validate_and_evaluate_extension.md`

The objective is to verify whether the developed BPMN extension:

* solves the intended problem;
* represents the target domain adequately;
* remains consistent with BPMN;
* can be understood by users;
* can be applied in realistic modelling scenarios.

## Source Artifact

This artifact is generated from:

`artifact_extension_specification_developed.md`

The developed extension is evaluated through practical application and quality assessment.

## Validation Objectives

The validation process should verify:

* conceptual correctness;
* BPMN compliance;
* modelling usefulness;
* completeness;
* consistency;
* usability;
* absence of conflicts.

## Required Sections

1. Validation Overview.
2. Validation Scenario.
3. Application of the Extension.
4. Evaluation Criteria.
5. Evaluation Results.
6. Identified Issues.
7. Improvement Recommendations.
8. Validation Decision.

---

# 1. Validation Overview

Describe:

* extension name;
* validation objective;
* validation scope;
* evaluated version;
* evaluation date.

## Example Questions

* Does the extension solve the intended problem?
* Can users understand the constructs?
* Is BPMN compatibility preserved?

---

# 2. Validation Scenario

Describe the scenario used during evaluation.

Include:

* domain/application area;
* process being modelled;
* stakeholders involved;
* modelling objectives.

The scenario should be representative of the extension domain.

## BPMN-BOT Guidance

Ask the user:

* Which process will be modelled?
* Why is this process representative?
* Which extension constructs will be exercised?

---

# 3. Application of the Extension

Describe how the extension was used.

Include:

* BPMN model produced;
* extension constructs applied;
* modelling decisions;
* examples of usage.

### Recorded Information

| Construct | Usage Description |
| --------- | ----------------- |

Attach diagrams when available.

---

# 4. Evaluation Criteria

Assess the extension according to predefined criteria.

Suggested criteria:

| Criterion          | Description                                |
| ------------------ | ------------------------------------------ |
| Correctness        | Constructs represent the intended concepts |
| Completeness       | All required concepts are represented      |
| Consistency        | No contradictions between constructs       |
| BPMN Compatibility | BPMN semantics are preserved               |
| Usability          | Easy to understand and use                 |
| Simplicity         | Limited additional complexity              |
| Reusability        | Applicable in similar scenarios            |

Additional criteria may be included when necessary.

---

# 5. Evaluation Results

Document the results obtained.

For each criterion register:

| Criterion | Result | Evidence |
| --------- | ------ | -------- |

Possible results:

* Satisfied
* Partially Satisfied
* Not Satisfied

Evidence should be linked to observations made during modelling.

---

# 6. Identified Issues

Register problems discovered during validation.

For each issue provide:

| Issue ID | Description | Severity | Related Construct |
| -------- | ----------- | -------- | ----------------- |

Possible severities:

* Low
* Medium
* High

Examples:

* Ambiguous graphical notation.
* Missing validation rule.
* Conflicting semantics.
* BPMN compatibility problem.

---

# 7. Improvement Recommendations

List improvements suggested during evaluation.

For each recommendation provide:

| Recommendation ID | Description | Priority |
| ----------------- | ----------- | -------- |

Possible priorities:

* Low
* Medium
* High

Recommendations should be actionable.

---

# 8. Validation Decision

Record the final decision.

Possible outcomes:

### Approved

The extension is considered suitable for publication and expert review.

### Approved with Revisions

The extension is acceptable but requires improvements.

### Rejected

Major problems prevent adoption.

Include justification for the decision.

---

# BPMN-BOT Guidance

When assisting users during validation, BPMN-BOT should:

1. Verify whether all extension constructs were exercised.
2. Check BPMN compatibility.
3. Identify inconsistencies.
4. Identify missing concepts.
5. Suggest evaluation criteria.
6. Suggest improvements.
7. Support preparation for expert review.

The assistant should never assume validation was successful without evidence.

---

# Expected Output

At the end of this artifact the following should exist:

* validation scenario;
* evaluation criteria;
* evaluation evidence;
* identified issues;
* improvement recommendations;
* validation decision.

These results become inputs for expert consultation and publication activities.

---

# Transition to the Next Process

After validation is completed, continue to:

`06_consult_experts.md`

The validated extension and evaluation results should be submitted for external review before publication.