import unittest

from parker.chords import Chord
from parker.progressions import Progression
from parker.scales import Major


class TestProgressions(unittest.TestCase):

    def setUp(self):
        self.p = Progression('D')

    def test_progression_scale(self):
        self.assertEqual(self.p.scale, Major('D4'))

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
