from fertilizers.interactors.dtos import UserDetailsDTO
from fertilizers.interactors.presenters.sign_up_presenter_interface import (
    SignUpPresenterInterface,
)
from fertilizers.interactors.storages.user_storage_interface import (
    UserStorageInterface,
)


class SignUpInteractor:
    def __init__(
        self,
        user_storage: UserStorageInterface,
        presenter: SignUpPresenterInterface,
    ):
        self.user_storage = user_storage
        self.presenter = presenter

    def sign_up(self, user_details_dto: UserDetailsDTO):
        import re

        strong_password_pattern = (
            "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        )
        result = re.findall(strong_password_pattern, user_details_dto.password)
        is_not_strong_password = not result
        if is_not_strong_password:
            return self.presenter.not_strong_password_exception()

        is_username_exists = self.user_storage.validate_username(
            username=user_details_dto.username
        )
        if is_username_exists:
            return self.presenter.username_already_exists_exception()

        self.user_storage.create_user_details(user_details_dto=user_details_dto)

        return self.presenter.sign_up_response()
