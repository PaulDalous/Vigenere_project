import pandas as pd

def import_dictionnaries():
    """ Import dictionnaries
        :return dictionnaries: dictionnary - a dictionnary in a form of
                {number of word in dictionnary: pd.DatFrame with all the words of this length """
    dictionnaries = dict()
    for word_size in range(1,25):
        path = './DATA/liste.de.mots.francais_{0}.txt'.format(str(word_size))
        dictionnaries[word_size] = pd.read_csv(path, names = ['mot'])
        dictionnaries[word_size] = dictionnaries[word_size].apply(lambda x: x[:][0].upper(), axis = 1)
        dictionnaries[word_size] = dictionnaries[word_size].T.values.tolist()
    return(dictionnaries)

