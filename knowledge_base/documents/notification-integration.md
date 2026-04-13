# Notification Integration Guide

**Owner:** geordi | **Reviewed by:** worf | **Last Updated:** 2026-04-11

---

## Purpose

This document defines the connectivity layer between the TNG agent system and external team communication tools (Microsoft Teams, Slack). It covers webhook setup, payload formats, which agent signals trigger notifications, and security requirements.

All notifications are **fire-and-forget** — agents never block on delivery. A failed notification is logged and ignored; it never halts a mission.

---

## Supported Channels

### Platform channels

| Platform | Env Var prefix | Protocol |
|----------|---------------|----------|
| Microsoft Teams | `TEAMS_WEBHOOK_*` | Incoming Webhook (MessageCard / Adaptive Cards) |
| Slack | `SLACK_WEBHOOK_*` | Incoming Webhook (Block Kit) |

### Logical channels

Each logical channel has its own webhook URL per platform. All URLs live in `knowledge_base/current/channel-config.md` (gitignored) and the corresponding GitHub secrets.

| Logical channel | Env var | Audience | Signals |
|---|---|---|---|
| `tng-bridge` | `TEAMS_WEBHOOK_BRIDGE` / `SLACK_WEBHOOK_BRIDGE` | Full crew + audit | Every signal (superset) |
| `tng-ready-room` | `TEAMS_WEBHOOK_READY_ROOM` / `SLACK_WEBHOOK_READY_ROOM` | Decision makers, architects | Ready Room lifecycle, MDR, AC, PRIORITY, CONFLICT |
| `tng-execution` | `TEAMS_WEBHOOK_EXECUTION` / `SLACK_WEBHOOK_EXECUTION` | riker, execution crew | Wave dispatches, BLOCKER, execution-complete, ROLLBACK |
| `tng-review` | `TEAMS_WEBHOOK_REVIEW` / `SLACK_WEBHOOK_REVIEW` | worf, troi, crusher, picard | Track C verdicts, FIX-IN-PLACE, SCOPED-READY-ROOM |
| `tng-oncall` | `TEAMS_WEBHOOK_ONCALL` / `SLACK_WEBHOOK_ONCALL` | On-call engineers | P0, P1, BLOCKER, ROLLBACK-FULL, EXTERNAL-EVENT:critical |
| `tng-stakeholders` | `TEAMS_WEBHOOK_STAKEHOLDERS` / `SLACK_WEBHOOK_STAKEHOLDERS` | Business stakeholders | READY-ROOM-OPEN, MISSION-CLOSED |

You do not need to configure every channel. Any channel with a blank or absent URL is silently skipped — no channel's absence blocks mission progress.

---

## Setup

### Microsoft Teams

1. In Teams, open the channel you want notifications in.
2. Click **...** → **Connectors** → **Incoming Webhook** → **Configure**.
3. Name it `TNG-Bridge`, upload the badge icon if desired, copy the generated URL.
4. Store the URL in `knowledge_base/current/teams-webhook.md` (never commit secrets — this file is gitignored or managed via GitHub Secrets).
5. For GitHub Actions workflows, store as a repo secret named `TEAMS_WEBHOOK_URL`.

### Slack

1. Go to your Slack workspace → **Apps** → search **Incoming Webhooks** → **Add to Slack**.
2. Choose the target channel, click **Add Incoming WebHooks Integration**, copy the URL.
3. Store the URL in `knowledge_base/current/slack-webhook.md`.
4. For GitHub Actions workflows, store as a repo secret named `SLACK_WEBHOOK_URL`.

---

## Agent Signals That Trigger Notifications

Agents emit structured signals throughout missions. The table below shows each signal's urgency and which logical channels receive it. `tng-bridge` always receives every signal and is omitted from the fan-out column for brevity.

