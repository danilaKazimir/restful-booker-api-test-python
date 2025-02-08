from src.models.health_check.health_check_response import HealthCheckResponse


class TestPing:
    def test_successful_ping(self, ping_api):
        response: HealthCheckResponse = ping_api.ping_request(201)
        ping_api.check_ping_response(response)
