NAME = 'duplicate'


def filter_function(file_meta, file_cache=None):
    return file_meta['uid'] in file_cache


def setup(app):
    app.register_plugin(NAME, filter_function)
