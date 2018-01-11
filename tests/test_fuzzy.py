import unittest

from fuzzyattr import fuzzyattr


class Human:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        return f'{self.name} ate {food}'

    def eat_eel(self):
        return f'{self.name} ate eel'

    def eel(self):
        return f'wrong thing'


@fuzzyattr
class FuzzyHuman(Human):
    pass


class TestFuzzy(unittest.TestCase):
    def test_nofuzzy(self):
        someone = Human('Someone')
        self.assertEqual(someone.eat('poop'), 'Someone ate poop')

    def test_nofuzzy_exception(self):
        someone = Human('Someone')
        with self.assertRaises(AttributeError):
            someone.ate('poop')

    def test_fuzzy_wrong_name(self):
        someone = FuzzyHuman('Someone')
        self.assertEqual(someone.ate('poop'), 'Someone ate poop')

    def test_fuzzy_correct_name(self):
        someone = FuzzyHuman('Someone')
        self.assertEqual(someone.eat('poop'), 'Someone ate poop')

if __name__ == '__main__':
    unittest.main()
