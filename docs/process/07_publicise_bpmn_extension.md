Process-ID: 6
Parent-Process: 0
Type: process

# 6. Publicise the BPMN Extension

## Relation to the Main BPMN Extension Process

This document details subprocess 6 of the BPMN Extension Process.

This subprocess is executed after the BPMN extension has been validated and evaluated.

Previous subprocess:
- `05_validate_and_evaluate_extension.md`

Input:
- BPMN extension evaluated and validated.
- Extension specification [Validated/evaluated].

Possible outcomes:
- BPMN extension endorsed.
- BPMN extension not endorsed.
- BPMN extension publicised.

Related process:
- `00_bpmn_extension_process_overview.md`

Use this process after the BPMN extension has been evaluated and validated. The goal is to register the extension in a catalogue, obtain endorsement when needed, and publish the extension so that it can be discovered and used by the BPMN community.

## Objective

Publicise the validated/evaluated BPMN extension.

The expected final outcome is:

- **BPMN extension publicised**.

Possible intermediate outcomes are:

- **BPMN extension endorsed**;
- **BPMN extension not endorsed**.

## Participants

- **Extender**: person or team responsible for registering, notifying, endorsing, and publishing the BPMN extension.
- **Experts in BPMN extensions**: evaluate whether the new extension is well defined and may endorse or reject endorsement.

## Inputs

- Extension evaluated and validated.
- Extension specification [Validated/evaluated].
- List of experts in BPMN extensions.
- Catalogue of BPMN extensions.

## BPMN Extension Catalogue

The BPMN Extension Catalogue should be considered the primary repository for registering BPMN extensions.

The BPMN-BOT should assist the Extender in preparing all information required for catalogue registration before publication.

Catalogue registration should occur before endorsement and publication activities.

## Supporting Artifacts Used in this Subprocess

The following artifacts are created, updated or consulted during this subprocess:

- Extension specification [Validated/evaluated].
- Catalogue entry for the BPMN extension.
- List of experts in BPMN extensions.
- Notification of a new extension.
- Endorsement decision.
- Publication package.
- BPMN extension endorsed.
- BPMN extension not endorsed.
- BPMN extension publicised.

These artifacts support the registration, endorsement and publication of the BPMN extension.

## Instructions

### Start: Extension Evaluated and Validated

Begin when the BPMN extension has already been evaluated and validated.

Use the **Extension specification [Validated/evaluated]** as the main publication artifact.

Before publication, verify that the specification includes:

- purpose and scope;
- domain/application area;
- concepts;
- metamodel;
- validation rules;
- concrete syntax;
- examples;
- validation/evaluation evidence;
- tool support information, when available.

### 6.1 Add the New BPMN Extension to the Catalogue

Register the BPMN extension in the catalogue of BPMN extensions.

The catalogue entry should include:

- extension name;
- version;
- authors or maintainers;
- purpose;
- application area;
- summary of introduced concepts;
- reused BPMN constructs;
- concrete syntax overview;
- link or reference to the full specification;
- validation/evaluation status;
- tool support status;
- publication or access location.

The catalogue entry should also document:

- extension type (Implementation or Specification Diagram);
- syntax level (abstract, concrete or both);
- syntax compatibility;
- conservative or non-conservative extension;
- graphical representation strategy;
- BPMN constructs modified;
- metamodel completeness;
- OMG guideline compliance;
- modelling tool support.

Decision: **Is there an expert in BPMN extensions as an Extender?**

- **Yes**: endorse the BPMN extension internally and continue to step 6.2.
- **No**: notify BPMN extension experts and continue to step 6.3.

### 6.2 Endorse the BPMN Extension

Use this step when an expert in BPMN extensions is already part of the extender team.

The expert should review the catalogue entry and the validated/evaluated specification.

Before endorsing, verify:

- the extension is well defined;
- the extension is compatible with BPMN;
- the specification is complete;
- validation/evaluation evidence is available;
- there are no unresolved critical issues;
- publication artifacts are ready.

If the extension is acceptable, register the endorsement and continue to publication in step 6.5.

### 6.3 Notify the Experts About the Extension

