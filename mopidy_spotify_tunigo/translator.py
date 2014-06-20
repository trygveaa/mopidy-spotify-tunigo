from __future__ import unicode_literals

import re


def parse_uri(uri):
    result = re.findall(r'^spotifytunigo:([a-z]+)(?::(\w+))?$', uri)
    if result:
        return result[0]
    return None, None
