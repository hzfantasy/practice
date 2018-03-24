from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv
import html5lib

URL = ''
ADDR = ''

if __name__ == '__main__':
    start_page = 1
    end_page = 10
    price = 7
    with open('ganji.csv', 'wb') as f:

        csv_writer = csv.writer(f, delimiter=',')
