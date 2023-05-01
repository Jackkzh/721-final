# Text to Image Generator

# Flask App for Text-to-Image Generation

This project is a simple Flask web application that utilizes Hugging Face's Inference API for text-to-image generation. Users can input a text description, and the app generates an image based on that description.

## Overview

This project demonstrates the integration of the Hugging Face Inference API with a Flask web application to generate images based on textual descriptions. The app utilizes the [Stable Diffusion v1.5 model](https://huggingface.co/runwayml/stable-diffusion-v1-5) available on the Hugging Face Model Hub. Given a text input, the model generates an image that visually represents the description provided by the user.

The Flask web application serves a simple user interface, which consists of a text box for entering a description, and a button to generate the image. Upon clicking the "Generate Image" button, the app sends a request to the Hugging Face Inference API with the given text input. The API returns an image as a response, which the app then displays below the text box.

This project showcases how to integrate state-of-the-art machine learning models into a web application, providing users with a straightforward and interactive way to generate images from textual descriptions. It demonstrates the power of natural language understanding and image synthesis, enabling users to generate realistic images based on their creative ideas.


<img width="869" alt="IDS721 final project photo" src="https://user-images.githubusercontent.com/70717089/235395725-d52d3f35-1b2e-4c2f-ae0a-d407607c4f62.png">


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

![generated_image](https://user-images.githubusercontent.com/70717089/235404405-ae3ae7d2-d8e7-4102-a1ab-67c2300c5b9b.jpeg)

## References

- Hugging Face Model: [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- Flask Web Framework: [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)
- Guide for [pipenv](https://towardsdatascience.com/comparing-python-virtual-environment-tools-9a6543643a44)
