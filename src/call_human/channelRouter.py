# Maps urgency and config to preferred channel

def route_channel(urgency, available_channels, config):
    preferred = config.get("NOTIFY_CHANNEL", {}).get(urgency, "log_only")
    if preferred in available_channels:
        return preferred
    for fallback in ["internal_dm", "email", "sms"]:
        if fallback in available_channels:
            return fallback
    return "log_only"
