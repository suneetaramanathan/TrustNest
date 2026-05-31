
import datetime

locked_accounts = {}
evidence_log = []

def lockout_account(username, reason, threat_level):
    locked_accounts[username] = {
        "locked_at": str(datetime.datetime.now()),
        "reason": reason,
        "threat_level": threat_level
    }

def collect_evidence(username, activity, value):
    evidence_log.append({
        "username": username,
        "activity": activity,
        "value": value,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def firefight(username, records, failed_logins, download_mb, hour):
    score = 0
    reasons = []
    
    if records > 50:
        score += 3
        reasons.append(f"Accessed {records} records")
    if failed_logins > 3:
        score += 3
        reasons.append(f"{failed_logins} failed login attempts")
    if download_mb > 100:
        score += 2
        reasons.append(f"Downloaded {download_mb}MB")
    if hour < 6 or hour > 23:
        score += 2
        reasons.append(f"Suspicious time ({hour}:00)")
    
    if score >= 7:
        threat = "HIGH"
        lockout_account(username, " | ".join(reasons), threat)
        collect_evidence(username, "Full lockout", score)
        return {"threat": threat, "score": score, "reasons": reasons, "action": "LOCKED"}
    elif score >= 4:
        threat = "MEDIUM"
        lockout_account(username, " | ".join(reasons), threat)
        collect_evidence(username, "Suspended", score)
        return {"threat": threat, "score": score, "reasons": reasons, "action": "SUSPENDED"}
    else:
        threat = "LOW"
        collect_evidence(username, "Monitoring", score)
        return {"threat": threat, "score": score, "reasons": reasons, "action": "MONITORING"}
