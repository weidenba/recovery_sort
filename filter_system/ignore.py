import logging

from .base import FilterSystem


class IgnoreFilterSystem(FilterSystem):

    FILTER_TYPE = 'ignore'

    def __init__(self, filters_to_apply):
        print('ignore_filter_init')
        super().__init__(filters_to_apply)
        self._file_cache = set()
        self.filters_to_apply.insert(0, 'duplicate')
        self.counter['duplicate'] = 0

    def filtered(self, file_meta):
        for c_filter in self.filters_to_apply:
            if self.filter_plugins[c_filter](file_meta, file_cache=self._file_cache):
                self.counter[c_filter] += 1
                logging.debug('{} ignored -> {}'.format(file_meta['path'], c_filter))
                return True
        self._file_cache.add(file_meta['uid'])
        return False
