from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipwho.is/{ip}")
        data = response.json()
        if not data.get("success", False):
            return None
        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "flag": data.get("flag", {}).get("emoji"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "isp": data.get("connection", {}).get("isp"),
            "org": data.get("connection", {}).get("org"),
            "asn": data.get("connection", {}).get("asn"),
            "is_vpn": data.get("security", {}).get("vpn", False),
            "map_link": f"https://www.google.com/maps?q={data.get('latitude')},{data.get('longitude')}"
        }
    except Exception as e:
        print("Error:", e)
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    ip_info = None
    if request.method == "POST":
        ip = request.form.get("ip")
        ip_info = get_ip_info(ip.strip()) if ip else None
    return render_template("index.html", info=ip_info)

if __name__ == "__main__":
    app.run(debug=True)
