from __future__ import unicode_literals

import time

import requests

from mopidy import backend
from mopidy.models import Ref

from . import translator


class SpotifyTunigoLibraryProvider(backend.LibraryProvider):
    root_directory = Ref.directory(uri='spotifytunigo:directory',
                                   name='Spotify Browse')

    def __init__(self, *args, **kwargs):
        super(SpotifyTunigoLibraryProvider, self).__init__(*args, **kwargs)

        self._root = [Ref.directory(uri='spotifytunigo:featured',
                                    name='Featured Playlists'),
                      Ref.directory(uri='spotifytunigo:toplists',
                                    name='Top Lists'),
                      Ref.directory(uri='spotifytunigo:genres',
                                    name='Genres & Moods'),
                      Ref.directory(uri='spotifytunigo:releases',
                                    name='New Releases')]

    def browse(self, uri):
        if uri == self.root_directory.uri:
            return self._root

        variant, identifier = translator.parse_uri(uri.lower())

        if variant == 'featured':
            return self._fetch_playlists(
                'featured-playlists',
                'dt={}'.format(time.strftime('%FT%T')))

        if variant == 'toplists':
            return self._fetch_playlists(variant)

        if variant == 'genres':
            if identifier:
                return self._fetch_playlists(identifier)
            else:
                return self._fetch_genres()

        if variant == 'releases':
            return self._fetch_releases()

        return []

    def _get(self, identifier, options=''):
        uri = ('https://api.tunigo.com/v3/space/{}?region={}&per_page=1000'
               .format(identifier,
                       self.backend.config['spotify_tunigo']['region']))
        if options:
            uri = '{}&{}'.format(uri, options)
        return requests.get(uri).json()['items']

    def _fetch_playlists(self, genre, options=''):
        playlists = []
        for item in self._get(genre, options):
            playlists.append(Ref.playlist(uri=item['playlist']['uri'],
                                          name=item['playlist']['title']))
        return playlists

    def _fetch_genres(self):
        genres = []
        for item in self._get('genres'):
            genre_id = item['genre']['templateName']
            if genre_id != 'toplists':
                genres.append(Ref.directory(
                    uri='spotifytunigo:genres:{}'.format(genre_id),
                    name=item['genre']['name']))
        return genres

    def _fetch_releases(self):
        playlists = []
        for item in self._get('new-releases'):
            name = '{} - {}'.format(item['release']['artistName'],
                                    item['release']['albumName'])
            playlists.append(Ref.album(uri=item['release']['uri'], name=name))
        return playlists
