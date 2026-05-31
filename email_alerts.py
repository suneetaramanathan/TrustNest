
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "inboxsuneeta26@gmail.com"
APP_PASSWORD = "your-app-password-here"

def send_real_alert(hotel_manager_email, staff_name, threat_level, reasons):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = hotel_manager_email
    msg["Subject"] = f"TrustNest Alert - {threat_level} THREAT - {staff_name}"
    body = f"""
Dear Hotel Manager,

TrustNest detected a {threat_level} threat.

Staff: {staff_name}
Reasons: {", ".join(reasons)}

Dashboard: https://web-production-0b35.up.railway.app/dashboard

TrustNest Security System
    """
    msg.attach(MIMEText(body, "plain"))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, hotel_manager_email, msg.as_string())
        server.quit()
        print(f"Email sent!")
    except Exception as e:
        print(f"Error: {e}")
