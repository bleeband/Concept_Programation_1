import doctest

def my_split(string, char):
    """
    Diviser une chaîne de caractères en une liste de sous-chaînes en fonction d'un caractère donné.

    Paramètres :

    chaîne (str) : La chaîne à diviser.
    caractère (char) : Le caractère de séparation.

    Retour : Une liste de sous-chaînes obtenues après la division de la chaîne d'entrée.

    >>> my_split('Hello,World,Python', ',')
    ['Hello', 'World', 'Python']

    >>> my_split('One:Two:Three', ':')
    ['One', 'Two', 'Three']

    >>> my_split('NoDelimiterHere', ',')
    ['NoDelimiterHere']
    """
    
    result = []
    current_substring = []

    for ch in string:
        if (ch != char):
            current_substring.append(ch)
        else:
            result.append(current_substring)
            current_substring = []

    result = [''.join(substring) for substring in result]

    return result


if __name__ == "__main__":
    import doctest
    verbose = False
    doctest.testmod()
