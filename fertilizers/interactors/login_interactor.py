from common.oauth2_storage import OAuth2SQLStorage
from fertilizers.exceptions.exceptions import InvalidPasswordException
from fertilizers.interactors.storages.user_storage_interface import (
    UserStorageInterface,
)
from fertilizers.interactors.presenters.login_presenter_interface import (
    LoginPresenterInterface,
)
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService


class LoginInteractor:
    def __init__(
        self,
        user_storage: UserStorageInterface,
        oauth_storage: OAuth2SQLStorage,
        presenter: LoginPresenterInterface,
    ):
        self.user_storage = user_storage
        self.presenter = presenter
        self.oauth_storage = oauth_storage

    def login(self, username: str, password: str):
        is_valid_username = self.user_storage.validate_username(
            username=username
        )

        is_invalid_username = not is_valid_username
        if is_invalid_username:
            return self.presenter.raise_invalid_username_exception()

        try:
            user_id = self.user_storage.get_user_id_for_valid_username_password(
                username=username, password=password
            )
        except InvalidPasswordException:
            return self.presenter.raise_invalid_password_exception()

        service = OAuthUserAuthTokensService(oauth2_storage=self.oauth_storage)
        access_token_dto = service.create_user_auth_tokens(user_id=user_id)

        user_profession = self.user_storage.get_user_profession(user_id=user_id)

        response = self.presenter.get_access_token_response(
            access_token_dto=access_token_dto, user_profession="AGO"
        )
        return response
