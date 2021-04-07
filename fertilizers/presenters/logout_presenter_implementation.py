import json

from django.http import HttpResponse

from fertilizers.interactors.presenters.logout_presenter_interface import (
    LogoutPresenterInterface,
)
from fertilizers.constants.exception_messages import INVALID_ACCESS_TOKEN


class LogoutPresenterImplementation(LogoutPresenterInterface):
    def raise_invalid_access_token_exception(self):
        response_dict = {
            "response_content": INVALID_ACCESS_TOKEN[0],
            "response": INVALID_ACCESS_TOKEN[1],
        }
        response_data = json.dumps(response_dict)
        return HttpResponse(response_data, status=403)

    def logout_response(self):
        return HttpResponse(status=205)
