import pytest

from udata import settings
from udata.app import create_app


@pytest.fixture
def app():
    app = create_app(settings.Defaults, override=settings.Testing)
    return app
