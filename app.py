#TrustNest v2.0 - Updated June 2026
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("trustnest_website.html")

@app.route("/signup")
def signup():
    return render_template("trustnest_signup.html")

@app.route("/login")
def login():
    return render_template("trustnest_login.html")

@app.route("/contact")
def contact():
    return render_template("trustnest_contact.html")

@app.route("/terms")
def terms():
    return render_template("trustnest_terms.html")

@app.route("/privacy")
def privacy():
    return render_template("trustnest_privacy.html")

@app.route("/pricing")
def pricing():
    return render_template("trustnest_pricing.html")

@app.route("/authenticate", methods=["GET", "POST"])
def authenticate():
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("trustnest_dashboard.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
