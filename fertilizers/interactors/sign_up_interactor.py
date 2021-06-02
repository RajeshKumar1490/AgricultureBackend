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

        if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', user_details_dto.password):
            return self.presenter.not_strong_password_exception()

        is_passwords_not_equal = (
            user_details_dto.password != user_details_dto.verify_password
        )
        if is_passwords_not_equal:
            return self.presenter.passwords_not_equal_exception()

        is_username_exists = self.user_storage.validate_username(
            username=user_details_dto.username
        )
        if is_username_exists:
            return self.presenter.username_already_exists_exception()

        is_email_exists = self.user_storage.check_is_email_exists(
            email=user_details_dto.email
        )
        if is_email_exists:
            return self.presenter.email_already_exists_exception(
                email=user_details_dto.email
            )

        self.user_storage.create_user_details(user_details_dto=user_details_dto)

        return self.presenter.sign_up_response()
