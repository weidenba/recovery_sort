import os
from common_helper_files import get_dir_of_file
from pluginbase import PluginBase
import logging


class FilterSystem():

    def __init__(self, filters_to_apply=[]):
        self._init_plugins()
        self._file_cache = set()
        self._set_filters_to_apply(filters_to_apply)

    def _init_plugins(self):
        self.plugin_base = PluginBase(package='filter_plugins')
        self.filter_plugins = dict()
        self.plugin_source = self.plugin_base.make_plugin_source(searchpath=[os.path.join(get_dir_of_file(__file__), '../filter_plugins')])
        plugin_list = self.plugin_source.list_plugins()
        for item in plugin_list:
            plugin = self.plugin_source.load_plugin(item)
            plugin.setup(self)

    def register_plugin(self, name, filter_function):
        self.filter_plugins[name] = filter_function

    def filtered(self, file_meta):
        for c_filter in self.filters_to_apply:
            if self.filter_plugins[c_filter](file_meta, file_cache=self._file_cache):
                self.counter[c_filter] += 1
                logging.debug('{} ignored -> {}'.format(file_meta['path'], c_filter))
                return True
        self._file_cache.add(file_meta['uid'])
        return False

    def _set_filters_to_apply(self, filter_list):
        self.counter = {'duplicate': 0}
        self.filters_to_apply = ['duplicate']
        for item in filter_list:
            if item in self.filter_plugins:
                self.filters_to_apply.append(item)
                self.counter[item] = 0
            else:
                logging.error('Filter "" is not available!'.format(item))
