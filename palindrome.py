import unittest

def is_palindrome(mystring):
    
    for indice in range (0, len(mystring)):                        #SE UTILIZA PARA TODAS LAS LETRAS SIN NECESIDAD DE PONER LUGARES PRECISOS
        if mystring[indice] != mystring[-(indice+1)]:
            return False
    return True

    """def is_palindrome (mystring):
        sin_espacios = mystring.replace ("","")
        return sin_espacios == sin_espacios [::-1]"""

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado = is_palindrome('ab')
        self.assertEqual(resultado, False)

    def test_aCs(self):        
        resultado = is_palindrome('aCs')
        self.assertEqual(resultado, False)

    def test_aca(self):
        resultado = is_palindrome('aca')
        self.assertEqual(resultado, True)
    
    def test_neuquen (self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_abca(self):
        resultado = is_palindrome('abca')
        self.assertEqual(resultado, False)

    def test_hacia(self):
        resultado = is_palindrome('hacia')
        self.assertEqual(resultado, False)

    def test_alla(self):
        resultado = is_palindrome('alla')
        self.assertEqual(resultado, True)
    
    def test_absca(self):
        resultado = is_palindrome('absca')
        self.assertEqual(resultado, False)

unittest.main()

