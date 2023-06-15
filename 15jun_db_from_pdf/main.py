from TextOfPdf import TextOfPdf
from Word import Word


def write_to_file(text_from_file):
    set_of_words = set()
    for page in text_from_file:
        for word in page:
            normal_word = Word(word).get_normalized_word()
            if normal_word:
                set_of_words.add(normal_word)

    with open('db_from_pdf.txt', 'w+') as out_file:
        for word in set_of_words:
            out_file.write(word + '\n')


sample = TextOfPdf('sample.pdf')
print(sample.get_text_from_pdf())

text_from_sample = sample.get_text_from_pdf()

write_to_file(text_from_sample)
