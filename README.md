# paper-downloader
Quickly download an academic paper from a URL or a filepath local to your system.

# Motivation

After experimenting with a number of Python libraries that claim to read and write to PDF files, with the ability to extract metadata such as Title information, I was left dissappointed and searching StackOverflow (SO) to see if anyone else had this issue. The answer was yes, and even worse, nobody else had a good solution to the issue. For example, `pdfrw` often returns, as a SO user [notes](https://stackoverflow.com/questions/44598758/how-to-extract-the-title-of-a-pdf-document-from-within-a-script-for-renaming) in a comment on another user's proposed solution for extracting the title embedded in a PDF file.

>This is very useful, but it's worth mentioning that many PDFs do not have Info.Title. Of 312 fairly random journal articles I checked, more than 1/3 don't have it. But this is great for those that do

Another shortcoming I discovered was the result of trying to get PDF [metadata](https://pypdf2.readthedocs.io/en/latest/modules/DocumentInformation.html) via `PyPDF2`, which similarly to `pdfrw` returned empty strings for key PDF metadata.

```
>>> import requests
>>> import PyPDF2
>>> filename = 'paper_download.pdf'
>>> pdf_file_obj = open(filename, 'rb')
>>> pdf_reader_obj = PyPDF2.PdfReader(pdf_file_obj)
>>> if pdf_reader_obj.getNumPages() > 0:
...     print(pdf_reader_obj.metadata)
... 
{'/Author': '', '/CreationDate': 'D:20211202014508Z', '/Creator': 'LaTeX with hyperref', '/Keywords': '', '/ModDate': 'D:20211202014508Z', '/PTEX.Fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.21 (TeX Live 2020) kpathsea version 6.3.2', '/Producer': 'pdfTeX-1.40.21', '/Subject': '', '/Title': '', '/Trapped': '/False'}
>>> 
```

# Quickstart

## For Mac or Linux

Download `paper_downloader.py` and place it in the directory of your choice.
`cd` into the directory.

Note that papers will be saved to the directory this file is placed in by default. If you wish to change where to save the renamed papers, change the global variable `DEFAULT_FILEPATH` in the `.py` file.

Run the following

```
python3 paper_downloader.py
```

You will be prompted for a `url`. Copy and paste a URL that links to an academic paper, such as something like [this](https://angeris.github.io/papers/perps.pdf) paper on perptual future contracts, when prompted. If you ran the code using the example paper on perptuals, you should see the below output in your terminal:

```
Xivv  qfinMF   Sep A primer on perpetuals Guillermo AngerisTarun ChitraAlex EvansMatthew Lorig This version September   Abstract
Trim start:
```

The prompt `Trim start: ` is asking for where to begin for renaming the paper downloaded from the url provided. For example if we were to enter `A`, the text parsed by the code `Xivv  qfinMF   Sep ` would be excluded from the renamed file. You will then receive a prompt `Trim end: ` similarly asking for where to end the new file name for the paper.

```
Xivv  qfinMF   Sep A primer on perpetuals Guillermo AngerisTarun ChitraAlex EvansMatthew Lorig This version September   Abstract
Trim start: A
Trim end: 
```

If we were to enter `s`, the renamed file would end at the 's' in the word 'perpetuals', and thus the pdf would be saved to the current working directory as `A primer on perpetuals.pdf`.

## For Windows

Still in development for Windows. 



