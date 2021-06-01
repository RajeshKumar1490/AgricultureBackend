import json

from django.views.decorators.csrf import csrf_exempt

from common.oauth2_storage import OAuth2SQLStorage
from fertilizers.interactors.login_interactor import LoginInteractor
from fertilizers.presenters.login_presenter_implementation import (
    LoginPresenterImplementation,
)
from fertilizers.storages.user_storage_implementation import (
    UserStorageImplementation,
)


@csrf_exempt
def login(request):

    print(request)
    request_data = json.loads(request.body)
    print(request_data)
    username = request_data.get("username", " ")
    password = request_data.get("password", " ")

    oauth_storage = OAuth2SQLStorage()
    user_storage = UserStorageImplementation()
    login_presenter = LoginPresenterImplementation()

    interactor = LoginInteractor(
        user_storage=user_storage,
        presenter=login_presenter,
        oauth_storage=oauth_storage,
    )

    response = interactor.login(username=username, password=password)
    return response
