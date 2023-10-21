import urllib.request
from time import perf_counter


# Yet another example on read-only computed properties


class WebPage:
    """A class to hold information about a webpage"""
    def __init__(self, url: str) -> None:
        self.url = url
        self._page: bytes | None = None
        self._load_time_sec: float | None = None
        self._page_size: int | None = None

    @property
    def url(self) -> str:
        """The page's URL"""
        return self._url

    @url.setter
    def url(self, new_url: str) -> None:
        """
        Updates the self._url and resets the following attributes to None:
            self._page
            self._load_time_sec
            self._page_size
            """
        self._url: str = new_url
        self._page: bytes | None = None
        self._load_time_sec: float | None = None
        self._page_size: int | None = None

    @property
    def page(self) -> bytes:
        """
        Returns the self._page. 
        If self._page is None, it downloads the page.
        """
        if self._page is None:
            self.download_page()
        return self._page

    @property
    def page_size(self) -> int:
        """
        Returns the self._page_size. 
        If self._page_size is None, it downloads the page.
        """
        if self._page is None:
            self.download_page()
        return self._page_size

    @property
    def time_elapsed(self) -> float:
        """
        Returns the self._load_time_sec. 
        If self._load_time_sec is None, it downloads the page.
        """
        if self._page is None:
            self.download_page()
        return self._load_time_sec

    def download_page(self) -> None:
        """
            Downloads the webpage and updates the following attributes:
                self._page_size (size of the webpage in bytes)
                self._page (the actual contents of the page)
                self._load_time_sec (time it take the webpage to download -in seconds)
        """
        self._page_size: int | None = None
        self._load_time_sec: float | None = None
        start_time: float = perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page: bytes | None = f.read()
        end_time: float = perf_counter()
        self._page_size: int = len(self._page)
        self._load_time_sec: float = end_time - start_time


urls: list[str] = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.facebook.com",
    "https://vk.com/feed",
]

pages: list[WebPage] = []

for u in urls:
    pages.append(WebPage(u))


print(pages, end="\n")
# [
# <__main__.WebPage object at 0x7f02dec8efa0>, 
# <__main__.WebPage object at 0x7f02dec8e400>, 
# <__main__.WebPage object at 0x7f02dec8c370>, 
# <__main__.WebPage object at 0x7f02dec8c1c0>, 
# <__main__.WebPage object at 0x7f02dec8c070>
# ]

for p in pages:
    print(f"Size: {p.page_size} - Time in seconds: {p.time_elapsed:.5f} - {p.url}")
# Size: 18028 - Time in seconds: 0.47779 - https://www.google.com
# Size: 50344 - Time in seconds: 0.43166 - https://www.python.org
# Size: 59253 - Time in seconds: 0.63206 - https://www.facebook.com
# Size: 196401 - Time in seconds: 1.95767 - https://vk.com/feed
