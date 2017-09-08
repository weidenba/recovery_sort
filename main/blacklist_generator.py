from common_helper_files import get_files_in_dir, write_binary_to_file
import logging

from helper.meta import generate_uid


def create_blacklist(input_dir, out_file):
    input_files = get_files_in_dir(input_dir)
    logging.info('{} files found'.format(len(input_files)))
    blacklist_uids = _generate_blacklist_uids(input_files)
    logging.info('Blacklisting {} unique files'.format(len(blacklist_uids)))
    _store_blacklist(blacklist_uids, out_file)


def _generate_blacklist_uids(input_files):
    uids = set()
    for item in input_files:
        uids.add(generate_uid(item))
    return list(uids)


def _store_blacklist(blacklist_uids, out_file):
    output = '\n'.join(blacklist_uids).encode(encoding='utf_8', errors='replace')
    write_binary_to_file(output, out_file)
