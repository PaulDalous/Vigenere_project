from CODE.Code_vigenere import Code_vigenere
from CODE.Get_key import *
from CODE.Verify_text import Verify_text


def loop_to_find_key(sorted_dict_frequencies, length_key, list_of_combinations, token_message, dictionnaries):
    """ Loop over list of combinations to find the key, given its length. List of combinations is a list of lists such
        as [0,0,0,1,0] for instance for a key of length 5. Numbers in it is 0 if the corresponding letter in the key
        will give an E for the most frequency-letter. It is a 1 if only the second letter ordered by frequency is chosen.
        :param sorted_dict_frequencies: list - list of dictionnary with frequencies for each letter in the cipher text
        :param length_key:              integer - length of the key
        :param list_of_combinations:    list - list of combinations of 0 and 1
        :param token_message:           string - tokenized message
        :param dictionaries:            dictionaries - list of dictionaries
        :return key:                    string - the key """

    verif = False
    compt_which_letter = 0

    while verif == False and compt_which_letter < len(list_of_combinations) - 1:

        print(compt_which_letter)
        key = get_key(sorted_dict_frequencies, length_key, list_of_combinations[compt_which_letter])

        tokenized_message = Code_vigenere(" ".join(token_message), key, decode = True).TOKENIZED_PLAIN_TEXT

        verif = Verify_text().is_message_in_dictionnary(dictionnaries, tokenized_message)
        compt_which_letter += 1

    return(key)