import os
import numpy as np
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io
import base64

app = Flask(__name__)

MODEL_PATH = os.path.join("artifacts", "training", "model.h5")
model = load_model(MODEL_PATH)

CLASS_NAMES = ["Normal", "Tumor"]

def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    try:
        img = Image.open(file.stream).convert("RGB")
        
        # Base64 for preview
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        # Predict
        img_array = preprocess_image(img)
        predictions = model.predict(img_array)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = float(np.max(predictions[0])) * 100
        
        return jsonify({
            "prediction": predicted_class,
            "confidence": round(confidence, 2),
            "image": img_base64
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)