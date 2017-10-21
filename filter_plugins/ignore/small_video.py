NAME = 'small_video'

THRESHOLD = 10240


def filter_function(file_meta, file_cache=None):
    return file_meta['size'] < THRESHOLD and 'video' in file_meta['mime']


def setup(app):
    app.register_plugin(NAME, filter_function)
