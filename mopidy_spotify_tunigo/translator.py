from __future__ import unicode_literals

import re

from mopidy.models import Ref


def parse_uri(uri):
    result = re.findall(r'^spotifytunigo:([a-z]+)(?::(\w+))?$', uri)
    if result:
        return result[0]
    return None, None


def to_mopidy_playlists(tunigo_playlists):
    playlists = []
    for playlist in tunigo_playlists:
        playlists.append(Ref.playlist(uri=playlist.uri, name=playlist.title))
    return playlists


def genres_to_mopidy_directories(tunigo_genres):
    genres = []
    for genre in tunigo_genres:
        uri = 'spotifytunigo:genres:{}'.format(genre.key)
        genres.append(Ref.directory(uri=uri, name=genre.name))
    return genres


def releases_to_mopidy_albums(tunigo_releases):
    releases = []
    for release in tunigo_releases:
        name = '{} - {}'.format(release.artist_name, release.album_name)
        releases.append(Ref.album(uri=release.uri, name=name))
    return releases
