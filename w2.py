import requests
import re
import json

s = requests.session()

urls = [
  'https://news.google.com/topstories?hl=de&gl=DE&ceid=DE:de',
  'https://de.wikipedia.org/wiki/Wikipedia:Hauptseite'
]


b = set()

for url in urls:
  d = s.get(url)
  a = re.findall("[A-Z][a-z]+", d.text)
  for i in a:
    if len(i) > 8:
      b.add(i)
print(json.dumps(list(b)))
