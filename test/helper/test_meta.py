import os
import pytest
import time
from common_helper_files import get_dir_of_file

from helper.meta import generate_uid, get_file_size, get_file_mime,\
    get_file_name, get_modification_date

TEST_DATA_DIR = os.path.join(get_dir_of_file(__file__), '../data')
TEST_FILE_PATH = os.path.join(TEST_DATA_DIR, 'small_image.png')


@pytest.mark.parametrize('input_data, expected', [
    (TEST_FILE_PATH, 'ed1015323e7c3a16936523ce1a64928a805f5b37534d74b596570d6931dc5684_159'),
    ('none_existing_file', '0_0')
])
def test_generate_uid(input_data, expected):
    assert generate_uid(input_data) == expected


@pytest.mark.parametrize('input_data, expected', [(TEST_FILE_PATH, 159), ('none_existing_file', 0)])
def test_get_file_size(input_data, expected):
    assert get_file_size(input_data) == expected


@pytest.mark.parametrize('input_data, expected', [(TEST_FILE_PATH, 'image/png'), ('none_existing_file', 'unknown')])
def test_get_file_mime(input_data, expected):
    assert get_file_mime(input_data) == expected


@pytest.mark.parametrize('input_data, expected', [('foo/bar.img', 'bar.img'), ('/bar.img', 'bar.img'), ('bar.img', 'bar.img')])
def test_get_file_name(input_data, expected):
    assert get_file_name(input_data) == expected


def test_get_modification_date():
    assert get_modification_date('none_existing') == '0'
    os.utime(TEST_FILE_PATH)
    today = time.strftime("%Y-%m-%d")
    assert get_modification_date(TEST_FILE_PATH) == today
