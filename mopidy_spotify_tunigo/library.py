from __future__ import unicode_literals

import requests

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
            return self._fetch_playlists(variant)

        if variant == 'genres':
            if identifier:
                return self._fetch_playlists(identifier)
            else:
                return self._fetch_genres()

        if variant == 'releases':
            return []

        return []

    def _get(self, identifier):
        uri = ('https://api.tunigo.com/v3/space/{0}?region={1}&per_page=1000'
               .format(identifier,
                       self.backend.config['spotify_tunigo']['region']))
        return requests.get(uri).json()['items']

    def _fetch_playlists(self, genre):
        playlists = []
        for item in self._get(genre):
            playlists.append(Ref.playlist(uri=item['playlist']['uri'],
                                          name=item['playlist']['title']))
        return playlists

    def _fetch_genres(self):
        genres = []
        for item in self._get('genres'):
            genre_id = item['genre']['templateName']
            if genre_id != 'toplists':
                genres.append(Ref.directory(
                    uri='spotifytunigo:genres:{0}'.format(genre_id),
                    name=item['genre']['name']))
        return genres
