from flask import Flask, render_template, request, url_for, redirect
from converter_service import ConverterService

app = Flask(__name__)
api = ConverterService()


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    filepath = request.form.get('filepath', None)
    api.convert_pdf_to_audiobook(filepath=filepath)

    return redirect(url_for('home'))

