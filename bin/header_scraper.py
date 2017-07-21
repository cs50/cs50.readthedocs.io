"""
    header_scraper.py

    Sean Walker

    Scrapes cppreference.com for contents of header files.
    Outputs to directories containing CSV, with format as follows:
        foo
        |-- functions.csv
        |-- macros.csv
        |-- typedefs.csv
        ...

        .csv:
        item_a, C##, until/since C##
        item_b, C##, until/since C##
        ...
        (where C## is the C standard it conforms to, if appropriate)
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
        self.functions.add(content)

    def addm(self, content):
        """Add macro."""
        self.macros.add(content)

    def addt(self, content):
        """Add typedef."""
        self.typedefs.add(content)

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

        # get <tr> elements containing all URLs we'll scrape
        header_list = client.get(HEADERS_URL)
        header_soup = BeautifulSoup(header_list.content, "lxml")
        rows = header_soup.find_all("table", class_="t-dsc-begin")[0].find_all("tr")

        # assemble URL list from each row's <a> element
        url_list = []
        for row in rows:
            link = row.find("a").get("href")
            url_list.append(BASE_URL + link)

        # scrape each header's (well, topic's) URL
        for url in url_list:
            result = client.get(url)

            # get HTML content as soup object
            soup = BeautifulSoup(result.content, "lxml")

            # get tables documenting C library functions
            # only search direct children, skipping first element so as not to include navbar, table of contents, and other irrelevant <table> elements
            tables = soup.find("div", id="mw-content-text").find_all("table", recursive=False)[1:]

            # iterate through each function table
            for table in tables:
                rows = table.find_all("tr")
                for row in rows:
                    data = row.find_all("td")

                    # skip empty data
                    if len(data) == 0:
                        continue

                    # categorize into library
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

                    # data[0] is the function, macro, or typedef (herein an "element")
                    # data[1] is the description and type (e.g. "function", "macro constant", etc.)
                    type = data[1].get_text()

                    # get span element containing all entries in this data block
                    # skip over empty data blocks
                    parent_span = data[0].find("span")
                    if not parent_span:
                        continue

                    # each row could contain multiple elements
                    # in which case, they are all the same type and version, but should be separate rows in the CSV
                    # create a string of all elements, later to be converted into a list
                    text = ""
                    for element in parent_span.find_all("span"):
                        text += element.get_text().strip() + "\n"

                    # add C standard to which this element conforms, if given
                    version = data[0].find("span", class_="t-mark-rev")
                    if version:
                        # remove parentheses
                        version = version.get_text().replace("(", "").replace(")", "")

                    # make a tuple for each element, all should be same type
                    for element in text.splitlines():
                        el_tuple = tuple()
                        el_tuple += (element,)

                        # add in version if it was given
                        if version:
                            # "until" and "since" lines should go in 3rd column of CSV
                            if "since" in version or "until" in version:
                                el_tuple += ("",)
                                el_tuple += (version,)
                            else:
                                el_tuple += (version,)
                                el_tuple += ("",)

                        # convert tuple to CSV format
                        el_csv = ",".join(el_tuple) + "\n"

                        # insert tuple into appropriate set
                        if "(function)" in type or "(function macro)" in type:
                            header.addf(el_csv)
                        elif "(macro constant)" in type:
                            header.addm(el_csv)
                        elif "(typedef)" in type:
                            header.addt(el_csv)

        # send output to CSV files
        csv_format(libraries)

def csv_format(libraries):
    """Output dictionary data in .csv file format."""
    # constant filenames
    FUNC_FILE = "functions.csv"
    MAC_FILE = "macros.csv"
    TYPE_FILE = "typedefs.csv"

    # iterate over all libraries in the dict
    for library_name, library_contents in libraries.items():

        # create directories for each if they don't already exist
        if not os.path.exists(library_name):
            os.makedirs(library_name)

        # for each library, create a functions, macros, and typedefs file
        with open(library_name + "/" + FUNC_FILE, 'w') as f:
            for function in library_contents.get_functions():
                f.write(function)
        with open(library_name + "/" + MAC_FILE, 'w') as f:
            for macro in library_contents.get_macros():
                f.write(macro)
        with open(library_name + "/" + TYPE_FILE, 'w') as f:
            for typedef in library_contents.get_typedefs():
                f.write(typedef)

if __name__ == "__main__":
    main()
