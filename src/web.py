import pandas as pd
import requests


URL = 'file:///D:/GitHub/SVNTools/html/test.html#'

tables = pd.read_html(URL)

print(type(tables))
print(tables)
'''
print("There are : ",len(tables)," tables")
print("Take look at table 0")
print(tables[0])'''