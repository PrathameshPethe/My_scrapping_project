from bs4 import BeautifulSoup
import requests
from csv import writer


response = requests.get('https://arstechnica.com/')

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find("article")

with open("articles.csv","w",newline="") as  file:
    csv_writer = writer(file)
    csv_writer.writerow(
        ['Title','Summary','Author','Date','Link','Thumbanail URL'])
    

for article in articles:
    title  = article.find("h2").get_text().strip()
    summary = article.find("p").get_text().strip()
    author = article.find("span").get_text().strip()
    date = article.find("time").get_text().strip()
    link = article.find("a")["href"]
    thumbnail_url = article.find("img")["src"]

    csv_writer.writerrow(
        [title,summary,author,date,link,thumbnail_url]
    )
