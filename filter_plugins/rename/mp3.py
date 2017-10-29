NAME = 'mp3'


def filter_function(file_meta):
    pass


def setup(app):
    app.register_plugin(NAME, filter_function)
