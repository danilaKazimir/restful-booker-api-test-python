class TestPing:
    def test_successful_ping(self, ping_api):
        ping_api.ping_request().check_ping_response()
