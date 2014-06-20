from __future__ import unicode_literals

from mopidy import backend
from mopidy.models import Ref


class SpotifyTunigoLibraryProvider(backend.LibraryProvider):
    root_directory = Ref.directory(uri='spotifytunigo:directory',
                                   name='Spotify Browse')

    def __init__(self, *args, **kwargs):
        super(SpotifyTunigoLibraryProvider, self).__init__(*args, **kwargs)

        self._root = []

    def browse(self, uri):
        if uri == self.root_directory.uri:
            return self._root

        return []
