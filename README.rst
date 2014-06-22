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

- ``Mopidy`` > 0.18.3. The music server that Mopidy-Spotify-Tunigo extends.

- ``Mopidy-Spotify`` > 1.1.3. The Mopidy extension for playing music from
  Spotify.


Installation
============

Install by running::

    pip install Mopidy-Spotify-Tunigo

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<http://apt.mopidy.com/>`_.


Configuration
=============

The following configuration values are available:

- ``spotify_tunigo/enabled``: If the Spotify-Tunigo extension should be enabled
  or not.
- ``spotify_tunigo/region``: The region to fetch playlists and releases for.
  Either "all" or a two letter country code. Defaults to "all".


Project resources
=================

- `Source code <https://github.com/trygveaa/mopidy-spotify-tunigo>`_
- `Issue tracker <https://github.com/trygveaa/mopidy-spotify-tunigo/issues>`_
- `Download development snapshot <https://github.com/trygveaa/mopidy-spotify-tunigo/archive/master.tar.gz#egg=Mopidy-Spotify-Tunigo-dev>`_


Changelog
=========

v0.1.0 (UNRELEASED)
-------------------

- Initial release.
