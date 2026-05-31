
from flask import Flask, request, redirect, send_from_directory
import os

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

@app.route("/dashboard")
def dashboard():
    return open("trustnest_dashboard.html").read()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
