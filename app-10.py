
from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("trustnest_website.html")

@app.route("/privacy")
def privacy():
    return render_template("trustnest_privacy.html")

@app.route("/terms")
def terms():
    return render_template("trustnest_terms.html")

@app.route("/dashboard")
def dashboard():
    return render_template("trustnest_dashboard.html")

@app.route("/login")
def login():
    return render_template("trustnest_login.html")

@app.route("/signup")
def signup():
    return render_template("trustnest_signup.html")

@app.route("/contact")
def contact():
    return render_template("trustnest_contact.html")

@app.route("/contact_submit", methods=["POST"])
def contact_submit():
    name = request.form.get("name")
    hotel = request.form.get("hotel_name")
    return f"<h1 style='color:#00d4ff;background:#1a1a2e;padding:40px;text-align:center'>Thank you {name}!</h1>"

@app.route("/authenticate", methods=["GET", "POST"])
def authenticate():
    return redirect("/dashboard")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
