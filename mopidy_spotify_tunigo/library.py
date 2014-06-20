from __future__ import unicode_literals

from mopidy import backend
from mopidy.models import Ref

from . import translator


class SpotifyTunigoLibraryProvider(backend.LibraryProvider):
    root_directory = Ref.directory(uri='spotifytunigo:directory',
                                   name='Spotify Browse')

    def __init__(self, *args, **kwargs):
        super(SpotifyTunigoLibraryProvider, self).__init__(*args, **kwargs)

        self._root = [Ref.directory(uri='spotifytunigo:toplists',
                                    name='Top Lists'),
                      Ref.directory(uri='spotifytunigo:genres',
                                    name='Genres & Moods'),
                      Ref.directory(uri='spotifytunigo:releases',
                                    name='New Releases')]

    def browse(self, uri):
        if uri == self.root_directory.uri:
            return self._root

        variant, identifier = translator.parse_uri(uri.lower())

        if variant == 'toplists':
            return []

        if variant == 'genres':
            return []

        if variant == 'releases':
            return []

        return []
