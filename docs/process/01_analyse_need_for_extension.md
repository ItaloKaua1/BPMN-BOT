Keywords: create BPMN extension, criar extensão BPMN, analyse need, necessidade de extensão, extension proposal

Process-ID: 1
Parent-Process: 00
Type: process

# 1. Analyse the Need for Extension

## Relation to the Main Process

This document details subprocess 1 of the BPMN extension process.

It starts from the intention to extend BPMN and decides whether a new BPMN extension should actually be proposed.

Previous state:
- Intention to extend BPMN.

Possible outcomes:
- Extension not proposed.
- Extension specification [Analysed].
- There is need for the extension.

Next step:
- If there is need for the extension, continue to `02_describe_extension_concepts.md`.
- If there is no need for the extension, the process ends.

Use this process to decide whether a new BPMN extension is really necessary before starting its specification. The analysis must verify the domain need, the concepts to be introduced, possible reuse of existing BPMN extensions, and whether standard BPMN can already model the requirement.

## Objective

Determine one of the following outcomes:

- **There is need for the extension**: generate an analysed extension specification and continue the extension proposal.
- **No need for the extension**: stop the proposal because BPMN or an existing extension already satisfies the need.

## Participants

- **Extender**: person or team proposing the BPMN extension and responsible for the analysis.
- **Experts in the domain/application area**: consulted when there are doubts about the domain concepts or application context.
- **Experts in BPMN extensions**: consulted when there are doubts about BPMN usage, BPMN default syntax, existing extensions, or modelling feasibility.

## Inputs

- Initial need for analysing whether an extension should be proposed.
- Purpose of the extension.
- Domain or application area.
- Practical aspects of the application area.
- References, contacted researchers, and domain literature.
- ISO/IEC 25010:2011 extension requirements, when applicable.
- Existing BPMN extension specifications and related extension lists.

## Supporting Artifacts Used in this Subprocess

The following artifacts may be created, updated or consulted during this subprocess:

- List of references and contacted researchers.
- List of concepts to be introduced.
- BPMN conformity checklist.
- Modelling observations.
- Class diagram of the extension.
- List of BPMN extensions related to the proposal.
- Extension requirements aligned with ISO/IEC 25010:2011.
- Extension specification [Analysed].

These artifacts are reused by later subprocesses of the BPMN extension lifecycle.

## Instructions

### 1.1 Study/Review the Domain or Application Area

Study the domain or application area where the extension need appears.

Capture:

- the purpose of the extension;
- the application area;
- practical aspects of the domain;
- relevant references;
- researchers or practitioners who may clarify domain issues.

If the purpose or application area is still unclear, refine it before continuing.

### 1.2 Identify the Concepts to Be Introduced by the Extension

List the domain concepts that the extension is expected to introduce into BPMN.

For each concept, describe:

- name;
- definition;
- source or reference;
- why the concept is relevant;
- expected relation with business process modelling.

Produce a **list of concepts to be introduced**. This list is the basis for the later checks.

### 1.3 Check for Issues About the Domain/Application Area

Evaluate whether there are open issues, ambiguities, or missing knowledge about the domain/application area.

If there is any issue:

1. Contact experts in the domain/application area.
2. Send the concepts, references, and specific questions.
3. Wait for the expert response.
4. Register the received issues and observations.

If there is no domain issue, continue to the BPMN suitability analysis.

### 1.4 Mitigate Domain/Application Issues

Domain/application experts must help mitigate the issues identified in step 1.3.

Use their feedback to:

- clarify concept definitions;
- remove concepts that are not relevant;
- add missing concepts;
- correct domain assumptions;
- update references and contacted researchers.

Record the mitigation result before continuing.

### 1.5 Receive Response About Domain Issues

Collect the response from domain/application experts and incorporate the relevant corrections into the proposal analysis.

The response should update the **modelling and observations** notes and may also update the list of concepts to be introduced.

### 1.6 Identify Whether BPMN Meets the Extension Requirements

Check whether BPMN already satisfies the extension requirements.

Use a **BPMN conformity checklist** to analyse:

- whether BPMN notation is suitable for the requirements;
- whether default BPMN elements can express the intended concepts;
- whether BPMN semantics cover the required behaviour;
- whether the proposal conflicts with BPMN syntax or semantics.

Decision: **Is BPMN notation suitable for meeting the requirements?**

- **No**: consider using another modelling language instead of extending BPMN.
- **Yes**: continue and check whether the requirement can already be modelled with default BPMN.

Decision: **Is there any issue whether it is possible to model with BPMN default syntax?**

