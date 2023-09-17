import jwt

from fastapi import Response

from src.conf import access_security, refresh_security, SECRET


def create_access_refresh_tokens(subject: dict):
    access_token = access_security.create_access_token(subject=subject)
    refresh_token = refresh_security.create_refresh_token(subject=subject)
    return access_token, refresh_token


def set_access_refresh_tokens(response: Response, access_token: str, refresh_token: str):
    access_security.set_access_cookie(response=response, access_token=access_token)
    refresh_security.set_refresh_cookie(response=response, refresh_token=refresh_token)
    return None


def create_set_access_refresh_tokens(response: Response, subject: dict):
    access_token, refresh_token = create_access_refresh_tokens(subject=subject)
    set_access_refresh_tokens(response, access_token, refresh_token)    
    return access_token, refresh_token


def delete_access_refresh_tokens(response: Response):
    access_security.unset_access_cookie(response)
    refresh_security.unset_refresh_cookie(response)
    return None


def refresh_tokens(response: Response, refresh_token: str):
    data = jwt.decode(refresh_token, SECRET, algorithms=['HS256'])
    access_token, refresh_token = create_access_refresh_tokens(subject=data['subject'])
    set_access_refresh_tokens(response, access_token, refresh_token)
    return access_token, refresh_token