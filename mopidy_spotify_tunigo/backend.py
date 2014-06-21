from __future__ import unicode_literals

import pykka

from mopidy import backend

from mopidy_spotify_tunigo.library import SpotifyTunigoLibraryProvider


class SpotifyTunigoBackend(pykka.ThreadingActor, backend.Backend):
    def __init__(self, config, audio):
        super(SpotifyTunigoBackend, self).__init__()

        self.config = config

        self.library = SpotifyTunigoLibraryProvider(backend=self)

        self.uri_schemes = ['spotifytunigo']
