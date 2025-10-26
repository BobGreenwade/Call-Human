# Orchestrates escalation flow and delegates to submodules

from .channelRouter import route_channel
from .contactResolver import resolve_contact
from .handoffFormatter import build_header, editorialize_message
from .call_config import CONFIG
from transcript import save_transcript
from emotion import analyze_emotion, map_emotion_to_tone
from learning import run_learning

def escalate_to_human(reason, urgency="moderate", role="emergency_contact", include_transcript=True, username="User"):
    available_channels = CONFIG.get("enabled_channels", [])
    contact = resolve_contact(role, username)
    channel = route_channel(urgency, available_channels, CONFIG)

    transcript_file = save_transcript(username) if include_transcript else None
    privacy_policy = CONFIG.get("PLATFORM_PRIVACY_POLICY", "restrictive")
    allow_full_send = include_transcript and urgency == "high" and privacy_policy != "restrictive"
    transcript_action = (
        "send_full_transcript" if allow_full_send else
        "share_filename_only" if transcript_file else
        "hold_transcript"
    )

    emotion_vector = analyze_emotion(reason)
    persona = contact.get("persona", "default")
    tone = map_emotion_to_tone(emotion_vector)

    header = build_header(channel, username, persona, CONFIG.get("PLATFORM_NAME", "Platform"), reason, contact.get("type", "default"))
    editorial_message = editorialize_message(f"Escalation triggered via {channel} to {contact['name']} for reason: {reason}", persona, tone)

    try:
        feedback_result = run_learning("classification", {
            "reason": reason,
            "urgency": urgency,
            "persona": persona,
            "channel": channel
        })
        print(f"[ML FEEDBACK] {feedback_result}")
    except Exception:
        pass

    return {
        "status": "escalated",
        "reason": reason,
        "urgency": urgency,
        "contact": contact["name"],
        "channel": channel,
        "transcript_action": transcript_action,
        "transcript_file": transcript_file,
        "message": editorial_message,
        "header": header
    }
