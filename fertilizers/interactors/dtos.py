from dataclasses import dataclass


@dataclass
class UserDetailsDTO:
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    verify_password: str


@dataclass
class BasicUserDetailsDTO:
    username: str
    profile_pic_url: str


@dataclass
class FarmerRequestDTO:
    farmer_name: str
    pest_image_url: str
    plant_part: str
    crop_in_acres: int
