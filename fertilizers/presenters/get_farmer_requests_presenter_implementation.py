import json

from django.http import HttpResponse
from typing import List

from fertilizers.interactors.dtos import FarmerRequestDTO
from fertilizers.interactors.presenters.get_farmers_requests_presenter_interface import \
    GetFarmersRequestsPresenterInterface


class GetFarmersRequestsPresenterImplementation(GetFarmersRequestsPresenterInterface):
    def get_farmer_request_response(self, farmer_request_dtos: List[FarmerRequestDTO]):
        count = 1
        farmers_requests = []
        for farmer_request_dto in farmer_request_dtos:
            farmers_requests.append(
                {
                    "s_no": count,
                    "farmer_name": farmer_request_dto.farmer_name,
                    "pesticide_picture": farmer_request_dto.pest_image_url,
                    "part_of_the_plant": farmer_request_dto.plant_part,
                    "crop_in_acres": farmer_request_dto.crop_in_acres
                }
            )
            count += 1

        complete_farmer_details = {
            "farmer_details": farmers_requests,
            "no_of_farmer_details": (count - 1)
        }

        response_data = json.dumps(complete_farmer_details)
        return HttpResponse(response_data, status=200)

