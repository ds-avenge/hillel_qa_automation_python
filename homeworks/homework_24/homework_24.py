import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging
from pathlib import Path

LOG_FILE = Path(__file__).parent / "test_search.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.propagate = False

@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()

    response = session.post("http://127.0.0.1:8080/auth",
                            auth=HTTPBasicAuth("test_user", "test_pass"))

    assert response.status_code == 200, f"Authentication failed: {response.text}"
    access_token = response.json()["access_token"]

    session.headers.update({"Authorization": f"Bearer {access_token}"})

    yield session
    session.close()

class TestCars:
    def test_auth(self, auth_session):
        print(auth_session.headers)

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

    def test_get_cars(self, auth_session, sort_by, limit):
        logger.info(
            f"Search cars: sort_by={sort_by}, limit={limit}"
        )

        response = auth_session.get("http://127.0.0.1:8080/cars",
                                    params={"sort_by": sort_by, "limit": limit})
        assert response.status_code == 200, f"Failed to get cars: {response.text}"

        cars = response.json()
        assert len(cars) == limit
        actual_values = [car[sort_by] for car in cars]
        expected_values = sorted(actual_values)

        assert actual_values == expected_values
        logger.info(
            f"Response status: {response.status_code}"
        )
        logger.info(
            f"Retrieved cars: {len(cars)}"
        )
        logger.info(
            f"Actual values: {actual_values}"
        )
        logger.info(
            f"Expected values: {expected_values}"
        )
        print(cars)
