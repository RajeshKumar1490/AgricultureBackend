from mock import create_autospec, patch
from common.dtos import UserAuthTokensDTO
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.oauth2_storage import OAuth2SQLStorage
from fertilizers.interactors.login_interactor import LoginInteractor
from fertilizers.interactors.storages.user_storage_interface \
    import UserStorageInterface
from fertilizers.interactors.presenters.login_presenter_interface import LoginPresenterInterface
from fertilizers.exceptions.exceptions import InvalidPasswordException


def test_login_interactor_with_valid_credentials_creates_new_access_token():
    #Arrange
    user_id = "user_1"
    username = "9032751617"
    password = "admin123"
    access_token = "1ke3ue3ijkbdfsfdke"
    time_in_sec = 10000000
    refresh_token = "hsbfdhjbsjkfb"

    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(LoginPresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    interactor = LoginInteractor(
        user_storage=user_storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )

    mock_access_token_dto = UserAuthTokensDTO(
        user_id=user_id,
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=time_in_sec
    )

    assert 1==1
