
from flask import Flask, request, redirect, send_from_directory
import os
import stripe
import json

stripe.api_key = "sk_test_your_secret_key_here"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "price_ids.json"), "r") as f:
    all_prices = json.load(f)

PRICE_MAP = {
    "basic": all_prices["TrustNest Basic"],
    "standard": all_prices["TrustNest Standard"],
    "premium": all_prices["TrustNest Premium"]
}

app = Flask(__name__)

def read_file(filename):
    return open(os.path.join(BASE_DIR, filename)).read()

@app.route("/manifest.json")
def manifest():
    return send_from_directory(BASE_DIR, "manifest.json")

@app.route("/service_worker.js")
def service_worker():
    return send_from_directory(BASE_DIR, "service_worker.js", mimetype="application/javascript")

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

@app.route("/checkout/<plan>/<period>")
def checkout(plan, period):
    price_id = PRICE_MAP[plan][period]
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{"price": price_id, "quantity": 1}],
        mode="subscription",
        success_url="https://web-production-0b35.up.railway.app/dashboard",
        cancel_url="https://web-production-0b35.up.railway.app/pricing",
    )
    return redirect(session.url)

@app.route("/dashboard")
def dashboard():
    return read_file("trustnest_dashboard.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
