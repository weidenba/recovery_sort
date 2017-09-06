import os
from common_helper_files import get_dir_of_file

from main.stocktaking import get_file_meta, stocktaking

TEST_DATA_DIR = os.path.join(get_dir_of_file(__file__), '../data')
TEST_FILE_PATH = os.path.join(TEST_DATA_DIR, 'small_image.png')
TEST_FILE_UID = '4399a63790261b66220050d60396736c55af15e5c4fb5d00806acd79faf27a936453bca773d508baf1fb88d302e6c03fc9925d31ed2ce3f1939f3a7e40847897_159'


def test_get_file_meta():
    result = get_file_meta(TEST_FILE_PATH)
    assert type(result) == dict
    assert result['path'] == TEST_FILE_PATH
    assert result['name'] == 'small_image.png'
    assert type(result['mod_date']) is str
    assert result['uid'] == TEST_FILE_UID
    assert result['size'] == 159
    assert result['mime'] == 'image/png'


def test_stocktaking():
    result = stocktaking(TEST_DATA_DIR)
    assert type(result) == dict
    assert len(result) == 3  # file duplicate is ignored
    assert TEST_FILE_UID in result.keys()
    assert result[TEST_FILE_UID]['size'] == 159
