import pytest
from filter_plugins.blacklist import filter_function, _apply_blacklist_filter


def test_filter_function():
    test_stock = {
        '4399a63790261b66220050d60396736c55af15e5c4fb5d00806acd79faf27a936453bca773d508baf1fb88d302e6c03fc9925d31ed2ce3f1939f3a7e40847897_159':
        {
            'uid': '4399a63790261b66220050d60396736c55af15e5c4fb5d00806acd79faf27a936453bca773d508baf1fb88d302e6c03fc9925d31ed2ce3f1939f3a7e40847897_159',
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
