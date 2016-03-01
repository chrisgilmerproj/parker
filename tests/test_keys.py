import unittest

from parker.keys import Key


class TestKeys(unittest.TestCase):

    def test_constructor(self):
        key = Key('C')
        self.assertEqual(key.key, 'C')
        self.assertEqual(key.mode, key.MAJOR)

    def test_str(self):
        key = Key('C')
        self.assertEqual(str(key), 'C major')

    def test_repr(self):
        key = Key('C')
        self.assertEqual(repr(key), "Key('C')")

    def test_is_major(self):
        key = Key('C')
        self.assertTrue(key.is_major())

    def test_is_minor(self):
        key = Key('C')
        self.assertFalse(key.is_minor())
