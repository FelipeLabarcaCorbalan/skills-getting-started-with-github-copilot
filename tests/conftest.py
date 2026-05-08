import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_data


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = copy.deepcopy(activities_data)
    yield
    activities_data.clear()
    activities_data.update(copy.deepcopy(original_activities))


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
