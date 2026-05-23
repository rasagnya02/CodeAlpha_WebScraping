import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

quote_blocks = soup.find_all("div", class_="quote")

for quote in quote_blocks:

    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    quotes.append(text)
    authors.append(author)

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

df.to_csv("quotes.csv", index=False)

print(df)

print("Web Scraping Completed Successfully")