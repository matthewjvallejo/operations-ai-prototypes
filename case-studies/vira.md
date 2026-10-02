# VIRA — Vehicle Incident Reporting Assistant

## Overview

VIRA is a mobile-first, browser-based incident reporting and investigation system designed to move an event from first awareness through structured fact gathering, witness evidence, investigation, and final Safety review.

The product is deliberately separated into four focused tools rather than one large form:

- **Notify** — capture the first usable signal that an incident occurred.
- **Initiate** — conduct the full structured incident interview and create a working draft.
- **Collect** — capture an independent witness statement while preserving source integrity.
- **Complete** — assemble the available records into a resumable investigation workspace for Safety review.

All four tools now exist as working browser prototypes and are being tested. They remain lightweight file-based workflows rather than a database-backed incident-management platform.

## Operating Model

The VIRA family follows a simple progression:

**Notify → Initiate → Collect → Complete**

The progression is operational, not a rigid technical chain. Records may be created independently and associated later by the Safety Manager using the available context.

Incident IDs are preserved when available, but they are **reference values rather than mandatory join keys**. A field user should not be blocked because they do not know an ID. The investigator can deliberately associate records using the incident date, person involved, source context, and any available reference ID.

VIRA does not automatically merge records simply because identifiers appear to match.

## VIRA — Notify
### Something Happened

Notify is the first-signal tool.

Its purpose is speed: capture enough reliable information for leadership or Safety to begin responding without forcing the reporter through the full incident interview.

It captures core reporter, incident, driver, vehicle, injury, emergency-response, location, and short-description information and produces a structured first-signal record.

The user can review, share, copy, or download that record and may open a device text or email draft. Opening a draft is not the same as sending or confirming delivery.

Notify does **not** create a final approved incident report.

## VIRA — Initiate
### What Do We Know?

Initiate is the full structured incident interview.

It captures the known facts, preserves missing or uncertain information, identifies follow-up items, and produces a clearly labeled working draft for Safety review.

The interview uses conditional questions and can capture areas such as:

- incident basics;
- police and emergency response;
- company vehicle and driver information;
- damage, towing, and out-of-service status;
- additional company vehicles;
- multiple non-company vehicles;
- insurance, license, VIN, and other available information.

Missing information remains visible rather than being converted into a false answer. Unknown, unavailable, skipped, and not-applicable states are kept distinct where appropriate.

The result is a working record, not a finalized or approved incident report.

## VIRA — Collect
### Tell Me What Happened

Collect is independent witness-evidence intake rather than a second incident questionnaire.

It supports English and Spanish and is designed to preserve what was actually provided while still creating a useful review record.

The workflow can preserve:

- witness identity and incident context;
- the original statement;
- reviewed wording when appropriate;
- original-language content;
- a separate English translation;
- approval and certification context;
- electronic signature and certification time.

Original, reviewed, translated, and certified content remain distinguishable. VIRA does not silently overwrite the source statement with a corrected or translated version.

A reference Incident ID may be included when known, but it is not intended to be a prerequisite for taking a witness statement.

## VIRA — Complete
### Resumable Investigation Workspace

Complete is intentionally **not** another questionnaire.

It is the Safety Manager's working investigation space.

The Safety Manager can import available VIRA source records, deliberately associate them with the investigation, choose the basis for the working incident overview, and continue the investigation over multiple sessions.

The current workflow supports:

1. importing Notify, Initiate, and Collect source records;
2. preserving the original source records and provenance;
3. deliberately associating records rather than automatically matching them;
4. selecting the source basis for the working incident overview;
5. writing investigation notes, actions taken, findings, open issues, and recommendations;
6. tracking evidence and follow-up while the underlying evidence remains in the organization's approved file repository;
7. adding company or non-company vehicles manually and using fleet-reference data when available;
8. exporting a structured, versioned TXT investigation package;
9. re-importing that package later to reconstruct the working investigation;
10. continuing the investigation until the Safety Manager deliberately marks it complete; and
11. generating a separate human-readable report.

The resumable package and the final report serve different purposes. The structured TXT package preserves working investigation state; the human-readable report is an output for review and distribution.

VIRA does not decide which conflicting account is true, determine fault or liability, or automatically assign root cause. Those remain human decisions.

## Design Principles

VIRA reflects several operating principles:

- **Problem first, platform second.**
- Break a broader process into focused tools with clear jobs.
- Preserve source wording when the information is evidence.
- Make missing information visible instead of manufacturing certainty.
- Keep working drafts, witness evidence, investigation work product, and final reporting distinct.
- Preserve provenance so reviewers can see where information came from.
- Use human judgment for source association, conflicts, conclusions, and final review.
- Prototype the smallest useful workflow, test it, and expand only when the concept earns it.

## Current Product Boundary

The current VIRA tools are browser-based workflows designed to work across phones, tablets, and workstations without requiring a native mobile application.

The current prototype intentionally does not provide:

- a persistent incident database;
- autosave or recovery of unexported browser work;
- automatic source matching or account reconciliation;
- automatic message delivery or delivery confirmation;
- automatic fault, liability, or root-cause determination;
- direct integration with the organization's document repository;
- an embedded evidence repository;
- offline application support.

That boundary is deliberate. The project first proves the operating behavior using portable files and explicit human review before adding heavier architecture.

## Why the Project Matters

VIRA demonstrates a practical approach to operational technology: understand the real workflow, divide it into clear stages, preserve the integrity of source information, prototype quickly, test the behavior that matters, and keep human judgment in control where the stakes require it.

The project also demonstrates iterative product development. The four tools were initially built independently around a common end-state vision, then reviewed together and standardized so terminology, source handling, missing-information behavior, approval context, filenames, and investigation flow work as a coherent system.

It is a working example of using AI-enabled development and lightweight web technology to improve an operational process without beginning with a large systems implementation.

## Confidentiality

This public case study is intentionally company-neutral and high level.

It excludes employer identification, internal branding, employee or customer data, credentials, private investigation records, recipient addresses, proprietary implementation details, and other organization-sensitive information.
