import pytest
import os
from tempfile import TemporaryDirectory
from common_helper_files import get_binary_from_file, get_dir_of_file

from main.blacklist_generator import _store_blacklist, _generate_blacklist_uids, create_blacklist


TEST_DATA_DIR = os.path.join(get_dir_of_file(__file__), '../data/get_files_test')


def test_generate_blacklist_uids():
    input_files = []
    input_files.append(os.path.join(TEST_DATA_DIR, 'image.jpg'))
    input_files.append(os.path.join(TEST_DATA_DIR, 'a_folder/a_test_file'))
    result = _generate_blacklist_uids(input_files)
    assert len(result) == 2
    assert '2e3a5a43a8516b8cdac92161f890a68caa5ac5b820125378c586ac40fe45250f_287352' in result
    assert '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08_4' in result


def test_store_blacklist():
    tmp_dir = TemporaryDirectory()
    tmp_file_path = os.path.join(tmp_dir.name, 'blacklist_test_file.txt')
    test_data = ['abc', 'def']
    _store_blacklist(test_data, tmp_file_path)
    assert os.path.exists(tmp_file_path)
    result = get_binary_from_file(tmp_file_path)
    assert result == b'abc\ndef'


@pytest.mark.parametrize('input_dir, expected', [(os.path.join(TEST_DATA_DIR, 'a_folder'), b'9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08_4'), ('/nonexisting/', b'')])
def test_create_blacklist(input_dir, expected):
    tmp_dir = TemporaryDirectory()
    tmp_file_path = os.path.join(tmp_dir.name, 'blacklist_test_file.txt')
    create_blacklist(input_dir, tmp_file_path)
    result = get_binary_from_file(tmp_file_path)
    assert result == expected
