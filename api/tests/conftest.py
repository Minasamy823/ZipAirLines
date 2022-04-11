import pytest
from rest_framework.test import APIClient
from mixer.backend.django import mixer as _mixer


@pytest.fixture
def api():
    return APIClient()


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def airplanes(mixer):
    mixer.cycle(2).blend('core.Airplane')
    return mixer.blend('core.Airplane',
                       airplane_id=2,
                       airplane_name="Aeroflot",
                       passengers_count=15
                       )
