from __future__ import unicode_literals

import unittest

from mopidy_spotify_tunigo import Extension


class ExtensionTest(unittest.TestCase):

    def test_get_default_config(self):
        ext = Extension()

        config = ext.get_default_config()

        self.assertIn('[spotify_tunigo]', config)
        self.assertIn('enabled = true', config)

    def test_get_config_schema(self):
        ext = Extension()

        schema = ext.get_config_schema()

        self.assertIn('region', schema)
        self.assertIn('cache_time', schema)

    # TODO Write more tests
