import re

NAME = 'thumbnail'


def filter_function(file_meta, file_cache=None):
    tmp = re.fullmatch(r't[0-9]+.jpg', file_meta['name'])
    return tmp is not None


def setup(app):
    app.register_plugin(NAME, filter_function)
