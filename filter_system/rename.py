from .base import FilterSystem


class RenameFilterSystem(FilterSystem):

    FILTER_TYPE = 'rename'

    def rename(self, file_meta):
        for c_filter in self.filters_to_apply:
            self.filter_plugins[c_filter](file_meta)
