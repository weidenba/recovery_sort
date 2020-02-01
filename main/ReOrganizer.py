from common_helper_files import get_files_in_dir
import logging
import os

from helper.file_system import fail_safe_copy
from filter_system.ignore import IgnoreFilterSystem
from main.stocktaking import get_file_meta
from filter_system.rename import RenameFilterSystem


class ReOrganizer():

    def __init__(self, out_dir='/tmp', ignore_filters_to_apply=[], rename_filters_to_apply=[], testing=False):
        self.out_dir = out_dir
        self.copy_counter = 0
        if not testing:
            self.ignore_filter_system = IgnoreFilterSystem(ignore_filters_to_apply)
            self.rename_filter_system = RenameFilterSystem(rename_filters_to_apply)
        else:
            self.ignore_filter_system = None
            self.rename_filter_system = None

    def reorganize_files(self, input_dir):
        files = get_files_in_dir(input_dir)
        logging.info('{} files found in {}'.format(len(files), input_dir))
        for file in files:
            self._process_file(file)
        self._log_stats()

    def _process_file(self, input_file):
        file_meta = get_file_meta(input_file)
        if not self.ignore_filter_system.filtered(file_meta):
            self.rename_filter_system.rename(file_meta)
            self._store_to_new_location(file_meta)

    def _store_to_new_location(self, file_meta):
        new_file_path = os.path.join(self.out_dir, self._generate_new_file_path(file_meta))
        fail_safe_copy(file_meta['path'], new_file_path)
        self.copy_counter += 1

    @staticmethod
    def _generate_new_file_path(file_meta):
        return '{mime_type}/{modification_year}/{modification_date}_{file_name}'.format(mime_type=file_meta['mime'], modification_year=file_meta['mod_date'][0:4], modification_date=file_meta['mod_date'], file_name=file_meta['name'])

    def _log_stats(self):
        logging.info('{} files copied to {}'.format(self.copy_counter, self.out_dir))
        for item in self.ignore_filter_system.counter.keys():
            logging.info('{} files ignored -> {}'.format(self.ignore_filter_system.counter[item], item))
