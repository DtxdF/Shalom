import sys

if (sys.version_info.major != 3):

    raise NotImplementedError('Ya no uso esta versión :/')

from random import shuffle

def _generate_key():

    keys = []

    for _ in range(1114111):

        try:

            keys.append(chr(_))

        except:

            pass

    return(keys)

def _int_to_str(n):

    n = str(int(n))

    return('+{}'.format(n) if not ('-' in n) else n)

class Shalom(object):

    def __init__(self, password=None, index=6, rest=6):

        if (password == None):

            self.password = _generate_key()

        else:

            if not (isinstance(password, list)):

                self.password = [x for x in str(password)]

            else:

                self.password = password

        index = _int_to_str(index)

        if ('-' in index):

            self.password = list(reversed(self.password[int(index):])) + self.password[:int(index)]

        else:

            self.password = self.password[int(index):] + list(reversed(self.password[:int(index)]))

        self.rest = _int_to_str(rest)

    def __call__(self, *args, **kwargs):

        self.__init__(*args, **kwargs)

    def random(self, rang):

        for _ in range(int(rang)):

            shuffle(self.password)

    def hard(self, rang, random=(True, 50), char='\00'):

        if not (isinstance(random, tuple)):

            raise TypeError('random, no está siguiendo la especificación acordada')

        [self.password.append(char) for x in range(int(rang))]

        if (random[0]):

            if (len(random) != 2):

                raise ValueError('La longitud de "random" no es correcta')

            self.random(int(random[1]))

    def encrypt(self, string, jumps):

        string = str(string)

        if not (isinstance(jumps, list)):

            raise TypeError('Debe seguir la especificación correspondiente')

        # Verifico el tipo de dato

        try:

            [int(x) for x in jumps]

        except (TypeError, ValueError):

            raise ValueError('Un salto no está siguiendo la especificación correspondiente')

        # Verifico la longitud

        if (len(string) != len(jumps)):

            raise ValueError('El "String" y los "Saltos" no son iguales en longitud')

        # Algoritmo de Shalom

        cipher = [(a+b, eval('{}{}'.format(b*-1, self.rest))) for a,b in list(zip([self.password.index(x) for x in string], jumps))]

        return(cipher)

    def decrypt(self, string):

        if not (isinstance(string, list)):

            raise TypeError('No está siguiendo la especificación correspondiente')

        string = [(int(a), int(b)) for a,b in string]
        rest = str(int(eval('{}*-1'.format(self.rest))))
        rest = '+{}'.format(rest) if not ('-' in rest) else rest
        parsed = []

        for a,b in string:

            b = str(eval('{}{}'.format(b, rest)))
            b = '+{}'.format(b) if not ('-' in b) else b
            parsed.append(self.password[eval('{}{}'.format(a, b))])

        return(''.join(parsed))
