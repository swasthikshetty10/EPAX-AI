import requests
from bs4 import BeautifulSoup as bs


header = {'useragent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url= 'https://esportsobserver.com/tag/india/'
def allarticles(url):
    page = requests.get(url ,headers=header)
    soup = bs(page.content,'html.parser')
    articles = soup.find_all(class_ = "jeg_post jeg_pl_md_2 format-standard")
    all_titles = []
    all_urls = []
    all_images = []
    all_descriptions =[]
    all_dates = []
    for article in articles:
        all_titles.append(article.find(class_ ="jeg_post_title").get_text())
        all_images.append(article.find(class_ ="thumbnail-container").img['data-src'])
        all_urls.append(article.find(class_ ="jeg_post_title").a['href'])
        all_dates.append(article.find(class_ ="jeg_meta_date").get_text())
        all_descriptions.append(article.find('p').get_text())
    return all_titles, all_urls ,all_dates, all_descriptions ,all_images 


def full_news(articleurl):

    page = requests.get(articleurl)
    soup = bs(page.content,'html.parser')
    article = soup.find(class_= 'jeg_inner_content')
    title =  article.find(class_ =  "jeg_post_title").get_text()
    date  = article.find(class_ ="jeg_meta_date").get_text()
    image = article.find(class_ ="thumbnail-container").img['data-src']
    body = article.find(class_ = "content-inner").find_all('p')
    bodies = []
    for b in body:
        bodies.append(b.get_text())
    
    return title , date , image , bodies
