import wolframalpha
# import os

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import requests
from dotenv import dotenv_values

app_id = dotenv_values(".env")['app_id']
client = wolframalpha.Client(app_id)


def askquest(question=None):
    res = client.query(question)
    answer = next(res.results).text
    if "Stephen Wolfram" in answer:
        answer = answer.replace("Stephen Wolfram", "Swasthik Shetty")
    return answer

# chrome_options = Options()
# chrome_options.add_argument("--window-size=1024x768")
# chrome_options.add_argument("--headless")
# print(f'{os.getcwd()}\chromedriver.exe'.replace('\\','/'))
# driver = webdriver.Chrome(ChromeDriverManager().install())


def ask_google(query):

    # # Search for query
    # query = query.replace(' ', '+')
    # url = 'http://www.google.com/search?q=' + query

    # driver.get(url)

    # #Get text from Google answer box

    # answer = driver.execute_script(
    #        "return document.elementFromPoint(arguments[0], arguments[1]);",
    #        350, 230).text

    return 'sorry i could not found what you are looking'
#print(ask_google('what is python'))
