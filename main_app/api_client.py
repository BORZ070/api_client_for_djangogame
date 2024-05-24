import time

import requests
from _settings import settings

url_game_create = settings.URL_GAME_CREATE
url_articles = settings.URL_ARTICLES
url_api_auth = settings.URL_API_AUTH
token = {'Authorization': f'Token {settings.TOKEN}'}


class ApiClient:
    # print(url_articles, url_api_auth, url_game_create, token)

    def get_request_api(self):
        for i in range(2):
            token = {'Authorization': f'Token {self.get_token_from_file()}'}
            print(token)
            try:
                get = requests.get(url=url_articles, headers=token)
                # get = get.json()
                print(get.status_code)
            except Exception as err:
                print(err)
                time.sleep(2)
                get = {'сервер': 'не отвечает'}
                continue
            if get.status_code == 401:
                self.get_token()
                continue
            if 500 <= get.status_code <= 599:
                continue
            break
        return get

    def get_token_from_file(self):
        print('get token from file')
        with open('token.txt', 'r') as file:
            token = file.read()
        return token

    def get_token(self):
        print('get new token')
        body = {
            "username": "DENI",
            "password": "9162"
        }
        auth_response = requests.post(url=url_api_auth, json=body)
        json_response = auth_response.json()
        token_api = json_response['token']
        print(auth_response)
        print(token_api)
        with open('token.txt', 'w') as file:
            file.write(token_api)

# api_client = ApiClient()
# x = api_client.get_request_api()


class Requests:
    def get_json(self):
        response = requests.get(url_articles, headers=token)
        json = response.json()
        status = response.status_code
        return json, status

    def post_json(self, data, genre, game_name, info, publisher, price):
        body = {
          "data": data,
          "genre": genre,
          "name": game_name,
          "info": info,
          "publisher": publisher,
          "price": price,
        }

        response = requests.post(url_game_create, headers=token, data=body,)
        json = response.json()
        status = response.status_code
        return json, status


class GetFromFile:
    def image_from_url(self, link):
        response = requests.get(link)
        image = {'image': ('image.jpeg', response.content)}
        return image

    def files_from_url(self, url):
        response = requests.get(url)
        files = {'files': ('file.pdf', response.content)}
        return files

    def double_files_from_url(self, link, url):
        response_image = requests.get(link)
        response_files = requests.get(url)
        image = ('image.jpeg', response_image.content)
        files = ('file.pdf', response_files.content)
        double_files = {'image': image, 'files': files}
        return double_files


class PostFile(GetFromFile):
    def image_post(self, data, genre, game_name, info, publisher, price, link):
        body = {
            "data": data,
            "genre": genre,
            "name": game_name,
            "info": info,
            "publisher": publisher,
            "price": price,
        }
        image = self.image_from_url(link)
        response = requests.post(url_game_create, headers=token, data=body, files=image)
        json = response.json()
        status = response.status_code
        return json, status

    def file_post(self, data, genre, game_name, info, publisher, price, url):
        body = {
            "data": data,
            "genre": genre,
            "name": game_name,
            "info": info,
            "publisher": publisher,
            "price": price,
        }
        files = self.files_from_url(url)
        response = requests.post(url_game_create, headers=token, data=body, files=files)
        json = response.json()
        status = response.status_code
        return json, status

    def post_image_and_files(self, data, genre, game_name, info, publisher, price, link, url):
        body = {
            "data": data,
            "genre": genre,
            "name": game_name,
            "info": info,
            "publisher": publisher,
            "price": price,
        }
        files = self.double_files_from_url(link, url)
        response = requests.post(url_game_create, headers=token, data=body, files=files)
        json = response.json()
        status = response.status_code
        return json, status


class ApiClientTwo(ApiClient, Requests, PostFile):
    pass

A2 = ApiClientTwo()
print(A2.post_image_and_files('fewa', 2, 'gresges', 'fewafaw', 2, 22,
                              'http://127.0.0.1:8000/media/game_main/GTAV_Official_Cover_Art_m0qAyLu.jpg',
                              'http://127.0.0.1:8000/media/game_files/sertifikat_konkursanta.pdf'))