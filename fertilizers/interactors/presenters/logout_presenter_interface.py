import abc


class LogoutPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_invalid_access_token_exception(self):
        pass

    @abc.abstractmethod
    def logout_response(self):
        pass
