import re

NAME = 'thumbnail'


def filter_function(file_stock):
    tmp_stock = dict()
    for item in file_stock.keys():
        if not _is_photorec_thumbnail_name(file_stock[item]['name']):
            tmp_stock[item] = file_stock[item]
    return tmp_stock


def setup(app):
    app.register_plugin(NAME, filter_function)


def _is_photorec_thumbnail_name(file_name):
    tmp = re.fullmatch(r't[0-9]+.jpg', file_name)
    return tmp is not None
