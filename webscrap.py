from bs4 import BeautifulSoup as bs  
import pandas as pd 
import requests
currentPage = 1 
link = "http://quotes.toscrape.com/page/1/"
pages = []
end = False 
Quotes = []
Authors = []
while end==False : 
    print(link)
    request = requests.get(link)
    if request.raise_for_status() !=None or currentPage == 10 : 
        print(request.raise_for_status())
        end=True 
    else: 
        pages.append(bs(request.text,"html.parser"))
        link=link.replace(str(currentPage),str(currentPage+1))
        currentPage=currentPage+1 
for soup in pages : 
    allQuotes = soup.find_all(class_='quote')
    for _ in allQuotes : 
        Quotes.append(_.find(class_='text').text)
        Authors.append(_.find(class_='author').text)
dataFrame=pd.DataFrame()
dataFrame["Quote"]=Quotes
dataFrame["Author"]=Authors
with open('result.csv','w',encoding='utf-8') as csv : 
    dataFrame.to_csv(csv,index=False,columns=['Quote','Author'])



