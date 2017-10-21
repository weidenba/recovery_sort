import os
from common_helper_files import get_dir_of_file
from pluginbase import PluginBase
import logging


class FilterSystem():

    FILTER_TYPE = None

    def __init__(self, selected_filters):
        print('base_filter_init')
        self._init_plugins()
        self._set_filters_to_apply(selected_filters)

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

    def _set_filters_to_apply(self, filter_list):
        self.counter = dict()
        self.filters_to_apply = list()
        for item in filter_list:
            if item in self.filter_plugins:
                self.filters_to_apply.append(item)
                self.counter[item] = 0
            else:
                logging.error('Filter "" is not available!'.format(item))
