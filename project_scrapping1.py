from bs4 import BeautifulSoup
import requests
from csv import writer
from pprint import pprint

response = requests.get('https://quotes.toscrape.com/')

soup =BeautifulSoup(response.text,"html.parser")

quotes = soup.find_all(class_="quote")

with open("quotes.csv","w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(
        ['Text','Author','AuthorURL','Tags']
    )

    for quote in quotes:
        text = quote.find("span").get_text().strip()
        author = quote.find("small").get_text().strip()
        authorUrL = quote.find("a")["href"]
        tags = quote.find(class_="tags").get_text().lstrip()

        csv_writer.writerow(
            [text,author,authorUrL,tags]
        )

print("Scrapping complete")