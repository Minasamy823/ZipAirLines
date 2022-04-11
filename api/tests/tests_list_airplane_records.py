import pytest

from core.models import Airplane

pytestmark = [
    pytest.mark.django_db
]


def test_list_airplane_record_ok(api, airplanes: Airplane) -> None:
    response = api.post(f'/api/v1/airplanes/', expected_status_code=200)

    assert response is not None

    got = response.json()

    assert len(got) == 3
