Artifact-Type: checklist

Artifact-ID: checklist-verification-completeness-consistency-conflicts

Produced-By:

* 03_develop_bpmn_extension.md

Used-By:

* 03_develop_bpmn_extension.md
* 05_validate_and_evaluate_extension.md
* 06_consult_experts.md

# Artifact: Checklist for Verification of Completeness, Consistency and Conflicts

## Purpose

This checklist is used to verify whether a BPMN extension is complete, internally consistent and free from conflicts.

The checklist should be applied during extension development, validation and expert review activities.

Its objective is to identify modelling problems before publication.

---

# Part 1 - Completeness Verification

Verify which extension levels have been defined.

## Completeness Checklist

| Extension Level                    | Verified |
| ---------------------------------- | -------- |
| Concept Definitions                | ☐        |
| Metamodel                          | ☐        |
| Validation Rules                   | ☐        |
| Concrete Syntax                    | ☐        |
| Examples                           | ☐        |
| XML Representation (if applicable) | ☐        |
| Tool Support (if applicable)       | ☐        |

### Verification Rule

Every introduced concept should appear in all required extension representations.

---

# Part 2 - Concept Consistency Verification

Verify whether every concept is consistently represented.

## Concept Traceability Matrix

| Concept   | Definition | Metamodel | Validation Rules | Concrete Syntax |
| --------- | ---------- | --------- | ---------------- | --------------- |
| Concept A | ☐          | ☐         | ☐                | ☐               |
| Concept B | ☐          | ☐         | ☐                | ☐               |

### Verification Questions

For each concept:

* Is the concept defined?
* Does the metamodel represent it?
* Are validation rules defined?
* Does a graphical notation exist?
* Are all representations aligned?

---

# Part 3 - BPMN Compatibility Verification

Verify that BPMN standard constructs remain valid.

## BPMN Elements Verification

### Events

| BPMN Construct     | Metamodel | Concrete Syntax |
| ------------------ | --------- | --------------- |
| Start Event        | ☐         | ☐               |
| Intermediate Event | ☐         | ☐               |
| End Event          | ☐         | ☐               |

### Activities

| BPMN Construct | Metamodel | Concrete Syntax |
| -------------- | --------- | --------------- |
| Task           | ☐         | ☐               |
| Subprocess     | ☐         | ☐               |

### Gateways

| BPMN Construct | Metamodel | Concrete Syntax |
| -------------- | --------- | --------------- |
| Gateway        | ☐         | ☐               |

### Swimlanes

| BPMN Construct | Metamodel | Concrete Syntax |
| -------------- | --------- | --------------- |
| Pool           | ☐         | ☐               |
| Lane           | ☐         | ☐               |

### Artifacts

| BPMN Construct  | Metamodel | Concrete Syntax |
| --------------- | --------- | --------------- |
| Data Object     | ☐         | ☐               |
| Data Store      | ☐         | ☐               |
| Group           | ☐         | ☐               |
| Text Annotation | ☐         | ☐               |

### Connecting Objects

| BPMN Construct | Metamodel | Concrete Syntax |
| -------------- | --------- | --------------- |
| Sequence Flow  | ☐         | ☐               |
| Message Flow   | ☐         | ☐               |
| Association    | ☐         | ☐               |

### Verification Rule

The extension must not invalidate BPMN standard constructs.

---

# Part 4 - Conflict Verification

Verify whether extension constructs create conflicts.

## Conflict Matrix

| Concept   | Multiple Symbols | Shared Symbol | Invalid BPMN Representation | Outside Extension Scope |
| --------- | ---------------- | ------------- | --------------------------- | ----------------------- |
| Concept A | ☐                | ☐             | ☐                           | ☐                       |
| Concept B | ☐                | ☐             | ☐                           | ☐                       |

---

# Part 5 - Conflict Details

Describe every identified conflict.

| Conflict ID | Description | Severity | Related Construct |
| ----------- | ----------- | -------- | ----------------- |

Possible severities:

* Low
* Medium
* High
* Critical

Examples:

* Two constructs using the same symbol.
* BPMN construct redefined with a different meaning.
* Missing metamodel representation.
* Missing graphical notation.

---

# Part 6 - Final Verification Decision

## Completeness

☐ Passed

☐ Failed

---

## Consistency

☐ Passed

☐ Failed

---

## Conflict Analysis

☐ Passed

☐ Failed

---

## Final Result

☐ Extension Approved

☐ Extension Requires Corrections

☐ Extension Rejected

### Justification

Describe the reasons supporting the final decision.

---

# BPMN-BOT Guidance

When assisting users, BPMN-BOT should use this checklist to verify:

1. Missing concepts.
2. Missing metamodel elements.
3. Missing validation rules.
4. Missing concrete syntax.
5. BPMN compatibility issues.
6. Duplicate constructs.
7. Symbol conflicts.
8. Semantic conflicts.

The assistant should recommend corrections whenever any verification item fails.

---

# Expected Output

The completed checklist should provide:

* completeness assessment;
* consistency assessment;
* BPMN compatibility assessment;
* conflict analysis;
* final verification decision.

This artifact supports development, evaluation and expert review activities.
