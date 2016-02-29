import unittest

from parker.notes import Note
from parker.scales import Aeolian
from parker.scales import Chromatic
from parker.scales import Dominant
from parker.scales import Dorian
from parker.scales import Ionian
from parker.scales import Locrian
from parker.scales import Lydian
from parker.scales import Major
from parker.scales import MajorBlues
from parker.scales import MajorPentatonic
from parker.scales import Minor
from parker.scales import MinorBlues
from parker.scales import MinorPentatonic
from parker.scales import Mixolydian
from parker.scales import Phrygian
from parker.scales import Scale
from parker.scales import diatonic_interval


class TestInterval(unittest.TestCase):

    def test_diatonic_interval_raises(self):
        with self.assertRaises(Exception):
            diatonic_interval(0)
        with self.assertRaises(Exception):
            diatonic_interval(8)

    def test_diatonic_interval_tonic_I(self):
        out = diatonic_interval(1)
        expected = [0, 2, 4, 5, 7, 9, 11]
        self.assertEqual(out, expected)

    def test_diatonic_interval_tonic_II(self):
        out = diatonic_interval(2)
        expected = [0, 2, 3, 5, 7, 9, 10]
        self.assertEqual(out, expected)

    def test_diatonic_interval_tonic_III(self):
        out = diatonic_interval(3)
        expected = [0, 1, 3, 5, 7, 8, 10]
        self.assertEqual(out, expected)

    def test_diatonic_interval_tonic_IV(self):
        out = diatonic_interval(4)
        expected = [0, 2, 4, 6, 7, 9, 11]
        self.assertEqual(out, expected)

    def test_diatonic_interval_tonic_V(self):
        out = diatonic_interval(5)
        expected = [0, 2, 4, 5, 7, 9, 10]
        self.assertEqual(out, expected)

    def test_diatonic_interval_tonic_VI(self):
        out = diatonic_interval(6)
        expected = [0, 2, 3, 5, 7, 8, 10]
        self.assertEqual(out, expected)

    def test_diatonic_interval_tonic_VII(self):
        out = diatonic_interval(7)
        expected = [0, 1, 3, 5, 6, 8, 10]
        self.assertEqual(out, expected)


class TestScale(unittest.TestCase):

    def _scale_tester(self, scale, notes_in_scale):
        notes = [str(s) for s in scale.notes]
        self.assertEqual(notes, notes_in_scale)
        for s in notes_in_scale:
            msg = "Note {} should be part of the scale {}".format(s, notes)
            self.assertTrue(Note(s) in scale, msg)
        self.assertEqual(len(scale), len(notes_in_scale))

    def test_constructor(self):
        scale = Scale('C4')
        in_scale = ['C4']
        self._scale_tester(scale, in_scale)

    def test_constructor_order_raises(self):
        with self.assertRaises(Exception):
            Scale('C4', order='not_an_order')

    def test_Scale_to_str(self):
        self.assertEqual(str(Scale('C4')), 'C4')

    def test_Scale_to_repr(self):
        self.assertEqual(repr(Scale('C4')), "Scale('C4')")

    def test_Ionian_on_C4(self):
        scale = Ionian('C4')
        in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Ionian('C4')")

    def test_Ionian_on_C4_descending(self):
        scale = Ionian('C4', order='descending')
        in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
        in_scale.reverse()
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

    def test_Minor_on_A4(self):
        scale = Minor(Note('A4'))
        in_scale = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Minor('A4')")

    def test_Major_equals_Minor(self):
        def compare_major_minor(major_root, minor_root):
            major = Major(major_root)
            minor = Minor(minor_root)
            major_notes = [n.get_note_without_octave() for n in major]
            minor_notes = [n.get_note_without_octave() for n in minor]
            major_notes.sort()
            minor_notes.sort()
            self.assertEqual(major_notes, minor_notes)
        compare_major_minor('C', 'A')
        compare_major_minor('G', 'E')
        compare_major_minor('D', 'B')
        compare_major_minor('A', 'F#')
        compare_major_minor('E', 'C#')
        compare_major_minor('B', 'G#')
        compare_major_minor('F#', 'D#')
        compare_major_minor('Gb', 'Eb')
        compare_major_minor('Db', 'Bb')
        compare_major_minor('Ab', 'F')
        compare_major_minor('Eb', 'C')
        compare_major_minor('Bb', 'G')
        compare_major_minor('F', 'D')

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
