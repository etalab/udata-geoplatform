# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from udata.i18n import get_locale
from udata.core.dataset.preview import PreviewPlugin

GEOP_PREFIX = 'geop'
RESOURCE_EXTRA = '{}:resource_id'.format(GEOP_PREFIX)
DATASET_EXTRA = '{}:dataset_id'.format(GEOP_PREFIX)
GEOP_URL_TEMPLATE = 'https://geo.data.gouv.fr/embed/datasets/{dataset_id}/resources/{resource_id}?lang={lang}'  # noqa


class GeoplatformPreview(PreviewPlugin):
    def get_resource_extra(self, resource):
        return getattr(resource, 'extras', {}).get(RESOURCE_EXTRA)

    def get_dataset_extra(self, resource):
        return getattr(resource.dataset, 'extras', {}).get(DATASET_EXTRA)

    def can_preview(self, resource):
        return self.get_resource_extra(resource) and \
               self.get_dataset_extra(resource)

    def preview_url(self, resource):
        return GEOP_URL_TEMPLATE.format(
            resource_id=self.get_resource_extra(resource),
            dataset_id=self.get_dataset_extra(resource),
            lang=get_locale(),
        )