| Signal | Sender | Urgency | Primary channel | Fan-out channels |
|--------|--------|---------|----------------|-----------------|
| `[READY-ROOM-OPEN: <slug>]` | picard | Info | `tng-ready-room` | `tng-stakeholders` |
| `[READY-ROOM-CLOSED: <slug>]` | picard | Info | `tng-ready-room` | `tng-engineering` |
| `[READY-ROOM-CONDITIONAL-CLOSE: <slug>]` | picard | Info | `tng-ready-room` | `tng-engineering` |
| `[MDR-ISSUED: <slug>]` | picard | Info | `tng-ready-room` | `tng-engineering` |
| `[AC-APPROVED: <slug>]` | picard | Info | `tng-ready-room` | — |
| `[PRIORITY: P0 \| ...]` | any agent | Critical | `tng-oncall` | `tng-ready-room` |
| `[PRIORITY: P1 \| ...]` | any agent | High | `tng-oncall` | `tng-ready-room` |
| `[PRIORITY: P2/P3 \| ...]` | any agent | Medium/Low | `tng-ready-room` | — |
| `[BLOCKER: <description>]` | any agent | High | `tng-oncall` | `tng-execution` |
| `[execution-complete]` | riker | Info | `tng-execution` | — |
| `[ROLLBACK-PARTIAL: <slug>]` | riker | High | `tng-execution` | `tng-oncall` |
| `[ROLLBACK-FULL: <slug>]` | riker | Critical | `tng-oncall` | `tng-execution` |
| Track C verdict (PASS/CONDITIONAL/FAIL) | worf/troi/crusher | Info/High | `tng-review` | — |
| `[FIX-IN-PLACE: <item>]` | picard | Info | `tng-review` | — |
| `[SCOPED-READY-ROOM: <item>]` | picard | Info | `tng-review` | `tng-ready-room` |
| `[MISSION-CLOSED: <slug>]` | picard | Info | `tng-stakeholders` | `tng-engineering` |
| `[EXTERNAL-EVENT: ... severity: critical]` | any agent | Critical | `tng-oncall` | `tng-ready-room` |
| `[EXTERNAL-EVENT: ... severity: significant/informational]` | any agent | Info | `tng-ready-room` | — |

---

## Payload Formats

### Microsoft Teams (Adaptive Card)

```json
{
  "@type": "MessageCard",
  "@context": "http://schema.org/extensions",
  "themeColor": "0076D7",
  "summary": "TNG Bridge Signal",
  "sections": [{
    "activityTitle": "🖖 TNG Bridge — [SIGNAL_NAME]",
    "activitySubtitle": "[MISSION_SLUG]",
    "activityText": "[DESCRIPTION]",
    "facts": [
      { "name": "Agent", "value": "[AGENT_NAME]" },
      { "name": "Priority", "value": "[P0|P1|P2|P3]" },
      { "name": "Time", "value": "[ISO_TIMESTAMP]" }
    ]
  }]
}
```

### Slack (Block Kit)

```json
{
  "blocks": [
    {
      "type": "header",
      "text": { "type": "plain_text", "text": "🖖 TNG Bridge — [SIGNAL_NAME]" }
    },
    {
      "type": "section",
      "fields": [
        { "type": "mrkdwn", "text": "*Mission:*\n[MISSION_SLUG]" },
        { "type": "mrkdwn", "text": "*Agent:*\n[AGENT_NAME]" },
        { "type": "mrkdwn", "text": "*Priority:*\n[P0|P1|P2|P3]" }
      ]
    },
    {
      "type": "section",
      "text": { "type": "mrkdwn", "text": "[DESCRIPTION]" }
    }
  ]
}
```

---

## Multi-Channel Dispatch Pattern

When a signal fans out to multiple channels, fire all webhooks in parallel — fire-and-forget.

