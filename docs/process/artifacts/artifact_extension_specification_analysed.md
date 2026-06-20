Artifact-Type: extension-specification

Artifact-ID: extension-specification-analysed

Produced-By:
- 01_analyse_need_for_extension.md
- 02_describe_extension_concepts.md
- 03_develop_bpmn_extension.md
- 04_support_extension_with_tool.md
- 05_validate_and_evaluate_extension.md
- 06_consult_experts.md

Used-By:
- 07_publicise_bpmn_extension.md

# BPMN Extension Specification

## Extension Identification

### Name

[Extension Name]

### Version

[Version]

### Authors

[Authors]

### Date

[Date]

### Application Domain

[Domain]

### Status

- Proposed
- Developed
- Validated
- Published

---

# 1. Executive Summary

Provide a high-level overview of the BPMN extension.

Include:

- motivation;
- modelling problem;
- target domain;
- expected benefits;
- scope.

---

# 2. Purpose and Scope

## Purpose

Describe why the extension was created.

## Scope

Define:

- application area;
- intended users;
- modelling objectives;
- limitations.

---

# 3. Domain Analysis

Artifact source:

- artifact_extension_specification_analysed.md

Document:

- domain studied;
- practical problems identified;
- BPMN limitations;
- justification for extending BPMN.

---

# 4. Existing Extensions Analysis

Document:

- searched extensions;
- related work;
- reuse opportunities;
- differences from existing extensions.

| Extension | Year | Relation |
|------------|------|-----------|

---

# 5. Extension Concepts

Artifact source:

- artifact_extension_specification_concepts_described.md

## Concepts

| ID | Concept | Description |
|----|----------|-------------|

---

# 6. Metamodel

Artifact source:

- artifact_metamodel_validation_rules.md

Describe:

- classes;
- attributes;
- relationships;
- cardinalities;
- BPMN integration.

Include metamodel diagram if available.

---

# 7. Validation Rules

Artifact source:

- artifact_metamodel_validation_rules.md

| Rule ID | Description | Severity |
|----------|-------------|-----------|

---

# 8. Concrete Syntax

Artifact source:

- artifact_concrete_syntax_representations.md

For each construct describe:

- graphical representation;
- notation;
- placement;
- BPMN mapping;
- constraints.

---

# 9. XML Representation

If applicable:

- XML Schema;
- serialization rules;
- BPMN XML compatibility.

---

# 10. Tool Support

Artifact source:

- artifact_tool_support.md

Document:

- supported tools;
- implementation approach;
- palette entries;
- validation support;
- import/export support.

---

# 11. Example Models

Provide example BPMN models using the extension.

For each example include:

- objective;
- diagram;
- explanation.

---

# 12. Validation and Evaluation

Artifact source:

- artifact_extension_specification_validated_evaluated.md

Document:

- modelling experiments;
- expert reviews;
- case studies;
- evaluation method;
- results.

---

# 13. Expert Feedback

Artifact source:

- artifact_expert_feedback.md

Document:

- consulted experts;
- recommendations;
- applied corrections;
- unresolved issues.

---

# 14. Consistency and Conflict Analysis

Document:

- completeness verification;
- consistency verification;
- conflict analysis;
- BPMN compatibility verification.

---

# 15. Compliance with BPMN Community Guidelines

Artifact source:

- guidelines_bpmn_community.md

Checklist:

- BPMN compatibility
- Metamodel defined
- Concrete syntax defined
- Validation rules defined
- Tool support evaluated
- XML representation evaluated
- Expert consultation performed

---

# 16. Publication Information

Document:

- publication status;
- catalogue registration;
- endorsement status;
- release notes;
- repository links.

---

# 17. References

List all references used during the extension development.

---

# BPMN-BOT Guidance

When answering questions about a BPMN extension, BPMN-BOT should treat this document as the primary source of truth.

The assistant should:

1. Use the extension specification before consulting individual artifacts.
2. Retrieve concepts, metamodel, syntax and validation rules from this document.
3. Explain how extension constructs relate to BPMN.
4. Cite supporting artifacts when additional detail is required.
5. Use this specification when generating extension proposals or reviews.

---

# Expected Result

This artifact should provide a complete and publishable specification of the BPMN extension, consolidating all outputs produced throughout the BPMN extension lifecycle.