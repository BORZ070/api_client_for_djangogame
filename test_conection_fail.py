import requests
import time

url = 'http://127.0.0.1:8000/api/articles/'
auth_link = 'http://127.0.0.1:8000/api-auth/'
# token = {'Authorization': 'Token 1fffe0ff7203dd15b490355ad8d9fe446f5ab498'}

counter = 1
#
#
# def get_token_from_file():
#     print('get token from file')
#     with open('token.txt', 'r') as file:
#         token = file.read()
#     return token
#
# def get_request_api():
#     for i in range(2):
#         token = {'Authorization': f'Token {get_token_from_file()}'}
#         print(token)
#         try:
#             get = requests.get(url=url, headers=token)
#             # get = get.json()
#             print(get.status_code)
#         except Exception as err:
#             print(err)
#             time.sleep(2)
#             get = {'сервер': 'не отвечает'}
#             continue
#         if get.status_code == 401:
#             get_token()
#             continue
#         if 500 <= get.status_code <= 599:
#             continue
#         break
#     return get
#
#
# def get_token():
#     print('get new token')
#     body = {
#         "username": "DENI",
#         "password": "9162"
#     }
#     auth_response = requests.post(auth_link, json=body)
#     json_response = auth_response.json()
#     token_api = json_response['token']
#     print(auth_response)
#     print(token_api)
#     with open('token.txt', 'w') as file:
#         file.write(token_api)
#
# def main():
#     response = get_request_api()
#     print(response.json())
# if __name__ == '__main__':
#     main()
#
# func = get_request_api()
# print(func)
