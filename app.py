from flask import Flask, render_template, request, send_file
import requests
import io
from PIL import Image

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {'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'}"}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form['prompt']
        payload = {"inputs": prompt}
        response = requests.post(API_URL, headers=headers, json=payload)
        image_bytes = response.content
        image = Image.open(io.BytesIO(image_bytes))
        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)