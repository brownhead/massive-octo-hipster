import pytest

import main
import request_globals

@pytest.fixture(scope="session", autouse=True)
def _init_app():
    main.init()

@pytest.fixture
def app(request):
    return request_globals.app.test_client()
