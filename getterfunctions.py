import json
import requests

url_followers = 'https://i.instagram.com/api/v1/friendships/{}/followers/'
url_following = 'https://i.instagram.com/api/v1/friendships/{}/following/'

headers = {
    'User-Agent': 'Instagram 10.3.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+',
}

def get_follow_response(url, cookies):
    response = requests.get(url, headers=headers, cookies=cookies)
    response.raise_for_status()
    return response.json()

def get_followers(user_id, cookies):
    url = url_followers.format(user_id)
    response = get_follow_response(url, cookies)

    # If the list is too big and next_max_id is not ""
    while response.get('next_max_id'):
        urln = url + '?max_id=' + response['next_max_id']
        response_next = get_follow_response(urln, cookies)
        response['users'].extend(response_next['users'])
        response['next_max_id'] = response_next.get('next_max_id', '')

    usernames = [user["username"] for user in response["users"]]

    # Create a dictionary with the usernames
    data = {"usernames": usernames}

    with open('followers.json', 'w') as f:
        json.dump(data, f)


def get_following(user_id, cookies):
    url = url_following.format(user_id)
    response = get_follow_response(url, cookies)

    # If the list is too big and next_max_id is not ""
    while response.get('next_max_id'):
        urln = url + '?max_id=' + response['next_max_id']
        response_next = get_follow_response(urln, cookies)
        response['users'].extend(response_next['users'])
        response['next_max_id'] = response_next.get('next_max_id', '')

    # Assuming 'users' is a list of users in the JSON response
    usernames = [user["username"] for user in response["users"]]

    # Create a dictionary with the usernames
    data = {"usernames": usernames}

    with open('following.json', 'w') as f:
        json.dump(data, f)

