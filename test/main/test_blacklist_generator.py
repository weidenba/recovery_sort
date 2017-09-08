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
    assert '7edc13f6c2fb4a4d983d754f1000364c7aa645a663bbd719e803103b335f2994081ff48454507a4db9fc38beacb93971c28d2f20303ff16f9082f56210663a82_287352' in result
    assert 'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff_4' in result


def test_store_blacklist():
    tmp_dir = TemporaryDirectory()
    tmp_file_path = os.path.join(tmp_dir.name, 'blacklist_test_file.txt')
    test_data = ['abc', 'def']
    _store_blacklist(test_data, tmp_file_path)
    assert os.path.exists(tmp_file_path)
    result = get_binary_from_file(tmp_file_path)
    assert result == b'abc\ndef'


@pytest.mark.parametrize('input_dir, expected', [(os.path.join(TEST_DATA_DIR, 'a_folder'), b'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff_4'), ('/nonexisting/', b'')])
def test_create_blacklist(input_dir, expected):
    tmp_dir = TemporaryDirectory()
    tmp_file_path = os.path.join(tmp_dir.name, 'blacklist_test_file.txt')
    create_blacklist(input_dir, tmp_file_path)
    result = get_binary_from_file(tmp_file_path)
    assert result == expected
