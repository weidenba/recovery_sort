from common_helper_files import get_dir_of_file
from common_helper_passwords import get_merged_password_set
import os

NAME = 'blacklist'


def filter_function(file_stock):
    blacklist_dir = _get_blacklist_dir()
    blacklist = get_merged_password_set(blacklist_dir)
    return _apply_blacklist_filter(file_stock, blacklist)


def setup(app):
    app.register_plugin(NAME, filter_function)


def _apply_blacklist_filter(file_stock, blacklist):
    tmp_stock = dict()
    for item in file_stock.keys():
        if item not in blacklist:
            tmp_stock[item] = file_stock[item]
    return tmp_stock


def _get_blacklist_dir():
    return os.path.join(get_dir_of_file(__file__), '../blacklist')
