from common_helper_files import create_dir_for_file
import logging
import shutil
import sys


def fail_safe_copy(src, dst):
    """
    Trys to copy a file from src to dst
    """
    logging.debug("{} -> {}".format(src, dst))
    try:
        create_dir_for_file(dst)
        shutil.copy2(src, dst)
    except Exception as e:
        logging.error("Could not copy file: {} {}".format(sys.exc_info()[0].__name__, e))
