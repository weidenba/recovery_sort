from common_helper_process import execute_shell_command_get_return_code
from common_helper_files import get_dir_of_file, get_string_list_from_file
from tempfile import TemporaryDirectory
import os


SRC_DIR = os.path.join(get_dir_of_file(__file__), '../../')
TEST_DATA_DIR = os.path.join(get_dir_of_file(__file__), '../data')
MAINSCRIPT = os.path.join(SRC_DIR, 'blacklist_generator.py')


def test_help():
    output, return_code = execute_shell_command_get_return_code('{} -h'.format(MAINSCRIPT), timeout=5)
    assert return_code == 0
    assert 'usage: blacklist_generator.py' in output


def test_blacklist_generation():
    tmp_dir = TemporaryDirectory()
    blacklist_file = os.path.join(tmp_dir.name, 'test.bl')
    output, return_code = execute_shell_command_get_return_code('{} -o {} {}'.format(MAINSCRIPT, blacklist_file, TEST_DATA_DIR), timeout=60)
    assert return_code == 0
    assert os.path.exists(blacklist_file)
    assert '4 files found' in output
    assert 'Blacklisting 3 unique files' in output
    blacklist_entries = get_string_list_from_file(blacklist_file)
    assert len(blacklist_entries) == 3
    assert '2e3a5a43a8516b8cdac92161f890a68caa5ac5b820125378c586ac40fe45250f_287352' in blacklist_entries
    tmp_dir.cleanup()
