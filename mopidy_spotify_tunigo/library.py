from __future__ import unicode_literals

from mopidy import backend, httpclient
from mopidy.models import Ref

from mopidy_spotify_tunigo import translator

from tunigo import Tunigo


class SpotifyTunigoLibraryProvider(backend.LibraryProvider):
    root_directory = Ref.directory(
        uri='spotifytunigo:directory',
        name='Spotify Browse')

    def __init__(self, backend):
        self._config = backend._config['spotify_tunigo']

        proxy = httpclient.format_proxy(backend._config['proxy'])

        self._tunigo = Tunigo(
            region=self._config['region'],
            cache_time=self._config['cache_time'],
            proxies={'http': proxy, 'https': proxy})

        self._root = [
            Ref.directory(
                uri='spotifytunigo:featured',
                name='Featured Playlists'),
            Ref.directory(
                uri='spotifytunigo:toplists',
                name='Top Lists'),
            Ref.directory(
                uri='spotifytunigo:genres',
                name='Genres & Moods'),
            Ref.directory(
                uri='spotifytunigo:releases',
                name='New Releases')]

    def browse(self, uri):
        if uri == self.root_directory.uri:
            return self._root

        variant, identifier, subidentifier = translator.parse_uri(uri.lower())

        if variant == 'featured':
            return translator.to_mopidy_playlists(
                self._tunigo.get_featured_playlists())

        if variant == 'toplists':
            return translator.to_mopidy_playlists(
                self._tunigo.get_top_lists())

        if variant == 'genres':
            if identifier:
                if subidentifier or not self._config['sub_genres']:
                    return translator.to_mopidy_playlists(
                        self._tunigo.get_genre_playlists(
                            identifier, subidentifier or 'all'))
                else:
                    return translator.genres_to_sub_genres_mopidy_directories(
                        self._tunigo.get_genres(), identifier)
            else:
                return translator.genres_to_mopidy_directories(
                    self._tunigo.get_genres())

        if variant == 'releases':
            return translator.releases_to_mopidy_albums(
                self._tunigo.get_new_releases())

        return []
