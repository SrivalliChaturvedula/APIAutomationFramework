#  Conftest

# Create token, create booking id, update booking, delete booking

# Verify that create booking id when we update it and delete also.

import allure
import pytest
import requests
import conftest
from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils


@pytest.mark.put
@allure.title("Test CRUD operation Update(PUT).")
@allure.description(
    "Verify that Full Update with the booking ID and Token is working.")
class TestCRUDBooking(object):
        @pytest.mark.put
        @allure.title("Test CRUD operation Update(PUT).")
        @allure.description(
            "Verify that Full Update with the booking ID and Token is working.")
        def test_update_booking_id_token(self, create_token, get_booking_id):
            put_url = APIConstants.url_patch_put_delete(booking_id=get_booking_id)
            print(put_url)
            response = put_request(
                url=put_url,
                headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
                payload=payload_update_booking(),
                auth=None,
                in_json=False
            )
            # Verification here & more
            verify_response_key(response.json()["firstname"], "Amit")
            verify_response_key(response.json()["lastname"], "Brown")
            verify_http_status_code(response_data=response, expected_data=200)

        def test_delete_booking_id(self, create_token, get_booking_id):
            delete_url = APIConstants.url_patch_put_delete(booking_id=get_booking_id)
            response = delete_request(
                url=delete_url,
                headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
                payload={ },
                auth=None,
                in_json=False
            )
            verify_response_delete(response=response.text)
            verify_http_status_code(response_data=response, expected_data=201)
