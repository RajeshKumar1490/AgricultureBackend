import json
from common.dtos import UserAuthTokensDTO
from fertilizers.presenters.login_presenter_implementation \
    import LoginPresenterImplementation


def test_get_access_token_response_returns_access_token():
    #Arrange
    access_token_dto = UserAuthTokensDTO(
        user_id="user_1", access_token='KQDt2vRGfdlgCxD8JnUG3rOa63u5tb',
        refresh_token='hpC1itwrO7X4AgjWdOVCLUfJC9P7CE',
        expires_in='1000000'
    )
    json_presenter = LoginPresenterImplementation()
    expected_access_token_response = {
        "user_id": access_token_dto.user_id,
        "access_token": access_token_dto.access_token,
        "refresh_token": access_token_dto.refresh_token,
        "expires_in": access_token_dto.expires_in
    }

    #Act
    response = \
        json_presenter.get_access_token_response(access_token_dto)

    #Assert
    access_token_response = response.content
    assert json.loads(access_token_response) == expected_access_token_response
    assert response.status_code == 200
