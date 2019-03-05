import codecs
from CODE.Text_processing import Text_processing
from CODE.Get_key_length import Get_key_length
from CODE.Frequence_analysis import Frequence_analysis
from CODE.Get_combinations import *
from CODE.Import_dictionnaries import *
from CODE.Loop import *



### Importing a text for example and coding it with key VOICILACLE ###

with codecs.open('DATA/texte.txt', 'r', encoding='utf8') as f:
    raw_text = f.read()

text = Text_processing().pre_process(text = raw_text)
print(text)

_CODE_VIGENERE_ = Code_vigenere(text, 'VOICILACLE')

cipher_text_without_spaces = _CODE_VIGENERE_.CIPHER_TEXT_WITHOUT_SPACES
token_message = _CODE_VIGENERE_.TOKENIZED_CIPHER_TEXT





### Finding the key length ###

length_key = Get_key_length().get_key_length(cipher_text_without_spaces)
print('The key length is : ' + str(length_key))





### Finding the key knowing its length ###

list_of_combinations = get_list_of_combinations_of_zeros_and_ones(length_key)
print('list_of_combinations has been calculated successfuly')

sorted_dict_frequencies = Frequence_analysis().create_dict_of_letter_freq(cipher_text_without_spaces, length_key)
print("sorted_dict_frequencies has been calculated successfuly")

print('Importing dictionnaries...')
dictionnaries = import_dictionnaries()
print('Dictionnaries imported successfully')

raw_key = get_key(sorted_dict_frequencies, length_key, list_of_combinations[0])
print('A raw version of the key is : ' + str(raw_key))

print('The final version of the key is : ')
print(loop_to_find_key(sorted_dict_frequencies, length_key, list_of_combinations, token_message, dictionnaries))


