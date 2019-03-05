class Verify_text():
    """ Verify if words of a text are in a dictionary with a certain level of confidence """

    def is_word_in_dictionnary(self, dictionary, word):
        """ Verify if a word is in a dictionary
            :param dictionary: pd.DataFrame - a data frame with all words of a certain length
            :param word:       string - a word to be checked
            :return:           bool - True if the word is in the dictionary """
        return word in dictionary[len(word)]

    def is_message_in_dictionnary(self, dictionary, message_token):
        """ Verify if text is 'reliable'. Reliable means that it contains a sufficient amount of words that are actually real words
            (in the dictionnary). We start with a confidence level of 0 and then increase it as we find words that are in the
            dictionary. We start with the longest words first. If the confidence level exceeds 10 we return true (false otherwise).
            :param dictionary:     pd.DataFrame - a data frame with all words of a certain length
            :param message_token:  string - a tokenized message to be checked
            :return:               bool - True if the confidence level exceeds 10 """

        message_token.sort(key=lambda word: len(word), reverse=True) # Sort the token by descending order of word length

        loop_counter = 0
        confidence_level = 0
        
        while (confidence_level < 10) and (loop_counter < 100): #loop_counter 100
            word = message_token[loop_counter]

            if self.is_word_in_dictionnary(dictionary, word):
                confidence_level += 1

            loop_counter += 1

        if confidence_level >= 10:
            return (True)
        else:
            return (False)