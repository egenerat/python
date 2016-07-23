from pyquery import PyQuery as pq
doc = pq('<html><body><p>Hello World</p></body></html>')
print(doc('p').text())

