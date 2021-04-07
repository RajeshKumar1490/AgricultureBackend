import abc
from common.dtos import UserAuthTokensDTO


class LoginPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_invalid_username_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_password_exception(self):
        pass

    @abc.abstractmethod
    def get_access_token_response(self, access_token_dto: UserAuthTokensDTO):
        pass
