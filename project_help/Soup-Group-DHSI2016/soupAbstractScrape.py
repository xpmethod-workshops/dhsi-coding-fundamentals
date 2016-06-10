# Test of using BeautifulSoup4 to scrape abstracts from *all* the pages directly linked 
# to from http://www.branchcollective.org/?page_id=13 .  The BS4 documentation is at
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# First let's see about just grabbing web content
# Sample code from https://docs.python.org/3/howto/urllib2.html
"""
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
	html = response.read()
	print(html)
"""

# Now let's see about just using BS4 to grab abstract content from a single page
from bs4 import BeautifulSoup

with urllib.request.urlopen('http://www.branchcollective.org/?ps_articles=erika-rappaport-object-lessons-and-colonial-histories-inventing-the-jubilee-of-indian-tea') as response:
	html = response.read()
	soup = BeautifulSoup(html_doc, 'html.parser')
	print(soup.div['article_extract'])
	
	