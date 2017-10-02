import pytest
import filter_plugins.blacklist


def test_get_blacklist():
    assert len(filter_plugins.blacklist.BLACKLIST) == 0
    filter_plugins.blacklist._get_blacklist()
    assert len(filter_plugins.blacklist.BLACKLIST) > 0


@pytest.mark.parametrize('file_meta, blacklist, expected', [
    ({'uid': 'a'}, set('ab'), True),
    ({'uid': 'a'}, set(), False)
])
def test_apply_blacklist_filter(file_meta, blacklist, expected):
    filter_plugins.blacklist.BLACKLIST = blacklist
    assert filter_plugins.blacklist.filter_function(file_meta) == expected
