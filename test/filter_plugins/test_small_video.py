import pytest
from filter_plugins.small_video import _is_small_video, filter_function


@pytest.mark.parametrize('file_meta, expected', [
    ({'mime': 'video/mpg', 'size': 100}, True),
    ({'mime': 'video/mpg', 'size': 100000}, False),
    ({'mime': 'image/jpg', 'size': 100}, False)
])
def test_is_photorec_thumbnail_name(file_meta, expected):
    assert _is_small_video(file_meta) == expected


@pytest.mark.parametrize('stock, expected_len', [
    ({'small_video': {'mime': 'video/mpg', 'size': 100}}, 0),
    ({'other_file': {'mime': 'text/plain', 'size': 100}}, 1),
    ({'small_video': {'mime': 'video/mpg', 'size': 100}, 'other_file': {'mime': 'text/plain', 'size': 100}}, 1)
])
def test_filter_function(stock, expected_len):
    assert len(filter_function(stock)) == expected_len
