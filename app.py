from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
from datetime import datetime

app = Flask(__name__)

model = tf.keras.models.load_model("malaria_model.h5")

IMG_SIZE = 128


def preprocess_image(image):

    img = Image.open(image).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE))

    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["file"]

    img_array = preprocess_image(file)

    prediction = model.predict(img_array)

    prob = float(prediction[0][0])

    print("Raw Probability:", prob)

    if prob < 0.5:
        result = "PARASITIZED"
        confidence = (1 - prob) * 100
        risk = "HIGH"
    else:
        result = "UNINFECTED"
        confidence = prob * 100
        risk = "NONE"

    return jsonify({
        "prediction": result,
        "confidence": round(confidence,2),
        "risk_level": risk,
        "parasite_probability": round((1-prob)*100,2),
        "interpretation": "Malaria parasites detected." if result=="PARASITIZED" else "No malaria parasites detected.",
        "recommendation": "Consult doctor immediately." if result=="PARASITIZED" else "No medical action required.",
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })


if __name__ == "__main__":
    app.run(debug=True)