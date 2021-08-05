from django.views.decorators.csrf import csrf_exempt

from fertilizers.interactors.get_user_details_interactor import GetUserDetailsInteractor
from fertilizers.interactors.get_farmers_requests_interactor import GetFarmersRequestsInteractor
from fertilizers.presenters.get_farmer_requests_presenter_implementation import (
    GetFarmersRequestsPresenterImplementation,
)
from fertilizers.presenters.get_user_details_presenter_implementation import GetUserDetailsPresenterImplementation
from fertilizers.storages.user_storage_implementation import (
    UserStorageImplementation,
)


@csrf_exempt
def GetFarmerRequests(request):
    access_token = str(request.headers["Authorization"][7:])

    user_storage = UserStorageImplementation()
    get_farmer_requests_presenter = GetFarmersRequestsPresenterImplementation()
    get_user_details_presenter = GetUserDetailsPresenterImplementation()

    user_details_interactor = GetUserDetailsInteractor(
        user_storage=user_storage,
        presenter=get_user_details_presenter
    )

    get_farmer_requests_interactor = GetFarmersRequestsInteractor(
        user_storage=user_storage,
        presenter=get_farmer_requests_presenter
    )

    user_id = user_details_interactor.get_user_id_for_access_token(access_token=access_token)

    response = get_farmer_requests_interactor.get_farmers_requests(user_id=user_id)

    return response
