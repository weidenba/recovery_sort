import os
from common_helper_files import get_dir_of_file
from pluginbase import PluginBase


class Filter():

    plugin_base = PluginBase(package='recovery_sort.filter_plugins')

    def __init__(self, file_stock, filter_list):
        self._init_pugins()
        return self._apply_filters(file_stock, filter_list)

    def _init_plugins(self):
        self.filter_plugins = dict()
        self.plugin_source = self.plugin_base.make_plugin_source(searchpath=[os.path.join(get_dir_of_file(__file__), '../filter_plugins')])
        plugin_list = self.plugin_source.list_plugins()
        for item in plugin_list:
            plugin = self.plugin_source.load_plugin(item)
            plugin.setup(self)

    def register_plugin(self, name, filter_function):
        self.filter_plugins[name] = filter_function

    def _apply_filters(self, file_stock, filter_list):
        for filter_name in filter_list:
            if filter_name in self.filter_plugins:
                file_stock = self.filter_plugins[filter_name](file_stock)
        return file_stock
