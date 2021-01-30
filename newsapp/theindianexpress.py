from bs4 import BeautifulSoup as bs

import requests
valid_urls = ['https://indianexpress.com/section/india/',
              'https://indianexpress.com/section/sports/',
              'https://indianexpress.com/section/cities/',
              'https://indianexpress.com/section/entertainment/',
              'https://indianexpress.com/section/lifestyle/',

              ]

def news_articles(url):
    
    page = requests.get(url)
    soup = bs(page.content,'html.parser')
    #print(soup)

    articles = soup.find_all(class_="articles")

    all_titles = []
    images = []
    all_dates = []
    all_descriptions = [] 
    all_urls = []
    all_images = []

    if url == 'https://indianexpress.com/section/entertainment/':
        for article in articles:

            all_titles.append(article.find("div", {"class" :"title"}).a.get_text())
            all_images.append(article.find(class_ ="snaps").a.img['data-lazy-src'])
            all_urls.append(article.find(class_ ="title").a['href'])
            all_dates.append(article.find(class_ ="date").get_text())
            all_descriptions.append(article.find('p').get_text())



    else :  


        for article in articles:

            all_titles.append(article.find(class_ ="title").get_text())
            all_images.append(article.find(class_ ="snaps").a.img['data-lazy-src'])
            all_urls.append(article.find(class_ ="title").a['href'])
            all_dates.append(article.find(class_ ="date").get_text())
            all_descriptions.append(article.find('p').get_text())
    return all_titles,all_urls, all_dates , all_descriptions , all_images



#synopsis
def full_news(url):
    page = requests.get(url)
    soup = bs(page.content,'html.parser')
    title = soup.find(class_="native_story_title").get_text().strip()
    description = soup.find(class_="synopsis").get_text().strip()
    body = soup.find(class_ = "full-details").find_all('p')
    image = soup.find(class_ = "articles").find(class_ = "full-details").find(class_ = "custom-caption").img['data-lazy-src']
    paragraphs = []
    for p in body:
        paragraphs.append(p.get_text())
    return title ,description, paragraphs , image

