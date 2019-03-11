# or import urllib2
# quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
# html_doc = urllib2.urlopen(quote_page)

# import requests
# r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
# html_doc = t.text

import sys
import requests
from bs4 import BeautifulSoup

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">   Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">La  cie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Ti  llie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html_doc, 'html.parser')
# sel = soup.select("a")
# for a in sel:
#     name = ''.join([ch for ch in a.string if ch != " "]);
#     print(name)

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    sys.exit(0)

url = 'http://www.atmovies.com.tw/movie/next/w' + sys.argv[1] + '/'

html_doc = requests.get(url).text

soup = BeautifulSoup(html_doc, 'html.parser')
sel = soup.select("div.filmTitle > a")
filter = ['\t', '\n']
for filmTitle in sel:
    print(''.join([ch for ch in filmTitle.string if not ch in filter]))