```bash
# Reusable helper: silently skips blank URLs, never blocks on failure
_tng_notify() {
  local url="$1" msg="$2"
  [ -n "$url" ] && curl -s -X POST "$url" \
    -H 'Content-Type: application/json' \
    -d "{\"text\":\"$msg\"}" &
}

# Example: [READY-ROOM-OPEN] fans out to tng-ready-room, tng-stakeholders, tng-bridge
_tng_notify "$TEAMS_WEBHOOK_READY_ROOM"   "🚀 Ready Room opened — <slug>"
_tng_notify "$TEAMS_WEBHOOK_STAKEHOLDERS" "🚀 Ready Room opened — <slug>"
_tng_notify "$TEAMS_WEBHOOK_BRIDGE"       "🚀 [READY-ROOM-OPEN] Ready Room opened — <slug>"
# No wait — all fire-and-forget
```

---

## GitHub Actions Integration

For automated workflows (e.g., CI failures, MDR-to-issue creation), use the `curl` step pattern with per-channel secrets:

```yaml
- name: Notify on completion
  if: always()
  env:
    TEAMS_WEBHOOK_BRIDGE: ${{ secrets.TEAMS_WEBHOOK_BRIDGE }}
    TEAMS_WEBHOOK_EXECUTION: ${{ secrets.TEAMS_WEBHOOK_EXECUTION }}
  run: |
    _notify() { [ -n "$1" ] && curl -s -X POST "$1" -H "Content-Type: application/json" -d "{\"text\":\"$2\"}" || true; }
    _notify "$TEAMS_WEBHOOK_EXECUTION" "🖖 TNG Bridge — CI Complete | ${{ github.workflow }} | ${{ job.status }}"
    _notify "$TEAMS_WEBHOOK_BRIDGE"    "🖖 TNG Bridge — CI Complete | ${{ github.workflow }} | ${{ job.status }}"
```

The `|| true` ensures a webhook failure never fails the workflow step.

---

## Security Requirements (worf-approved)

1. **Never commit webhook URLs** to the repository. Use GitHub Secrets or a gitignored local file.
2. The `knowledge_base/current/teams-webhook.md` and `knowledge_base/current/slack-webhook.md` files must be listed in `.gitignore`.
3. Webhook URLs grant write access to a channel — treat them as secrets with the same care as API keys.
4. Rotate webhook URLs if they are ever exposed in logs or commits.
5. Use HTTPS endpoints only. Reject any `http://` webhook URL.
6. Notifications must never include PII, authentication credentials, or internal IP addresses in the payload.

---

## Testing the Integration

```bash
# Test Teams webhook (replace URL with your actual webhook)
curl -X POST "$TEAMS_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"@type":"MessageCard","summary":"TNG Test","themeColor":"0076D7","sections":[{"activityTitle":"🖖 TNG Bridge — Test Signal","activityText":"Connectivity verified. geordi returns control."}]}'

# Test Slack webhook
curl -X POST "$SLACK_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"text":"🖖 TNG Bridge — Test Signal. Connectivity verified."}'
```

---

## Recommended Channel Topology

| Channel name | Slug | Purpose | Key signals |
|---|---|---|---|
| `#tng-bridge` | `tng-bridge` | Full audit feed — all signals | Everything |
| `#tng-ready-room` | `tng-ready-room` | Decision phase visibility | READY-ROOM-OPEN/CLOSED, MDR, AC, PRIORITY, CONFLICT |
| `#tng-execution` | `tng-execution` | Bridge execution feed | Wave dispatches, BLOCKER, execution-complete, ROLLBACK |
| `#tng-review` | `tng-review` | Track C review feed | Verdicts, FIX-IN-PLACE, SCOPED-READY-ROOM |
| `#tng-oncall` | `tng-oncall` | Urgent escalations only | P0, P1, BLOCKER, ROLLBACK-FULL |
| `#tng-stakeholders` | `tng-stakeholders` | Business-level visibility | READY-ROOM-OPEN, MISSION-CLOSED |

You do not need all channels active. A minimal setup with only `tng-bridge` and `tng-oncall` covers the most important cases.

---

## Version History

```
2026-04-13: geordi — Multi-channel routing added. Expanded from 2 channels to 6 logical channels with fan-out routing table, multi-webhook dispatch pattern, and per-channel env var naming convention.
2026-04-11: geordi — Created. Covers Teams, Slack, payload formats, signal mapping, security requirements.
```
