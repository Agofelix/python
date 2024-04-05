import fitz

def extract_pages_with_word(pdf_path, search_phrase):
    pdf = fitz.open(pdf_path)
    pdf2 = fitz.open()

    for page_number in range(len(pdf)):
        page = pdf.load_page(page_number)
        text = page.get_text()

        words = text.split()
        
        if any(search_word in word for word in words for search_word in search_phrase.split()):
            pdf2.insert_pdf(pdf, from_page=page_number, to_page=page_number)

    if pdf2.page_count > 0:
        pdf2.save("output.pdf")
        print("Pagine contenenti la frase '{}' sono state estratte con successo.".format(search_phrase))
    else:
        print("Nessuna pagina contiene la frase '{}'.".format(search_phrase))

def read_search_phrase_from_file(file_path):
    with open(file_path, 'r') as file:
        search_phrase = file.readline().strip()
    return search_phrase

def read_search_phrase2_from_file(file_path):
    with open(file_path, 'r') as file:
        file.readline()  # Salta la prima riga
        search_phrase2 = file.readline().strip()  # Legge la seconda riga
    return search_phrase2

search_phrase = read_search_phrase_from_file("parametri.txt")
search_phrase2 = read_search_phrase2_from_file("parametri.txt")

extract_pages_with_word(search_phrase2, search_phrase)
