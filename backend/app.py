from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import json
import uuid
import os

app = Flask(__name__)
CORS(app)

# Load model
model = tf.keras.models.load_model("models/plant_disease_recog_model_pwp.keras")

# Load disease information
with open("plant_disease.json", "r") as file:
    plant_disease = json.load(file)


@app.route('/uploadimages/<path:filename>')
def uploaded_images(filename):
    return send_from_directory("uploadimages", filename)


def extract_features(image_path):
    image = tf.keras.utils.load_img(image_path, target_size=(160, 160))
    image = tf.keras.utils.img_to_array(image)
    image = np.array([image])
    return image


def predict_image(image_path):
    img = extract_features(image_path)

    prediction = model.predict(img)

    confidence = float(np.max(prediction) * 100)

    index = int(np.argmax(prediction))

    disease = plant_disease[index]

    return disease, confidence


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({"message": "No image uploaded"}), 400

    image = request.files["image"]

    os.makedirs("uploadimages", exist_ok=True)

    filename = f"{uuid.uuid4().hex}_{image.filename}"

    filepath = os.path.join("uploadimages", filename)

    image.save(filepath)

    disease, confidence = predict_image(filepath)

    return jsonify({
        "data": {
            "image_name": image.filename,
            "disease": disease["name"],
            "confidence": round(confidence, 2),
            "treatment": disease["cure"],
            "weather": "Keep the field dry and monitor crop regularly.",
            "report_url": ""
        }
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)