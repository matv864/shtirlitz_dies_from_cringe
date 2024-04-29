import httpx

HOST = "http://127.0.0.1:8000"


class Test_auth:
    def _registration_request(
        self,
        username: str,
        password: str
    ) -> httpx.Response:
        url = f"{HOST}/registration"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        user_credentials = {
            "username": username,
            "password": password
        }
        response = httpx.post(url, json=user_credentials, headers=headers)
        return response

    def _login_request(
        self,
        username: str,
        password: str
    ) -> httpx.Response:
        url = f"{HOST}/login"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        user_credentials = {
            "username": username,
            "password": password
        }
        response = httpx.post(url, data=user_credentials, headers=headers)

        return response

    def _refresh_request(self, refresh_token: str):
        url = f"{HOST}/refresh"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        user_credentials = {
            "refresh_token": refresh_token
        }

        response = httpx.post(url, json=user_credentials, headers=headers)
        return response

    def _who_am_i_request(self, access_token: str):
        url = f"{HOST}/who_am_i"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = httpx.post(url, headers=headers)
        return response

    # tests

    def test_register(self):
        response = self._registration_request("111", "111")
        assert (
            response.status_code == 201 or
            response.json()["detail"] == "user exists"
        )

    def test_good_login(self):
        response = self._login_request("111", "111")
        response_json = response.json()
        assert response_json["token_type"] == "bearer"
        response_json["access_token"]
        response_json["refresh_token"]

    def test_bad_login(self):
        response = self._login_request("111", "112")
        assert response.status_code == 403

    def test_refresh_token(self):
        response = self._login_request("111", "111")
        refresh_token = response.json()["refresh_token"]
        response = self._refresh_request(refresh_token)
        response.json()["access_token"]
        assert response.status_code == 200

    def test_who_am_i(self):
        response = self._login_request("111", "111")
        access_token = response.json()["access_token"]
        response = self._who_am_i_request(access_token)
        str(response.content)
