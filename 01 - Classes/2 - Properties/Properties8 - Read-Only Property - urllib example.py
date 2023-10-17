import urllib.request
from time import perf_counter


# Yet another example on read-only computed properties


class WebPage:
    """A class to hold information about a webpage"""
    def __init__(self, url: str):
        self.url = url
        self._page = None
        self._load_time_sec = None
        self._page_size = None

    @property
    def url(self):
        """The page's URL"""
        return self._url

    @url.setter
    def url(self, new_url):
        """
        Updates the self._url and resets the following attributes to None:
            self._page
            self._load_time_sec
            self._page_size
            """
        self._url = new_url
        self._page = None
        self._load_time_sec = None
        self._page_size = None

    @property
    def page(self):
        """
        Returns the self._page. 
        If self._page is None, it downloads the page.
        """
        if self._page is None:
            self.download_page()
        return self._page

    @property
    def page_size(self):
        """
        Returns the self._page_size. 
        If self._page_size is None, it downloads the page.
        """
        if self._page is None:
            self.download_page()
        return self._page_size

    @property
    def time_elapsed(self):
        """
        Returns the self._load_time_sec. 
        If self._load_time_sec is None, it downloads the page.
        """
        if self._page is None:
            self.download_page()
        return self._load_time_sec

    def download_page(self):
        """
            Downloads the webpage and updates the following attributes:
                self._page_size (size of the webpage in bytes)
                self._page (the actual contents of the page)
                self._load_time_sec (time it take the webpage to download -in seconds)
        """
        self._page_size = None
        self._load_time_sec = None
        start_time = perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page = f.read()
        end_time = perf_counter()
        self._page_size = len(self._page)
        self._load_time_sec = end_time - start_time


urls = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.facebook.com",
    "https://www.udemy.com/",
    "https://vk.com/feed",
]

pages = []

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
# Size: 14199	- Time in seconds: 0.45024 - https://www.google.com
# Size: 49862	- Time in seconds: 0.27002 - https://www.python.org
# Size: 222829	- Time in seconds: 0.38165 - https://www.facebook.com
# Size: 223453	- Time in seconds: 0.99914 - https://www.udemy.com/
# Size: 51356	- Time in seconds: 3.26882 - https://vk.com/feed
