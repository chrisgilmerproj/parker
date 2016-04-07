import unittest

from parker.chords import Chord
from parker.progressions import Progression
from parker.scales import Major


class TestProgressions(unittest.TestCase):

    def setUp(self):
        self.p = Progression('D')

    def test_progression_scale(self):
        self.assertEqual(self.p.scale, Major('D4'))

    def test_all_progressions(self):
        out = self.p.all_progressions()
        expected = {'I': Chord('DM'),
                    'I7': Chord('DM7'),
                    'II': Chord('Em'),
                    'II7': Chord('Em7'),
                    'III': Chord('F#m'),
                    'III7': Chord('F#m7'),
                    'IV': Chord('GM'),
                    'IV7': Chord('GM7'),
                    'V': Chord('AM'),
                    'V7': Chord('AM7'),
                    'VI': Chord('Bm'),
                    'VI7': Chord('Bm7'),
                    'VII': Chord('C#dim'),
                    'VII7': Chord('C#dim7')}
        self.assertEquals(out, expected)
