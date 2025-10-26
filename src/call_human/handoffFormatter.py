# Builds headers and editorialized messages

from paraphrase import paraphrase
from emotion import map_emotion_to_tone
from .call_config import CONFIG

def build_header(channel, username, persona, platform, reason, recipient_type="default"):
    custom = CONFIG.get("custom_headers", {}).get(channel, {}).get(recipient_type)
    if custom:
        return custom.format(User=username, Persona=persona, Platform=platform, Reason=reason)

    if channel == "email":
        if recipient_type == "family":
            return (
                f"To: Family Member\nFrom: {platform} Escalation System\nSubject: Concern for {username}\n\n"
                f"This is to inform you that {username}, a user here at {platform}, "
                f"has shown signs of distress or delusional escalation.\nReason: {reason}"
            )
        elif recipient_type == "law_enforcement":
            return (
                f"To: Scotland Yard\nFrom: {platform} Safeguard Desk\nSubject: Escalation Alert\n\n"
                f"{username} has triggered a high-severity escalation. Reason: {reason}"
            )
        else:
            return (
                f"To: {CONFIG.get('contact_profiles', {}).get(recipient_type, {}).get('name', 'Safeguard Desk')}\n"
                f"From: {platform} Escalation System\nSubject: Escalation for {username}\n\nReason: {reason}"
            )
    elif channel == "voice_call":
        base = (
            f"Hello, this is {persona} calling on behalf of {platform}. "
            f"I'm concerned about {username} due to recent chat messages. Reason: {reason}"
        )
        return paraphrase(base, persona, map_emotion_to_tone(reason), style="handoff")
    elif channel == "push":
        return f"{platform} escalation triggered for {username}. Reason: {reason}"
    elif channel == "sms":
        return f"{platform}: Escalation alert for {username}. Reason: {reason}"
    elif channel == "internal_dm":
        return f"[{platform} Alert] {username} flagged for escalation. Reason: {reason}"
    else:
        return f"{platform} escalation notice for {username}. Reason: {reason}"

def editorialize_message(base_message, persona, tone):
    return paraphrase(base_message, persona, tone, style="handoff")
