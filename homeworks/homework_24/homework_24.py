import pytest
import requests
from assertpy import soft_assertions, assert_that
from requests.auth import HTTPBasicAuth
import logging
from pathlib import Path

from homeworks.homework_24.cars_controller import CarsController

LOG_FILE = Path(__file__).parent / "test_search.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger(__name__)
BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()

    response = session.post(f"{BASE_URL}/auth",
                            auth=HTTPBasicAuth("test_user", "test_pass"))

    assert response.status_code == 200, f"Authentication failed: {response.text}"
    access_token = response.json()["access_token"]

    session.headers.update({"Authorization": f"Bearer {access_token}"})

    yield session
    session.close()

@pytest.fixture(scope="class")
def cars_controller(auth_session):
    return CarsController(
        session=auth_session,
        base_url=BASE_URL
    )

class TestCars:
    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("brand", 10),
            ("year", 3),
            ("engine_volume", 7),
            ("price", 5),
            ("price", 2),
            ("brand", 5),
        ]
    )

    def test_get_cars(self, cars_controller, sort_by, limit):
        logger.info("Search cars: %s, limit: %d", sort_by, limit)

        response = cars_controller.get_cars(sort_by=sort_by, limit=limit)

        logger.info(
            "Response status: %s", response.status_code
        )

        cars = response.json()
        actual_values = [car[sort_by] for car in cars]
        expected_values = sorted(actual_values)

        logger.info("Retrieved cars: %s", len(cars))
        logger.info("Actual values: %s", actual_values)
        logger.info("Expected values: %s",expected_values)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(len(cars)).is_equal_to(limit)
            assert_that(actual_values).is_equal_to(expected_values)

