import pandas as pd
from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

app = Flask(__name__)

# Load the pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("ealvaradob/bert-finetuned-phishing")
model = AutoModelForSequenceClassification.from_pretrained("ealvaradob/bert-finetuned-phishing")
classifier = pipeline(task="text-classification", model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get("akshat")
    result = classifier(url)
    return render_template('result.html', url=url, result=result[0])

if __name__ == '__main__':
    app.run(debug=True)
