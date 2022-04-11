import pytest
from django.db import IntegrityError

pytestmark = [
    pytest.mark.django_db
]


def test_create_airplane_record_ok(api) -> None:
    response = api.post(f'/api/v1/airplanes/',
                        data={
                            "airplane_id": 1,
                            "airplane_name": "first",
                            "passengers_count": 5,
                        },
                        expected_status_code=200)

    assert response is not None

    got = response.json()

    assert got['capacity'] == '200 ℓ'
    assert got['consumption_per_min'] == '0.01 ℓ/min'
    assert got['max_minutes_able_to_fly'] == '20000 min'


def test_create_airplane_record_wrong_passenger_count_fail(api) -> None:
    with pytest.raises(IntegrityError):
        api.post(f'/api/v1/airplanes/',
                 data={
                     "airplane_id": 1,
                     "airplane_name": "first",
                     "passengers_count": -5,
                 },
                 )


def test_create_airplane_record_required_fields_fail(api) -> None:
    response = api.post(f'/api/v1/airplanes/',
                        data={
                            "airplane_id": 1,
                            "airplane_name": "first",
                        },
                        expected_status_code=200)

    assert response

    got = response.json()

    assert got == {'passengers_count': ['This field is required.']}
