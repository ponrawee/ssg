import unittest
from ssg import syllable_tokenize, decode

class TestTokenize(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(decode('ทดสอบ', ['0', '0', '1', '0', '0', '0']),
        ['ทด', 'สอบ'])

    def test_tokenize(self):
        self.assertEqual(syllable_tokenize('ทดสอบ'), ['ทด','สอบ'])