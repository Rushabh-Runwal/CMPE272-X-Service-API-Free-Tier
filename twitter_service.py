# twitter_service.py
import tweepy
import requests
from requests_oauthlib import OAuth1
import json
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
API_SECRET_KEY = os.environ.get("API_SECRET_KEY")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_ID_SECRET = os.environ.get("CLIENT_ID_SECRET")
#

# INITIALIZE TWITTER API
auth_api = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def get_user_details():
    URL = "https://api.x.com/2/users/me"
    headers = {"Content-Type": "application/json"}
    response = requests.get(
        URL, auth=auth_api, headers=headers
    )
    return response.json()

def get_user_by_username(username):
    URL = f'https://api.x.com/2/users/by/username/{username}'
    headers = {"Content-Type": "application/json"}
    response = requests.get(
        URL, auth=auth_api, headers=headers
    )
    return response.json()


def create_tweet(text):
    URL = "https://api.x.com/2/tweets"
    headers = {"Content-Type": "application/json"}
    data_payload = {"text": text}
    response = requests.post(
        URL, auth=auth_api, headers=headers, data=json.dumps(data_payload)
    )
    return response.json()


def delete_tweet(tweet_id):
    URL = f"https://api.x.com/2/tweets/{tweet_id}"
    response = requests.delete(URL, auth=auth_api)
    return response.json()
