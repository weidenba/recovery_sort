import pytest
from filter_plugins.blacklist import filter_function, _apply_blacklist_filter


def test_filter_function():
    test_stock = {
        'ed1015323e7c3a16936523ce1a64928a805f5b37534d74b596570d6931dc5684_159':
        {
            'uid': 'ed1015323e7c3a16936523ce1a64928a805f5b37534d74b596570d6931dc5684_159',
            'name': 'test_file',
            'size': 159,
            'mime': 'image/png'
        }
    }
    result = filter_function(test_stock)
    assert type(result) == dict


@pytest.mark.parametrize('input_stock, blacklist, expected', [
    ({'a': 1, 'b': 2, 'c': 3}, {'a', 'b'}, {'c': 3}),
    ({'a': 1}, {'a', 'b', 'c'}, dict()),
    (dict(), {'a', 'b', 'c'}, dict()),
    ({'a': 1}, set(), {'a': 1})
])
def test_apply_blacklist_filter(input_stock, blacklist, expected):
    assert _apply_blacklist_filter(input_stock, blacklist) == expected