- **Yes**: continue to step 1.7.
- **No**: if BPMN default syntax is sufficient, record that there is no need for the extension.

### 1.7 Model an Example With the Identified Concepts Using BPMN

Create a BPMN model example using the identified concepts with standard BPMN notation.

Produce:

- a model containing the relevant scenario;
- modelling observations;
- a class diagram of the proposed extension, if a structural representation is needed.

Use the model to decide whether the concepts can be represented adequately with BPMN alone.

### 1.8 Contact Experts in BPMN Extension

If there is any issue about modelling with BPMN, contact BPMN extension experts.

Send:

- the list of concepts to be introduced;
- the BPMN model example;
- modelling observations;
- the BPMN conformity checklist;
- the question about whether standard BPMN or an existing extension is sufficient.

Decision: **Is there any issue about modelling with BPMN?**

- **Yes**: collect expert feedback and continue to step 1.9.
- **No**: continue the analysis of default BPMN and existing extensions.

### 1.9 Mitigate Issues About the Usage of BPMN

BPMN extension experts must help mitigate issues about the usage of BPMN.

Use their feedback to:

- correct BPMN modelling mistakes;
- identify default BPMN constructs that can represent the need;
- identify semantic limitations;
- identify notation conflicts;
- refine the extension requirements.

Record the mitigated issues and update the modelling observations.

### 1.10 Receive Response About BPMN Issues

Collect the response from BPMN extension experts and incorporate it into the analysis.

Decision: **Was it possible to design with BPMN default syntax?**

- **Yes**: record **No need for the extension** and stop the process.
- **No**: continue to analyse whether an existing BPMN extension already satisfies the need.

### 1.11 Identify Whether There Are Extensions Related to the Current Proposal

Search for existing BPMN extensions related to the current proposal.

Use:

- the list of BPMN extensions related to the new proposal;
- analysed extension specifications;
- references and researchers identified during the domain review.

For each related extension, verify:

- concepts covered;
- notation introduced;
- semantics;
- scope and application area;
- compatibility with the current proposal;
- whether the extension already satisfies the current need.

Decision: **Is there an extension suitable for your need?**

- **Yes**: record **No need for the extension** and stop the process.
- **No**: continue to step 1.12.

### 1.12 Generate Extension Specification [Analysed]

If standard BPMN is not sufficient and no existing BPMN extension satisfies the need, generate the analysed extension specification.

The analysed specification must include:

- purpose of the extension;
- domain/application area;
- practical aspects;
- references and contacted researchers;
- list of concepts to be introduced;
- BPMN conformity checklist result;
- modelling observations;
- domain issues and mitigations;
- BPMN usage issues and mitigations;
- related BPMN extensions analysed;
- justification for why a new extension is needed.

The output of this step is **Extension specification [Analysed]** and the final decision **There is need for the extension**.

## Guidance for BPMN-BOT

When supporting a user during this subprocess, BPMN-BOT should help the user answer the following questions:

1. What is the purpose of the proposed BPMN extension?
2. Which domain or application area is being addressed?
3. Which concepts cannot be represented adequately using standard BPMN?
4. Is BPMN suitable for representing the problem?
5. Can the concepts already be represented using BPMN default syntax?
6. Are there existing BPMN extensions that already solve the problem?
7. Which experts, researchers or references support the proposal?
8. What evidence justifies the creation of a new BPMN extension?

BPMN-BOT should encourage the user to evaluate BPMN before proposing a new extension and should avoid recommending new extensions when BPMN or an existing extension is already sufficient.

## Decision Summary

Use the following decision rules:

- If the domain/application area is unclear, consult domain experts and mitigate the issue.
- If BPMN notation is not suitable for the requirements, use another modelling language.
- If BPMN default syntax can model the need, there is no need for the extension.
- If an existing BPMN extension satisfies the need, there is no need for the extension.
- If BPMN default syntax is insufficient and no existing BPMN extension satisfies the need, generate the analysed extension specification.

## Expected Outputs

- List of references and contacted researchers.
- List of concepts to be introduced.
- Extension requirements aligned with ISO/IEC 25010:2011, when applicable.
- BPMN conformity checklist.
- BPMN modelling example and observations.
- List of BPMN extensions related to the proposal.
- Analysed extension specification.
- Final decision about whether the BPMN extension is needed.

## Transition to the Next Subprocess

If the final decision is that a BPMN extension is needed, the generated Extension Specification [Analysed] becomes the primary input for:

`02_describe_extension_concepts.md`

The concepts identified in this subprocess will be refined, related to BPMN constructs and prepared for the extension design phase.