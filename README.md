# Text to Image Generator

# Flask App for Text-to-Image Generation

This project is a simple Flask web application that utilizes Hugging Face's Inference API for text-to-image generation. Users can input a text description, and the app generates an image based on that description.

## Overview

The web app leverages the Hugging Face model [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) to generate images from text. It uses the Flask web framework to create a user-friendly interface for inputting text and displaying the generated image. 

## Usage

To use the application, follow these steps:

1. Clone the repository:
```bash
git clone git@github.com:carolinechen99/text-to-img.git
```

2. Install the required dependencies using Pipenv:
```bash
pipenv install
```

3. Run the application:
```bash
pipenv run flask run
```

4. Open your web browser and visit http://127.0.0.1:8080/.

5. Enter a text description in the input field and click "Generate Image" to generate an image based on the text.

Example:

- Input: "Astronaut riding a horse"
- Output: An image of an astronaut riding a horse.

## References

- Hugging Face Model: [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- Flask Web Framework: [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)
- Guide for [pipenv](https://towardsdatascience.com/comparing-python-virtual-environment-tools-9a6543643a44)