def get_key(sort_dict_frequencies, length_key, which_letter):
    """ Get the key of a ciphered message given its dict_frequencies attribute
        :param sort_dict_frequencies: list - list of sorted list where the first element is the most frequent letter for the correspondant letter of the key
        :param length_key: integer - length of the key
        :param which_letter : list - list of which frequencies we take for each letter of the key (the max or the second max)
        :return key: string - value of the decoded key """
    
    key = ""
    al  = ("".join([ chr(97+i) for i in range(0,26) ])).upper()
    
    for index in range(length_key):
        x = which_letter[index]
        letter = sort_dict_frequencies[index][x]
        p = al.find(letter)
        key += al[(p + 26 - al.find("E")) % 26]
        
    return(key)