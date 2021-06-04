from django.views.decorators.csrf import csrf_exempt

from fertilizers.interactors.get_user_details_interactor import GetUserDetailsInteractor
from fertilizers.presenters.get_user_details_presenter_implementation import (
    GetUserDetailsPresenterImplementation,
)
from fertilizers.storages.user_storage_implementation import (
    UserStorageImplementation,
)


@csrf_exempt
def GetBasicUserDetails(request):
    access_token = str(request.headers["Authorization"][7:])

    user_storage = UserStorageImplementation()
    presenter = GetUserDetailsPresenterImplementation()

    interactor = GetUserDetailsInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    user_id = interactor.get_user_id_for_access_token(access_token=access_token)

    response = interactor.get_basic_user_details(user_id=user_id)
    return response
