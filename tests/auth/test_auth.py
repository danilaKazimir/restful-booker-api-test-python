import pytest
import allure

from config import ADMIN_USERNAME, ADMIN_PASSWORD
from src.models.create_token.create_token_response import CreateTokenValidResponse, CreateTokenInvalidResponse


class TestAuth:
    @allure.feature('Auth API')
    @allure.title('Token creation')
    @allure.description('Check that token is successful created')
    def test_successful_token_creation(self, auth_api):
        auth_api.create_token(ADMIN_USERNAME, ADMIN_PASSWORD, 200, CreateTokenValidResponse)

    @pytest.mark.parametrize('username,password', [
        ('fake_admin', 'password123'),
        ('admin', 'fake_password'),
        ('fake_admin', 'fake_password'),
        (None, 'password123'),
        ('admin', None),
        (None, None)
    ])
    @allure.feature('Auth API')
    @allure.title('Token unsuccessful creation')
    @allure.description('Check that token cannot be created with invalid credential')
    def test_unsuccessful_token_creation(self, auth_api, username, password):
        response = auth_api.create_token(username, password, 200, CreateTokenInvalidResponse)
        auth_api.check_invalid_response(response)
