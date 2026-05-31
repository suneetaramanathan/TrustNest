
from flask import Flask, request, redirect, send_from_directory
import os
from firefight import firefight, locked_accounts, evidence_log

app = Flask(__name__, static_folder="static")

@app.route("/manifest.json")
def manifest():
    return send_from_directory(".", "manifest.json")

@app.route("/service_worker.js")
def service_worker():
    return send_from_directory(".", "service_worker.js", mimetype="application/javascript")

@app.route("/")
@app.route("/home")
def home():
    return open("trustnest_website.html").read()

@app.route("/signup")
def signup():
    return open("trustnest_signup.html").read()

@app.route("/login")
def login():
    return open("trustnest_login.html").read()

@app.route("/contact")
def contact():
    return open("trustnest_contact.html").read()

@app.route("/contact_submit", methods=["POST"])
def contact_submit():
    name = request.form.get("name")
    hotel = request.form.get("hotel_name")
    return f"<h1 style=\'color:#00d4ff;background:#1a1a2e;padding:40px;text-align:center\'>Thank you {name} from {hotel}! We will contact you soon!</h1>"

@app.route("/authenticate", methods=["GET", "POST"])
def authenticate():
    return redirect("/dashboard")

@app.route("/scan", methods=["POST"])
def scan():
    username = request.form.get("username")
    records = int(request.form.get("records", 0))
    failed_logins = int(request.form.get("failed_logins", 0))
    download_mb = int(request.form.get("download_mb", 0))
    hour = int(request.form.get("hour", 12))
    result = firefight(username, records, failed_logins, download_mb, hour)
    color = "#ff4444" if result["threat"] == "HIGH" else "#ff8800" if result["threat"] == "MEDIUM" else "#00aa44"
    return f"""
    <div style="background:{color};padding:20px;margin:10px;border-radius:8px;color:white;">
    <h2>{result["threat"]} THREAT — {result["action"]}</h2>
    <p>Score: {result["score"]}/10</p>
    <p>Reasons: {", ".join(result["reasons"]) if result["reasons"] else "Normal activity"}</p>
    </div>"""

@app.route("/dashboard")
def dashboard():
    return open("trustnest_dashboard.html").read()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
