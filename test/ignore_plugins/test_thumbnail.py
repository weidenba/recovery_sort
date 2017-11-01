import pytest

from filter_plugins.ignore.thumbnail import filter_function


@pytest.mark.parametrize('name, expected', [
    ({'name': 'abc.jpg'}, False),
    ({'name': 't12345.jpg'}, True),
    ({'name': 'blah_t12345.jpg'}, False)
])
def test_is_photorec_thumbnail_name(name, expected):
    assert filter_function(name) == expected
