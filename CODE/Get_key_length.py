class Get_key_length():
    """ Gets the key length of a ciphered message """

    def get_dictionnary_with_all_recurrent_patterns(self, cipher_text_without_spaces, len_pattern=3):
        """ Iterates through the cipher text and stores the couples 'key':[value] for each pattern of length
            len_pattern. For instance, 'AEV': [34, 45, 67] indicates that pattern 'AEV' has been found 3
            times in cipher text, at indexes 34, 45 and 67.
            :param  cipher_text_without_spaces:   string - cipher text (without spaces)
            :param len_pattern: integer - length of the initial pattern to search for in cipher text
            :return dico:       dictionnary - dictionnary with all couples
                                'Pattern':[indexes where the pattern appears in the text]"""
        dico = {}
        for index in range(0, len(cipher_text_without_spaces) - 2):
            pattern = cipher_text_without_spaces[index:index + len_pattern]
            if pattern in dico:
                dico[pattern].append(index)
            else:
                dico[pattern] = [index]
        return (dico)

    def get_distance_between_recurrent_patterns(self, dico):
        """ Iterates through the dictionnary to get the distances between two occurences of the same pattern.
            For instance, input {'AEV': [34, 45, 67]} will return the differences 45-34 and 67-45.
            :param dico:      dictionnary - dictionnary with all couples
                              'Pattern':[indexes where the pattern appears in the text]
            :return distance: list - list of distances between two occurences of the same pattern
                              if the pattern is repeated at least more than 2 times """
        distance = []
        for pattern in dico:
            pattern_occurences = dico[pattern]
            if len(pattern_occurences) > 1:
                for index in range(0, len(pattern_occurences) - 1):
                    distance.append(pattern_occurences[index + 1] - pattern_occurences[index])
        return (distance)

    def PGCD(self, m, n):
        """ Get the highest common divisor of two integers
            :param m: integer
            :param n: integer
            :return : integer - the highest common divisor of two integers """
        if (m == 0):
            return n
        elif (n==0):
            return m
        else:
            return self.PGCD(n, m % n)

    def get_key_length(self, cipher_text_without_spaces, len_pattern=3):
        """ Find the length of the key based on the following principles.
            plain text      : .....DES...........DES...........DES.........DES....DES
            key (ABC)       : ABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCD
            cipher text     : .....EGV.........................EGV.........EGV..........
            distance        :      <----------24--------------><----8----->
            Here the length of the key should divide 24 and 8.
            The function is recursive through the length of the pattern, starting 3 till it finds it.

            :param cipher_text_without_spaces: string - cipher text (without spaces)
            :return length: integer - length of the key """

        dico = self.get_dictionnary_with_all_recurrent_patterns(cipher_text_without_spaces, len_pattern)
        distance = self.get_distance_between_recurrent_patterns(dico)

        if len(distance) == 0: raise Exception("impossible de determiner la clé")
        if len(distance) == 1: return distance[0]

        length = self.PGCD(distance[0], distance[1])
        for dis in distance:
            length = self.PGCD(length, dis)

        if length > 5:  # If the length is high enough, the results has more statistical chances to be good
            return (length)
        else:  # If not, we run the algorithm again with a higher pattern length
            return (self.get_key_length(cipher_text_without_spaces, len_pattern + 1))