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
        self.root = 'D'
        self.p = Progression(self.root)

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
        expected = {'I7': Chord('D7'),
                    'ii7': Chord('Em7'),
                    'iii7': Chord('F#m7'),
                    'IV7': Chord('G7'),
                    'V7': Chord('A7'),
                    'vi7': Chord('Bm7'),
                    'vii7': Chord('C#m7')}
        self.assertEquals(out, expected)

    def test_all_progressions(self):
        out = self.p.all_progressions()
        expected = {'I': Chord('DM'),
                    'I7': Chord('D7'),
                    'II': Chord('EM'),
                    'II7': Chord('E7'),
                    'III': Chord('F#M'),
                    'III7': Chord('F#7'),
                    'IV': Chord('GM'),
                    'IV7': Chord('G7'),
                    'V': Chord('AM'),
                    'V7': Chord('A7'),
                    'VI': Chord('BM'),
                    'VI7': Chord('B7'),
                    'VII': Chord('C#dim'),
                    'VII7': Chord('C#7'),
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
                    'vii7': Chord('C#m7')}
        self.assertEquals(out, expected)

    def test_from_string(self):
        out = self.p.from_string('ii')
        expected = Chord('Em')
        self.assertEquals(out, expected)

    def test_from_string_raises(self):
        self.assertRaises(Exception, self.p.from_string, '+viii')

    def test_from_string_flat(self):
        out = self.p.from_string('bii')
        expected = Chord('Ebm')
        self.assertEquals(out, expected)

    def test_from_string_sharp(self):
        out = self.p.from_string('#ii')
        expected = Chord('Fm')
        self.assertEquals(out, expected)

    def test_from_list(self):
        prog_list = ['ii7', 'V7', 'iii7', 'VI7']
        out = self.p.from_list(prog_list)
        expected = [Chord('Em7'), Chord('A7'), Chord('F#m7'), Chord('B7')]
        self.assertEquals(out, expected)

    def test_satin_doll(self):
        PROGRESSIONS = [(1, ['ii7', 'V7', 'iii7', 'VI7'],
                            ['Em7', 'A7', 'F#m7', 'B7']),
                        (1, ['II7', 'bII7', 'IM7', 'IV7', 'iii7', 'VI7'],
                            ['E7', 'Eb7', 'DM7', 'G7', 'F#m7', 'B7']),
                        (1, ['ii7', 'V7', 'iii7', 'VI7'],
                            ['Em7', 'A7', 'F#m7', 'B7']),
                        (1, ['II7', 'bII7', 'IM7', 'IM7'],
                            ['E7', 'Eb7', 'DM7', 'DM7']),
                        (4, ['ii7', 'V7', 'IM7', 'IM7'],
                            ['Am7', 'D7', 'GM7', 'GM7']),
                        (5, ['ii7', 'V7', 'v7', 'I7'],
                            ['Bm7', 'E7', 'Em7', 'A7']),
                        (1, ['ii7', 'V7', 'iii7', 'VI7'],
                            ['Em7', 'A7', 'F#m7', 'B7']),
                        (1, ['II7', 'bII7', 'IM7', 'IV7', 'iii7', 'VI7'],
                            ['E7', 'Eb7', 'DM7', 'G7', 'F#m7', 'B7']),
                        ]
        song_key = Major(self.root)
        for scale_int, phrase, expected in PROGRESSIONS:
            scale = song_key.notes[scale_int - 1]
            p = Progression(scale)
            chord_list = p.from_list(phrase)
            out = [str(ch) for ch in chord_list]
            self.assertEquals(out, expected)
