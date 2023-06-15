class Word:
    def __init__(self, str_word: str):
        self.val = str_word

    def make_lowercase(self):
        return Word(self.val.lower())

    def remove_symbols(self):
        special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
                              '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        if not self.val.isalpha():
            for i in special_characters:
                self.val.replace(i, '')
        return Word(self.val)

    def is_word_in_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if self.val in line:
                    return True
        return False

    def normalize(self, file_path):
        # just checking if word in library or not, for now!!!
        if self.is_word_in_file(file_path):
            return self.val

    def get_normalized_word(self, file_for_normalizing='words_alpha.txt'):
        lowercase_word = self.make_lowercase()
        clean_word = lowercase_word.remove_symbols()
        normalized_word = clean_word.normalize(file_for_normalizing)

        return normalized_word
