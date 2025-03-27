from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import logging

# Attempt to import CORS
try:
    from flask_cors import CORS
    cors_enabled = True
except ImportError:
    cors_enabled = False

app = Flask(__name__)
if cors_enabled:
    CORS(app)  # Enable CORS if available

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load trained KMeans model
with open("kmeans_Hack1.pkl", "rb") as file:
    kmeans = pickle.load(file)

# Load places dynamically from CSV
def load_places():
    df = pd.read_csv("Mechanic_dataset1.csv")
    return df[df['is_open'] == 1].to_dict(orient="records")  # Filter only open places

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        latitude = float(data.get("latitude", ""))
        longitude = float(data.get("longitude", ""))

        if latitude == "" or longitude == "":
            return jsonify({"error": "Invalid coordinates received."})

        # Predict cluster
        cluster = kmeans.predict(np.array([[latitude, longitude]]))[0]

        # Get recommended places in the same cluster
        places = load_places()
        recommendations = [
            {
                "name": place["name"],
                "contact_number": place["contact_number"],
                "address": place["address"],
                "city": place["city"],
                "stars": place["stars"],
                "review_count": place["review_count"],
                "latitude": place["latitude"],
                "longitude": place["longitude"]

            }
            for place in places if place["cluster"] == cluster
        ]

        return jsonify({"recommendations": recommendations})

    except ValueError:
        return jsonify({"error": "Invalid input format. Ensure latitude and longitude are valid numbers."})
    except Exception as e:
        logging.error(f"Error in /recommend: {str(e)}")
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)