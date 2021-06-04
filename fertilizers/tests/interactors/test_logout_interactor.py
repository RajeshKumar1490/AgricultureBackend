from mock import create_autospec
from fertilizers.interactors.logout_interactor \
    import LogoutInteractor
from fertilizers.interactors.storages.user_storage_interface \
    import UserStorageInterface
from fertilizers.interactors.presenters.logout_presenter_interface \
    import LogoutPresenterInterface


def test_logout_interactor_with_invalid_access_token_raises_exception():
    #Arrane
    access_token = "akufiuwebfkjkrnfgkjvndfkj"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(LogoutPresenterInterface)
    interactor = LogoutInteractor(
        user_storage=user_storage, presenter=presenter
    )
    user_storage.validate_access_token.return_value = False

    #Act
    interactor.logout(access_token=access_token)

    #Assert
    user_storage.validate_access_token.assert_called_once_with(
        access_token=access_token
    )
    presenter.raise_invalid_access_token_exception.assert_called_once()


def test_logout_interactor_with_valid_access_token_deletes_access_token():
    #Arrane
    access_token = "akufiuwebfkjkrnfgkjvndfkj"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(LogoutPresenterInterface)
    interactor = LogoutInteractor(
        user_storage=user_storage, presenter=presenter
    )
    user_storage.validate_access_token.return_value = True

    #Act
    interactor.logout(access_token=access_token)

    #Assert
    user_storage.validate_access_token.assert_called_once_with(
        access_token=access_token
    )
    user_storage.delete_access_token.assert_called_once_with(
        access_token=access_token
    )
    presenter.logout_response.assert_called_once()
