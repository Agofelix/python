PDF Page Extractor based on Keyword
This Python program allows extracting pages from a PDF document that contain a specified keyword or phrase provided by the user.

Functionality
The program relies on two main functions:

extract_pages_with_word(pdf_path, search_phrase): This function takes the input of the PDF document's path and the keyword to search for. It opens the PDF document using the fitz (PyMuPDF) library and iterates through each page. For each page, it extracts the text and checks if the keyword is present. If found, it inserts the page into a new PDF document created to contain only the pages that meet the criteria. Finally, if at least one page is found, the new PDF document is saved.

read_search_phrase_from_file(file_path): This function reads the search keyword from an external text file. The path to the external text file is specified as the file_path parameter. The keyword is expected on the first line of the text file.

Usage
To use the program, follow these steps:

Ensure Python is installed on your system.
Install the program's dependencies by running pip install -r requirements.txt.
Create an external text file (e.g., parameters.txt) containing the path to the PDF document and the keyword on separate lines, respectively.
Run the program using the command python program_name.py.
The program will extract the pages of the PDF document containing the specified keyword and save them in a new PDF document named "output.pdf" in the same directory.
Dependencies
The program uses the fitz (PyMuPDF) library for PDF file manipulation. Dependencies are listed in the requirements.txt file.

Please note that this program has been developed and tested on Python 3.x. Modifications may be necessary for use with earlier versions of Python.
