import abc
from typing import List

from fertilizers.interactors.dtos import FarmerRequestDTO


class GetFarmersRequestsPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_farmer_request_response(self, farmer_request_dtos: List[FarmerRequestDTO]):
        pass
