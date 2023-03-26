import requests

from instapi.config import settings


def get_token(code: str, redirect_uri: str):
    data = {
        "client_id": settings.instagram_app_id,
        "client_secret": settings.instagram_app_secret,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri,
        "code": code,
    }
    res = requests.post("https://api.instagram.com/oauth/access_token", data=data)
    res.raise_for_status()

    return res.json()["access_token"]

def get_long_lived_token(token: str):
    params = {
        "grant_type": "ig_exchange_token",
        "client_secret": settings.instagram_app_secret,
        "access_token": token
    }
    res = requests.get("https://graph.instagram.com/access_token", params=params)
    res.raise_for_status()

    return res.json()["access_token"]

def refresh_token(access_token):
    params = {
        "grant_type": "ig_refresh_token",
        "access_token": access_token,
    }
    res = requests.get("https://graph.instagram.com/refresh_access_token", params=params)
    res.raise_for_status()

    return res.json()["access_token"]

def get_last_post(access_token):
    params = {
        "access_token": access_token,
        "fields": "caption,media_url,timestamp,id"
    }
    res = requests.get("https://graph.instagram.com/me/media", params=params)
    res.raise_for_status()

    return res.json()
