from typing import Optional

from fertilizers.interactors.dtos import UserDetailsDTO
from fertilizers.interactors.storages.user_storage_interface import (
    UserStorageInterface,
)
from fertilizers.models import User


class UserStorageImplementation(UserStorageInterface):
    def validate_username(self, username: str) -> bool:
        is_valid_username = User.objects.filter(username=username).exists()
        return is_valid_username

    def check_is_email_exists(self, email: str) -> bool:
        is_email_exists = User.objects.filter(email=email).exists()
        return is_email_exists

    def get_user_id_for_valid_username_password(
        self, username: str, password: str
    ) -> Optional[int]:
        user = User.objects.get(username=username)
        from fertilizers.exceptions.exceptions import InvalidPasswordException

        if user.check_password(password):
            return user.id
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
