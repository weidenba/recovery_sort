from common_helper_files import get_binary_from_file
from hashlib import sha256
import os
import time
import logging
import magic
import sys


def generate_uid(file_path):
    file_data = get_binary_from_file(file_path)
    if file_data == b'' or type(file_data) is not bytes:
        return "0_0"
    file_hash = sha256(file_data).hexdigest()
    file_size = get_file_size(file_path)
    return "{}_{}".format(file_hash, file_size)


def get_modification_date(file_path):
    '''
    Return a string of the modification date: YYYY-MM-DD
    '''
    try:
        mod_date = os.path.getmtime(file_path)
        mod_date = time.localtime(mod_date)
        return time.strftime('%Y-%m-%d', mod_date)
    except Exception as e:
        logging.error('Could not get timestamp: {} {}'.format(sys.exc_info()[0].__name__, e))
        return '0'


def get_file_size(file_path):
    '''
    Returns size of a file in bytes
    '''
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        logging.error('Could not get file size: {} {}'.format(sys.exc_info()[0].__name__, e))
    return 0


def get_file_name(file_path):
    '''
    Returns a the file name
    '''
    file_name = file_path.split('/')[-1:][0]
    return file_name


def get_file_mime(file_path):
    '''
    Returns the mime_type of a file
    '''
    try:
        return magic.from_file(file_path, mime=True)
    except Exception as e:
        logging.error('Could not get file type: {} {}'.format(sys.exc_info()[0].__name__, e))
        return 'unknown'
