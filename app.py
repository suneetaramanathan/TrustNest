from flask import Flask, request, redirect, render_template, session
import os
import stripe
import json

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "trustnest2026")

# Load hotel credentials
try:
    with open("hotel_credentials.json", "r") as f:
        hotel_credentials = json.load(f)
except Exception as e:
    print(f"Error loading credentials: {e}")
    hotel_credentials = {}

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

@app.route("/contact_submit", methods=["POST"])
def contact_submit():
    name = request.form.get("name")
    hotel = request.form.get("hotel_name")
    return f"<h1 style='color:#00d4ff;background:#1a1a2e;padding:40px;text-align:center'>Thank you {name} from {hotel}!</h1>"

@app.route("/authenticate", methods=["GET", "POST"])
def authenticate():
    if request.method == "POST":
        email = request.form.get("username")
        password = request.form.get("password")
        if email in hotel_credentials:
            if hotel_credentials[email]["password"] == password:
                session["hotel"] = hotel_credentials[email]["hotel"]
                session["email"] = email
                return redirect("/dashboard")
        return redirect("/login")
    return redirect("/login")

@app.route("/dashboard")
def dashboard():
    hotel_name = session.get("hotel", "Demo Hotel")
    return f"""
    <html>
    <head>
        <title>TrustNest Dashboard</title>
        <style>
            body{{font-family:Arial;background:#1a1a2e;color:white;margin:0;padding:0;}}
            nav{{background:#16213e;padding:15px;display:flex;justify-content:space-between;}}
            .logo{{color:#00d4ff;text-decoration:none;font-size:20px;font-weight:bold;}}
            h1{{color:#00d4ff;text-align:center;padding-top:20px;}}
            .hotel{{text-align:center;color:#aaa;margin-bottom:20px;}}
            .stats{{display:flex;justify-content:center;gap:20px;margin:20px;flex-wrap:wrap;}}
            .stat{{background:#16213e;padding:20px;border-radius:10px;text-align:center;min-width:150px;}}
            .stat h2{{color:#00d4ff;}}
            .alerts{{padding:20px;}}
            .alert{{background:#ff4444;padding:15px;margin:10px;border-radius:8px;}}
            .normal{{background:#00aa44;padding:15px;margin:10px;border-radius:8px;}}
        </style>
    </head>
    <body>
    <nav>
        <a href="/home" class="logo">🔐 TrustNest</a>
        <a href="/login" style="color:#aaa;text-decoration:none;">Logout</a>
    </nav>
    <h1>🔐 TrustNest Security Dashboard</h1>
    <p class="hotel">Welcome — {hotel_name}</p>
    <div class="stats">
        <div class="stat"><h2>210</h2><p>Activities Scanned</p></div>
        <div class="stat"><h2>199</h2><p>Normal ✅</p></div>
        <div class="stat"><h2>11</h2><p>Suspicious 🚨</p></div>
    </div>
    <div class="alerts">
        <h2>Live Security Alerts:</h2>
        <div class="alert">🚨 Unknown Hacker — 80 records at 3:00am — Account LOCKED!</div>
        <div class="alert">🚨 John Mueller — 65 records + 350MB download — Account LOCKED!</div>
        <div class="normal">✅ Anna Weber — 8 records at 9:00am — Normal</div>
        <div class="normal">✅ Maria Schmidt — 3 records at 10:00am — Normal</div>
        <div class="normal">✅ Peter Klein — 18 records at 11:00am — Normal</div>
    </div>
    </body>
    </html>
    """

@app.route("/checkout/<plan>/<period>")
def checkout(plan, period):
    try:
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

        if plan not in price_ids or period not in price_ids[plan]:
            return "Invalid plan or period", 400

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{"price": price_ids[plan][period], "quantity": 1}],
            mode="subscription",
            success_url="https://web-production-0b35.up.railway.app/dashboard",
            cancel_url="https://web-production-0b35.up.railway.app/pricing",
        )
        return redirect(checkout_session.url)

    except stripe.error.StripeError as e:
        return f"Stripe error: {str(e)}", 400
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
