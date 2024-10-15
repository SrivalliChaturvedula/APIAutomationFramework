"""
API Testcase

URL -> api_constants.py
headers -> utils.py
payload -> payload_manager.py
HTTP POST -> api_request_wrapper.py
verification -> common_verification.py

"""

import allure
import pytest
import requests
from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils
import logging


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should "
        "not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        logger = logging.getLogger(__name__)
        logger.info("Starting the testcase: TC1 - positive")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        logger.info(response.json()["bookingid"])
        logger.info("End of Testcase: TC1 - positive")

    @pytest.mark.negative
    @allure.title("Verify that Create Booking Status does not work without payload")
    @allure.description(
        "Creating a Booking without payload and status code should be 520")
    def test_create_booking_negative(self):
        response_data = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=response_data, expected_data=500)
