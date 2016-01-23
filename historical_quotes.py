"""
Download historical data for a single security from google.com/finance/historical
"""

import requests
import urllib2
from bs4 import BeautifulSoup as bs
import re

ticker =
enddate =

# URL information + request
payload = { 'historicalq': ticker, 'num': '1', 'startdate': "Jan+1+2006", 'enddate': enddate }
payload_str = "&".join("%s=%s" % (k,v) for k,v in payload.items())
r = urllib2.urlopen('https://www.google.com/finance/', params=payload_str)

soup = bs(r)
print soup.prettify()

#<table class="gf-table historical_price">
#<tr class=bb>
#<th class="bb lm lft">Date
#<th class="rgt bb">Open
#<th class="rgt bb">High
#<th class="rgt bb">Low
#<th class="rgt bb">Close *we want close value*
#<th class="rgt bb rm">Volume
#<tr>
#<td class="lm">Jan 22, 2016
#<td class="rgt">13.52
#<td class="rgt">13.66
#<td class="rgt">13.36
#<td class="rgt">13.38 ********THIS ONE********
#<td class="rgt rm">5,563,702
#</table>

print soup(text='re.compile('>Close'))

page = r.text
soup = BeautifulSoup.BeautifulSoup(data)
element = soup.find('span', attrs={'class': re.compile(r".*\btxt_resultad_busca_casamento\b.*")})
print element.text


find_string = soup.body.findAll(text='>Close')

month= vector(1:12)
day= 1
year= vector()

def get_quote(): "https://www.google.com/finance/historical?q=" + ticker + "&startdate=Jan+1+2006&enddate=" + month + day + year + "&num=1",sep=""
