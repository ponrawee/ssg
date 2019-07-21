import unittest
from copy import deepcopy
from ssg import Featurizer

class TestFeaturize(unittest.TestCase):
    def setUp(self):
        self.F = Featurizer(N=3)
        self.true_result = {'X': [
            ['-1|#', '0|a', '-2|#', '1|b', '-3|#', '2|c', '-4|#', '3|d', '-4|###', '-3|###', '-2|##a', '-1|#ab', '0|abc', '1|bcd'], 
            ['-1|a', '0|b', '-2|#', '1|c', '-3|#', '2|d', '-4|#', '3|e', '-4|###', '-3|##a', '-2|#ab', '-1|abc', '0|bcd', '1|cde'], 
            ['-1|b', '0|c', '-2|a', '1|d', '-3|#', '2|e', '-4|#', '3|f', '-4|##a', '-3|#ab', '-2|abc', '-1|bcd', '0|cde', '1|def'], 
            ['-1|c', '0|d', '-2|b', '1|e', '-3|a', '2|f', '-4|#', '3|#', '-4|#ab', '-3|abc', '-2|bcd', '-1|cde', '0|def', '1|ef#'], 
            ['-1|d', '0|e', '-2|c', '1|f', '-3|b', '2|#', '-4|a', '3|#', '-4|abc', '-3|bcd', '-2|cde', '-1|def', '0|ef#', '1|f##'], 
            ['-1|e', '0|f', '-2|d', '1|#', '-3|c', '2|#', '-4|b', '3|#', '-4|bcd', '-3|cde', '-2|def', '-1|ef#', '0|f##', '1|###'],
            ['-1|f', '0|#', '-2|e', '1|#', '-3|d', '2|#', '-4|c', '3|#', '-4|cde', '-3|def', '-2|ef#', '-1|f##', '0|###', '1|###']],
        'Y': 
            ['0', '0', '0', '1', '0', '0', '0']}

    def test_features(self):
        r = self.F.featurize('abc~def')
        self.assertEqual(r, self.true_result)

    def test_features_single_syllable(self):
        r = self.F.featurize('abcdef')
        t = deepcopy(self.true_result)
        t['Y'] = ['0', '0', '0', '0', '0', '0', '0']
        self.assertEqual(r['X'], self.true_result['X'])
        self.assertEqual(r['Y'], t['Y'])