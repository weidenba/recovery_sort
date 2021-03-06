import os
from common_helper_files import get_dir_of_file
from pluginbase import PluginBase
import logging


class FilterSystem():

    FILTER_TYPE = None

    def __init__(self, selected_filters):
        self._init_plugins()
        if selected_filters == 'all':
            self._set_all_filters()
        else:
            self._set_filters_to_apply(selected_filters)
        self._setup_counters()

    def _init_plugins(self):
        self.plugin_base = PluginBase(package='filter_plugins.{}'.format(self.FILTER_TYPE))
        self.filter_plugins = dict()
        self.plugin_source = self.plugin_base.make_plugin_source(searchpath=[os.path.join(get_dir_of_file(__file__), '../filter_plugins/{}'.format(self.FILTER_TYPE))])
        plugin_list = self.plugin_source.list_plugins()
        for item in plugin_list:
            plugin = self.plugin_source.load_plugin(item)
            plugin.setup(self)

    def register_plugin(self, name, filter_function):
        self.filter_plugins[name] = filter_function

    def _set_all_filters(self):
        self.filters_to_apply = list(self.filter_plugins.keys())

    def _setup_counters(self):
        self.counter = dict()
        for item in self.filters_to_apply:
            self.counter[item] = 0

    def _set_filters_to_apply(self, filter_list):
        self.filters_to_apply = list()
        for item in filter_list:
            if item in self.filter_plugins:
                self.filters_to_apply.append(item)
            else:
                logging.error('Filter "{}" is not available!'.format(item))
