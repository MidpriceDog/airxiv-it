
import requests
import PyPDF2
import numpy as np
import pandas as pd
import os
from pathlib import Path

DEFAULT_FILEPATH = 'cwd'


def rename_paper_from_url(url, fpath='cwd'):
    """
    Download the academic paper (pdf) located at the specified url to the specified fpath and rename it
    """
    # Define HTTP Headers
    headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }
    download_pdf(url, headers)
    rename_paper_from_fpath(fpath)


def rename_paper_from_fpath(fpath='cwd'):
    """
    Rename the academic paper (pdf) located at the specified fpath
    """
    if fpath.casefold() == 'cwd':
        cwd_fpath = os.getcwd()
        rename_paper_at_fpath(f"{cwd_fpath}/temp_name.pdf")
    else:
        rename_paper_at_fpath(fpath)


def get_download_folder_fpath():
    """
    Get user's download folder location on Mac or Linux
    """
    path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
    return path_to_download_folder


def download_pdf(url: str, headers: dict, download_fpath: str = os.getcwd()):
    """
    Download pdf from the specified url to the specified download_fpath. Default is the current working directory.

    Args:
      url [str]: Valid URl ending with .pdf
      headers [dict]: Information about the request context.
    """
    # Send GET request
    response = requests.get(url, headers=headers)
    # Save the PDF
    if response.status_code == 200:
        with open(f"{download_fpath}/temp_name.pdf", "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)


def rename_paper_at_fpath(fpath: str):
    """
    Returns the title from the academic paper at the specified filepath on the user's system

    Args:
        filepath [str]: Absolute filepath to the academic paper to get the title of
    """
    # Create PDF file object
    pdf_file_obj = open(fpath, 'rb')
    # Create pdf reader object
    pdf_reader_obj = PyPDF2.PdfReader(pdf_file_obj)
    cleaned_results = []

    if pdf_reader_obj.getNumPages() > 0:
        # Create page object
        pageObj = pdf_reader_obj.getPage(0)
        # Extract text from page
        newline_split_list = pageObj.extract_text().split("\n")
        # print(newline_split_list)
        line = 0
        result = ''
        while not 'Abstract' in result:
            # Uncleaned title, authors, university / lab affiliations, dates, etc. of the paper
            dirty_title_series = pd.Series(list(newline_split_list[line]))

            dirty_title_indexer = dirty_title_series.apply(
                lambda c: c.isalpha() or c == ' ')
            result = ''.join(dirty_title_series.where(
                dirty_title_indexer).astype('str')).replace('nan', '')
            cleaned_results.append(result)
            line += 1
        print(' '.join(cleaned_results) + "\n")
        rough_title = ' '.join(cleaned_results)
        trimmed_title = rough_title
        start_word = input("Trim start: ")
        end_word = input("Trim end: ")
        final_title = trimmed_title[rough_title.index(
            start_word):rough_title.index(end_word) + len(end_word)] + ".pdf"

        os.rename('temp_name.pdf', final_title)
        print(f"\nFile saved as '{final_title}'")
    return None


if __name__ == "__main__":
    url = input("url: ")
    print("\n")
    rename_paper_from_url(url, DEFAULT_FILEPATH)
