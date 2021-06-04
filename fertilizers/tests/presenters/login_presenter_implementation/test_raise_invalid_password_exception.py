import json

from fertilizers.presenters.login_presenter_implementation \
    import LoginPresenterImplementation
from fertilizers.constants.exception_messages \
    import INVALID_PASSWORD_EXCEPTION


def test_raise_invalid_password_exception():
    #Arrange
    json_presenter = LoginPresenterImplementation()
    expected_exception_message = INVALID_PASSWORD_EXCEPTION[1]
    expected_response = INVALID_PASSWORD_EXCEPTION[0]

    #Act
    response_obj = json_presenter.raise_invalid_password_exception()

    #Assert
    response = json.loads(response_obj.content)
    assert response["response_content"] == expected_exception_message
    assert response["response"] == expected_response
