from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "49708bc0daa7ba60ff0c16eae4c7bdb7"

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    else:
        return {"error": f"Could not retrieve weather for '{city}'"}

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400
    data = get_weather_data(city)
    return jsonify(data)
