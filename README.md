# 🌍 GeoTrace

GeoTrace is a powerful IP tracing tool with both a modern Flask-based web app and a Python CLI utility. It provides:
- 📍 IP Geolocation (City, Country, ISP, etc.)
- 🛡 VPN detection
- 🗺 Live map preview (Leaflet.js)
- ⚡ Fast, clean dark UI

### 🔧 Features
- Input any IP and view:
  - City, Country, Region
  - ASN, ISP, ORG
  - VPN/Proxy detection
  - Embedded map with marker
- Google Maps link for deeper inspection

### 🖥 Run Locally
```bash
# Setup virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Flask app
set FLASK_APP=app.py
flask run
