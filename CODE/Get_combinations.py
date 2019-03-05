import itertools

def get_list_of_combinations_of_zeros_and_ones(length_key):
    """ Create a list of all combination of n binay value :
        For n = 3, we obtain [[0,0,0], [0,0,1], [0,1,0], [0,1,1], ... [1,1,1]]
        :param lengh_key :          integer - length of the key
        :return tot_which_letter :  list of list, with one list is the digits of a binary number """

    ist_of_combinations_of_zeros_and_ones = list(map(list,itertools.product([0,1], repeat=length_key)))
    ist_of_combinations_of_zeros_and_ones.sort(key=lambda _list: sum(_list))
    return(ist_of_combinations_of_zeros_and_ones)