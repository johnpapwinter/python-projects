from flask import Flask, render_template, request
from dataclasses import asdict
from dotenv import load_dotenv
from api_service import ApiService
from model import Page, SearchFilters

load_dotenv()

app = Flask(__name__)
api = ApiService()


@app.route('/')
def home():
    random_quote = api.get_random_quote()

    return render_template('index.html', quote=random_quote)


@app.route('/characters')
def get_characters():
    page_number = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 5))

    race = request.args.get('race', None)
    gender = request.args.get('gender', None)
    realm = request.args.get('realm', None)
    name = request.args.get('name', None)

    page = Page(page=page_number, limit=limit)
    filters = SearchFilters(race=race, gender=gender, realm=realm, name=name)
    response = asdict(api.get_characters(page=page, filters=filters))

    return render_template('characters.html', data=response)


@app.route('/quotes')
def get_quotes():
    page_number = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 5))

    page = Page(page=page_number, limit=limit)
    response = asdict(api.get_quotes(page=page))

    return render_template('quote.html', data=response)
