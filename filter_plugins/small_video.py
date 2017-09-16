NAME = 'small_video'

THRESHOLD = 10240


def filter_function(file_stock):
    tmp_stock = dict()
    for item in file_stock.keys():
        if not _is_small_video(file_stock[item]):
            tmp_stock[item] = file_stock[item]
    return tmp_stock


def setup(app):
    app.register_plugin(NAME, filter_function)


def _is_small_video(file_meta):
    return file_meta['size'] < THRESHOLD and 'video' in file_meta['mime']
