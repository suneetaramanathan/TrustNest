import stripe
import os
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
from flask import Flask, request, redirect, render_template
import os

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

@app.route("/privacy")
def privacy():
    return render_template("trustnest_privacy.html")

@app.route("/terms")
def terms():
    return render_template("trustnest_terms.html")

@app.route("/pricing")
def pricing():
    return render_template("trustnest_pricing.html")
    
    @app.route("/checkout/<plan>/<period>")
def checkout(plan, period):
    price_ids = {
        "basic": {
            "monthly": "price_1TdKacQ5mjF6aOU8QlGIO7W6",
            "quarterly": "price_1TdKadQ5mjF6aOU8aQxNcOt0",
            "biannual": "price_1TdKadQ5mjF6aOU8VsUdPiav",
            "annual": "price_1TdKadQ5mjF6aOU8bS6L4Pjs"
        },
        "standard": {
            "monthly": "price_1TdKaeQ5mjF6aOU8k3rgE0f2",
            "quarterly": "price_1TdKaeQ5mjF6aOU8aiVh2fJa",
            "biannual": "price_1TdKaeQ5mjF6aOU8TEsxCevi",
            "annual": "price_1TdKafQ5mjF6aOU8yf7CybsX"
        },
        "premium": {
            "monthly": "price_1TdKafQ5mjF6aOU8bRx555sL",
            "quarterly": "price_1TdKagQ5mjF6aOU8DIZ6vzKw",
            "biannual": "price_1TdKagQ5mjF6aOU8JBJHJKHW",
            "annual": "price_1TdKagQ5mjF6aOU8rIZ20Jjl"
        }
    }
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{"price": price_ids[plan][period], "quantity": 1}],
        mode="subscription",
        success_url="https://web-production-0b35.up.railway.app/dashboard",
        cancel_url="https://web-production-0b35.up.railway.app/pricing",
    )
    return redirect(session.url)

@app.route("/authenticate", methods=["GET", "POST"])
def authenticate():
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("trustnest_dashboard.html")

@app.route("/contact_submit", methods=["POST"])
def contact_submit():
    name = request.form.get("name")
    hotel = request.form.get("hotel_name")
    return f"<h1 style='color:#00d4ff;background:#1a1a2e;padding:40px;text-align:center'>Thank you {name}!</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
