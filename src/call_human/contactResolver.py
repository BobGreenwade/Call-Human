# Resolves contact based on role, opt-in, and persona

from embedding import get_user_profile
from .call_config import CONFIG

def resolve_contact(role, username="User"):
    profile = get_user_profile(username)
    if role == "emergency_contact" and profile.get("escalation_opt_in"):
        contacts = profile.get("emergency_contacts", [])
        return contacts[0] if contacts else default_contact("family")
    return CONFIG.get("contact_profiles", {}).get(role, default_contact("default"))

def default_contact(recipient_type):
    return {
        "name": "Platform Safeguard Desk",
        "channel": "email",
        "type": recipient_type,
        "persona": "default"
    }
