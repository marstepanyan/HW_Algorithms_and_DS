import PyPDF2


class TextOfPdf:
    def __init__(self, pdf_path):
        self.pdf = pdf_path

    def get_text_from_pdf(self):
        # creating a pdf file object
        pdf_file_obj = open(self.pdf, 'rb')

        # creating a pdf reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

        # print(len(pdf_reader.pages))

        list_of_page_obj = []
        for i in range(len(pdf_reader.pages)):
            list_of_page_obj.append(pdf_reader.pages[i])

        list_of_texts_in_page = []
        for page in list_of_page_obj:
            list_of_texts_in_page.append(page.extract_text().split())

        pdf_file_obj.close()

        return list_of_texts_in_page
