import gc
import pytest

from udata.i18n import language
from udata.core.dataset.factories import DatasetFactory, ResourceFactory


@pytest.fixture
def no_gc():
    '''Prevent garbage collecting during test with anonymous objects (factories)'''
    gc.disable()
    yield
    gc.collect()
    gc.enable()


pytestmark = [
    pytest.mark.usefixtures('clean_db', 'no_gc'),
    pytest.mark.options(PLUGINS=['geoplatform']),
]

LOCALES = ['en', 'fr']


@pytest.mark.parametrize('locale', LOCALES)
def test_display_preview_for_api_resources(locale):
    resource = ResourceFactory(extras={
        'geop:resource_id': 'RID',
    })
    DatasetFactory(resources=[resource], extras={
        'geop:dataset_id': 'DID'
    })
    expected = 'https://geo.data.gouv.fr/embed/datasets/DID/resources/RID?lang={0}'.format(locale)  # noqa
    with language(locale):
        assert resource.preview_url == expected


@pytest.mark.options(DEFAULT_LANGUAGE='fr')
def test_fallback_to_default_locale():
    resource = ResourceFactory(extras={
        'geop:resource_id': 'RID',
    })
    DatasetFactory(resources=[resource], extras={
        'geop:dataset_id': 'DID'
    })
    expected = 'https://geo.data.gouv.fr/embed/datasets/DID/resources/RID?lang=fr'  # noqa
    assert resource.preview_url == expected


def test_display_no_preview_for_no_resource_extra():
    resource = ResourceFactory()
    DatasetFactory(resources=[resource], extras={
        'geop:dataset_id': 'DID'
    })
    assert resource.preview_url is None


def test_display_no_preview_for_no_dataset_extra():
    resource = ResourceFactory(extras={
        'geop:resource_id': 'RID',
    })
    DatasetFactory(resources=[resource])
    assert resource.preview_url is None
