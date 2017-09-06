from tempfile import TemporaryDirectory
from common_helper_files import get_dir_of_file
import os

from helper.file_system import fail_safe_copy

TEST_DATA_DIR = os.path.join(get_dir_of_file(__file__), '../data')
TEST_FILE_PATH = os.path.join(TEST_DATA_DIR, 'small_image.png')


def test_fail_safe_copy():
    tmp_dir = TemporaryDirectory()
    src_file = TEST_FILE_PATH
    dst = os.path.join(tmp_dir.name, "foo/bar/image_copy.jpg")
    fail_safe_copy(src_file, dst)
    assert os.path.exists(dst)
    # test error
    fail_safe_copy(os.path.join(tmp_dir.name, "none_existing"), "/tmp/foo")
