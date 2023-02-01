import unittest
frtranslator import englishToFrench, frenchToEnglish

class TestMyTests(unittest.TestCase):
    def test1_1englishToFrench1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def test2_frenchToEnglish1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    def test3_englishToFrench2(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def test4_frenchToEnglish2(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    def test5_englishToFrench3(self):
        self.assertEqual(englishToFrench(' '), ' ' )
    def test6_frenchToEnglish3(self):
        self.assertEqual(frenchToEnglish(' '), ' ')

if __name__=="__main__":
    unittest.main()
