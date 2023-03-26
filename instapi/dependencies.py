from typing import Annotated

from fastapi import Header, HTTPException

from instapi.config import settings


async def verify_key(api_key: str):
    if api_key != settings.secret_key:
        raise HTTPException(status_code=401, detail="API Key param invalid")
    return api_key
