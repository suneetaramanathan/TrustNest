
from flask import Flask, request, redirect
import os

app = Flask(__name__)

WEBSITE = '''<!DOCTYPE html>
<html>
<head>
    <title>TrustNest</title>
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#00d4ff">
    <style>
        body{font-family:Arial;background:#1a1a2e;color:white;margin:0;padding:0;}
        nav{background:#16213e;padding:15px;display:flex;justify-content:space-between;align-items:center;}
        .logo{color:#00d4ff;text-decoration:none;font-size:20px;font-weight:bold;}
        .nav-links a{color:white;text-decoration:none;margin:0 15px;}
        .get-started{color:#00d4ff;border:1px solid #00d4ff;padding:8px 15px;border-radius:20px;}
        .hero{text-align:center;padding:80px 20px;background:#1a1a2e;}
        h1{color:#00d4ff;font-size:48px;}
        .button{background:#00d4ff;color:black;padding:15px 40px;border-radius:25px;font-size:18px;text-decoration:none;display:inline-block;margin-top:20px;}
        .features{display:flex;justify-content:center;gap:30px;padding:60px 20px;background:#1a1a2e;flex-wrap:wrap;}
        .feature{background:#16213e;padding:30px;border-radius:15px;width:220px;text-align:center;}
        .feature h3{color:#00d4ff;}
        .pricing{text-align:center;padding:60px 20px;background:#16213e;}
        .price-card{display:inline-block;background:#1a1a2e;padding:30px;border-radius:15px;margin:10px;width:180px;}
        .price{color:#00d4ff;font-size:32px;font-weight:bold;}
        footer{text-align:center;padding:20px;color:#aaa;background:#1a1a2e;}
    </style>
</head>
<body>
<nav>
    <a href="/home" class="logo">🔐 TrustNest</a>
    <div class="nav-links">
        <a href="/home">Home</a>
        <a href="/pricing">Pricing</a>
        <a href="/contact">Contact</a>
        <a href="/login">Login</a>
        <a href="/signup" class="get-started">Get Started</a>
    </div>
</nav>
<div class="hero">
    <h1>🔐 TrustNest</h1>
    <p style="font-size:20px">AI-Powered Cybersecurity for Independent Hotels</p>
    <p>Protect your guests. Secure your data. Sleep peacefully.</p>
    <a href="/signup" class="button">Get Started Free</a>
</div>
<div class="features">
    <div class="feature"><h3>🤖 AI Detection</h3><p>Monitors hotel systems 24/7</p></div>
    <div class="feature"><h3>🚨 Instant Alerts</h3><p>Get notified immediately</p></div>
    <div class="feature"><h3>📊 Dashboard</h3><p>See all activity clearly</p></div>
    <div class="feature"><h3>🔒 GDPR Safe</h3><p>Fully compliant</p></div>
</div>
<div class="pricing">
    <h2>Simple Pricing</h2>
    <div class="price-card"><h3>Basic</h3><div class="price">€500</div><p>/month</p><a href="/checkout/basic/monthly" style="background:#00d4ff;color:black;padding:10px 20px;border-radius:20px;text-decoration:none;display:block;margin-top:10px;">Start Basic</a></div>
    <div class="price-card"><h3>Standard</h3><div class="price">€1,000</div><p>/month</p><a href="/checkout/standard/monthly" style="background:#00d4ff;color:black;padding:10px 20px;border-radius:20px;text-decoration:none;display:block;margin-top:10px;">Start Standard</a></div>
    <div class="price-card"><h3>Premium</h3><div class="price">€2,000</div><p>/month</p><a href="/checkout/premium/monthly" style="background:#00d4ff;color:black;padding:10px 20px;border-radius:20px;text-decoration:none;display:block;margin-top:10px;">Start Premium</a></div>
</div>
<footer>
© 2026 TrustNest — Founded by Suneeta Ramanathan · Munich, Germany<br>
<a href="/privacy" style="color:#00d4ff;text-decoration:none;margin:0 10px;">Privacy Policy</a>
<a href="/terms" style="color:#00d4ff;text-decoration:none;margin:0 10px;">Terms & Conditions</a>
<a href="/contact" style="color:#00d4ff;text-decoration:none;margin:0 10px;">Contact</a>
</footer>
</body>
</html>'''
DASHBOARD = '''<!DOCTYPE html>
<html>
<head>
    <title>TrustNest Dashboard</title>
    <style>
        body{font-family:Arial;background:#1a1a2e;color:white;padding:0;margin:0;}
        nav{background:#16213e;padding:15px;display:flex;justify-content:space-between;}
        .logo{color:#00d4ff;text-decoration:none;font-size:20px;font-weight:bold;}
        h1{color:#00d4ff;text-align:center;padding-top:20px;}
        .stats{display:flex;justify-content:center;gap:20px;margin:20px;flex-wrap:wrap;}
        .stat{background:#16213e;padding:20px;border-radius:10px;text-align:center;}
        .stat h2{color:#00d4ff;}
        .alerts{padding:20px;}
        .alert{background:#ff4444;padding:15px;margin:10px;border-radius:8px;}
        .normal{background:#00aa44;padding:15px;margin:10px;border-radius:8px;}
    </style>
</head>
<body>
<nav><a href="/home" class="logo">🔐 TrustNest</a></nav>
<h1>🔐 TrustNest Security Dashboard</h1>
<div class="stats">
    <div class="stat"><h2>210</h2><p>Activities Scanned</p></div>
    <div class="stat"><h2>199</h2><p>Normal ✅</p></div>
    <div class="stat"><h2>11</h2><p>Suspicious 🚨</p></div>
</div>
<div class="alerts">
    <h2>Live Alerts:</h2>
    <div class="alert">🚨 Unknown Hacker — 71 records at 23:19</div>
    <div class="alert">🚨 John Mueller — 55 records at 23:19</div>
    <div class="normal">✅ Anna Weber — 9 records at 23:19</div>
    <div class="normal">✅ Maria Schmidt — 12 records at 23:19</div>
</div>
</body>
</html>'''
LOGIN = '''<!DOCTYPE html>
<html>
<head>
    <title>TrustNest Login</title>
    <style>
        body{font-family:Arial;background:#1a1a2e;color:white;margin:0;padding:0;}
        nav{background:#16213e;padding:15px;}
        .logo{color:#00d4ff;text-decoration:none;font-size:20px;font-weight:bold;}
        .container{max-width:500px;margin:60px auto;background:#16213e;padding:40px;border-radius:15px;}
        h1{color:#00d4ff;text-align:center;}
        input{width:100%;padding:12px;margin:10px 0;border-radius:8px;border:1px solid #00d4ff;background:#1a1a2e;color:white;font-size:16px;box-sizing:border-box;}
        .button{width:100%;background:#00d4ff;color:black;padding:15px;border:none;border-radius:25px;font-size:18px;cursor:pointer;margin-top:20px;}
        a{color:#00d4ff;}
    </style>
</head>
<body>
<nav><a href="/home" class="logo">🔐 TrustNest</a></nav>
<div class="container">
    <h1>Welcome Back</h1>
    <form action="/authenticate" method="POST">
    <input type="email" name="username" placeholder="Email Address"/>
    <input type="password" name="password" placeholder="Password"/>
    <button type="submit" class="button">Login to Dashboard</button>
    </form>
    <p style="text-align:center">Don\'t have an account? <a href="/signup">Sign up here</a></p>
</div>
</body>
</html>'''
SIGNUP = '''<!DOCTYPE html>
<html>
<head>
    <title>TrustNest Signup</title>
    <style>
        body{font-family:Arial;background:#1a1a2e;color:white;margin:0;padding:0;}
        nav{background:#16213e;padding:15px;}
        .logo{color:#00d4ff;text-decoration:none;font-size:20px;font-weight:bold;}
        .container{max-width:500px;margin:60px auto;background:#16213e;padding:40px;border-radius:15px;}
        h1{color:#00d4ff;text-align:center;}
        input{width:100%;padding:12px;margin:10px 0;border-radius:8px;border:1px solid #00d4ff;background:#1a1a2e;color:white;font-size:16px;box-sizing:border-box;}
        .button{width:100%;background:#00d4ff;color:black;padding:15px;border:none;border-radius:25px;font-size:18px;cursor:pointer;margin-top:20px;}
        a{color:#00d4ff;}
    </style>
</head>
<body>
<nav><a href="/home" class="logo">🔐 TrustNest</a></nav>
<div class="container">
    <h1>Create Your Account</h1>
    <form action="/authenticate" method="POST">
    <input type="text" name="hotel" placeholder="Hotel Name"/>
    <input type="text" name="name" placeholder="Your Full Name"/>
    <input type="email" name="username" placeholder="Email Address"/>
    <input type="password" name="password" placeholder="Password"/>
    <button type="submit" class="button">Start Free Trial</button>
    </form>
    <p style="text-align:center">Already have an account? <a href="/login">Login here</a></p>
</div>
</body>
</html>'''
CONTACT = '''<!DOCTYPE html>
<html>
<head>
    <title>TrustNest Contact</title>
    <style>
        body{font-family:Arial;background:#1a1a2e;color:white;margin:0;padding:0;}
        nav{background:#16213e;padding:15px;}
        .logo{color:#00d4ff;text-decoration:none;font-size:20px;font-weight:bold;}
        .container{max-width:500px;margin:60px auto;background:#16213e;padding:40px;border-radius:15px;}
        h1{color:#00d4ff;text-align:center;}
        input,textarea{width:100%;padding:12px;margin:10px 0;border-radius:8px;border:1px solid #00d4ff;background:#1a1a2e;color:white;font-size:16px;box-sizing:border-box;}
        textarea{height:120px;}
        .button{width:100%;background:#00d4ff;color:black;padding:15px;border:none;border-radius:25px;font-size:18px;cursor:pointer;margin-top:20px;}
    </style>
</head>
<body>
<nav><a href="/home" class="logo">🔐 TrustNest</a></nav>
<div class="container">
    <h1>Contact TrustNest</h1>
    <form action="/contact_submit" method="POST">
    <input type="text" name="hotel_name" placeholder="Hotel Name"/>
    <input type="text" name="name" placeholder="Your Name"/>
    <input type="email" name="email" placeholder="Email Address"/>
    <textarea name="message" placeholder="Tell us about your hotel..."></textarea>
    <button type="submit" class="button">Send Message</button>
    </form>
</div>
</body>
</html>'''
PRIVACY = '''<!DOCTYPE html>
<html>
<head>
    <title>TrustNest Privacy Policy</title>
    <style>
        body{font-family:Arial;background:#1a1a2e;color:white;margin:0;padding:0;}
        nav{background:#16213e;padding:15px;display:flex;justify-content:space-between;align-items:center;}
        .logo{color:#00d4ff;text-decoration:none;font-size:20px;font-weight:bold;}
        .container{max-width:800px;margin:40px auto;padding:40px;background:#16213e;border-radius:15px;}
        h1{color:#00d4ff;}
        h2{color:#00d4ff;margin-top:30px;}
        p{color:#cccccc;line-height:1.8;}
        footer{text-align:center;padding:20px;color:#aaa;}
    </style>
</head>
<body>
<nav>
    <a href="/home" class="logo">🔐 TrustNest</a>
</nav>
<div class="container">
    <h1>Privacy Policy</h1>
    <p>Last updated: June 2026</p>
    <h2>1. Who We Are</h2>
    <p>TrustNest is an AI-powered cybersecurity platform for independent hotels, founded by Suneeta Ramanathan, Munich, Germany. We comply fully with GDPR.</p>
    <h2>2. What Data We Collect</h2>
    <p>• Hotel name and contact information</p>
    <p>• Manager email for security alerts</p>
    <p>• Staff activity logs only</p>
    <p>• We NEVER store actual guest personal data</p>
    <h2>3. How Long We Keep Data</h2>
    <p>• Security logs: 90 days</p>
    <p>• Account info: Duration of subscription + 30 days</p>
    <p>• All data deleted permanently on request</p>
    <h2>4. Your GDPR Rights</h2>
    <p>You have the right to access, delete, correct, and port your data at any time.</p>
    <h2>5. Contact</h2>
    <p>inboxsuneeta26@gmail.com · Munich, Germany</p>
</div>
<footer>© 2026 TrustNest</footer>
</body>
</html>'''
TERMS = '''<!DOCTYPE html>
<html>
<head>
    <title>TrustNest Terms and Conditions</title>
    <style>
        body{font-family:Arial;background:#1a1a2e;color:white;margin:0;padding:0;}
        nav{background:#16213e;padding:15px;display:flex;justify-content:space-between;align-items:center;}
        .logo{color:#00d4ff;text-decoration:none;font-size:20px;font-weight:bold;}
        .container{max-width:800px;margin:40px auto;padding:40px;background:#16213e;border-radius:15px;}
        h1{color:#00d4ff;}
        h2{color:#00d4ff;margin-top:30px;}
        p{color:#cccccc;line-height:1.8;}
        footer{text-align:center;padding:20px;color:#aaa;}
    </style>
</head>
<body>
<nav>
    <a href="/home" class="logo">🔐 TrustNest</a>
</nav>
<div class="container">
    <h1>Terms and Conditions</h1>
    <p>Last updated: June 2026</p>
    <h2>1. Service Description</h2>
    <p>TrustNest provides AI-powered cybersecurity monitoring for independent hotels on a monthly SaaS subscription basis.</p>
    <h2>2. Subscription Terms</h2>
    <p>• Subscriptions are billed monthly, quarterly, biannually or annually</p>
    <p>• 30-day free trial — no credit card required</p>
    <p>• Cancel anytime with 30 days notice</p>
    <p>• No cancellation fees</p>
    <h2>3. Plans and Pricing</h2>
    <p>• Basic: €500/month</p>
    <p>• Standard: €1,000/month</p>
    <p>• Premium: €2,000/month</p>
    <h2>4. Data Processing</h2>
    <p>TrustNest acts as a data processor under GDPR. We process only staff activity logs — never guest personal data. A Data Processing Agreement is available on request.</p>
    <h2>5. Liability</h2>
    <p>TrustNest provides security monitoring as a best-effort service. We are not liable for breaches that occur despite our monitoring. Our liability is limited to the monthly subscription fee paid.</p>
    <h2>6. Governing Law</h2>
    <p>These terms are governed by German law. Disputes are subject to Munich courts.</p>
    <h2>7. Contact</h2>
    <p>inboxsuneeta26@gmail.com · Munich, Germany</p>
</div>
<footer>© 2026 TrustNest</footer>
</body>
</html>'''

@app.route("/")
@app.route("/home")
def home():
    return WEBSITE

@app.route("/dashboard")
def dashboard_page():
    return DASHBOARD

@app.route("/login")
def login_page():
    return LOGIN

@app.route("/signup")
def signup_page():
    return SIGNUP

@app.route("/contact")
def contact_page():
    return CONTACT

@app.route("/privacy")
def privacy_page():
    return PRIVACY

@app.route("/terms")
def terms_page():
    return TERMS

@app.route("/contact_submit", methods=["POST"])
def contact_submit():
    name = request.form.get("name")
    hotel = request.form.get("hotel_name")
    return f"<h1 style='color:#00d4ff;background:#1a1a2e;padding:40px;text-align:center'>Thank you {name} from {hotel}!</h1>"

@app.route("/authenticate", methods=["GET", "POST"])
def authenticate():
    return redirect("/dashboard")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
