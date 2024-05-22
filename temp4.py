import requests

url = 'http://127.0.0.1:8000/api/game-create/'
token = {'Authorization': 'Token 1fffe0ff7203dd15b490355ad8d9fe446f5ab498'}

url_jpg = 'https://cs12.pikabu.ru/post_img/2022/08/24/0/1661289326286226607.jpg'
url_pdf = 'http://127.0.0.1:8000/media/game_files/sertifikat_konkursanta.pdf'

body = {
    "data": 'data',
    "genre": 2,
    "name": 'game_name',
    "info": 'info',
    "publisher": 2,
    "price": 50,
}
response_jpg = requests.get(url_jpg)
response_pdf = requests.get(url_pdf)
files = {'image': ('image.jpeg', response_jpg.content), 'files': ('files.pdf', response_pdf.content)}

# image = open('GTAV_Official_Cover_Art.jpg', 'rb')
# pdf = open('sertifikat_konkursanta.pdf', 'rb')
# files  = {'files': pdf, 'image': image}
xxx = requests.post(url=url, data=body, headers=token, files=files)
print(xxx.status_code)
print(xxx.json())
