from fertilizers.interactors.storages.user_storage_interface import (
    UserStorageInterface,
)
from fertilizers.interactors.presenters.get_user_details_presenter_interface import (
    GetUserDetailsPresenterInterface,
)


class GetUserDetailsInteractor:
    def __init__(
        self,
        user_storage: UserStorageInterface,
        presenter: GetUserDetailsPresenterInterface,
    ):
        self.user_storage = user_storage
        self.presenter = presenter

    def get_user_id_for_access_token(self, access_token: str) -> str:
        user_id = self.user_storage.get_user_id_for_access_token(access_token=access_token)
        return user_id

    def get_basic_user_details(self, user_id: str):
        basic_user_details_dto = self.user_storage.get_basic_user_details(
            user_id=user_id
        )

        response = self.presenter.get_basic_user_details_response(
            basic_user_details_dto=basic_user_details_dto
        )
        return response
