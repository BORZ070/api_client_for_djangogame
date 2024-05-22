import requests

link = 'http://127.0.0.1:8000/api/game-create/'
token = {'Authorization': 'Token 1fffe0ff7203dd15b490355ad8d9fe446f5ab498'}

image = {'image': open('GTAV_Official_Cover_Art.jpg', 'rb')}

body = {
  "data": "string",
  "genre": 2,
  "name": "string",
  "info": "string",
  "publisher": 1,
  "price": 40
}

x = requests.post(link, data=body, files=image)

print(x, x.json())
