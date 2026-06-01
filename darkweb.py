
def check_dark_web(email):
    
    known_breached = [
        "admin@hotel.com",
        "manager@oldhotel.de",
        "reception@testhotel.com"
    ]
    
    if email in known_breached:
        return {
            "breached": True,
            "email": email,
            "action": "Force password reset immediately!"
        }
    else:
        return {
            "breached": False,
            "email": email,
            "action": "No action needed"
        }
