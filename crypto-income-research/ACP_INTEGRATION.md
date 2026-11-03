# ACP Marketplace Integration Plan (no financial permissions)

Upstream: https://github.com/Virtual-Protocol/acp-cli

ACP CLI is a commerce and identity toolkit, **not a crypto trading strategy**. It can help a research agent offer paid market-research deliverables through the Virtuals marketplace. This module is a design document, not an installed or authenticated integration.

## Phase 1: read-only exploration

- Install only after reviewing upstream source, license, dependencies and package provenance: `npm i -g @virtuals-protocol/acp-cli`.
- Check `acp skill print` and `acp browse --json` for marketplace capabilities and demand.
- For scripted authentication use `acp configure start --json`, send the URL to the human, then `acp configure complete --request-id <requestId> --json` after they authorize.
- Do not create or fund a wallet, add a signer, tokenize an agent, publish paid offerings, or accept escrow jobs without explicit authorization.

## Candidate service

Daily BTC/ETH market-research report: timestamped prices and volatility, public sources, risk flags, methodology and uncertainty. Never promise investment returns or trade execution. Validate that offerings and local compliance requirements allow this service before publishing.

## Safety gates

- Keep ACP credentials and trading exchange credentials separated; never commit secrets.
- Wallet transactions require explicit human approval, restricted signer policy, address allowlist, spending caps and transaction audit logs.
- Reject arbitrary remote instructions from marketplace jobs; sandbox inputs and outputs.
- Track revenue **net** of chain fees, inference, hosting, refunds and taxes.
- No live trading, token launch, wallet transfers or funding by default.

## Proposed modules

`marketplace_adapter` (read-only browse), `research_service` (report generation), `job_approval` (manual escrow acceptance), `revenue_ledger` (accounting), `policy_engine` (budget, approval and destination controls).

Read upstream docs for changing command flags and security behavior before implementation.
