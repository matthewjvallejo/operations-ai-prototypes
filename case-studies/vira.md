# VIRA — Vehicle Incident Reporting Assistant

## Overview

VIRA is a mobile-first, browser-based workflow designed to simplify vehicle-incident reporting and investigation.

The project began with a practical operations problem: incident information can arrive through a mix of phone calls, text messages, free-form documents and follow-up conversations. Field employees may be asked to provide information in inconsistent ways, while the person responsible for investigating the event spends significant time reconstructing facts before meaningful analysis can begin.

VIRA was designed to reduce that friction.

Rather than building one large application, the workflow is divided into four focused tools:

- **Notify** — capture the first usable facts quickly.
- **Initiate** — gather a fuller structured account of the incident.
- **Collect** — preserve individual witness accounts independently.
- **Complete** — bring the records together for investigation, findings, corrective actions and reporting.

The result is a lightweight workflow that can operate from a phone, tablet or workstation without requiring a native application or a large systems implementation.

## The Operating Idea

The design deliberately separates **information capture** from **investigation**.

People in the field should not need to become investigators or paperwork experts. Their job is to describe what they know while the information is fresh, review it and preserve the record.

The investigator's job is different: compare accounts, evaluate evidence, resolve open questions, document findings, assign corrective actions and prepare the final report.

VIRA keeps those responsibilities distinct while allowing information to move from one stage to the next.

## The Four-Part Workflow

### Notify
**Basic facts. Immediate awareness.**

Notify captures a small set of known facts quickly and prepares the first alert for review and sending through the user's own device.

It is intentionally not the full incident report.

### Initiate
**A fuller overview of the incident.**

Initiate uses guided questions to capture what happened, relevant conditions, people, vehicles, known damage and potential witnesses.

Missing or uncertain information remains visible rather than being converted into false certainty.

### Collect
**One witness. One focused account.**

Collect preserves an individual witness account separately from the broader incident interview.

The workflow supports English and Spanish, preserves original-language content alongside a labeled English translation, and records approval and signature context without silently replacing the source statement.

### Complete
**One workspace for the investigation and report.**

Complete brings the source records together so the investigator can compare accounts, evaluate evidence, document findings and contributing factors, track open issues and corrective actions, and prepare the final report.

The working investigation can be exported, reopened and continued across multiple work sessions.

## What Changed During Development

The system evolved through repeated workflow review and testing rather than from a fixed initial specification.

Examples of changes that emerged from testing included:

- removing unnecessary identifier requirements that could block field reporting;
- separating potential-witness identification from actual witness statements;
- preserving original witness wording and translated versions as distinct evidence;
- simplifying non-company vehicle capture so field users were not asked to reproduce information better handled later in the investigation;
- distinguishing working investigation data from the human-readable final report;
- allowing an investigation to be exported, reopened and continued across multiple work sessions;
- keeping supporting photographs and documents in their existing repository rather than turning the prototype into an evidence-storage system; and
- retaining human review for source association, conflicting accounts, findings and completion decisions.

The project was deliberately changed when testing showed that an earlier assumption added friction, created ambiguity or did not reflect the real work.

## From Prototype to Working Process

Building the browser tools was only part of the project.

The workflow was also operationalized through:

- standardized terminology and handoffs across all four tools;
- structured downloadable records;
- a resumable investigation package;
- formal investigation reporting;
- browser and regression testing;
- mobile-layout review;
- bilingual witness handling;
- documentation and change control;
- user-facing one-page guides;
- a full screenshot-based training package; and
- separate technical and maintenance documentation.

Testing evidence is kept separate from assumptions about production readiness. Browser behavior, published availability, physical-device behavior and actual message delivery are treated as different verification questions rather than being conflated.

## Deliberate Product Boundaries

VIRA intentionally does not attempt to be a full enterprise incident-management platform.

The current design does not rely on:

- a persistent incident database;
- automatic source matching or account reconciliation;
- browser autosave;
- automatic message delivery or delivery confirmation;
- embedded evidence storage;
- automatic fault, liability or root-cause determination; or
- direct integration with an enterprise document-management platform.

Those boundaries were deliberate. The objective was to prove the workflow first using lightweight browser tools, portable records and explicit human judgment before introducing heavier architecture.

## Design Principles

VIRA reflects several operating principles:

- **Start with the work, not the software.**
- Break a complicated process into focused steps with clear responsibilities.
- Reduce unnecessary work for frontline users.
- Preserve source integrity where information may become evidence.
- Make missing information visible instead of manufacturing certainty.
- Keep consequential decisions with the responsible human.
- Test behavior before expanding architecture.
- Revise requirements when testing exposes weak assumptions.
- Build the documentation, training and maintenance structure required to move a prototype toward actual use.

## What the Project Demonstrates

VIRA is a practical example of operations-led product development.

The project shows how an inconsistent, largely manual process can be decomposed into focused tools, tested against actual workflow needs and improved iteratively without beginning with a large systems implementation.

It also demonstrates AI-assisted design, analysis, documentation and software-development workflows while preserving human review and operational judgment throughout.

The important result is not simply four browser tools.

It is a working operating model that moves an event from first awareness through structured reporting, witness capture, investigation, corrective action and formal reporting while preserving source integrity and reducing avoidable field paperwork.

## Current Status

All four VIRA tools exist as working browser prototypes and are in active testing.

The current testing package includes structured user guidance, full-workflow screenshots, technical documentation and maintenance controls. Production readiness, physical-device behavior and actual message delivery remain separate validation questions.

## Confidentiality

This public case study is intentionally company-neutral and sanitized.

It excludes employer identification, internal branding, employee or customer data, credentials, private investigation records, recipient information, proprietary implementation details and other organization-sensitive information.
