import requests
import random
from bs4 import BeautifulSoup
import time
import facebook
import os

graph = facebook.GraphAPI(access_token=os.environ["token"])

quo = [""]

for p in range(100):

    URL = 'https://www.goodreads.com/quotes?page={}'.format(p)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    quote = soup.find_all('div', class_="quoteText")

    for q in quote:
        auth = q.find('span', class_="authorOrTitle")
        tw = q.contents[0] + auth.text 
        quo.append(tw)

T = 10
while True:
    for t in range(T):
        if t == 0:
            quotes = random.choice(quo)
            try:
                graph.put_object("me", "feed", message=quotes.strip())
            except GraphAPIError:
                pass
            print("DONE")
            time.sleep(7200)
    

