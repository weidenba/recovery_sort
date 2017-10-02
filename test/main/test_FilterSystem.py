from main.filter_system import FilterSystem


def test_init_PlugIns():
    filter_system = FilterSystem()
    assert len(filter_system.filter_plugins.keys()) > 0
    for plugin in filter_system.filter_plugins.keys():
        assert callable(filter_system.filter_plugins[plugin])
