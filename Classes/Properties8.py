import urllib.request
from time import perf_counter

# Yet another example on read-only computed properties


class WebPage:
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
        self._url = new_url
        self._page = None
        self._load_time_sec = None
        self._page_size = None

    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page

    @property
    def page_size(self):
        if self._page is None:
            self.download_page()
        return self._page_size

    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_sec

    def download_page(self):
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

for p in pages:
    print(f"{p.url} - Size: {p.page_size} - Time in seconds: {p.time_elapsed}")

