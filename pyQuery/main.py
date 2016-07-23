from pyquery import PyQuery as pq
from lxml import etree
import urllib

d = pq("<html></html>")
d = pq(etree.fromstring("<html></html>"))
#d = pq(url=your_url)
#d = pq(url=your_url, opener=lambda url, **kw: urlopen(url).read())
#d = pq(filename=path_to_html_file)

d("#hello")
p = d("#hello")
print(p.html())
p.html("you know <a href='http://python.org/'>Python</a> rocks")
print(p.html())
print(p.text())


doc = pq('<html><body><p>Hello World</p></body></html>')
print doc('p').text()
