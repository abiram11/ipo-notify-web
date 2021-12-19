import requests
from bs4 import BeautifulSoup
import json

URL = 'https://zerodha.com/ipo/'
HTML_SEARCH_TEXT = 'upcoming ipos'

def fetch_html_content(url):
    try:
        html_page = requests.get(url)
        html_text = html_page.text
        return html_text
    except Exception as err:
        print(err)
        return('Unable to fetch HTML content from the url.')

def get_ipo_data_from_html(soup, html_search_text=HTML_SEARCH_TEXT):
    data = []

    hidden_elements = soup.find_all('span', {"class": "hidden"})
    for element in hidden_elements:
        element.decompose()

    start = soup.find(text= lambda x: x.lower()==html_search_text).parent
    table = start.find_next('table')


    header = table.find('thead')
    cols = header.find_all('th')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        row
        cols = row.find_all('td')
        cols = [ " ".join(ele.text.strip().replace('\t',' ').replace('\n',' ').split()) for ele in cols ]
        data.append([ele for ele in cols if ele])
    return data

def generate_json_data_array(data_list, keys):
    data_dict_list = []
    for data in data_list:
        data_dict = {}
        for value, key in zip(data, keys):
            data_dict[key] = value
        data_dict_list.append(data_dict)
    return json.dumps(data_dict_list)

def fetch_latest_ipo_information():
    html_text = fetch_html_content(URL)
    soup = BeautifulSoup(html_text, 'html.parser')
    data = get_ipo_data_from_html(soup)
    json_array = generate_json_data_array(data[1:], data[0])
    return json_array
