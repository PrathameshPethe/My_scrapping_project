from bs4 import BeautifulSoup
import requests
from csv import writer

response = requests.get('https://books.toscrape.com/')

soup = BeautifulSoup(response.text,"html.parser")

books = soup.find_all('article')

with open("books_list.csv","w",newline="") as file:
    csv_writer = writer(file)
    csv_writer.writerow(
        ['URL','Book_image','Book_title','Price','Add_to_basket']
    )

    for book in books:
        url = book.find("a")["href"]
        book_image = book.find("img")["src"]
        book_title = book.find("h3").get_text().strip()
        price = book.find("p").get_text().strip()
        button = book.find("button").get_text().strip()

        csv_writer.writerow(
            [url,book_image,book_title,price,button]
        )

print("Scrapping Done")

