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

import csv
import os
import re
import requests

from bs4 import BeautifulSoup

def main():
    HEADERS_URL = "http://en.cppreference.com/w/c/header"
    BASE_URL = "http://en.cppreference.com"

    # Dictionary where key is library name, value is list of sets of functions, macros, typedefs
    libraries = {}

    with requests.session() as client:
        print("Accessing headers url...", end="")

        # Get <tr> elements containing all URLs we'll scrape
        header_list = client.get(HEADERS_URL)
        header_soup = BeautifulSoup(header_list.content, "lxml")
        rows = header_soup.find_all("table", class_="t-dsc-begin")[0].find_all("tr")

        # Assemble URL list from each row's <a> element
        url_list = []
        for row in rows:
            link = row.find("a").get("href")
            url_list.append(BASE_URL + link)

        print("done\nScraping each header page...", end="")
        # Scrape each header's (well, topic's) URL
        for url in url_list:
            result = client.get(url)

            # Get HTML content as soup object
            soup = BeautifulSoup(result.content, "lxml")

            # Get tables documenting C library functions
            # Only search direct children, skipping first element so as not to include navbar, table of contents, and other irrelevant <table> elements
            tables = soup.find("div", id="mw-content-text").find_all("table", recursive=False)[1:]

            # Iterate through each function table
            for table in tables:
                rows = table.find_all("tr")
                for row in rows:
                    data = row.find_all("td")

                    # Skip empty data
                    if len(data) == 0:
                        continue

                    # Categorize into library
                    if len(data) < 2:
                        # Exclude non-library headings
                        if "header" in data[0].get_text():
                            name = re.search("\w+\.h", data[0].get_text()).group(0).split(".")[0]
                            if name not in libraries.keys():
                                # List of three sets (functions, macros, typedefs) for each library
                                header = [set() for _ in range(3)]
                                libraries[name] = header
                            else:
                                header = libraries[name]
                        continue

                    # data[0] is the function, macro, or typedef (herein an "element")
                    # data[1] is the description and type (e.g. "function", "macro constant", etc.)
                    type = data[1].get_text()

                    # Get span element containing all entries in this data block
                    # Skip over empty data blocks
                    parent_span = data[0].find("span")
                    if not parent_span:
                        continue

                    # Each row could contain multiple elements
                    # In which case, they are all the same type and version, but should be separate rows in the CSV
                    # Create a string of all elements, later to be converted into a list
                    text = ""
                    for element in parent_span.find_all("span"):
                        text += element.get_text().strip() + "\n"

                    # Make a tuple for each element, all should be same type
                    for element in text.splitlines():
                        el_tuple = tuple()
                        el_tuple += (element,)

                        # Add C standard to which this element conforms, if given
                        version = data[0].find("span", class_="t-mark-rev")
                        if version:
                            version = version.get_text()
                            # "until" lines go in third column of CSV
                            if "until" in version:
                                el_tuple += ("",)
                                el_tuple += (re.search("C[0-9][0-9]" ,version).group(0),)
                            # "since" and vanilla standard numbers go in second column
                            else:
                                el_tuple += (re.search("C[0-9][0-9]" ,version).group(0),)
                                el_tuple += ("",)

                        # Insert tuple into appropriate set
                        if "(function)" in type or "(function macro)" in type:
                            header[0].add(el_tuple)
                        elif "(macro constant)" in type:
                            header[1].add(el_tuple)
                        elif "(typedef)" in type:
                            header[2].add(el_tuple)

        print("done\nParsing into CSV...")
        # Send output to CSV files
        csv_format(libraries)
        print("done")

def csv_format(libraries):
    """Output dictionary data in .csv file format."""
    # Constant filenames
    FUNC_FILE = "functions.csv"
    MAC_FILE = "macros.csv"
    TYPE_FILE = "typedefs.csv"

    # Iterate over all libraries in the dict
    for library_name, library_contents in libraries.items():
        # Create directories for each if they don't already exist
        if not os.path.exists(library_name):
            os.makedirs(library_name)

        # For each library, create a functions, macros, and typedefs file
        with open(library_name + "/" + FUNC_FILE, "w", newline="") as f:
            for function in library_contents[0]:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(function)
        with open(library_name + "/" + MAC_FILE, "w", newline="") as f:
            for macro in library_contents[1]:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(macro)
        with open(library_name + "/" + TYPE_FILE, "w", newline="") as f:
            for typedef in library_contents[2]:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(typedef)
        print(library_name, end=", ")
    print()

if __name__ == "__main__":
    main()
