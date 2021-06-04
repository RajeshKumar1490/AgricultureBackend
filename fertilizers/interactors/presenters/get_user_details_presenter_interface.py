import abc

from fertilizers.interactors.dtos import BasicUserDetailsDTO


class GetUserDetailsPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_basic_user_details_response(self, basic_user_details_dto: BasicUserDetailsDTO):
        pass
