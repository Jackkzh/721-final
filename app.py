from flask import Flask, render_template, request, send_file
import requests
import io
from PIL import Image

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
# Replace with your actual API token
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.content)
    print(response.headers['Content-Type'])
    return response.content


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_input = request.form['text_input']
        image_bytes = query({"inputs": text_input})
        image = Image.open(io.BytesIO(image_bytes))
        image.save('static/generated_image.jpg', 'JPEG')
        return send_file('static/generated_image.jpg', mimetype='image/jpeg')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
