<h1>PDF Page Extractor based on Keyword</h1>

<p>This Python program allows extracting pages from a PDF document that contain a specified keyword or phrase provided by the user.</p>

<h2>Functionality</h2>

<p>The program relies on two main functions:</p>

<ol>
  <li><code>extract_pages_with_word(pdf_path, search_phrase)</code>: This function takes the input of the PDF document's path and the keyword to search for. It opens the PDF document using the <code>fitz</code> (PyMuPDF) library and iterates through each page. For each page, it extracts the text and checks if the keyword is present. If found, it inserts the page into a new PDF document created to contain only the pages that meet the criteria. Finally, if at least one page is found, the new PDF document is saved.</li>
  <li><code>read_search_phrase_from_file(file_path)</code>: This function reads the search keyword from an external text file. The path to the external text file is specified as the <code>file_path</code> parameter. The keyword is expected on the first line of the text file.</li>
</ol>

<h2>Usage</h2>

<p>To use the program, follow these steps:</p>

<ol>
  <li>Ensure Python is installed on your system.</li>
  <li>Install the program's dependencies by running <code>pip install -r requirements.txt</code>.</li>
  <li>Create an external text file (e.g., <code>parameters.txt</code>) containing the path to the PDF document and the keyword on separate lines, respectively.</li>
  <li>Run the program using the command <code>python program_name.py</code>.</li>
  <li>The program will extract the pages of the PDF document containing the specified keyword and save them in a new PDF document named "output.pdf" in the same directory.</li>
</ol>

<h2>Dependencies</h2>

<p>The program uses the <code>fitz</code> (PyMuPDF) library for PDF file manipulation. Dependencies are listed in the <code>requirements.txt</code> file.</p>

<p>Please note that this program has been developed and tested on Python 3.x. Modifications may be necessary for use with earlier versions of Python.</p>
