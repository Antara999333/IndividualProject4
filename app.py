# app.py
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = ""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_text", methods=["POST"])
def generate_text():
    generated_text = None

    if request.method == "POST":
        prompt = request.form.get("prompt", "")

        # Use OpenAI API to generate a sentence containing the input word
        response = openai.Completion.create(
            engine="text-davinci-002",  # Use an appropriate engine
            prompt=f"Create a sentence using the word '{prompt}'.",
            max_tokens=100,
            temperature=0.7,  # Adjust temperature as needed
        )

        # Extract the generated text from the OpenAI response
        generated_text = response.choices[0].text.strip()

    return render_template("generator.html", generated_text=generated_text)


if __name__ == "__main__":
    app.run(debug=True)
