import unittest

from parker.chords import Chord
from parker.notes import Note
from parker.progressions import is_valid_progression
from parker.progressions import Progression
from parker.scales import Major
from parker.scales import Minor


class TestProgressionMethods(unittest.TestCase):

    def test_is_valid_progression(self):
        self.assertTrue(is_valid_progression('I'))
        self.assertTrue(is_valid_progression('ii'))
        self.assertTrue(is_valid_progression('biii'))
        self.assertTrue(is_valid_progression('IV7'))
        self.assertTrue(is_valid_progression('Vdim'))
        self.assertTrue(is_valid_progression('#VI'))

    def test_is_not_valid_progression(self):
        self.assertFalse(is_valid_progression('c'))
        self.assertFalse(is_valid_progression('b7'))
        self.assertFalse(is_valid_progression('VIII'))
        self.assertFalse(is_valid_progression('IX'))
        self.assertFalse(is_valid_progression('x'))


class TestProgressions(unittest.TestCase):

    def setUp(self):
        self.p = Progression('D')

    def test_progression_scale(self):
        self.assertEqual(self.p.root, Note('D4'))
        self.assertEqual(self.p.scale, Major('D4'))
        self.assertEqual(self.p.scale_cls, Major)

    def test_Progression_to_str(self):
        self.assertEqual(str(Progression('D4')), 'D4')

    def test_Progression_to_repr(self):
        self.assertEqual(repr(Progression('D4')), "Progression('D4')")

    def test_Progression_to_repr_with_scale_cls(self):
        p = Progression('D4', scale_cls=Minor)
        self.assertEqual(repr(p), "Progression('D4', scale_cls=Minor)")

    def test_Progression_call(self):
        out = self.p('ii')
        expected = Chord('Em')
        self.assertEquals(out, expected)

    def test_standard_triads(self):
        out = self.p.standard_triads()
        expected = {'I': Chord('DM'),
                    'ii': Chord('Em'),
                    'iii': Chord('F#m'),
                    'IV': Chord('GM'),
                    'V': Chord('AM'),
                    'vi': Chord('Bm'),
                    'vii': Chord('C#dim')}
        self.assertEquals(out, expected)

    def test_standard_sevenths(self):
        out = self.p.standard_sevenths()
        expected = {'I7': Chord('DM7'),
                    'ii7': Chord('Em7'),
                    'iii7': Chord('F#m7'),
                    'IV7': Chord('GM7'),
                    'V7': Chord('AM7'),
                    'vi7': Chord('Bm7'),
                    'vii7': Chord('C#dim7')}
        self.assertEquals(out, expected)

    def test_all_progressions(self):
        out = self.p.all_progressions()
        expected = {'I': Chord('DM'),
                    'I7': Chord('DM7'),
                    'II': Chord('EM'),
                    'II7': Chord('EM7'),
                    'III': Chord('F#M'),
                    'III7': Chord('F#M7'),
                    'IV': Chord('GM'),
                    'IV7': Chord('GM7'),
                    'V': Chord('AM'),
                    'V7': Chord('AM7'),
                    'VI': Chord('BM'),
                    'VI7': Chord('BM7'),
                    'VII': Chord('C#dim'),
                    'VII7': Chord('C#dim7'),
                    'i': Chord('Dm'),
                    'i7': Chord('Dm7'),
                    'ii': Chord('Em'),
                    'ii7': Chord('Em7'),
                    'iii': Chord('F#m'),
                    'iii7': Chord('F#m7'),
                    'iv': Chord('Gm'),
                    'iv7': Chord('Gm7'),
                    'v': Chord('Am'),
                    'v7': Chord('Am7'),
                    'vi': Chord('Bm'),
                    'vi7': Chord('Bm7'),
                    'vii': Chord('C#dim'),
                    'vii7': Chord('C#dim7')}
        self.assertEquals(out, expected)

    def test_from_string(self):
        out = self.p.from_string('ii')
        expected = Chord('Em')
        self.assertEquals(out, expected)

    def test_from_string_raises(self):
        with self.assertRaises(Exception):
            self.p.from_string('+viii')

    def test_from_string_flat(self):
        out = self.p.from_string('bii')
        expected = Chord('Ebm')
        self.assertEquals(out, expected)

    def test_from_list(self):
        prog_list = ['ii7', 'V7', 'iii7', 'vi7']
        out = self.p.from_list(prog_list)
        expected = [Chord('Em7'), Chord('AM7'), Chord('F#m7'), Chord('Bm7')]
        self.assertEquals(out, expected)
