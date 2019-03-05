import unicodedata

class Text_processing():
    """ Encodes or decodes text according to vigenere ciphering """

    def pre_process(self, text):
        """ Removes useless characters from plain text and normalizes its general form
            :param text:        string - raw text to be preprocessed
            :return plain_text: string - plain text ready to be used """
        text = text.replace("\n", "").replace("\r", "").replace("\t", "").replace(",", "").replace(")", "")
        text = text.replace(";", "").replace(":", "").replace(".", "").replace("'", " ").replace("\"", "")
        text = text.replace("-", "").replace("!", "").replace("?", "").replace("(", "")  # .replace (" ", "")
        plain_text = text.upper()
        plain_text = self.remove_accent(plain_text)
        return (plain_text)

    def remove_accent(self, text):
        """ Removes accents from a text
            :param text:  string - text with accents
            :return text: string - text without accents """
        try:
            text = unicode(text, 'utf-8')
        except NameError:  # unicode is a default on python 3
            pass
        text = unicodedata.normalize('NFD', text) \
            .encode('ascii', 'ignore') \
            .decode("utf-8")
        return str(text)
