import os
from main.stocktaking import stocktaking
from helper.file_system import fail_safe_copy


def reorganize_files(input_dir, out_dir, filter_list):
    file_stock = stocktaking(input_dir)

    _store_to_new_location(file_stock, out_dir)


def _store_to_new_location(file_stock, out_dir):
    for item in file_stock:
        new_file_path = os.path.join(out_dir, _generate_new_file_path(file_stock[item]))
        fail_safe_copy(file_stock[item]['path'], new_file_path)


def _generate_new_file_path(file_meta):
    return '{}/{}_{}'.format(file_meta['mime'], file_meta['mod_date'], file_meta['name'])
