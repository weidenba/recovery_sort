from common_helper_files import get_dir_of_file
from common_helper_passwords import get_merged_password_set
import logging
import os

NAME = 'blacklist'

BLACKLIST = list()


def filter_function(file_meta, file_cache=None):
    _get_blacklist()
    return file_meta['uid'] in BLACKLIST


def setup(app):
    app.register_plugin(NAME, filter_function)


def _get_blacklist():
    global BLACKLIST
    if len(BLACKLIST) == 0:
        blacklist_dir = _get_blacklist_dir()
        BLACKLIST = get_merged_password_set(blacklist_dir)
        logging.debug('blacklist with {} entries loaded'.format(len(BLACKLIST)))


def _get_blacklist_dir():
    return os.path.join(get_dir_of_file(__file__), '../../blacklist')
