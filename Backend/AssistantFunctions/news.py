import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"

def get_news():
  Client=urlopen(news_url)
  xml_page=Client.read()
  Client.close()

  soup_page=soup(xml_page,"xml")
  news_list=soup_page.findAll("item")
  # Print news title, url and publish date

  news_dict = {}
  for news in news_list:
    news_dict[f"{news.title.text}"] = {"link":str(news.link.text),"date":str(news.pubDate.text)}
 
  return news_dict  

# n = get_news()
# print(n)
