
from flask import Flask, request, redirect, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

def read_file(filename):
    filepath = os.path.join(BASE_DIR, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    return f"<h1>Page coming soon!</h1>"

@app.route("/")
@app.route("/home")
def home():
    return read_file("trustnest_website.html")

@app.route("/pricing")
def pricing():
    return read_file("trustnest_pricing.html")

@app.route("/signup")
def signup():
    return read_file("trustnest_signup.html")

@app.route("/login")
def login():
    return read_file("trustnest_login.html")

@app.route("/contact")
def contact():
    return read_file("trustnest_contact.html")

@app.route("/privacy")
def privacy():
    return read_file("trustnest_privacy.html")

@app.route("/terms")
def terms():
    return read_file("trustnest_terms.html")

@app.route("/contact_submit", methods=["POST"])
def contact_submit():
    name = request.form.get("name")
    hotel = request.form.get("hotel_name")
    return f"<h1 style=\'color:#00d4ff;background:#1a1a2e;padding:40px;text-align:center\'>Thank you {name} from {hotel}!</h1>"

@app.route("/authenticate", methods=["GET", "POST"])
def authenticate():
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return read_file("trustnest_dashboard.html")

@app.route("/manifest.json")
def manifest():
    return send_from_directory(BASE_DIR, "manifest.json")

@app.route("/service_worker.js")
def service_worker():
    return send_from_directory(BASE_DIR, "service_worker.js", mimetype="application/javascript")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
