from machinetranslation import translator
from flask import Flask, jsonify, request
import json
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/englishToFrench')
def englishToFrench():
    text_to_translate = request.args.get('textToTranslate')
    
    translated_text = translator.english_to_french(text_to_translate)
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.french_to_english(text_to_translate)
    return translated_text

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
