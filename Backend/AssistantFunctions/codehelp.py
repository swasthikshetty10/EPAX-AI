from urllib.parse import quote_plus
import webbrowser
from howdoi import howdoi
# from bs4 import BeautifulSoup as bs
# import requests


def stackoverflow(question=None):
    question = quote_plus(question)
    url = f'https://stackoverflow.com/search?q={question}&s=513e6549-a9d9-462a-ae1c-81199bb30247'
    webbrowser.open(url)
    # header = {'useragent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
    # page = requests.get(url ,headers=header)
    # soup = bs(page.content,'html.parser').prettify()
    # print(soup)

#stackoverflow('pyaudio error')


def askhow(query):
    if 'how do i ' in query:
        query = query.replace("how do i ", '')

    if 'how to ' in query:
        query = query.replace("how to ", '')
    if 'how ' in query:
        query = query.replace("how ", '')
    if 'write ' in query:
        query = query.replace("write ", '')
    if 'use ' in query:
        query = query.replace("use ", '')
    # parser = howdoi.get_parser()
    # args = vars(parser.parse_args(query.split(' ')))
    # print(query)
    output = howdoi.howdoi(query)
    return output
