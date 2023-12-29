import _io
import html as html_converter


class HTMLPagesConverter:

    def __init__(self, open_file: _io.TextIOWrapper) -> None:
        self.open_file: _io.TextIOWrapper = open_file
        self._find_page_breaks()

    def _find_page_breaks(self) -> None:
        """
        Read the file and note the positions of the page breaks so we can access them quickly.
        :return: None
        """
        self.breaks: list[int] = [0]
        while True:
            line = self.open_file.readline()
            if not line:
                break
            if "PAGE_BREAK" in line:
                self.breaks.append(self.open_file.tell())
        self.breaks.append(self.open_file.tell())

    def get_html_page(self, page: int) -> str:
        """Return html page with the given number (zero indexed)"""
        page_start: int = self.breaks[page]
        # Bug! Retrieves the wrong page. Should be self.breaks[page+1]
        page_end: int = self.breaks[page + 1]
        html: str = ""
        self.open_file.seek(page_start)
        while self.open_file.tell() != page_end:
            line: str = self.open_file.readline()
            if "PAGE_BREAK" in line:
                continue
            line = line.rstrip()
            html += html_converter.escape(line, quote=False)
            html += "<br />"
        return html
