from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse

from instapi import instagram, token
from instapi.config import settings
from instapi.dependencies import verify_key

app = FastAPI(dependencies=[Depends(verify_key)])

@app.get("/")
async def root():
    access_token = token.load_token()
    refreshed_access_token = instagram.refresh_token(access_token)
    token.save_token(refreshed_access_token)

    return instagram.get_last_post(refreshed_access_token)

@app.get("/init")
async def init():
    app_id = settings.instagram_app_id
    redirect_uri = app.url_path_for("callback").make_absolute_url(settings.base_url)
    url = f"https://api.instagram.com/oauth/authorize?client_id={app_id}&redirect_uri={redirect_uri}&scope=user_profile,user_media&response_type=code"
    return RedirectResponse(url=url)

@app.get("/callback")
async def callback(code: str | None = None):
    redirect_uri = app.url_path_for("callback").make_absolute_url(settings.base_url)

    short_access_token = instagram.get_token(code, redirect_uri)

    long_access_token = instagram.get_long_lived_token(short_access_token)

    token.save_token(long_access_token)

    return {"status": "OK"}
