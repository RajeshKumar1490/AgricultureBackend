from django.views.decorators.csrf import csrf_exempt

from fertilizers.interactors.logout_interactor import LogoutInteractor
from fertilizers.presenters.logout_presenter_implementation import (
    LogoutPresenterImplementation,
)
from fertilizers.storages.user_storage_implementation import (
    UserStorageImplementation,
)


@csrf_exempt
def logout(request):
    access_token = request.headers["Authorization"][8:]

    user_storage = UserStorageImplementation()
    presenter = LogoutPresenterImplementation()

    logout_interactor = LogoutInteractor(
        user_storage=user_storage, presenter=presenter
    )

    response = logout_interactor.logout(access_token=access_token)
    return response
