import os
import re
from common_helper_files import get_dir_of_file, get_files_in_dir
from tempfile import TemporaryDirectory

from main.ReOrganizer import ReOrganizer


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
    re_organizer = ReOrganizer(testing=True)
    assert re_organizer._generate_new_file_path(input_data) == 'text/plain/2017-01-01_test_file.txt'


def test_store_to_new_location():
    tmp_dir = TemporaryDirectory()
    file_meta = {
        'path': TEST_FILE_PATH,
        'mime': 'image/png',
        'mod_date': '2017-01-01',
        'name': 'test_image.png'
    }
    re_organizer = ReOrganizer(out_dir=tmp_dir.name, testing=True)
    re_organizer._store_to_new_location(file_meta)
    assert os.path.exists(os.path.join(tmp_dir.name, 'image/png/2017-01-01_test_image.png'))


def test_process_file():
    tmp_dir = TemporaryDirectory()
    re_organizer = ReOrganizer(out_dir=tmp_dir.name, testing=False)
    re_organizer._process_file(TEST_FILE_PATH)
    result = get_files_in_dir(tmp_dir.name)
    assert len(result) == 1
    assert re.search(r'image\/png\/[0-9]{4}-[0-9]{2}-[0-9]{2}_small_image\.png', result[0]) is not None


def test_reorganize_files():
    tmp_dir = TemporaryDirectory()
    re_organizer = ReOrganizer(out_dir=tmp_dir.name, testing=False)
    re_organizer.reorganize_files(TEST_DATA_DIR)
    result = get_files_in_dir(tmp_dir.name)
    assert len(result) == 5
