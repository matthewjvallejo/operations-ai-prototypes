# Customer Operations Triage Demo

This small demo shows a simple way to classify incoming customer issues, assign priority, and surface recurring themes.

The example uses synthetic data only.

## Why this matters

In customer operations, fast response is useful, but speed alone does not solve the underlying customer problem. A stronger operation also needs to understand:

- what type of issue is occurring
- how urgent it is
- where it should be routed
- whether the issue is isolated or recurring
- what patterns may require a process, product, billing, or technical fix

## Categories

The demo classifies issues into:

- Billing
- Product
- Technical
- Account Access
- Subscription / Plan Change
- General Support

## Priority logic

A basic rule set assigns:

- P1 — urgent customer-impacting or access issue
- P2 — important issue requiring timely resolution
- P3 — routine support request

## Files

- `triage_demo.py` — simple Python example
- `sample_tickets.csv` — synthetic support tickets

This is intentionally lightweight. It is meant to demonstrate operating logic and problem framing, not production software.
