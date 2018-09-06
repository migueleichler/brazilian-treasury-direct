import requests
from lxml import html


def get_older_suspensions():
    page = requests.get('http://www.tesouro.fazenda.gov.br/avisos')
    page_html = html.fromstring(page.content)
    href = page_html.xpath('//a[@class="next"]//@href')

    return href
