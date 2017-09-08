NAME = 'blacklist'


def filter_function(file_stock):
    return file_stock


def setup(app):
    app.register_plugin(NAME, filter_function)
