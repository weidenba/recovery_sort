from filter_system.ignore import IgnoreFilterSystem


def test_init_PlugIns():
    filter_system = IgnoreFilterSystem([])
    assert len(filter_system.filter_plugins.keys()) > 0
    for plugin in filter_system.filter_plugins.keys():
        assert callable(filter_system.filter_plugins[plugin])
