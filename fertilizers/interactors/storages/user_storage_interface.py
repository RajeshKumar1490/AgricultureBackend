from typing import Optional
import abc

from fertilizers.interactors.dtos import UserDetailsDTO, BasicUserDetailsDTO


class UserStorageInterface(abc.ABC):
    @abc.abstractmethod
    def get_user_id_for_access_token(self, access_token: str) -> str:
        pass

    @abc.abstractmethod
    def validate_username(self, username: str) -> bool:
        pass

    @abc.abstractmethod
    def check_is_email_exists(self, email: str) -> bool:
        pass

    @abc.abstractmethod
    def get_user_id_for_valid_username_password(
        self, username: str, password: str
    ) -> Optional[str]:
        pass

    @abc.abstractmethod
    def validate_access_token(self, access_token: str) -> bool:
        pass

    @abc.abstractmethod
    def delete_access_token(self, access_token: str):
        pass

    @abc.abstractmethod
    def create_user_details(self, user_details_dto: UserDetailsDTO):
        pass

    @abc.abstractmethod
    def get_basic_user_details(self, user_id: str) -> BasicUserDetailsDTO:
        pass

