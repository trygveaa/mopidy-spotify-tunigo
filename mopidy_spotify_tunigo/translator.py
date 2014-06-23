from __future__ import unicode_literals

import re

from mopidy.models import Ref


def parse_uri(uri):
    result = re.findall(r'^spotifytunigo:([a-z]+)(?::(\w+))?(?::(\w+))?$', uri)
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


def genres_to_sub_genres_mopidy_directories(tunigo_genres, genre_key):
    sub_genres = []
    for genre in tunigo_genres:
        if genre.key == genre_key:
            sub_genres.append(Ref.directory(
                uri='spotifytunigo:genres:{}:all'.format(genre_key),
                name='All'))
            sub_genres.append(Ref.directory(uri=genre.playlist.uri,
                                            name='Top tracks'))
            for sub_genre in genre.sub_genres:
                uri = 'spotifytunigo:genres:{}:{}'.format(genre_key,
                                                          sub_genre.key)
                sub_genres.append(Ref.directory(uri=uri, name=sub_genre.name))
            break
    return sub_genres


def releases_to_mopidy_albums(tunigo_releases):
    releases = []
    for release in tunigo_releases:
        name = '{} - {}'.format(release.artist_name, release.album_name)
        releases.append(Ref.album(uri=release.uri, name=name))
    return releases
