import requests
from  bs4 import BeautifulSoup
URL = 'https://en.wikipedia.org/wiki/Washington,_D.C.'

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_posts = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    citations_needed_count = 0
    for post in all_posts:
        citations_needed_count += 1
    print("Number of citations needed is", citations_needed_count)
    return citations_needed_count


def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    division = soup.find('div', class_="mw-body-content mw-content-ltr")
    paragraphs = division.find_all("p")
    citation_needed_list = []
    for paragraph in paragraphs:
        citations = paragraph.find_all("sup", class_="noprint Inline-Template Template-Fact")
        if citations:
            citation_needed_list.append(paragraph.text)
    print(citation_needed_list)

get_citations_needed_count(URL)
get_citations_needed_report(URL)   

