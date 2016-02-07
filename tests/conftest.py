from __future__ import unicode_literals

import mock

from mopidy_spotify_tunigo import backend, library

import pytest

import tunigo


@pytest.fixture
def config(tmpdir):
    return {
        'core': {
            'cache_dir': '%s' % tmpdir.join('cache'),
            'data_dir': '%s' % tmpdir.join('data'),
        },
        'proxy': {
        },
        'spotify_tunigo': {
            'region': 'no',
            'sub_genres': True,
            'cache_time': 3600,
        }
    }


@pytest.yield_fixture
def tunigo_mock():
    patcher = mock.patch.object(library, 'Tunigo', spec=tunigo.Tunigo)
    yield patcher.start().return_value
    patcher.stop()


@pytest.fixture
def backend_mock(config):
    backend_mock = mock.Mock(spec=backend.SpotifyTunigoBackend)
    backend_mock._config = config
    return backend_mock


@pytest.fixture
def provider(tunigo_mock, backend_mock):
    return library.SpotifyTunigoLibraryProvider(backend_mock)
