import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)
URL = 'https://www.mohfw.gov.in'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


@app.route("/")
def hello():
  sum = 0
  for div in soup.find_all('div', { "class" : "site-stats-count"}):
    for li in div.find_all('li'):
      for value in li.find_all('strong'):
        sum += int(value.text)
        
    return str(sum)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
