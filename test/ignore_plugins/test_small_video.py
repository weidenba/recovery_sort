import pytest
from filter_plugins.ignore.small_video import filter_function


@pytest.mark.parametrize('file_meta, expected', [
    ({'mime': 'video/mpg', 'size': 100}, True),
    ({'mime': 'video/mpg', 'size': 100000}, False),
    ({'mime': 'image/jpg', 'size': 100}, False)
])
def test_is_photorec_thumbnail_name(file_meta, expected):
    assert filter_function(file_meta) == expected
