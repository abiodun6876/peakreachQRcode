from flask import Flask, request, redirect, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

# Links to Play Store and App Store
APP_STORE_URL = "https://apps.apple.com/ng/app/peakreach/id6469102132"
PLAY_STORE_URL = "https://play.google.com/store/apps/details?id=com.peakreach.android"

@app.route("/")
def home():
    qr_url = "https://peakreach-q-rcode.vercel.app/qrcode"  # URL pointing to the QR code route
    qr = qrcode.make(qr_url)

    # Convert QR code to image
    img_io = BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

@app.route("/qrcode")
def generate_qr():
    user_agent = request.headers.get('User-Agent', '').lower()

    if "iphone" in user_agent or "ipad" in user_agent:
        return redirect(APP_STORE_URL)  # Redirect to Apple App Store
    elif "android" in user_agent:
        return redirect(PLAY_STORE_URL)  # Redirect to Google Play Store
    else:
        return "Unsupported Device. Please visit from an iPhone or Android device.", 400
