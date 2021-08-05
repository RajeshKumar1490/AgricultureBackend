from fertilizers.interactors.storages.user_storage_interface import (
    UserStorageInterface,
)
from fertilizers.interactors.presenters.get_farmers_requests_presenter_interface import (
    GetFarmersRequestsPresenterInterface,
)


class GetFarmersRequestsInteractor:
    def __init__(
        self,
        user_storage: UserStorageInterface,
        presenter: GetFarmersRequestsPresenterInterface,
    ):
        self.user_storage = user_storage
        self.presenter = presenter

    def get_farmers_requests(self, user_id: str):
        farmer_request_dtos = self.user_storage.get_farmer_requests(
            user_id=user_id
        )

        response = self.presenter.get_farmer_request_response(
            farmer_request_dtos=farmer_request_dtos
        )
        return response
