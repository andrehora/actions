class StringParser:

    def count_uppercase_words(self, text):
        counter = 0
        for word in text.split():
            if word.isupper():
                counter += 1
        return counter