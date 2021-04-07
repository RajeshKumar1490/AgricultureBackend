from typing import Optional
import abc


class UserStorageInterface(abc.ABC):
    @abc.abstractmethod
    def validate_username(self, username: str) -> bool:
        pass

    @abc.abstractmethod
    def get_user_id_for_valid_username_password(
        self, username: str, password: str
    ) -> Optional[int]:
        pass

    @abc.abstractmethod
    def validate_access_token(self, access_token: str) -> bool:
        pass

    @abc.abstractmethod
    def delete_access_token(self, access_token: str):
        pass
