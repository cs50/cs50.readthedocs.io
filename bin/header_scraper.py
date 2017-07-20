'''
    header_scraper.py

    Sean Walker

    Scrapes cppreference.com for contents of header files.
    outputs to YAML, with format as follows:
        foo.h:
            typedefs:
                - a
                - b
            functions:
                - c
                - d
            macros:
                - X
                - Y
        bar.h:
            ...
'''

from bs4 import BeautifulSoup
import re
import requests

class Header:
    '''Contains a list of functions, macros, and typedefs for every C standard library header.'''
    def __init__(self):
        # dictionary to store all functions, macros
        self.content = {
            'functions': [],
            'macros': [],
            'typedefs': []
        }

    def appendf(self, content):
        '''Add function.'''
        self.content['functions'].append(content)

    def appendm(self, content):
        '''Add macro.'''
        self.content['macros'].append(content)

    def appendt(self, content):
        '''Add typedef.'''
        self.content['typedefs'].append(content)

    def get_content(self):
        '''Return contents of library.'''
        return self.content


def main():
    HEADERS_URL = 'http://en.cppreference.com/w/c/header'
    BASE_URL = 'http://en.cppreference.com'

    # dict of Headers
    libraries = {}

    # list of elements which have been added to the YAML
    seen = []

    with requests.session() as client:

        # first, get a list of all URLs we'll scrape, from cppreference's list of header files
        header_list = client.get(HEADERS_URL)
        header_soup = BeautifulSoup(header_list.content, 'lxml')
        rows = header_soup.find_all('table', class_='t-dsc-begin')[0].find_all('tr')

        # assemble list of URLs from provided href tags
        url_list = []
        for row in rows:
            link = row.find('a').get('href')
            url_list.append(BASE_URL + link)

        for url in url_list:

            # scrape target URL
            result = client.get(url)

            # get HTML content as soup object
            soup = BeautifulSoup(result.content, 'lxml')

            # get all tables from relevant part of page
            # only search direct children so as not to include Navbar
            # exclude first element, which is TOC
            tables = soup.find('div', id='mw-content-text').find_all('table', recursive=False)[1:]

            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    data = row.find_all('td')

                    # skip empty data
                    if len(data) == 0:
                        continue

                    # categorize into header
                    if len(data) < 2:
                        # exclude non-library headings
                        if 'header' in data[0].get_text():
                            name = re.search('\w+\.h', data[0].get_text()).group(0)
                            if name not in libraries.keys():
                                header = Header()
                                libraries[name] = header
                            else:
                                header = libraries[name]
                        continue

                    # data[0] will be the function, macro, etc.
                    # data[1] will be the description and type (e.g. 'function', 'macro constant', etc.)
                    type = data[1].get_text()
                    # get span element containing all entries in this data block
                    span = data[0].find('span')
                    if not span:
                        continue
                    # iterate over individual elements' spans
                    text = ''
                    for element in span.find_all('span'):
                        text += element.get_text().strip() + '\n'
                    text = text.splitlines()

                    # don't insert duplicates
                    if text in seen:
                        continue
                    if '(function)' in type or '(function macro)' in type:
                        header.appendf(text)
                    elif '(macro constant)' in type:
                        header.appendm(text)
                    elif '(typedef)' in type:
                        header.appendt(text)

        # send output to YAML file
        yaml_format(libraries)

def yaml_format(libraries):
    '''Output dictionary data in .yml file format.'''
    OUTFILE = 'out.yml'

    with open(OUTFILE, 'w') as f:
        for library_name, library_contents in libraries.items():
            f.write(library_name + '\n')
            for contents_category, category_contents in library_contents.get_content().items():
                f.write('\t' + contents_category + ':\n')
                for element in sum(category_contents, []):
                    f.write('\t\t- ' + element + '\n')


if __name__ == '__main__':
    main()
