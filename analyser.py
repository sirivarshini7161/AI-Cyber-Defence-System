def risk_score(log):
    """
    Assign risk score based on event type
    """

    event = log.get("event", "").lower()

    if "failed login" in event:
        return 80

    if "sql" in event:
        return 95

    if "ddos" in event or "traffic spike" in event:
        return 90

    if "malware" in event:
        return 85

    return 10