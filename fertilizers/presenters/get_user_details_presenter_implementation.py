import json

from django.http import HttpResponse
from fertilizers.interactors.dtos import BasicUserDetailsDTO
from fertilizers.interactors.presenters.get_user_details_presenter_interface import (
    GetUserDetailsPresenterInterface,
)


class GetUserDetailsPresenterImplementation(GetUserDetailsPresenterInterface):
    def get_basic_user_details_response(self, basic_user_details_dto: BasicUserDetailsDTO):
        basic_user_details = {
            "username": basic_user_details_dto.username,
            "profile_pic_rul": basic_user_details_dto.profile_pic_url,
        }

        response_data = json.dumps(basic_user_details)
        return HttpResponse(response_data, status=200)
