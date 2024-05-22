import requests

from main_app.api_client import ApiClient


# link = 'https://cs12.pikabu.ru/post_img/2022/08/24/0/1661289326286226607.jpg'
# api_client = ApiClient()
# image = api_client.image_from_url(link)
# json_, status = api_client.image_post(data='07-05-2025', game_name='GTAV', genre=5, info='xxx', publisher=2, price=30,
#                                       link=link)
# print(json_)
# print(status)
#
#
# url = 'http://127.0.0.1:8000/media/game_files/sertifikat_konkursanta.pdf'
# files = api_client.files_from_url(url)
# xxx = api_client.file_post(data='25-05-2025', game_name='konkurs', genre=2, info='xxx', publisher=2, price=777,
#                            url=url)


link = 'https://cs12.pikabu.ru/post_img/2022/08/24/0/1661289326286226607.jpg'
url = 'http://127.0.0.1:8000/media/game_files/sertifikat_konkursanta.pdf'
api_client = ApiClient()
json_, status = api_client.post_image_and_files(data='25-05-2025', game_name='konkurs', genre=2, info='xxx', publisher=2,
                                                price=777, link=link, url=url)
print(json_)
print(status)
