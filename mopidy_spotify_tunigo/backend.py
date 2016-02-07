from __future__ import unicode_literals

from mopidy import backend

from mopidy_spotify_tunigo.library import SpotifyTunigoLibraryProvider

import pykka


class SpotifyTunigoBackend(pykka.ThreadingActor, backend.Backend):
    def __init__(self, config, audio):
        super(SpotifyTunigoBackend, self).__init__()

        self._config = config

        self.library = SpotifyTunigoLibraryProvider(backend=self)

        self.uri_schemes = ['spotifytunigo']
