import requests
from bs4 import BeautifulSoup
import re

res = requests.get('https://blog.python.org/blog')
soup = BeautifulSoup(res.content, 'html5lib')
articles = soup.find_all('div', class_=re.compile(r'\bdivide-y\b'))
for article in articles:
    title = article.find('h3', class_="text-base font-semibold leading-snug text-zinc-900 transition-colors group-hover:text-[#306998] dark:text-zinc-100 dark:group-hover:text-[#ffd43b]").text
    author = article.find('a', class_="font-medium text-zinc-600 hover:text-[#306998] dark:text-zinc-300 dark:hover:text-[#ffd43b] transition-colors").text
    time = article.find('time')
    print(f"Title: {title}\nAuthor: {author}\nTime: {time}")