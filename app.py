# TrustNest v2.0 - Updated June 2026
from flask import Flask, request, redirect

app = Flask(__name__)

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

@app.route("/authenticate", methods=["GET", "POST"])
def authenticate():
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return open("trustnest_dashboard.html").read()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
