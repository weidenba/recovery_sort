import os
from common_helper_files import get_dir_of_file

from main.stocktaking import get_file_meta

TEST_DATA_DIR = os.path.join(get_dir_of_file(__file__), '../data')
TEST_FILE_PATH = os.path.join(TEST_DATA_DIR, 'small_image.png')
TEST_FILE_UID = 'ed1015323e7c3a16936523ce1a64928a805f5b37534d74b596570d6931dc5684_159'


def test_get_file_meta():
    result = get_file_meta(TEST_FILE_PATH)
    assert type(result) == dict
    assert result['path'] == TEST_FILE_PATH
    assert result['name'] == 'small_image.png'
    assert type(result['mod_date']) is str
    assert result['uid'] == TEST_FILE_UID
    assert result['size'] == 159
    assert result['mime'] == 'image/png'
