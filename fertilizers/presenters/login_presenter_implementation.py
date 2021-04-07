import json

from django.http import HttpResponse

from common.dtos import UserAuthTokensDTO
from fertilizers.interactors.presenters.login_presenter_interface import (
    LoginPresenterInterface,
)
from fertilizers.constants.exception_messages import (
    INVALID_USERNAME_EXCEPTION,
    INVALID_PASSWORD_EXCEPTION,
)


class LoginPresenterImplementation(LoginPresenterInterface):
    def raise_invalid_username_exception(self):
        response_dict = {
            "response_content": INVALID_USERNAME_EXCEPTION[0],
            "response": INVALID_USERNAME_EXCEPTION[1],
        }
        response_data = json.dumps(response_dict)
        return HttpResponse(response_data, status=403)

    def raise_invalid_password_exception(self):
        response_dict = {
            "response_content": INVALID_PASSWORD_EXCEPTION[0],
            "response": INVALID_PASSWORD_EXCEPTION[1],
        }
        response_data = json.dumps(response_dict)
        return HttpResponse(response_data, status=403)

    def get_access_token_response(self, access_token_dto: UserAuthTokensDTO):
        access_token_response = {
            "user_id": access_token_dto.user_id,
            "access_token": access_token_dto.access_token,
            "refresh_token": access_token_dto.refresh_token,
            "expires_in": str(access_token_dto.expires_in),
        }

        response_data = json.dumps(access_token_response)
        return HttpResponse(response_data, status=200)
