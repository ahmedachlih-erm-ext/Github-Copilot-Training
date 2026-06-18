from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as app_activities

original_activities = deepcopy(app_activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_activities.clear()
    app_activities.update(deepcopy(original_activities))
    yield


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def sample_activities():
    return deepcopy(original_activities)
