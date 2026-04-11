---
name: teams-webhook
description: Microsoft Teams incoming webhook URL for Bridge Notifications
type: reference
---

# Teams Webhook Configuration

## Webhook URL

```
# Paste your Teams incoming webhook URL below — leave blank to disable notifications
TEAMS_WEBHOOK_URL=
```

## How to get the URL

1. Open the target Teams channel
2. Click `...` → **Connectors** → **Incoming Webhook** → **Configure**
3. Give it a name (e.g., `TNG Bridge`) and optionally upload an icon
4. Click **Create** → copy the generated URL
5. Paste it into `TEAMS_WEBHOOK_URL` above

## Notification mode

Default: **milestone-only**

To enable full visibility (parallel batch dispatches + completions), tell picard: *"teams full visibility"*

## Test command

Once the URL is set, verify it works:

```bash
curl -s -X POST \
  -H 'Content-Type: application/json' \
  -d '{"text":"🖖 TNG Bridge connected — notifications active"}' \
  "<your-webhook-url>"
```

A `1` response from Teams means success.
