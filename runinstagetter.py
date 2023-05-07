from getterfunctions import get_followers, get_following
import json

user_id = '3136507569'
cookies = {
    'csrftoken': 'YOUR_TOKEN',
    'sessionid': 'YOUR_SESSIONID',
    'ds_user_id': 'YOUR_ID'
}

followers = get_followers(user_id, cookies)
following = get_following(user_id, cookies)

with open('followers.json', 'r') as f:
    followers = json.load(f)

with open('following.json', 'r') as f:
    following = json.load(f)

dataFi = following["usernames"]
dataFe = followers["usernames"]

not_following_back = []
for username in dataFi:
    if username not in dataFe:
        not_following_back.append(username)

# Save the result to a new JSON file
with open('not_following_back.json', 'w') as f:
    json.dump(not_following_back, f)
