from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import joblib

from legal_map import LEGAL_MAP
from fir_generator import generate_fir
from pdf_utils import create_fir_pdf

app = Flask(__name__)
CORS(app)  # allow browser requests

# Load trained model
model = joblib.load("../model/crime_classifier.pkl")


@app.route("/", methods=["GET"])
def home():
    return "CyberFIR API running ✅"


# ---------- JSON endpoint for web UI preview ----------
@app.route("/generate_fir", methods=["POST"])
def generate_fir_api():
    data = request.get_json()
    user = data.get("name", "")
    city = data.get("city", "")
    incident = data.get("incident", "")

    if not user or not city or not incident:
        return jsonify({"error": "Missing required fields"}), 400

    crime = model.predict([incident])[0]
    sections = LEGAL_MAP.get(crime, [])
    fir_text = generate_fir(user, city, incident, crime, sections)

    # RETURN JSON here (NOT PDF)
    return jsonify({
        "crime": crime,
        "sections": sections,
        "fir": fir_text
    })


# ---------- PDF endpoint for download button ----------
@app.route("/generate_fir_pdf", methods=["POST"])
def generate_fir_pdf():
    data = request.get_json()
    user = data.get("name", "")
    city = data.get("city", "")
    incident = data.get("incident", "")

    if not user or not city or not incident:
        return jsonify({"error": "Missing required fields"}), 400

    crime_ml = model.predict([incident])[0]
    crime = apply_rules(incident, crime_ml)

    sections = LEGAL_MAP.get(crime, [])
    fir_text = generate_fir(user, city, incident, crime, sections)

    pdf_buffer = create_fir_pdf(fir_text)

    # RETURN PDF here
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name="CyberFIR.pdf",
        mimetype="application/pdf"
    )

def apply_rules(incident_text, predicted_crime):
    text = incident_text.lower()

    fraud_keywords = [
        "money", "paid", "amount", "rupees", "taken", "asked for payment",
        "blocked", "scam", "registration fee", "advance payment", "took money"
    ]

    extortion_keywords = [
        "leak", "threaten", "blackmail", "pay me", "ruin reputation",
        "private photos", "personal videos", "otherwise i will"
    ]

    harassment_keywords = [
        "abuse", "vulgar", "insult", "bad words", "obscene", "humiliate"
    ]

    stalking_keywords = [
        "keeps messaging", "blocked him", "follows me", "monitor",
        "keeps asking", "comes online", "comments on everything"
    ]

    # Rule Engine Overrides
    if any(k in text for k in fraud_keywords):
        return "fraud"

    if any(k in text for k in extortion_keywords):
        return "extortion"

    if any(k in text for k in harassment_keywords):
        return "harassment"

    if any(k in text for k in stalking_keywords):
        return "stalking"

    # Default = ML prediction
    return predicted_crime



if __name__ == "__main__":
    app.run(debug=True)
