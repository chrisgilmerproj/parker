import unittest

from parker.keys import ORDER_OF_FLATS
from parker.keys import ORDER_OF_SHARPS
from parker.keys import Key
from parker.notes import Note
from parker.scales import Major
from parker.scales import Minor


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

    def test_C_is_major(self):
        key = Key('C')
        self.assertTrue(key.is_major())
        self.assertFalse(key.is_minor())

    def test_a_is_minor(self):
        key = Key('a')
        self.assertTrue(key.is_minor())
        self.assertFalse(key.is_major())

    def test_signature_C(self):
        key = Key('C')
        self.assertEqual(key.signature, 0)

    def test_signature_a(self):
        key = Key('a')
        self.assertEqual(key.signature, 0)

    def test_accidentals_C(self):
        key = Key('C')
        self.assertEqual(key.accidentals, [])

    def test_accidentals_a(self):
        key = Key('a')
        self.assertEqual(key.accidentals, [])

    def test_accidentals_C_flat(self):
        key = Key('Cb')
        self.assertEqual(key.signature, -7)
        self.assertEqual(key.accidentals, ORDER_OF_FLATS)

    def test_accidentals_C_sharp(self):
        key = Key('C#')
        self.assertEqual(key.signature, 7)
        self.assertEqual(key.accidentals, ORDER_OF_SHARPS)

    def test_accidentals_a_flat(self):
        key = Key('ab')
        self.assertEqual(key.signature, -7)
        self.assertEqual(key.accidentals, ORDER_OF_FLATS)

    def test_accidentals_a_sharp(self):
        key = Key('a#')
        self.assertEqual(key.signature, 7)
        self.assertEqual(key.accidentals, ORDER_OF_SHARPS)

    def test_get_accidental_notes_C_sharp(self):
        key = Key('C#')
        expected = ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#']
        expected = [Note(n) for n in expected]
        self.assertEqual(key.get_accidental_notes(), expected)

    def test_get_accidental_notes_C_flat(self):
        key = Key('Cb')
        expected = ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb']
        expected = [Note(n) for n in expected]
        self.assertEqual(key.get_accidental_notes(), expected)

    def test_get_scale_C_major(self):
        key = Key('C')
        scale = key.get_scale()
        self.assertEqual(scale, Major('C'))

    def test_get_scale_a_minor(self):
        key = Key('a')
        scale = key.get_scale()
        self.assertEqual(scale, Minor('A'))

    def test_accidental_notes_in_C_sharp(self):
        key = Key('C#')
        key_notes = [n.normalize(use_sharps=True)
                     for n in key.get_accidental_notes()]
        scale_notes = [n.normalize(use_sharps=True)
                       for n in key.get_scale().notes]
        for note in key_notes:
            self.assertTrue(note in scale_notes)

    def test_accidental_notes_in_C_flat(self):
        key = Key('Cb')
        key_notes = [n.normalize(use_sharps=True)
                     for n in key.get_accidental_notes()]
        scale_notes = [n.normalize(use_sharps=True)
                       for n in key.get_scale().notes]
        for note in key_notes:
            self.assertTrue(note in scale_notes)
