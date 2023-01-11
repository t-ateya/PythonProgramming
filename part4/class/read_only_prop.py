from math import pi


class Circle:
    def __init__(self, r) -> None:
        self._r = r
        self._area = None 

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError("Radius must be non-negative")
        self._r = r 
        self._area = None 

    #Read Only property
    @property
    def area(self):
        if self._area is None:
            self._area = pi *(self.radius ** 2)
        return self._area
        


class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius 
        self._area = None 


    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._area = None
        self._radius = value 

    @property
    def area(self):
        if self._area is None:
            print("Calculating area ...")
            self._area =  pi * (self.radius ** 2)
        return self._area
        
            
"""
c = Circle(1)   
print(c.area)
print(c.__dict__)
print("============================")
print(c.area)

c.radius = 2

print(c.__dict__)
"""

import urllib.request as ur
from time import perf_counter

class WebPage:
    def __init__(self, url) -> None:
        self._url = url 
        self._page = None 
        self._load_time_secs = None 
        self._page_size = None 

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value 
        self._page = None 

    #Read-Only Properties
    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page

    @property
    def page_size(self):
        if not self._page:
            self.download_page()
        return self._page_size

    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs

    def download_page(self):
        self._page_size = None 
        self._load_time_secs = None 
        start_time = perf_counter()
        with ur.urlopen(self.url) as f:
            self._page = f.read()
        end_time = perf_counter()
        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time
    

    
urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.yahoo.com'
]

for url in urls:
    page = WebPage(url)
    print(f'{url}\tsize={format(page.page_size, "_")}\telapsed={page.time_elapsed:.2f} secs')