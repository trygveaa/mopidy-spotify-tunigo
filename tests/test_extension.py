from __future__ import unicode_literals

import mock

from mopidy_spotify_tunigo import Extension, backend as backend_lib


class TestExtension(object):

    def test_get_default_config(self):
        ext = Extension()

        config = ext.get_default_config()

        assert '[spotify_tunigo]' in config
        assert 'enabled = true' in config

    def test_get_config_schema(self):
        ext = Extension()

        schema = ext.get_config_schema()

        assert 'region' in schema
        assert 'cache_time' in schema

    def test_setup(self):
        registry = mock.Mock()

        ext = Extension()
        ext.setup(registry)

        registry.add.assert_called_with(
            'backend', backend_lib.SpotifyTunigoBackend)
