import io
import pytest
from src.html_pages import HTMLPagesConverter

"""A FAKE is a copy of a resource which has an implementation, but is unsuitable for production. """

real_file_location: str = "./file_test.txt"
fake_file = io.StringIO(
    """\
page one
PAGE_BREAK
page two
PAGE_BREAK
page three
PAGE_BREAK
page four
"""
)


# @pytest.mark.skip("This is the real file")
def test_convert_second_page_with_file() -> None:
    test_file = open("./test/file_test.txt")
    converter = HTMLPagesConverter(test_file)
    converted_text: str = converter.get_html_page(1)
    assert converted_text == "page two<br />"


def test_convert_second_page_with_fake() -> None:
    converter = HTMLPagesConverter(fake_file)
    converted_text: str = converter.get_html_page(1)
    assert converted_text == "page two<br />"
