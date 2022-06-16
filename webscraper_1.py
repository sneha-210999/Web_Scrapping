from bs4 import BeautifulSoup as bs
import requests
from csv import writer
import pandas as pd
import csv

url=requests.get( "https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD11A1?hl=en#bands")
soup = bs(url.content, 'html.parser')
lists = soup.find('table', class_="eecat")
#print(lists)
            
with open('Terraland_1.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = csv.writer(f)
    header = ['Name', 'Units', 'Min', 'Max','Scale','Offset','Description']
    thewriter.writerow(header)
    list_of_rows = []
    seen=set()
    for row in lists.find_all('tr') :
         list_of_cells = []
         cells= row.find_all('td')
         #print(cells)
         
         for cell in cells:
             text = cell.text
             text=text.strip()
             list_of_cells.append(text)
         
         for item in list_of_cells:
            item=item.strip()         
            thewriter.writerow(list_of_cells)         
        
file=pd.read_csv('Terraland_1.csv')
file=file.drop_duplicates()
file=file.fillna("")
file.to_csv('Terraland_1.csv')



