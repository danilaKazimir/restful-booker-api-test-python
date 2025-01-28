class TestPing:
    def test_successful_ping(self, ping_api):
        ping_api.ping_request(201)
        ping_api.check_ping_response()
