import pytest

from udata.core.dataset.factories import DatasetFactory, ResourceFactory

pytestmark = [
    pytest.mark.usefixtures('clean_db'),
    pytest.mark.options(PLUGINS=['geoplatform']),
]


def test_display_preview_for_api_resources():
    resource = ResourceFactory(extras={
        'geop:resource_id': 'RID',
    })
    DatasetFactory(resources=[resource], extras={
        'geop:dataset_id': 'DID'
    })
    assert resource.preview_url == 'https://geo.data.gouv.fr/embed/datasets/DID/resources/RID?lang=fr'  # noqa


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
