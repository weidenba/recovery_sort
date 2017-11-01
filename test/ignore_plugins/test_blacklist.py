import pytest
import filter_plugins.ignore.blacklist


def test_get_blacklist():
    assert len(filter_plugins.ignore.blacklist.BLACKLIST) == 0
    filter_plugins.ignore.blacklist._get_blacklist()
    assert len(filter_plugins.ignore.blacklist.BLACKLIST) > 0


@pytest.mark.parametrize('file_meta, blacklist, expected', [
    ({'uid': 'a'}, set('ab'), True),
    ({'uid': 'a'}, set(), False)
])
def test_apply_blacklist_filter(file_meta, blacklist, expected):
    filter_plugins.ignore.blacklist.BLACKLIST = blacklist
    assert filter_plugins.ignore.blacklist.filter_function(file_meta) == expected
