"""
    header_scraper.py

    Sean Walker

    Scrapes cppreference.com for contents of header files.
    Outputs to directories containing CSV, with format as follows:
        foo
        ├── functions.csv
        ├── macros.csv
        └── typedefs.csv
        ...

        .csv:
        item_a, C## standard
        item_b, C## standard
        ...
"""

import os
import re
import requests

from bs4 import BeautifulSoup

class Header:
    """Contains a list of functions, macros, and typedefs for every C standard library header."""
    def __init__(self):
        # dictionary to store all functions, macros
        self.functions = set()
        self.macros = set()
        self.typedefs = set()

    def addf(self, content):
        """Add function."""
        self.functions.update(content)

    def addm(self, content):
        """Add macro."""
        self.macros.update(content)

    def addt(self, content):
        """Add typedef."""
        self.typedefs.update(content)

    def get_functions(self):
        """Return functions of library."""
        return self.functions

    def get_macros(self):
        """Return macros of library."""
        return self.macros

    def get_typedefs(self):
        """Return typedefs of library."""
        return self.typedefs


def main():
    HEADERS_URL = "http://en.cppreference.com/w/c/header"
    BASE_URL = "http://en.cppreference.com"

    # dict of Headers
    libraries = {}

    with requests.session() as client:

        # first, get a list of all URLs we'll scrape, from cppreference's list of header files
        header_list = client.get(HEADERS_URL)
        header_soup = BeautifulSoup(header_list.content, "lxml")
        rows = header_soup.find_all("table", class_="t-dsc-begin")[0].find_all("tr")

        # assemble list of URLs from provided href tags
        url_list = []
        for row in rows:
            link = row.find("a").get("href")
            url_list.append(BASE_URL + link)

        for url in url_list:

            # scrape target URL
            result = client.get(url)

            # get HTML content as soup object
            soup = BeautifulSoup(result.content, "lxml")

            # get all tables from relevant part of page
            # only search direct children so as not to include Navbar
            # exclude first element, which is TOC
            tables = soup.find("div", id="mw-content-text").find_all("table", recursive=False)[1:]

            for table in tables:
                rows = table.find_all("tr")
                for row in rows:
                    data = row.find_all("td")

                    # skip empty data
                    if len(data) == 0:
                        continue

                    # categorize into header
                    if len(data) < 2:
                        # exclude non-library headings
                        if "header" in data[0].get_text():
                            name = re.search("\w+\.h", data[0].get_text()).group(0).split(".")[0]
                            if name not in libraries.keys():
                                header = Header()
                                libraries[name] = header
                            else:
                                header = libraries[name]
                        continue

                    # data[0] will be the function, macro, etc.
                    # data[1] will be the description and type (e.g. "function", "macro constant", etc.)
                    type = data[1].get_text()
                    # get span element containing all entries in this data block
                    span = data[0].find("span")
                    if not span:
                        continue
                    # iterate over individual elements' spans
                    text = ""
                    for element in span.find_all("span"):
                        text += element.get_text().strip()

                    # add version of C this was added in, if appropriate
                    version = data[0].find("span", class_="t-mark-rev")
                    if version:
                        text += " " + version.get_text()

                    text += "\n"
                    text = text.splitlines()

                    # don't insert duplicates
                    if "(function)" in type or "(function macro)" in type:
                        header.addf(text)
                    elif "(macro constant)" in type:
                        header.addm(text)
                    elif "(typedef)" in type:
                        header.addt(text)

        # send output to CSV files
        csv_format(libraries)

def csv_format(libraries):
    """Output dictionary data in .csv file format."""
    FUNC_FILE = "functions.csv"
    MAC_FILE = "macros.csv"
    TYPE_FILE = "typedefs.csv"

    for library_name, library_contents in libraries.items():
        if not os.path.exists(library_name):
            os.makedirs(library_name)
        with open(library_name + "/" + FUNC_FILE, 'w') as f:
            for function in library_contents.get_functions():
                f.write(",".join(function.split(" "))  + "\n")
        with open(library_name + "/" + MAC_FILE, 'w') as f:
            for macro in library_contents.get_macros():
                f.write(",".join(macro.split(" "))  + "\n")
        with open(library_name + "/" + TYPE_FILE, 'w') as f:
            for typedef in library_contents.get_typedefs():
                f.write(",".join(typedef.split(" ")) + "\n")

if __name__ == "__main__":
    main()
