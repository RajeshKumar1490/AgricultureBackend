from dataclasses import dataclass


@dataclass
class UserDetailsDTO:
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
