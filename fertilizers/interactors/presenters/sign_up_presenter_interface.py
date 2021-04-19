import abc


class SignUpPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def not_strong_password_exception(self):
        pass

    @abc.abstractmethod
    def passwords_not_equal_exception(self):
        pass

    @abc.abstractmethod
    def username_already_exists_exception(self):
        pass

    @abc.abstractmethod
    def email_already_exists_exception(self, email: str):
        pass

    @abc.abstractmethod
    def sign_up_response(self):
        pass
