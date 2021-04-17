import json

from django.views.decorators.csrf import csrf_exempt

from fertilizers.interactors.sign_up_interactor import SignUpInteractor
from fertilizers.presenters.sign_up_presenter_implementation import (
    SignUpPresenterImplementation,
)
from fertilizers.storages.user_storage_implementation import (
    UserStorageImplementation,
)


@csrf_exempt
def sign_up(request):
    request_data = json.loads(request.body)
    first_name = request_data.get("first_name", "")
    last_name = request_data.get("last_name", "")
    email = request_data.get("email", "")
    password = request_data.get("password", "")
    username = request_data.get("username", "")

    user_storage = UserStorageImplementation()
    sign_up_presenter = SignUpPresenterImplementation()

    interactor = SignUpInteractor(
        user_storage=user_storage,
        presenter=sign_up_presenter,
    )

    from fertilizers.interactors.dtos import UserDetailsDTO

    user_details_dto = UserDetailsDTO(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        username=username,
    )

    response = interactor.sign_up(user_details_dto=user_details_dto)
    return response
