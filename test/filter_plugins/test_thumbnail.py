import pytest


from filter_plugins.thumbnail import _is_photorec_thumbnail_name,\
    filter_function


@pytest.mark.parametrize('name, expected', [('abc.jpg', False), ('t12345.jpg', True), ('blah_t12345.jpg', False)])
def test_is_photorec_thumbnail_name(name, expected):
    assert _is_photorec_thumbnail_name(name) == expected


@pytest.mark.parametrize('stock, expected_len', [
    ({'thumb': {'name': 't1234.jpg'}}, 0),
    ({'file': {'name': 'f1234.jpg'}}, 1),
    ({'file': {'name': 'f1234.jpg'}, 'thumb': {'name': 't1234.jpg'}}, 1)
])
def test_filter_function(stock, expected_len):
    assert len(filter_function(stock)) == expected_len
