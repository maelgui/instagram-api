import requests

from instapi.config import settings


API_VERSION = "v21.0"
PAGE_ID = "17841408587413183"  # bagadmenru

def get_token(code: str, redirect_uri: str):
    data = {
        "client_id": settings.instagram_app_id,
        "client_secret": settings.instagram_app_secret,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri,
        "code": code,
    }
    res = requests.post(f"https://graph.facebook.com/{API_VERSION}/oauth/access_token", data=data)
    res.raise_for_status()

    return res.json()["access_token"]

def get_long_lived_token(token: str):
    params = {
        "grant_type": "fb_exchange_token",
        "client_id": settings.instagram_app_id,
        "client_secret": settings.instagram_app_secret,
        "fb_exchange_token": token
    }
    res = requests.get(f"https://graph.facebook.com/{API_VERSION}/oauth/access_token", params=params)
    res.raise_for_status()
    print(res.json())
    return res.json()["access_token"]

def refresh_token(access_token):
    return get_long_lived_token(access_token)

def get_last_post(access_token):
    params = {
        "access_token": access_token,
        "fields": "caption,media_url,timestamp,id"
    }
    res = requests.get(f"https://graph.facebook.com/{API_VERSION}/{PAGE_ID}/media", params=params)
    print(res.text)
    res.raise_for_status()

    return res.json()
