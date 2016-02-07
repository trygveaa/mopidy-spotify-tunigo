from __future__ import unicode_literals


class TestSpotifyTunigoLibraryProvider(object):

    def test_has_root_directory(self, provider):
        assert provider.root_directory.uri == 'spotifytunigo:directory'
        assert provider.root_directory.name == 'Spotify Browse'

    def test_returns_empty_array_on_unknown_uri(self, provider):
        result = provider.browse('spotifytunigo:unknown')

        assert result == []

    def test_returns_root_directories(self, provider):
        result = provider.browse('spotifytunigo:directory')

        assert len(result) == 4

        assert result[0].uri == 'spotifytunigo:featured'
        assert result[0].name == 'Featured Playlists'

        assert result[1].uri == 'spotifytunigo:toplists'
        assert result[1].name == 'Top Lists'

        assert result[2].uri == 'spotifytunigo:genres'
        assert result[2].name == 'Genres & Moods'

        assert result[3].uri == 'spotifytunigo:releases'
        assert result[3].name == 'New Releases'

    def test_returns_featured(self, provider, tunigo_mock):
        provider.browse('spotifytunigo:featured')

        tunigo_mock.get_featured_playlists.assert_called_once_with()

    def test_returns_top_lists(self, provider, tunigo_mock):
        provider.browse('spotifytunigo:toplists')

        tunigo_mock.get_top_lists.assert_called_once_with()

    def test_returns_genres(self, provider, tunigo_mock):
        provider.browse('spotifytunigo:genres')

        tunigo_mock.get_genres.assert_called_once_with()

    def test_returns_sub_genres_for_genre(self, provider, tunigo_mock):
        provider.browse('spotifytunigo:genres:genre0')

        tunigo_mock.get_genres.assert_called_once_with()

    def test_returns_playlists_for_sub_genre(self, provider, tunigo_mock):
        provider.browse('spotifytunigo:genres:genre0:subgenre0')

        tunigo_mock.get_genre_playlists.assert_called_once_with(
            'genre0', 'subgenre0')

    def test_returns_releases(self, provider, tunigo_mock):
        provider.browse('spotifytunigo:releases')

        tunigo_mock.get_new_releases.assert_called_once_with()

    def test_returns_playlists_for_genre_when_sub_genres_config_is_false(
            self, config, provider, tunigo_mock):
        config['spotify_tunigo']['sub_genres'] = False

        provider.browse('spotifytunigo:genres:genre0')

        tunigo_mock.get_genre_playlists.assert_called_once_with(
            'genre0', 'all')
