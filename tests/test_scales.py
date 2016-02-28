import unittest

from parker.notes import Note
from parker.scales import Scale


NOTES_SET = set(['C4', 'C#4', 'Db4', 'D4', 'D#4',
                 'Eb4', 'E4', 'E#4', 'Fb4', 'F#4',
                 'Gb4', 'G4', 'G#4', 'Ab4', 'A4',
                 'A#4', 'Bb4', 'B4', 'B#4', 'Cb5',
                 'C5'])


class TestScale(unittest.TestCase):

    def _scale_tester(self, scale, notes_in_scale):
        for s in notes_in_scale:
            self.assertTrue(Note(s) in scale,
                            "Note %s should be part of this scale" % s)
        for s in NOTES_SET - set(notes_in_scale):
            self.assertTrue(Note(s) not in scale,
                            "Note %s should not be part of this scale" % s)

    def test_constructor(self):
        scale = Scale('C4')
        in_scale = ['C4']
        self._scale_tester(scale, in_scale)

    def test_Scale_to_str(self):
        self.assertEqual(str(Scale('C4')), 'C4')

    def test_Scale_to_repr(self):
        self.assertEqual(repr(Scale('C4')), "Scale('C4')")
