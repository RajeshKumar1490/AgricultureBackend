import json

from django.http import HttpResponse

from fertilizers.constants.exception_messages import (
    NOT_A_STRONG_PASSWORD,
    PASSWORDS_NOT_EQUAL,
    USERNAME_ALREADY_EXISTS,
    EMAIL_ALREADY_EXISTS,
)
from fertilizers.interactors.presenters.sign_up_presenter_interface import (
    SignUpPresenterInterface,
)


class SignUpPresenterImplementation(SignUpPresenterInterface):
    def sign_up_response(self):
        return HttpResponse(status=201)

    def passwords_not_equal_exception(self):
        response_dict = {
            "response_content": PASSWORDS_NOT_EQUAL[1],
            "response": PASSWORDS_NOT_EQUAL[0],
        }
        response_data = json.dumps(response_dict)
        return HttpResponse(response_data, status=400)

    def not_strong_password_exception(self):
        response_dict = {
            "response_content": NOT_A_STRONG_PASSWORD[1],
            "response": NOT_A_STRONG_PASSWORD[0],
        }
        response_data = json.dumps(response_dict)
        return HttpResponse(response_data, status=400)

    def username_already_exists_exception(self):
        response_dict = {
            "response_content": USERNAME_ALREADY_EXISTS[1],
            "response": USERNAME_ALREADY_EXISTS[0],
        }
        response_data = json.dumps(response_dict)
        return HttpResponse(response_data, status=400)

    def email_already_exists_exception(self, email: str):
        response_dict = {
            "response_content": EMAIL_ALREADY_EXISTS[1].format(email),
            "response": EMAIL_ALREADY_EXISTS[0],
        }
        response_data = json.dumps(response_dict)
        return HttpResponse(response_data, status=400)
