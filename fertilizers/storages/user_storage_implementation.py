from typing import Optional, List

from fertilizers.interactors.dtos import UserDetailsDTO, BasicUserDetailsDTO, FarmerRequestDTO
from fertilizers.interactors.storages.user_storage_interface import (
    UserStorageInterface,
)
from fertilizers.models import User


class UserStorageImplementation(UserStorageInterface):
    def get_user_id_for_access_token(self, access_token: str) -> str:
        from oauth2_provider.models import AccessToken
        user_id = str(AccessToken.objects.get(token=access_token).user_id)
        return user_id

    def get_basic_user_details(self, user_id: str) -> BasicUserDetailsDTO:
        user_details = User.objects.filter(id=user_id).values('username', "profile_pic_url").first()
        return BasicUserDetailsDTO(
            username=user_details["username"],
            profile_pic_url=user_details["profile_pic_url"]
        )

    def validate_username(self, username: str) -> bool:
        is_valid_username = User.objects.filter(username=username).exists()
        return is_valid_username

    def check_is_email_exists(self, email: str) -> bool:
        is_email_exists = User.objects.filter(email=email).exists()
        return is_email_exists

    def get_user_id_for_valid_username_password(
        self, username: str, password: str
    ) -> Optional[str]:
        user = User.objects.get(username=username)
        from fertilizers.exceptions.exceptions import InvalidPasswordException

        if user.check_password(password):
            return str(user.id)
        else:
            raise InvalidPasswordException

    def validate_access_token(self, access_token: str) -> bool:
        from oauth2_provider.models import AccessToken

        is_valid_access_token = AccessToken.objects.filter(
            token=access_token
        ).exists()
        return is_valid_access_token

    def delete_access_token(self, access_token: str):
        from oauth2_provider.models import AccessToken

        AccessToken.objects.get(token=access_token).delete()
        return

    def create_user_details(self, user_details_dto: UserDetailsDTO):
        user = User.objects.create(
            first_name=user_details_dto.first_name,
            last_name=user_details_dto.last_name,
            email=user_details_dto.email,
            username=user_details_dto.username,
        )
        user.set_password(raw_password=user_details_dto.password)
        user.save()

    def get_user_profession(self, user_id: str) -> str:
        user_obj = User.objects.get(id=user_id)
        return user_obj.profession

    def get_farmer_requests(self, user_id: str) -> List[FarmerRequestDTO]:
        from fertilizers.models import FarmerRequest
        request_objs = FarmerRequest.objects.filter(user_id=user_id)

        farmer_request_dtos = [
                FarmerRequestDTO(
                    farmer_name=request_obj.user.username,
                    pest_image_url=request_obj.pest_image_url,
                    crop_in_acres=request_obj.crop_in_acres,
                    plant_part=request_obj.plant_part
                )
            for request_obj in request_objs
        ]
        return farmer_request_dtos