Use this step when no BPMN extension expert is part of the extender team.

Notify the selected BPMN extension experts about the new extension.

Send:

- Extension specification [Validated/evaluated];
- catalogue entry;
- purpose of the extension;
- validation/evaluation evidence;
- examples or models;
- tool support information, when available;
- request for endorsement.

The notification creates the **Notification of a new extension** event for the BPMN extension experts.

### 6.4 Endorse the BPMN Extension

BPMN extension experts analyse the notified extension and decide whether it is well defined.

Decision: **Is the BPMN extension well-defined?**

- **Yes**: endorse the BPMN extension.
- **No**: do not endorse the BPMN extension.

The expert analysis should consider:

- completeness of the specification;
- consistency with BPMN;
- absence of unresolved conflicts;
- clarity of concepts;
- adequacy of metamodel and validation rules;
- adequacy of concrete syntax;
- validation/evaluation evidence;
- usefulness for the intended application area.

Possible outputs:

- **BPMN extension endorsed**;
- **BPMN extension not endorsed**.

If the extension is endorsed, continue to publication in step 6.5.

If the extension is not endorsed, record the reason and do not publish it as an endorsed BPMN extension.

### 6.5 Publish the BPMN Extension

Publish the BPMN extension after it has been added to the catalogue and endorsed.

Publication should make available:

- Extension specification [Validated/evaluated];
- catalogue entry;
- examples and model files;
- metamodel and validation rules;
- concrete syntax documentation;
- tool support or installation instructions, when available;
- endorsement information;
- version and release notes;
- contact or contribution information.

The output of this step is **BPMN extension publicised**.

## BPMN-BOT Publication States

| State | Process Step | Bot Action | Artifact Updated |
|---------|---------|---------|---------|
| `6.1_add_to_catalogue` | Add BPMN extension to catalogue | Collect catalogue metadata and register extension | Catalogue Entry |
| `6.2_internal_endorsement` | Endorse BPMN extension | Verify endorsement by BPMN extension expert in the team | Endorsement Record |
| `6.3_notify_experts` | Notify BPMN extension experts | Prepare and send endorsement request | Notification Record |
| `6.4_external_endorsement` | External endorsement review | Record expert endorsement decision | Endorsement Record |
| `6.5_publish_extension` | Publish BPMN extension | Prepare publication package and publication channels | Published BPMN Extension |

## Guidance for BPMN-BOT

When supporting a user during this subprocess, BPMN-BOT should help answer questions such as:

1. Is the BPMN extension ready to be publicised?
2. What information must be added to the catalogue?
3. Is there a BPMN extension expert in the extender team?
4. Should external BPMN extension experts be notified?
5. What should be sent to experts for endorsement?
6. What makes a BPMN extension well-defined?
7. Can the extension be published as endorsed?
8. What publication artifacts should be made available?
9. What information is required by the BPMN Extension Catalogue?
10. Does the extension satisfy endorsement requirements?
11. Which publication channel is most appropriate?

BPMN-BOT should distinguish between adding an extension to the catalogue, endorsing the extension, and publishing the extension.

## Decision Summary

Use the following decision rules:

- If an expert in BPMN extensions is part of the extender team, the endorsement may be performed directly by the extender team.
- If no BPMN extension expert is part of the extender team, notify external BPMN extension experts.
- If experts determine that the extension is well defined, the BPMN extension is endorsed and may be published.
- If experts determine that the extension is not well defined, record the reason and do not publish it as endorsed.
- Publish only after the catalogue entry and publication artifacts are ready.

## Expected Outputs

- Catalogue entry for the BPMN extension.
- Notification of a new extension, when external experts are consulted.
- BPMN extension endorsed or not endorsed.
- Publication package or public access location.
- BPMN extension publicised.

## Final Outcome of the BPMN Extension Process

After this subprocess is completed, the BPMN extension process may end with:

- BPMN extension publicised, when the extension is added to the catalogue, endorsed when required, and published.
- BPMN extension not endorsed, when experts determine that the extension is not well-defined.

The published extension should be discoverable by the BPMN community and supported by its validated/evaluated specification.