from typing import Annotated

from fastapi import Header, HTTPException

from instapi.config import settings


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != settings.secret_key:
        raise HTTPException(status_code=401, detail="X-Key header invalid")
    return x_key
