import pytest


class TestAuth:
    VALID_USERNAME = 'admin'
    VALID_PASSWORD = 'password123'

    def test_successful_token_creation(self, get_auth_token):
        get_auth_token()

    @pytest.mark.parametrize('username,password', [
        ('fake_admin', 'password123'),
        ('admin', 'fake_password'),
        ('fake_admin', 'fake_password'),
        (None, 'password123'),
        ('admin', None),
        (None, None)
    ])
    def test_unsuccessful_token_creation(self, auth_api, username, password):
        auth_api.create_token(username, password, 200)
        auth_api.check_invalid_response()
