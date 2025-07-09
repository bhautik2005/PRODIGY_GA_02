from flask import Flask, render_template, request, jsonify
import requests
import base64
from PIL import Image
import io
import os

app = Flask(__name__)

# Replace this with your real token or load from .env
HF_API_KEY = os.environ.get("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/ZB-Tech/Text-to-Image"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def generate_image_from_prompt(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code != 200:
        raise Exception(f"Failed to generate image: {response.content.decode()}")
    
    image_bytes = response.content
    image = Image.open(io.BytesIO(image_bytes))

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate-image', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    try:
        image_base64 = generate_image_from_prompt(prompt)
        return jsonify({"image_base64": image_base64})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
