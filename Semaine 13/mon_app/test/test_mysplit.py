import unittest
from mon_package.my_split import my_split, MyCustomTypeError

class TestMonModule(unittest.TestCase):

    def test_single_input(self):
        input = "salut tout le monde"
        output = my_split(input)
        expected = ["salut", "tout", "le", "monde"]
        self.assertEqual(output, expected)

    def test_is(self):
        a = [42]
        b = [42]
        c = a

        self.assertIs(a, c)
        self.assertIsNot(a, b)

    def test_boolean(self):
        a = True
        b = 1
        c = 1
        d = "Je suis une chaine de caracteres"
        e = {"OK"}
        
        self.assertTrue(a)
        self.assertTrue(b)
        self.assertTrue(c)
        self.assertTrue(d)
        self.assertTrue(e)

    def test_none(self):
        a = None
        b = 42
        self.assertIsNone(a)
        self.assertIsNotNone(b)

    def test_in(self):
        a = "salut tout le monde"
        self.assertIn("salut", a)
        self.assertIn("tout", a)
        self.assertIn("le", a)
        self.assertIn("monde", a)
        self.assertNotIn("bonjour", a)

    def test_isinstance(self):
        a = "salut tout le monde"
        b = 42
        c = [1, 2, 3]
        self.assertIsInstance(a, str)
        self.assertIsInstance(b, int)
        self.assertIsInstance(c, list)
        self.assertNotIsInstance(a, int)
        self.assertNotIsInstance(b, str)
        self.assertNotIsInstance(c, dict)

    def test_exception_if_not_string(self):
        input = 42
        self.assertRaises(MyCustomTypeError, my_split, input, "-")