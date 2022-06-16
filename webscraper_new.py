import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd
def url_get_contents(url):
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()
xhtml = url_get_contents('https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD11A1?hl=en#bands').decode('utf-8')
p = HTMLTableParser()
p.feed(xhtml)
table=pd.DataFrame(p.tables[0])
print(table)
table.to_csv('Terraland.csv', encoding='utf-8', index=False)