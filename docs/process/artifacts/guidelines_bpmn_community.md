Artifact-Type: guideline

Referenced-By:
- 01
- 02
- 03
- 05
- 07

# BPMN Community Guidelines for BPMN Extensions

## Purpose

This document consolidates the BPMN community guidelines for proposing, developing, validating and publishing BPMN extensions.

The guidelines aim to ensure consistency, interoperability, completeness and alignment with BPMN standards defined by the Object Management Group (OMG).

---

## Relation to the BPMN Extension Process

This artifact supports multiple phases of the BPMN Extension Process.

It provides recommendations, constraints and best practices that should be considered throughout the BPMN extension lifecycle.

The guidelines may be consulted during:

- 01 Analyse Need for Extension
- 02 Describe Extension Concepts
- 03 Develop BPMN Extension
- 05 Validate and Evaluate BPMN Extension
- 07 Publicise BPMN Extension

Related process:
- 00_bpmn_extension_process_overview.md

## G1 - Preserve the Original BPMN Syntax

All BPMN standard constructs should be preserved.

Recommendations:

* Do not remove BPMN native elements.
* Avoid non-conservative extensions.
* Maintain compatibility with the original language.

---

## G2 - Follow a Structured Extension Process

BPMN extensions should not be developed in an ad-hoc manner.

Recommendations:

* Follow a systematic process.
* Avoid inconsistencies.
* Avoid incompleteness.
* Avoid conflicts between extension elements.
* Use PRISE or a similar methodology when available.

---

## G3 - Perform Literature Review and Consult Experts

Before proposing an extension:

* Study the target domain.
* Review existing BPMN extensions.
* Consult domain experts.
* Consult BPMN experts.
* Model representative scenarios from the application area.

Purpose:

* Improve conceptual accuracy.
* Reduce modelling errors.
* Improve extension quality.

---

## G4 - Define Extension Concepts Clearly

Every concept introduced by the extension should have a clear definition.

Recommendations:

* Describe concepts explicitly.
* Avoid ambiguous terminology.
* Document the meaning of each concept.

---

## G5 - Define Abstract and Concrete Syntax

The extension should provide:

### Abstract Syntax

* Metamodel
* Relationships
* Constraints
* Well-formedness rules

### Concrete Syntax

* Visual representation
* Symbols
* Graphical notation

Both syntaxes are required.

---

## G6 - Ensure Consistency Between Abstract and Concrete Syntax

Verify that:

* Every graphical element has a corresponding metamodel element.
* Every metamodel element has a graphical representation.
* No construct exists in only one syntax.

---

## G7 - Relate Extension Concepts to BPMN Concepts

New concepts should be integrated with BPMN constructs.

Possible approaches:

* Specialization of BPMN elements.
* BPMN relationships.
* Additional extension relationships.

---

## G8 - Minimize Modifications to BPMN

The extension should introduce the smallest possible number of changes.

Goals:

* Preserve BPMN simplicity.
* Improve usability.
* Maintain scalability.
* Avoid language distortion.

---

## G9 - Use Simple Graphical Representations

New graphical elements should:

* Be easy to understand.
* Be easy to draw manually.
* Follow BPMN visual principles.
* Support rapid modelling and discussion.

---

## G10 - Define Quality Requirements Based on ISO/IEC 25010

Extension requirements should consider quality attributes such as:

* Usability
* Reliability
* Performance efficiency
* Maintainability
* Compatibility

The objective is to align the extension with recognized quality standards.

---

## G11 - Assess BPMN Suitability Before Extending

Before creating an extension:

* Verify whether BPMN is appropriate for the target domain.
* Apply a BPMN conformity checklist.
* Evaluate conceptual alignment.

If BPMN is not suitable, another modelling language should be considered.

---

## G12 - Provide a Structural Representation Aligned with the BPMN Metamodel

The extension should include:

* Classes
* Attributes
* Relationships
* Specializations

The structure must remain consistent with the BPMN metamodel.

---

## G13 - Systematize Conceptual and Structural Characterization

Document:

* Equivalences
* Relationships
* Distinctions
* Integration points

This helps explain how the extension interacts with BPMN.

---

## G14 - Provide an OMG-Compliant XML Representation

The extension should define:

* XML Schema
* BPMN XML compatibility
* Formal serialization rules

This enables interoperability with BPMN tools.

---

## G15 - Consider Tool Support

Evaluate whether the extension requires:

* Modelling support
* Validation support
* Execution support

Tool support increases practical applicability.

---

## G16 - Implement the Extension in Modelling Tools

When necessary:

* Add new constructs to modelling tools.
* Provide graphical support.
* Support validation and usage of the extension.

The goal is to facilitate adoption in real-world scenarios.

---

## Summary

A BPMN extension should:

1. Preserve BPMN compatibility.
2. Follow a structured development process.
3. Define concepts clearly.
4. Provide abstract and concrete syntax.
5. Ensure consistency.
6. Minimize complexity.
7. Support interoperability.
8. Include tool support when appropriate.
9. Be aligned with OMG standards.