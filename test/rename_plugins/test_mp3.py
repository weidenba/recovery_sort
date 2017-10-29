from copy import deepcopy
from common_helper_files import get_dir_of_file
import os
import pytest

from filter_plugins.rename.mp3 import filter_function


TEST_DATA_DIR = os.path.join(get_dir_of_file(__file__), '../data')
TEST_FILE_WITH_META = os.path.join(TEST_DATA_DIR, 'complete_meta.mp3')
TEST_FILE_WITHOUT_META = os.path.join(TEST_DATA_DIR, 'no_meta.mp3')


def test_none_mp3_file():
    test_meta_none_mp3_file = {'mime': 'text_plain'}
    meta_backup = deepcopy(test_meta_none_mp3_file)
    filter_function(test_meta_none_mp3_file)
    assert test_meta_none_mp3_file == meta_backup


@pytest.mark.parametrize('input_data, expected', [
    (TEST_FILE_WITH_META, 'Rec Sort Project/Test Album/Rec Sort Test MP3.mp3'),
    (TEST_FILE_WITHOUT_META, 'unknown/unknown/original_name.mp3'),
    ('foo/bar/none_existing_path', 'original_name.mp3')
])
def test_mp3_file(input_data, expected):
    test_meta = {'path': input_data, 'name': 'original_name.mp3', 'mime': 'audio/mpeg'}
    filter_function(test_meta)
    assert test_meta['name'] == expected
