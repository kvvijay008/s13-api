import requests
import json

def get_github_user(user_id):
    url = f'https://api.github.com/{user_id}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

user_data = get_github_user('kvvijay008')
print(user_data)
