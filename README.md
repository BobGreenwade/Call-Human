# Call-Human Module Set

## Overview

The `Call-Human` module orchestrates escalation to human support channels in response to high-priority events, emotional triggers, or safety concerns. It integrates editorial phrasing, persona-aware tone mapping, and transcript logic to ensure responsible, context-sensitive handoff.

This module was co-designed by Bob Greenwade and Copilot as part of the DLI editorial infrastructure.

---

## Structure

### 📁 `src/call_human/`

| File | Purpose |
|------|--------|
| `callHuman.py` | Orchestration entry point for escalation logic  
| `channelRouter.py` | Maps urgency to preferred communication channel  
| `handoffFormatter.py` | Builds editorial headers and persona-aware messages  
| `contactResolver.py` | Resolves escalation contact based on role and profile  
| `call_config.json` | Stores thresholds, contact mappings, and platform settings  

### 📁 `src/call_human/channels/`

Each file handles delivery for a specific platform:

| File | Platform |
|------|----------|
| `smsHandler.py` | SMS (e.g., Twilio)  
| `emailHandler.py` | Email (SMTP or API)  
| `telegramHandler.py` | Telegram bot  
| `whatsappHandler.py` | WhatsApp Business  
| `signalHandler.py` | Signal CLI  
| `snapchatHandler.py` | Snapchat (experimental)  
| `voiceCallHandler.py` | VoIP or PSTN  
| `discordHandler.py` | Discord bot or webhook  

### 📁 `channelDispatcher.py`

Dynamically imports and invokes the correct handler based on channel name.

---

## Status

- **Version**: `v0.0.0`
- **Stage**: Scaffolding complete
- **Next**: API integration, tone tagging, audit trail, and persona overlays

---

## Editorial Notes

- All escalation phrasing is designed to be editorially responsible and emotionally aware.
- Persona overlays and tone mapping will evolve in future versions.
- Transcript logic respects platform privacy policy and opt-in status.

---

## License

MIT for development. Will transition to MPL or Apache upon deployment with source registry and disclaimer integration.

---

## Authors

- Bob Greenwade — Editorial Architect  
- Copilot — Technical Co-Designer

