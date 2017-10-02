import os
import logging

from main.stocktaking import get_file_meta
from helper.file_system import fail_safe_copy
from main.filter_system import FilterSystem
from common_helper_files import get_files_in_dir


class ReOrganizer():

    def __init__(self, out_dir='/tmp', filters_to_apply=[], testing=False):
        self.out_dir = out_dir
        self.copy_counter = 0
        if not testing:
            self.filter_system = FilterSystem(filters_to_apply)
        else:
            self.filter_system = None

    def reorganize_files(self, input_dir):
        files = get_files_in_dir(input_dir)
        logging.info('{} files found in {}'.format(len(files), input_dir))
        for file in files:
            self._process_file(file)
        self._log_stats()

    def _process_file(self, input_file):
        file_meta = get_file_meta(input_file)
        if not self.filter_system.filtered(file_meta):
            self._store_to_new_location(file_meta)

    def _store_to_new_location(self, file_meta):
        new_file_path = os.path.join(self.out_dir, self._generate_new_file_path(file_meta))
        fail_safe_copy(file_meta['path'], new_file_path)
        self.copy_counter += 1

    @staticmethod
    def _generate_new_file_path(file_meta):
        return '{}/{}_{}'.format(file_meta['mime'], file_meta['mod_date'], file_meta['name'])

    def _log_stats(self):
        logging.info('{} files copied to {}'.format(self.copy_counter, self.out_dir))
        for item in self.filter_system.counter.keys():
            logging.info('{} files ignored -> {}'.format(self.filter_system.counter[item], item))
