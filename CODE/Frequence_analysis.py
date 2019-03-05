import numpy as np
import operator

class Frequence_analysis():
    ''' Gets the frequencies for each set of letter corresponding to one letter in the key,
        based on key length. For instance :
        cipher text : XY TWKLVQUM I LLEU XAZU UZMCL MK AVMHV
                      X- ---L---- I ---- X--- -Z--- -K ----V  -> {'X': 0.3,'L':0.1,'I':0.1,'Z':0.1,'K':0.1,'V':0.1}
                      -Y ----V--- - L--- -A-- --M-- -- A----  -> ...
                      -- T----Q-- - -L-- --Z- ---C- -- -V---  -> ...
                      -- -W----U- - --E- ---U ----L -- --M--  -> ...
                      -- --K----M - ---U ---- U---- M- ---H-  -> ... '''

    def get_n_lists_of_letters(self, cipher_text_without_spaces, length_key):
        ''' Get the n lists of letters, n corresponding to the lenght of the key.
            For instance for the cipher text : XY TWKLVQUM I LLEU XAZU UZMCL MK AVMHV with a key of
            length 5, we get the folowing list :
                                [ ['X', 'L', 'I', 'X', 'Z', 'K', 'V'],
                                  ['Y', 'V', 'L', 'A', 'M', 'A'],
                                  ['T', 'Q', 'L', 'Z', 'C', 'V'],
                                  ['W', 'U', 'E', 'U', 'L', 'M'],
                                  ['K', 'M', 'U', 'U', 'M', 'H']      ]
            :param cipher_text_without_spaces: string - cipher text (without spaces)
            :param length_key:                 integer - length of the key
            :return n_list: list - list of the same size as the key, with list of letters corresponding '''
        n_list = [[] for i in range(length_key)]
        for index_letter, letter in enumerate(cipher_text_without_spaces):
            n_list[index_letter % length_key].append(letter)
        return (n_list)

    def get_letter_frequencies(self, n_list):
        ''' Get the frequencies of each letter in a list of letter
            :param n_list:     list - list of the same size as the key, with list of letters corresponding
            :return dict_freq: list - list of dictionaries with couples 'letter' : frequence in the list '''
        dict_freq = dict()
        total_number_of_letter = len(n_list)
        for letter in n_list:
            if letter in dict_freq.keys():
                dict_freq[letter] += 1
            else:
                dict_freq[letter] = 1
        dict_freq = {k: np.round((v / total_number_of_letter) * 100, 2) for k, v in dict_freq.items()}
        return (dict_freq)

    def create_dict_of_letter_freq(self, cipher_text_without_spaces, length_key):
        """ Concatenate functions get_letter_frequencies, get_n_lists_of_letters and sort_dict
            :param cipher_text_without_spaces: string - cipher text (without spaces)
            :param length_key:                 integer - length of the key
            :return list_sorted_letter :       list - list of list of each letter in each dictionnary, sorted by
                                               descending frequencies """
        n_list = self.get_n_lists_of_letters(cipher_text_without_spaces, length_key)
        dict_frequencies = [self.get_letter_frequencies(liste) for liste in n_list]
        list_sorted_letter = self.sort_dict(dict_frequencies)
        return(list_sorted_letter)

    def sort_dict(self, dict_frequencies):
        """ Get the list of the letters, sorted by frequencies
            :param dict_frequencies :    list - list of dictionnary with frequencies for each letter in the cipher text
            :return list_sorted_letter : list - list of list of each letter in each dictionnary, sorted by growing
                                                frequencies """
        list_sorted_letter = []
        for dico in dict_frequencies:
            sorted_dict = sorted(dico.items(), key=operator.itemgetter(1))
            sorted_letter = [car[0] for car in sorted_dict]
            sorted_letter.reverse() #reverse to have the higher frequency first
            list_sorted_letter.append(sorted_letter)
        return(list_sorted_letter)

