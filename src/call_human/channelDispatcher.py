# Dispatches escalation payload to the appropriate channel handler

def dispatch_channel(channel, payload, contact_info):
    """
    Dynamically dispatches escalation to the correct channel handler.
    Args:
        channel (str): Channel name (e.g., 'sms', 'email', 'discord')
        payload (dict): Escalation payload (header, message, transcript, metadata)
        contact_info (dict): Contact details for escalation target
    Returns:
        dict: delivery_status
    """
    try:
        handler = _get_handler(channel)
        return handler.send_escalation(payload, contact_info)
    except Exception as e:
        return {"status": "error", "channel": channel, "error": str(e)}

def _get_handler(channel):
    """
    Imports the appropriate handler module based on channel name.
    """
    if channel == "sms":
        import channels.smsHandler as handler
    elif channel == "email":
        import channels.emailHandler as handler
    elif channel == "telegram":
        import channels.telegramHandler as handler
    elif channel == "whatsapp":
        import channels.whatsappHandler as handler
    elif channel == "signal":
        import channels.signalHandler as handler
    elif channel == "snapchat":
        import channels.snapchatHandler as handler
    elif channel == "voice_call":
        import channels.voiceCallHandler as handler
    elif channel == "discord":
        import channels.discordHandler as handler
    elif channel == "internal_dm":
        import channels.internalDMHandler as handler  # Optional future stub
    else:
        raise ValueError(f"Unsupported channel: {channel}")
    return handler
