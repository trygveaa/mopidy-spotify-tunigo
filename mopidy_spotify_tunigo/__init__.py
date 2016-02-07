from __future__ import unicode_literals

import os

from mopidy import config, ext


__version__ = '1.0.0'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Spotify-Tunigo'
    ext_name = 'spotify_tunigo'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['region'] = config.String(optional=True)
        schema['sub_genres'] = config.Boolean()
        schema['cache_time'] = config.Integer(minimum=0, optional=True)
        return schema

    def setup(self, registry):
        from .backend import SpotifyTunigoBackend
        registry.add('backend', SpotifyTunigoBackend)
