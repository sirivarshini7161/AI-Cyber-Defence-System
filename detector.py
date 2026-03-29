def detect_attack(log):
    """
    Detect attack type from input log
    Accepts: dict with key 'event'
    """

    event = log.get("event", "").lower()

    if "failed login" in event or "login failed" in event:
        return "Brute Force Attack"

    if "sql" in event:
        return "SQL Injection Attack"

    if "ddos" in event or "traffic spike" in event or "request spike" in event:
        return "DDoS Attack"

    if "malware" in event:
        return "Malware Activity"

    return "Normal Traffic"