import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import jsonify

app = Flask(__name__)

URL = 'https://www.mohfw.gov.in'

@app.route("/")
def details():
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  sum = 0
  data = []
  for div in soup.find_all('div', { "class" : "site-stats-count"}):
    for li in div.find_all('li'):
      for value in li.find_all('strong'):
        data.append(value.text)
        sum += int(value.text)
        
    data.append(sum)

    json = {}
    json['Active Cases'] = data[0]
    json['Cured / Discharged'] = data[1]
    json['Deaths'] = data[2]
    json['Migrated'] = data[3]
    json['Total'] = str(data[4])

    return jsonify(json)


@app.route("/total")
def total():
  sum = 0
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  for div in soup.find_all('div', { "class" : "site-stats-count"}):
    for li in div.find_all('li'):
      for value in li.find_all('strong'):
        sum += int(value.text)

    return str(sum)


if __name__ == '__main__':
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.run(host='0.0.0.0',port=80)
