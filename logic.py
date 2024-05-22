import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_settings.settings")
django.setup()

import requests
from main_app.models import ApiGames
# headers = {'Authorization': 'Token 1fffe0ff7203dd15b490355ad8d9fe446f5ab498'}
# link = f"http://127.0.0.1:8000/api/articles"
# response = requests.get(link, headers=headers)
# print(response.status_code)
# print(response.json())


# auth_link = 'http://127.0.0.1:8000/api-auth/'
# body = {
#     "username": "DENI",
#     "password": "9162"
# }
# auth_response = requests.post(auth_link, json=body)
# print(auth_response)
# print(auth_response.json())


headers = {'Authorization': 'Token 1fffe0ff7203dd15b490355ad8d9fe446f5ab498'}
link = f"http://127.0.0.1:8000/api/games"
response = requests.get(link, headers=headers)
print(response.status_code)

for game in response.json():
    game_name = game['name']
    game_image = game['image']
    game_publisher = game['publisher']['publisher']
    new_game = ApiGames(game_name=game_name, game_image=game_image, game_publisher=game_publisher)
    new_game.save()
