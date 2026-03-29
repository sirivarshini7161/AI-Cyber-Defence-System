def generate_response(attack_type, score):
    """
    AI response generator based on attack type + risk score
    """

    if score >= 90:
        level = "CRITICAL"
    elif score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    if attack_type == "Brute Force Attack":
        return f"🔐 {level}: Multiple failed login attempts detected. Block IP immediately."

    if attack_type == "SQL Injection Attack":
        return f"💉 {level}: SQL Injection attempt detected. Secure database queries."

    if attack_type == "DDoS Attack":
        return f"🌐 {level}: Traffic spike detected. Possible DDoS attack. Enable rate limiting."

    if attack_type == "Malware Activity":
        return f"🦠 {level}: Malware behavior detected. Isolate system immediately."

    return f"✅ {level}: System is normal. No threat detected."