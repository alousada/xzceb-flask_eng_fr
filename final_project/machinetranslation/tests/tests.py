import unittest

from machinetranslation.translator import english_to_french, french_to_english

class Test_englishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(list(english_to_french('white').values())[0].pop()['translation'], 'Blanc') # test 1.1.
        self.assertEqual(list(english_to_french('black').values())[0].pop()['translation'], 'Noir') # test 1.2.    
    def test2(self): 
        self.assertEqual(list(english_to_french('').values())[0].pop()['translation'], '') # test 2.1.
    def test3(self): 
        self.assertEqual(list(english_to_french('Hello').values())[0].pop()['translation'], 'Bonjour') # test 3.1.

class Test_frenchToEnglish(unittest.TestCase): 
    def test4(self): 
        self.assertEqual(list(french_to_english('Blanc').values())[0].pop()['translation'], 'white') # test 4.1.
        self.assertEqual(list(french_to_english('Noir').values())[0].pop()['translation'], 'black') # test 4.2.
    def test5(self): 
        self.assertEqual(list(french_to_english('').values())[0].pop()['translation'], '') # test 5.1.
    def test6(self):     
        self.assertEqual(list(french_to_english('Bonjour').values())[0].pop()['translation'], 'Hello') # test 6.1.

unittest.main()

