from typing import Optional

from fertilizers.interactors.storages.user_storage_interface import (
    UserStorageInterface,
)
from fertilizers.models import User


class UserStorageImplementation(UserStorageInterface):
    def validate_username(self, username: str) -> bool:
        is_valid_username = User.objects.filter(username=username).exists()
        return is_valid_username

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
