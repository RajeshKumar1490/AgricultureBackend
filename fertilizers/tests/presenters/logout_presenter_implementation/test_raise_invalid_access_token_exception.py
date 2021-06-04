import json

import pytest
from fertilizers.presenters.logout_presenter_implementation \
    import LogoutPresenterImplementation
from fertilizers.constants.exception_messages \
    import INVALID_ACCESS_TOKEN


def test_raise_invalid_access_token_exception():
    #Arrange
    json_presenter = LogoutPresenterImplementation()
    expected_exception_message = INVALID_ACCESS_TOKEN[0]
    expected_response = INVALID_ACCESS_TOKEN[1]

    #Act
    response_obj = json_presenter.raise_invalid_access_token_exception()

    #Assert
    response = json.loads(response_obj.content)
    assert response["response_content"] == expected_exception_message
    assert response["response"] == expected_response
