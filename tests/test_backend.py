from __future__ import unicode_literals

from mopidy import backend as backend_api

from mopidy_spotify_tunigo import backend, library


class TestSpotifyTunigoBackend(object):

    def get_backend(self, config):
        return backend.SpotifyTunigoBackend(config=config, audio=None)

    def test_uri_schemes(self, config):
        backend = self.get_backend(config)

        assert 'spotifytunigo' in backend.uri_schemes

    def test_init_sets_up_the_providers(self, config):
        backend = self.get_backend(config)

        assert isinstance(
            backend.library, library.SpotifyTunigoLibraryProvider)
        assert isinstance(backend.library, backend_api.LibraryProvider)
