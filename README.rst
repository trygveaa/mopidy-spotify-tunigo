*******
WARNING
*******

As of 2019, **the Tunigo service is no longer operational**. Thus, the
maintenance of this extension has been stopped. Some or all of the
functionality this extension provided is available through the `Spotify Web API
<https://developer.spotify.com/documentation/web-api/>`_, and may be
implemented in `Mopidy-Spotify <https://github.com/mopidy/mopidy-spotify>`_ in
the future.

*********************
Mopidy-Spotify-Tunigo
*********************

.. image:: https://img.shields.io/pypi/v/Mopidy-Spotify-Tunigo.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-Spotify-Tunigo/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-Spotify-Tunigo.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-Spotify-Tunigo/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/travis/trygveaa/mopidy-spotify-tunigo/master.png?style=flat
    :target: https://travis-ci.org/trygveaa/mopidy-spotify-tunigo
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/trygveaa/mopidy-spotify-tunigo/master.svg?style=flat
   :target: https://coveralls.io/r/trygveaa/mopidy-spotify-tunigo?branch=master
   :alt: Test coverage

`Mopidy <http://www.mopidy.com/>`_ extension for providing the browse feature
of `Spotify <http://www.spotify.com/>`_. This lets you browse playlists, genres
and new releases.

Uses the `Tunigo <http://tunigo.com/>`_ API, which is also what Spotify itself
uses. Note that the API is not documented or officially released, so it may
change at any time.


Dependencies
============

- ``Mopidy`` >= 0.19.0. The music server that Mopidy-Spotify-Tunigo extends.

- ``Mopidy-Spotify`` >= 1.2.0. The Mopidy extension for playing music from
  Spotify.

- ``Python-Tunigo`` >= 1.0.0. A library for accessing the Tunigo API.


Installation
============

Debian/Ubuntu/Raspbian: Install the ``mopidy-spotify-tunigo`` package from
`apt.mopidy.com <http://apt.mopidy.com/>`_::

    sudo apt-get install mopidy-spotify-tunigo

Arch Linux: Install the ``mopidy-spotify-tunigo`` package from
`AUR <https://aur.archlinux.org/packages/mopidy-spotify/>`_, e.g.::

    yaourt -S mopidy-spotify-tunigo

Else: Install the ``Mopidy-Spotify-Tunigo`` package from PyPI::

    pip install Mopidy-Spotify-Tunigo


Configuration
=============

The following configuration values are available:

- ``spotify_tunigo/enabled``: If the Spotify-Tunigo extension should be enabled
  or not.
- ``spotify_tunigo/region``: The region to fetch playlists and releases for.
  The value should be a two letter country code if set. Defaults to empty,
  which means all regions.
- ``spotify_tunigo/sub_genres``: Whether to show sub genres and top tracks
  under each genre. Defaults to True.
- ``spotify_tunigo/cache_time``: The amount of seconds to cache the results
  from the API. A value of 0 will disable the cache. Defaults to 3600.


License
=======

Mopidy-Spotify-Tunigo is licensed under the `Apache License, Version 2.0
<http://www.apache.org/licenses/LICENSE-2.0>`_.


Project resources
=================

- `Source code <https://github.com/trygveaa/mopidy-spotify-tunigo>`_
- `Issue tracker <https://github.com/trygveaa/mopidy-spotify-tunigo/issues>`_
- `Download development snapshot <https://github.com/trygveaa/mopidy-spotify-tunigo/archive/master.tar.gz#egg=Mopidy-Spotify-Tunigo-dev>`_


Changelog
=========

v1.0.0 (2016-02-07)
-------------------

- Support using a proxy when connecting to Tunigo. (Fixes: #6)
- Add a config option for only returning the genre playlists for a genre,
  instead of an extra level with the top tracks and sub genres for the genre as
  well.
- Change default region from all to empty.
- Add tests for all classes.

v0.2.1 (2014-07-21)
-------------------

- Update dependencies.
- Fix flake8 errors, unused imports and docs syntax.
- Test config options.

v0.2.0 (2014-06-23)
-------------------

- Move Tunigo API into a separate library.
- Add option to specify cache time.
- List top tracks and sub genres in each genre.

v0.1.0 (2014-06-21)
-------------------

- Initial release.
