from flask import Flask, render_template
from email_flask import email_extractor_bp
from pdf_flask import pdf_extractor_bp
from pptx_flask import pptx_extractor_bp
from word_flask import word_extractor_bp
import os
from flask_cors import CORS

app = Flask(__name__)
extract_email = app.register_blueprint(email_extractor_bp)
extract_pdf = app.register_blueprint(pdf_extractor_bp)
extract_pptx = app.register_blueprint(pptx_extractor_bp)
extract_word = app.register_blueprint(word_extractor_bp)
CORS(app)

@app.route('/')
def index():
    return render_template('pop_up.html')

@app.route('/email', methods=['POST'])
def email():
    return extract_email
    
@app.route('/pdf', methods=['POST'])
def pdf():
    return extract_pdf

@app.route('/ppt', methods=['POST'])
def ppt():
    return extract_pptx

@app.route('/word', methods=['POST'])
def word():
    return extract_word
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

