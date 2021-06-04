import datetime
from dataclasses import dataclass


@dataclass
class UserAuthTokensDTO:
    user_id: str
    access_token: str
    refresh_token: str
    expires_in: str


@dataclass
class AccessTokenDTO:
    access_token_id: int
    token: str
    expires: datetime.datetime


@dataclass
class RefreshTokenDTO:
    token: str
    access_token: int
    user_id: str
    revoked: datetime.datetime


@dataclass
class Application:
    application_id: int
