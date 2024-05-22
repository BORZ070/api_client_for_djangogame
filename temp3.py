# import requests
#
# link = 'http://127.0.0.1:8000/media/game_main/GTAV_Official_Cover_Art_m0qAyLu.jpg'
# response = requests.get(link)
# with open('image.jpeg', 'wb') as file:
#     file.write(response.content)

with open('token.txt', 'r') as file:
    token = file.read()
print(type(token))