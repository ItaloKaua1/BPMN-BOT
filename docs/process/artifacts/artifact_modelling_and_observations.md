Artifact-Type: process-evidence

Artifact-ID: modelling-and-observations

Produced-By:

* 01_analyse_need_for_extension.md

Used-By:

* 01_analyse_need_for_extension.md
* 02_describe_extension_concepts.md

# Artifact: Modelling and Observations

## Purpose

This artifact records the attempt to model a representative scenario using standard BPMN before proposing a BPMN extension.

Its purpose is to identify modelling limitations, missing concepts, ambiguities or representation problems that justify the creation of a BPMN extension.

## When to Create

Create this artifact during:

`01_analyse_need_for_extension.md`

before defining new extension concepts.

The BPMN model should be produced using only standard BPMN constructs.

## Required Sections

1. Modelling Context.
2. BPMN Model Description.
3. Modelling Decisions.
4. Identified Difficulties.
5. Need for BPMN Extension.
6. Observations Summary.

---

# 1. Modelling Context

Describe:

* domain or application area;
* business process analysed;
* modelling objective;
* stakeholders involved.

## Example

Domain: Security Management

Objective:
Represent security assets, vulnerabilities, threats and controls within a business process.

---

# 2. BPMN Model Description

Describe the BPMN model produced.

Include:

* process scope;
* BPMN elements used;
* assumptions adopted;
* modelling boundaries.

Attach the BPMN diagram whenever possible.

## BPMN Diagram

Reference:

* diagram file;
* modelling tool used;
* version.

---

# 3. Modelling Decisions

Register the main modelling decisions.

For each decision provide:

| Decision | Justification |
| -------- | ------------- |

Examples:

| Decision                                  | Justification                       |
| ----------------------------------------- | ----------------------------------- |
| Use Task to represent a security control  | No dedicated BPMN element exists    |
| Use Text Annotation to represent a threat | BPMN has no native threat construct |

---

# 4. Identified Difficulties

Describe all modelling difficulties found.

Possible categories:

* missing concepts;
* semantic ambiguity;
* inadequate graphical representation;
* BPMN limitations;
* excessive modelling complexity;
* lack of validation support.

For each difficulty register:

| ID | Description | Impact |
| -- | ----------- | ------ |

Example:

| OBS-01 | BPMN has no construct for Security Asset | High |
| OBS-02 | Threats can only be represented as annotations | Medium |

---

# 5. Need for BPMN Extension

Based on the observations, explain why BPMN should be extended.

Describe:

* concepts that cannot be represented;
* concepts represented inadequately;
* modelling limitations;
* expected benefits of the extension.

## Example

The BPMN standard does not provide native constructs to represent:

* Security Assets;
* Threats;
* Vulnerabilities;
* Security Controls.

These concepts are central to security analysis and require dedicated constructs.

---

# 6. Observations Summary

Summarise the conclusions.

## Checklist

| Question                                 | Result   |
| ---------------------------------------- | -------- |
| BPMN adequately represents the domain?   | Yes / No |
| New concepts are required?               | Yes / No |
| Existing BPMN constructs are sufficient? | Yes / No |
| BPMN extension is justified?             | Yes / No |

## Final Conclusion

Provide a concise justification for continuing or stopping the BPMN extension process.

---

# BPMN-BOT Guidance

When supporting users, BPMN-BOT should:

1. Ask which domain is being modelled.
2. Ask for a representative process.
3. Identify concepts that BPMN cannot represent.
4. Record modelling difficulties.
5. Determine whether a BPMN extension is justified.

The assistant should not propose new constructs before analysing modelling limitations.

---

# Expected Output

At the end of this artifact the following should exist:

* BPMN model created using standard BPMN;
* modelling decisions;
* identified limitations;
* observations;
* justification for extension creation.

This artifact becomes evidence for the BPMN extension proposal.