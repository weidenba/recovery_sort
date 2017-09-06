import os
from common_helper_files import get_dir_of_file
from tempfile import TemporaryDirectory

from main.main import _generate_new_file_path, _store_to_new_location


TEST_DATA_DIR = os.path.join(get_dir_of_file(__file__), '../data')
TEST_FILE_PATH = os.path.join(TEST_DATA_DIR, 'small_image.png')


def test_generate_new_file_path():
    input_data = {
        'uid': 'abcde',
        'size': 10,
        'name': 'test_file.txt',
        'mod_date': '2017-01-01',
        'mime': 'text/plain'
    }
    assert _generate_new_file_path(input_data) == 'text/plain/2017-01-01_test_file.txt'


def test_store_to_new_location():
    tmp_dir = TemporaryDirectory()
    file_stock = {
        'abc': {
            'path': TEST_FILE_PATH,
            'mime': 'image/png',
            'mod_date': '2017-01-01',
            'name': 'test_image.png'
        }
    }
    _store_to_new_location(file_stock, tmp_dir.name)
    assert os.path.exists(os.path.join(tmp_dir.name, 'image/png/2017-01-01_test_image.png'))
