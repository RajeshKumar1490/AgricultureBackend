from fertilizers.interactors.storages.user_storage_interface import (
    UserStorageInterface,
)
from fertilizers.interactors.presenters.logout_presenter_interface import (
    LogoutPresenterInterface,
)


class LogoutInteractor:
    def __init__(
        self,
        user_storage: UserStorageInterface,
        presenter: LogoutPresenterInterface,
    ):
        self.user_storage = user_storage
        self.presenter = presenter

    def logout(self, access_token: str):
        is_valid_access_token = self.user_storage.validate_access_token(
            access_token=access_token
        )

        is_invalid_access_token = not is_valid_access_token

        if is_invalid_access_token:
            return self.presenter.raise_invalid_access_token_exception()

        self.user_storage.delete_access_token(access_token=access_token)
        return self.presenter.logout_response()
