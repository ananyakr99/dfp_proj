from bs4 import BeautifulSoup
import requests
import re
import json
import pandas as pd
def stock_analysis(stock):
    pd.set_option("max_rows", None)
    url1 = 'http://financials.morningstar.com/finan/financials/getFinancePart.html?&callback=xxx&t='+stock
    soup1 = BeautifulSoup(json.loads(re.findall(r'xxx\((.*)\)', requests.get(url1).text)[0])['componentData'], 'lxml')
    df = pd.read_html(soup1.prettify())
    df = df[0]
    df = df.dropna()
    html = df.to_html()
    text_file = open("index.html", "w")
    text_file.write(html)
    text_file.close()
    
