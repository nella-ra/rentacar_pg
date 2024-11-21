
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Viber bot token (zamenite sa svojim stvarnim tokenom)
VIBER_BOT_TOKEN = "YOUR_VIBER_BOT_TOKEN_HERE"
VIBER_API_URL = "https://chatapi.viber.com/pa/send_message"

# Funkcija za slanje obaveštenja putem Vibera
def send_viber_notification(phone, message):
    payload = {
        "receiver": phone,
        "type": "text",
        "text": message,
        "auth_token": VIBER_BOT_TOKEN
    }
    response = requests.post(VIBER_API_URL, json=payload)
    return response.status_code, response.json()

# Ruta za obradu rezervacija
@app.route("/reserve", methods=["POST"])
def reserve():
    # Prikupljanje podataka iz formulara
    vehicle = request.form.get("vehicle")
    name = request.form.get("name")
    phone = request.form.get("phone")
    date = request.form.get("date")
    time = request.form.get("time")

    # Provera unosa
    if not all([vehicle, name, phone, date, time]):
        return jsonify({"error": "Sva polja su obavezna!"}), 400

    # Kreiranje poruke za Viber
    message = (
        f"Rezervacija potvrđena!\n"
        f"Ime: {name}\n"
        f"Telefon: {phone}\n"
        f"Vozilo: {vehicle}\n"
        f"Datum: {date}\n"
        f"Vreme: {time}\n"
    )

    # Slanje obaveštenja na Viber
    status_code, response = send_viber_notification(phone, message)
    if status_code == 200:
        return jsonify({"message": "Rezervacija uspešno potvrđena i obaveštenje poslato na Viber."}), 200
    else:
        return jsonify({"error": "Došlo je do greške pri slanju obaveštenja na Viber.", "details": response}), 500

# Pokretanje Flask aplikacije
if __name__ == "__main__":
    app.run(debug=True, port=5000)
