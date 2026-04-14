# Notification Integration Guide

**Owner:** geordi | **Reviewed by:** worf | **Last Updated:** 2026-04-11

---

## Purpose

This document defines the connectivity layer between the TNG agent system and external team communication tools (Microsoft Teams, Slack). It covers webhook setup, payload formats, which agent signals trigger notifications, and security requirements.

All notifications are **fire-and-forget** — agents never block on delivery. A failed notification is logged and ignored; it never halts a mission.

---

## Supported Channels

| Channel | Env Var | Config File | Protocol |
|---------|---------|-------------|----------|
| Microsoft Teams | `TEAMS_WEBHOOK_URL` | `knowledge_base/current/teams-webhook.md` | Incoming Webhook (Adaptive Cards) |
| Slack | `SLACK_WEBHOOK_URL` | `knowledge_base/current/slack-webhook.md` | Incoming Webhook (Block Kit) |

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

Agents emit structured signals throughout missions. The following signals fire external notifications when a webhook is configured.

| Signal | Sender | Target Channel | Urgency |
|--------|--------|---------------|---------|
| `[READY-ROOM-OPEN: <slug>]` | picard | Stakeholder channel | Info |
| `[READY-ROOM-CLOSED: <slug>]` | picard | Engineering channel | Info |
| `[MDR-ISSUED: <slug>]` | picard | Engineering channel | Info |
| `[BLOCKER: <description>]` | any agent | On-call / urgent channel | High |
| `[MISSION-CLOSED: <slug>]` | picard | Team summary channel | Info |
| `[P0: <description>]` | picard | On-call channel | Critical |
| `[P1: <description>]` | picard | Engineering channel | High |

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

## GitHub Actions Integration

For automated workflows (e.g., CI failures, MDR-to-issue creation), use the `curl` step pattern:

```yaml
- name: Notify Teams on completion
  if: always()
  env:
    TEAMS_WEBHOOK_URL: ${{ secrets.TEAMS_WEBHOOK_URL }}
  run: |
    if [ -n "$TEAMS_WEBHOOK_URL" ]; then
      curl -s -X POST "$TEAMS_WEBHOOK_URL" \
        -H "Content-Type: application/json" \
        -d "{
          \"@type\": \"MessageCard\",
          \"summary\": \"TNG Bridge Signal\",
          \"themeColor\": \"0076D7\",
          \"sections\": [{
            \"activityTitle\": \"🖖 TNG Bridge — CI Complete\",
            \"activitySubtitle\": \"${{ github.repository }}\",
            \"activityText\": \"Workflow: ${{ github.workflow }} | Status: ${{ job.status }}\"
          }]
        }" || true
    fi
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

| Channel Name | Purpose | Signals |
|-------------|---------|---------|
| `#tng-bridge` | All agent signals, main feed | All signals |
| `#tng-engineering` | Dev team notifications | MDR-ISSUED, READY-ROOM-CLOSED, MISSION-CLOSED |
| `#tng-oncall` | Urgent escalations only | P0, P1, BLOCKER |
| `#tng-stakeholders` | Business-level visibility | READY-ROOM-OPEN, MISSION-CLOSED |

---

## Version History

```
2026-04-11: geordi — Created. Covers Teams, Slack, payload formats, signal mapping, security requirements.
```
