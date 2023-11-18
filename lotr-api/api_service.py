import os
import requests
import random
from model import Character, Quote, Movie, PaginatedResponse, SearchFilters, Page
from dataclasses import asdict
from dotenv import load_dotenv

load_dotenv()


class ApiService:
    def __init__(self):
        self.bearer_token = os.getenv('API_KEY')
        self.headers = {'Authorization': f'Bearer {self.bearer_token}', 'Content-Type': 'application/json'}
        self.url = os.getenv('BASE_URL')

    def get_characters(self, page: Page, filters: SearchFilters):
        search_params = self._create_search_filter_parameters(search_filter=filters)
        json_data = self._make_request(f'character?page={page.page}&limit={page.limit}{search_params}')
        return self._map_to_paginated_character(json_data=json_data)

    def get_single_character(self, char_id: str):
        json_data = self._make_request(f'character/{char_id}')
        payload = json_data.get('docs')[0]
        return self._map_to_character(json_data=payload)

    def get_quotes(self, page: Page):
        json_data = self._make_request(f'quote?page={page.page}&limit={page.limit}')
        return self._map_to_paginated_quote(json_data=json_data)

    def get_random_quote(self):
        page = Page(page=1, limit=10000)
        json_data = self._make_request(f'quote?page={page.page}&limit={page.limit}')
        json_quote = random.choice(json_data.get('docs'))
        return self._map_to_quote(json_data=json_quote)

    def _make_request(self, endpoint: str):
        response = requests.get(f'{self.url}/{endpoint}', headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return "Error"

    def _get_single_movie(self, movie_id: str):
        json_data = self._make_request(f'movie/{movie_id}')
        payload = json_data.get('docs')[0]
        return self._map_to_movie(json_data=payload)

    def _map_to_paginated_quote(self, json_data: dict):
        docs_list = [self._map_to_quote(item) for item in json_data['docs']]
        paginated_response = PaginatedResponse(
            docs=docs_list,
            total=json_data.get('total', None),
            limit=json_data.get('limit', None),
            offset=json_data.get('offset', None),
            page=json_data.get('page', None),
            pages=json_data.get('pages', None)
        )
        return paginated_response

    def _map_to_paginated_character(self, json_data: dict):
        docs_list = [self._map_to_character(item) for item in json_data['docs']]
        paginated_response = PaginatedResponse(
            docs=docs_list,
            total=json_data.get('total', None),
            limit=json_data.get('limit', None),
            offset=json_data.get('offset', None),
            page=json_data.get('page', None),
            pages=json_data.get('pages', None)
        )
        return paginated_response

    def _map_to_character(self, json_data: dict):
        return Character(
            _id=json_data['_id'],
            height=json_data.get('height', None),
            race=json_data.get('race', None),
            gender=json_data.get('gender', None),
            birth=json_data.get('birth', None),
            spouse=json_data.get('spouse', None),
            death=json_data.get('death', None),
            realm=json_data.get('realm', None),
            hair=json_data.get('hair', None),
            name=json_data.get('name', None),
            wikiUrl=json_data.get('wikiUrl', None)
        )

    def _map_to_quote(self, json_data: dict):
        return Quote(
            _id=json_data['_id'],
            dialog=json_data.get('dialog', None),
            movie=self._get_single_movie(json_data.get('movie')).name,
            character=self.get_single_character(json_data.get('character')).name,
            id=json_data.get('id', None)
        )

    def _map_to_movie(self, json_data: dict):
        return Movie(
            _id=json_data['_id'],
            name=json_data.get('name', None)
        )

    def _create_search_filter_parameters(self, search_filter: SearchFilters):
        if all(value is None for value in asdict(search_filter).values()):
            return ""

        filters_dictionary = asdict(search_filter)
        filters = {key: value for key, value in filters_dictionary.items() if value is not None}

        return "&" + "&".join(f"{key}={value}" for key, value in filters.items())
