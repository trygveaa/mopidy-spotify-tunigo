from __future__ import unicode_literals

from mopidy.models import Ref

from mopidy_spotify_tunigo import translator

from tunigo import Genre, Playlist, Release, SubGenre


class TestParseUri(object):

    def test_returns_one_part_on_match(self):
        part1, part2, part3 = translator.parse_uri(
            'spotifytunigo:partone')

        assert part1 == 'partone'
        assert part2 == ''
        assert part3 == ''

    def test_returns_two_parts_on_match(self):
        part1, part2, part3 = translator.parse_uri(
            'spotifytunigo:partone:parttwo')

        assert part1 == 'partone'
        assert part2 == 'parttwo'
        assert part3 == ''

    def test_returns_three_parts_on_match(self):
        part1, part2, part3 = translator.parse_uri(
            'spotifytunigo:partone:parttwo:partthree')

        assert part1 == 'partone'
        assert part2 == 'parttwo'
        assert part3 == 'partthree'

    def test_returns_none_on_no_match(self):
        part1, part2, part3 = translator.parse_uri('spotifytunigo')

        assert part1 is None
        assert part2 is None
        assert part3 is None

    def test_does_not_allow_number_in_first_part(self):
        part1, part2, part3 = translator.parse_uri(
            'spotifytunigo:part1:parttwo:partthree')

        assert part1 is None
        assert part2 is None
        assert part3 is None

    def test_allows_number_in_second_and_third_part(self):
        part1, part2, part3 = translator.parse_uri(
            'spotifytunigo:partone:part2:part3')

        assert part1 == 'partone'
        assert part2 == 'part2'
        assert part3 == 'part3'


class TestToMopidyPlaylists(object):

    def test_returns_list_of_playlists_converted_to_mopidy_playlists(self):
        playlist0 = Playlist(title='Playlist 0', uri='uri:0')
        playlist1 = Playlist(title='Playlist 1', uri='uri:1')

        playlists = translator.to_mopidy_playlists([playlist0, playlist1])

        assert len(playlists) == 2

        assert isinstance(playlists[0], Ref)
        assert playlists[0].type == Ref.PLAYLIST
        assert playlists[0].name == 'Playlist 0'
        assert playlists[0].uri == 'uri:0'

        assert isinstance(playlists[1], Ref)
        assert playlists[1].type == Ref.PLAYLIST
        assert playlists[1].name == 'Playlist 1'
        assert playlists[1].uri == 'uri:1'


class TestGenresToMopidyDirectories(object):

    def test_returns_list_of_genres_converted_to_mopidy_directories(self):
        genre0 = Genre(name='Genre 0', template_name='genre0')
        genre1 = Genre(name='Genre 1', template_name='genre1')

        genres = translator.genres_to_mopidy_directories([genre0, genre1])

        assert len(genres) == 2

        assert isinstance(genres[0], Ref)
        assert genres[0].type == Ref.DIRECTORY
        assert genres[0].name == 'Genre 0'
        assert genres[0].uri == 'spotifytunigo:genres:genre0'

        assert isinstance(genres[1], Ref)
        assert genres[1].type == Ref.DIRECTORY
        assert genres[1].name == 'Genre 1'
        assert genres[1].uri == 'spotifytunigo:genres:genre1'


class TestGenresToSubGenresMopidyDirectories(object):

    def test_returns_list_of_sub_genres_converted_to_mopidy_directories(self):
        genre0 = Genre(
            name='Genre 0',
            template_name='genre0',
            playlist_uri='uri:playlist',
            sub_genres=[
                SubGenre(name='SubGenre 00', key='subgenre00'),
                SubGenre(name='SubGenre 01', key='subgenre01'),
            ]
        )
        genre1 = Genre(name='Genre 1', template_name='genre1', sub_genres=[
            SubGenre(name='SubGenre 10', key='subgenre10'),
        ])

        sub_genres = translator.genres_to_sub_genres_mopidy_directories(
            [genre0, genre1], 'genre0')

        assert len(sub_genres) == 4

        assert isinstance(sub_genres[0], Ref)
        assert sub_genres[0].type == Ref.DIRECTORY
        assert sub_genres[0].name == 'All'
        assert sub_genres[0].uri == 'spotifytunigo:genres:genre0:all'

        assert isinstance(sub_genres[1], Ref)
        assert sub_genres[1].type == Ref.DIRECTORY
        assert sub_genres[1].name == 'Top tracks'
        assert sub_genres[1].uri == 'uri:playlist'

        assert isinstance(sub_genres[2], Ref)
        assert sub_genres[2].type == Ref.DIRECTORY
        assert sub_genres[2].name == 'SubGenre 00'
        assert sub_genres[2].uri == 'spotifytunigo:genres:genre0:subgenre00'

        assert isinstance(sub_genres[3], Ref)
        assert sub_genres[3].type == Ref.DIRECTORY
        assert sub_genres[3].name == 'SubGenre 01'
        assert sub_genres[3].uri == 'spotifytunigo:genres:genre0:subgenre01'


class TestReleasesToMopidyAlbums(object):

    def test_returns_list_of_releases_converted_to_mopidy_albums(self):
        release0 = Release(
            artist_name='Artist 0', album_name='Album 0', uri='uri:0')
        release1 = Release(
            artist_name='Artist 1', album_name='Album 1', uri='uri:1')

        releases = translator.releases_to_mopidy_albums([release0, release1])

        assert len(releases) == 2

        assert isinstance(releases[0], Ref)
        assert releases[0].type == Ref.ALBUM
        assert releases[0].name == 'Artist 0 - Album 0'
        assert releases[0].uri == 'uri:0'

        assert isinstance(releases[1], Ref)
        assert releases[1].type == Ref.ALBUM
        assert releases[1].name == 'Artist 1 - Album 1'
        assert releases[1].uri == 'uri:1'
