# -*- coding: UTF-8 -*-

from random import shuffle, randint
import re
from platform import system
import copy

class notCorrectFormat(Exception):"""
Cuando el formato es invalido
"""

class Shalom(object):

        def __init__(self, index=6, rest=6):

            """
            :index - 'El indice donde se moveran los caracteres del mapa de caracteres'
            :rest - 'Resto que se usara para evitar que se sepa el indice de grado de los caracteres'
            """

	    self.__start(index=index, rest=rest)

        def __call__(self, i, r):

            self.__start(i, r)

	def __start(self, index, rest):

            if (system() == 'Windows'):
                maps = ['<', '>', ',', '.', '-', ';', ':', '_', '\xef', '`', '+', '\x87', '\xf9', '^', '*', '\x80', '{', '[', ']', '}', '\xad', '\'', '\xa7', '\xa6', '\xa8', '?', '!', '"', '\xfa', '$', '%', '&', '/', '(', ')', '=', '\\', '|', '@', '#', '~', '?', '\xaa', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '\xa4', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '\xa5', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '\n', '\r', '\t', '\a', '\f', '\v', '\b']
            else:
                maps = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\xc2\xb4', '\xc3\xa7', '\xc2\xa8', '\xc2\xba', '\xc2\xaa', '\xc2\xb7', '\xc2\xbd', '\xc2\xac', '\xc2\xbf', '\xc2\xa1', '>', '<', '\\', ',', '.', '-', ';', ':', '_', '`', '+', '^', '*', '!', '|', "'", '"', '@', '#', '$', '~', '%', '&', '/', '{', '(', '[', ')', ']', '=', '}', '?', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '\xc3\xb1', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '\xc3\x91', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '\n', '\r', '\t', '\a', '\f', '\v', '\b']
	    self.rest = rest
	    self.index = int(index) # Convertimos a un entero
            self.maps = self.__order(maps)
        
        def hard(self, char='\xff', rang=500):

            """
            Agrega el caracter :char: deacuerdo al rango :rang: para ampliar el mapa de caracteres y aumentar la seguridad
            """

            chars = ''

            for _ in range(rang):

                chars += char

                self.maps.append(chars)

	def __xrangeStr(self, mn, mx):

		return([x for x in xrange(0,10)])

	def __order(self, string):

		if (self.index == 0):

			return(string)

		if ('-' in str(self.index)):

                        a = string[:self.index]
                        b = string[self.index:]
                        b.reverse()

                        return(b+a)

                else:

                        a = string[self.index:]
                        b = string[:self.index]
                        b.reverse()

                        return(a+b)

	def setMapsRandom(self, rang=randint(100, 100000)):

            """
            :rang - 'Usando el algoritmo de shuffle se colocara al "azar" todos los caracteres del mapa de caracteres'
            """

	    for _ in xrange(rang):

	        shuffle(self.maps)

	def key(self):

            """
            Muestra el mapa de caracteres
            """

	    return(self.maps)

	def __encryptChar(self, char, jumps):

		if (char == '') or (str(jumps) == '0'):

		    return('0(0)')

		jumps = int(jumps)
		_key = self.key()
                repeat = True

		while (True):

	    	    try:

                        if (repeat == True):

                            repeat = False

                            if not ('-' in str(self.rest)):

                                rest = '+%s' % (self.rest)

                            else:

                                rest = self.rest

                        if not ('-' in str(jumps)):

                            jumps = '+%s' % (jumps)

                        result = eval('%s%s' % (_key.index(char), jumps))

		        data = _key[result]
			ident =  _key.index(data)

                        return('%d(%d)' % (ident+1, eval('%s%s' % (jumps, rest))))

		    except IndexError:

			_key += _key

			continue

        def __check_special(self, string):

            return(string in self.maps)

	def encrypt(self, string, jumps):

                """
                Cifra el 'string' deacuerdo a los 'jumps', usando la siguiente sintaxis: Mensaje: ['m', 'e', 'n', 's', 'a', 'j', 'e'], Saltos (jumps): [5, 10, -5, 4, 9, -9, 6]

                :string - 'El mensaje'
                :jumps - 'Saltos'
                """

		new_string = ''
		lon = 0
                
		string = list(string)
		jumps = list(jumps)
                lon_string = len(string)
                lon_jumps = len(jumps)

		for _ in range(len(jumps)):

		    id_ = int(jumps[_])

                    if (id_ == self.rest*-1):

                        raise TypeError('El salto no debe ser el contrario del resto: "%s(%s)"' % (string[_], id_))

                if not (lon_jumps == lon_string):

                    raise TypeError('El string y los saltos no son de la misma longitud')

		for _ in string:

                    new_string += self.__encryptChar(_, jumps[lon])

                    lon += 1

		return(new_string)

        def __decryptChar(self, string, jumps):

            string = str(int(string)-1)
            rest = str(self.rest*-1)
            jumps = str(jumps)

            if not ('-' in rest):

                rest = '+%s' % (rest)

            real_jump = eval('%s%s' % (jumps, rest))
            real_jump = real_jump*-1

            if not ('-' in str(real_jump)):

                real_jump = '+%s' % (real_jump)

            _key = self.key()
            
            while (True):

                try:

                    return(_key[eval('%s%s' % (string,real_jump))])

                except IndexError:

                    _key += _key

                    continue

	def decrypt(self, string):

                """
                Descifra un mensaje cifrado.

                :string - 'El texto cifrado'
                """

		if not (re.match(r'([\d]+[\(][(\d|\-\d)]+[\)])+', string)):

			raise notCorrectFormat('Error en el formato!')

		regular_expression = re.compile(r'[\(]|[\)]')
		re_string = regular_expression.split(string)[:-1]

		lon_string = 0
		lon_jumps = 1

		string = []
		jumps = []

		decrypted_data = ''
		lon_decrypted = 0

		while (True):

			try:

				string.append(re_string[lon_string])
				jumps.append(re_string[lon_jumps])

			except IndexError:

				break

			lon_string += 2
			lon_jumps += 2

		for _ in string:

			if (_ == '0') or (str(jumps[lon_decrypted]) == '0'):

				decrypted_data += ' '

			else:

				decrypted_data += self.__decryptChar(_, jumps[lon_decrypted])

			lon_decrypted += 1

		return(decrypted_data)
