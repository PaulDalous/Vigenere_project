from nltk import word_tokenize

class Code_vigenere():
    """ Encode or decode a text according to vigenere ciphering, giving the key
        :param text:             string - plain text or cipher text
        :param key:              string - vigenere key
        :param decode:           bool -
        :return PLAIN_TEXT :     string - plain text
                CIPHER_TEXT:     string - cipher text

                PLAIN_TEXT_WITHOUT_SPACES :     string - plain text without spaces
                CIPHER_TEXT_WITHOUT_SPACES:     string - cipher text without spaces

                TOKENIZED_PLAIN_TEXT :          list - list of words in plain text
                TOKENIZED_CIPHER_TEXT:          list - list of words in cipher text """

    def __init__(self, text, key, decode=False):

        self.KEY = key

        # Encoding or decoding the text
        if decode:  # cipher_text -> plain_text
            self.CIPHER_TEXT = text
            self.PLAIN_TEXT = self.decode_vigenere(self.CIPHER_TEXT, self.KEY)
        else:  # plain_text -> cipher_text
            self.PLAIN_TEXT = text
            self.CIPHER_TEXT = self.encode_vigenere(self.PLAIN_TEXT, self.KEY)

        # Creating useful variables for later
        self.TOKENIZED_CIPHER_TEXT = word_tokenize(self.CIPHER_TEXT)
        self.CIPHER_TEXT_WITHOUT_SPACES = self.CIPHER_TEXT.replace(' ', '')
        self.TOKENIZED_PLAIN_TEXT = word_tokenize(self.PLAIN_TEXT)
        self.PLAIN_TEXT_WITHOUT_SPACES = self.PLAIN_TEXT.replace(' ', '')

    def code_vigenere(self, input_message, key, decode=False):
        """ Encode or decode a text according to vigenere ciphering, giving the key
            :param input_message:    string - plain text or cipher text
            :param key:              string - vigenere key
            :param decode:           bool -
            :return output_message : string - plain text (if Decode = true), cipher text otherwise """

        output_message = ""
        compt_letter = 0
        for index_letter, letter in enumerate(input_message):
            if letter == " ":
                output_message += " "
            else:
                key_letter = key[compt_letter % len(key)]
                d = ord(key_letter) - 65
                if decode: d = 26 - d
                output_message += chr((ord(letter) - 65 + d) % 26 + 65)
                compt_letter += 1
        return output_message

    def decode_vigenere(self, input_message, key):
        return self.code_vigenere(input_message, key, True)

    def encode_vigenere(self, input_message, key):
        return self.code_vigenere(input_message, key)