import unittest

from parker.notes import Note
from parker.scales import Aeolian
from parker.scales import Chromatic
from parker.scales import Diatonic
from parker.scales import Dominant
from parker.scales import Dorian
from parker.scales import Ionian
from parker.scales import Locrian
from parker.scales import Lydian
from parker.scales import Major
from parker.scales import MajorBlues
from parker.scales import MajorPentatonic
from parker.scales import MinorBlues
from parker.scales import MinorPentatonic
from parker.scales import Mixolydian
from parker.scales import NaturalMinor
from parker.scales import Phrygian
from parker.scales import Scale


class TestScale(unittest.TestCase):

    def _scale_tester(self, scale, notes_in_scale):
        notes = [str(s) for s in scale.get_notes()]
        for s in notes_in_scale:
            msg = "Note {} should be part of the scale {}".format(s, notes)
            self.assertTrue(Note(s) in scale, msg)
        self.assertEqual(len(scale), len(notes_in_scale))

    def test_constructor(self):
        scale = Scale('C4')
        in_scale = ['C4']
        self._scale_tester(scale, in_scale)

    def test_Scale_to_str(self):
        self.assertEqual(str(Scale('C4')), 'C4')

    def test_Scale_to_repr(self):
        self.assertEqual(repr(Scale('C4')), "Scale('C4')")

    def test_Diatonic_on_C4(self):
        scale = Diatonic('C4')
        in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Diatonic('C4')")

    def test_Ionian_on_C4(self):
        scale = Ionian('C4')
        in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Ionian('C4')")

    def test_Major_on_C4(self):
        scale = Major('C4')
        in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Major('C4')")

    def test_Dorian_on_C4(self):
        scale = Dorian(Note('C4'))
        in_scale = ['C4', 'D4', 'Eb4', 'F4', 'G4', 'A4', 'Bb4']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Dorian('C4')")

    def test_Phrygian_on_E4(self):
        scale = Phrygian(Note('E4'))
        in_scale = ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Phrygian('E4')")

    def test_Lydian_on_F4(self):
        scale = Lydian(Note('F4'))
        in_scale = ['F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Lydian('F4')")

    def test_Mixolydian_on_G4(self):
        scale = Mixolydian(Note('G4'))
        in_scale = ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Mixolydian('G4')")

    def test_Dominant_on_G4(self):
        scale = Dominant(Note('G4'))
        in_scale = ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Dominant('G4')")

    def test_Aeolian_on_A4(self):
        scale = Aeolian(Note('A4'))
        in_scale = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Aeolian('A4')")

    def test_NaturalMinor_on_A4(self):
        scale = NaturalMinor(Note('A4'))
        in_scale = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "NaturalMinor('A4')")

    def test_Locrian_on_B4(self):
        scale = Locrian(Note('B4'))
        in_scale = ['B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Locrian('B4')")

    def test_Chromatic_on_C4(self):
        scale = Chromatic(Note('C4'))
        in_scale = ['C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4',
                    'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Chromatic('C4')")

    def test_MajorPentatonic_on_C4(self):
        scale = MajorPentatonic(Note('C4'))
        in_scale = ['C4', 'D4', 'E4', 'G4', 'A4']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "MajorPentatonic('C4')")

    def test_MinorPentatonic_on_C4(self):
        scale = MinorPentatonic(Note('C4'))
        in_scale = ['C4', 'Eb4', 'F4', 'G4', 'Bb4']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "MinorPentatonic('C4')")

    def test_MajorBlues_on_C4(self):
        scale = MajorBlues(Note('C4'))
        in_scale = ['C4', 'D4', 'Eb4', 'E4', 'G4', 'A4']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "MajorBlues('C4')")

    def test_MinorBlues_on_C4(self):
        scale = MinorBlues(Note('C4'))
        in_scale = ['C4', 'Eb4', 'F4', 'F#4', 'G4', 'Bb4']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "MinorBlues('C4')")
