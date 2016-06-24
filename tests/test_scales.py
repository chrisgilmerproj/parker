import unittest

from parker.mixins import Aug
from parker.mixins import Dim
from parker.notes import Note
from parker.scales import Aeolian
from parker.scales import Altered
from parker.scales import Chromatic
from parker.scales import Diatonic
from parker.scales import DiminishedWholeTone
from parker.scales import Dominant
from parker.scales import Dorian
from parker.scales import HalfWholeDiminished
from parker.scales import HarmonicMajor
from parker.scales import HarmonicMinor
from parker.scales import Ionian
from parker.scales import Locrian
from parker.scales import Lydian
from parker.scales import Major
from parker.scales import MajorBlues
from parker.scales import MajorPentatonic
from parker.scales import MedievalLydian
from parker.scales import MelodicMinor
from parker.scales import Minor
from parker.scales import MinorBlues
from parker.scales import MinorPentatonic
from parker.scales import Mixolydian
from parker.scales import NaturalMinor
from parker.scales import Octatonic
from parker.scales import OctatonicModeOne
from parker.scales import OctatonicModeTwo
from parker.scales import Phrygian
from parker.scales import PhrygianDominant
from parker.scales import Scale
from parker.scales import SuperLocrian
from parker.scales import WholeHalfDiminished
from parker.scales import _scale_creator
from parker.scales import circle_of_fifths
from parker.scales import circle_of_fourths
from parker.scales import dorian_scales
from parker.scales import major_blues_scales
from parker.scales import major_pentatonic_scales
from parker.scales import major_scales
from parker.scales import minor_blues_scales
from parker.scales import minor_pentatonic_scales
from parker.scales import minor_scales
from parker.scales import mixolydian_scales


class TestScales(unittest.TestCase):

    def test_Scale_equality(self):
        self.assertTrue(Dorian('D') == Major('C'))
        self.assertTrue(Dorian('D') == Dorian('D'))
        self.assertFalse(Dorian('D') == Note('D'))
        self.assertFalse(Dorian('D') == Dorian('F'))


class TestDiatonicInterval(unittest.TestCase):

    def setUp(self):
        self.scale = Diatonic('C')

    def test_Diatonic_generate_interval_raises(self):
        self.assertRaises(Exception, self.scale._generate_intervals, 0)
        self.assertRaises(Exception, self.scale._generate_intervals, 8)

    def test_Diatonic_generate_interval_tonic_I(self):
        out = self.scale._generate_intervals(1)
        expected = [0, 2, 4, 5, 7, 9, 11, 12]
        self.assertEqual(out, expected)

    def test_Diatonic_generate_interval_tonic_II(self):
        out = self.scale._generate_intervals(2)
        expected = [0, 2, 3, 5, 7, 9, 10, 12]
        self.assertEqual(out, expected)

    def test_Diatonic_generate_interval_tonic_III(self):
        out = self.scale._generate_intervals(3)
        expected = [0, 1, 3, 5, 7, 8, 10, 12]
        self.assertEqual(out, expected)

    def test_Diatonic_generate_interval_tonic_IV(self):
        out = self.scale._generate_intervals(4)
        expected = [0, 2, 4, 6, 7, 9, 11, 12]
        self.assertEqual(out, expected)

    def test_Diatonic_generate_interval_tonic_IV_aug_3(self):
        out = self.scale._generate_intervals(4, aug_dim_cls=[(3, Aug)])
        expected = [0, 2, 4, Aug(5), 7, 9, 11, 12]
        self.assertEqual(out, expected)

    def test_Diatonic_generate_interval_tonic_IV_dim_3(self):
        out = self.scale._generate_intervals(4, aug_dim_cls=[(3, Dim)])
        expected = [0, 2, 4, Dim(7), 7, 9, 11, 12]
        self.assertEqual(out, expected)

    def test_Diatonic_generate_interval_tonic_IV_aug_dim_raises(self):
        self.assertRaises(Exception, self.scale._generate_intervals,
                          4, aug_dim_cls=[(3, Note)])

    def test_Diatonic_generate_interval_tonic_V(self):
        out = self.scale._generate_intervals(5)
        expected = [0, 2, 4, 5, 7, 9, 10, 12]
        self.assertEqual(out, expected)

    def test_Diatonic_generate_interval_tonic_VI(self):
        out = self.scale._generate_intervals(6)
        expected = [0, 2, 3, 5, 7, 8, 10, 12]
        self.assertEqual(out, expected)

    def test_Diatonic_generate_interval_tonic_VII(self):
        out = self.scale._generate_intervals(7)
        expected = [0, 1, 3, 5, 6, 8, 10, 12]
        self.assertEqual(out, expected)


class TestScaleBase(unittest.TestCase):

    def _scale_tester(self, scale, notes_in_scale):
        notes = [str(s) for s in scale.notes]
        self.assertEqual(notes, notes_in_scale)
        for s in notes_in_scale:
            msg = "Note {0} should be part of the scale {1}".format(s, notes)
            self.assertTrue(Note(s) in scale, msg)
        self.assertEqual(len(scale), len(notes_in_scale))


class TestScale(TestScaleBase):

    def test_constructor(self):
        scale = Scale('C4')
        in_scale = ['C4']
        self._scale_tester(scale, in_scale)

    def test_constructor_order_raises(self):
        self.assertRaises(Exception, Scale, 'C4', order='not_an_order')

    def test_Scale_to_str(self):
        self.assertEqual(str(Scale('C4')), 'C4')

    def test_Scale_to_repr(self):
        self.assertEqual(repr(Scale('C4')), "Scale('C4')")

    def test_whole_half_construction(self):
        scale = Major('C4')
        out = scale.get_whole_half_construction()
        expected = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
        self.assertEquals(out, expected)

    def test_whole_half_construction_len_one(self):
        scale = Scale('C4')
        out = scale.get_whole_half_construction()
        expected = []
        self.assertEquals(out, expected)

    def test_whole_half_construction_major_blues(self):
        scale = MajorBlues('C4')
        out = scale.get_whole_half_construction()
        expected = ['W', 'H', 'H', 3, 'W']
        self.assertEquals(out, expected)

    def test_whole_half_construction_minor_blues(self):
        scale = MinorBlues('C4')
        out = scale.get_whole_half_construction()
        expected = [3, 'W', 'H', 'H', 3]
        self.assertEquals(out, expected)

    def test_tone_semitone_construction(self):
        scale = Major('C4')
        out = scale.get_tone_semitone_construction()
        expected = ['T', 'T', 's', 'T', 'T', 'T', 's']
        self.assertEquals(out, expected)

    def test_tone_semitone_construction_major_blues(self):
        scale = MajorBlues('C4')
        out = scale.get_tone_semitone_construction()
        expected = ['T', 's', 's', 3, 'T']
        self.assertEquals(out, expected)

    def test_tone_semitone_construction_minor_blues(self):
        scale = MinorBlues('C4')
        out = scale.get_tone_semitone_construction()
        expected = [3, 'T', 's', 's', 3]
        self.assertEquals(out, expected)

    def test_is_generic_note_in_scale(self):
        scale = Major('C4')
        self.assertTrue(scale.is_generic_note_in_scale('C'))
        self.assertTrue(scale.is_generic_note_in_scale(Note('C4')))
        self.assertTrue(scale.is_generic_note_in_scale(Note('C6')))
        self.assertTrue(scale.is_generic_note_in_scale(Note('G7')))


class TestDiatonicScale(TestScaleBase):

    def test_Ionian_on_C4(self):
        scale = Ionian('C4')
        in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Ionian('C4')")

    def test_Ionian_on_C4_descending(self):
        scale = Ionian('C4', order='descending')
        in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
        in_scale.reverse()
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Ionian('C4', order='descending')")

    def test_Major_on_C4(self):
        scale = Major('C4')
        in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Major('C4')")

    def test_HarmonicMajor_on_C4(self):
        scale = HarmonicMajor('C4')
        in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'Bb4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "HarmonicMajor('C4')")

    def test_Dorian_on_C4(self):
        scale = Dorian(Note('C4'))
        in_scale = ['C4', 'D4', 'Eb4', 'F4', 'G4', 'A4', 'Bb4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Dorian('C4')")

    def test_Phrygian_on_E4(self):
        scale = Phrygian(Note('E4'))
        in_scale = ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Phrygian('E4')")

    def test_PhrygianDominant_on_E4(self):
        scale = PhrygianDominant(Note('E4'))
        in_scale = ['E4', 'F4', 'G#4', 'A4', 'B4', 'C5', 'D5', 'E5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "PhrygianDominant('E4')")

    def test_MedievalLydian_on_F4(self):
        scale = MedievalLydian(Note('F4'))
        in_scale = ['F4', 'G4', 'A4', 'Cb5', 'C5', 'D5', 'E5', 'F5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "MedievalLydian('F4')")

    def test_Lydian_on_F4(self):
        scale = Lydian(Note('F4'))
        in_scale = ['F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Lydian('F4')")

    def test_Mixolydian_on_G4(self):
        scale = Mixolydian(Note('G4'))
        in_scale = ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Mixolydian('G4')")

    def test_Dominant_on_G4(self):
        scale = Dominant(Note('G4'))
        in_scale = ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Dominant('G4')")

    def test_Aeolian_on_A4(self):
        scale = Aeolian(Note('A4'))
        in_scale = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Aeolian('A4')")

    def test_Minor_on_A4(self):
        scale = Minor(Note('A4'))
        in_scale = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Minor('A4')")

    def test_NaturalMinor_on_A4(self):
        scale = NaturalMinor(Note('A4'))
        in_scale = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "NaturalMinor('A4')")

    def test_HarmonicMinor_on_A4(self):
        scale = HarmonicMinor(Note('A4'))
        in_scale = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G#5', 'A5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "HarmonicMinor('A4')")

    def test_MelodicMinor_on_A4(self):
        scale = MelodicMinor(Note('A4'))
        in_scale = ['A4', 'B4', 'C5', 'D5', 'E5', 'F#5', 'G#5', 'A5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "MelodicMinor('A4')")

    def test_Major_equals_Minor(self):
        def compare_major_minor(major_root, minor_root):
            major = Major(major_root)
            minor = Minor(minor_root)
            self.assertEqual(major, minor)
            self.assertEqual(major.minor_third_down(), minor)
            self.assertEqual(minor.minor_third_up(), major)
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
        in_scale = ['B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Locrian('B4')")

    def test_SuperLocrian_on_B4(self):
        scale = SuperLocrian(Note('C4'))
        in_scale = ['C4', 'Db4', 'Eb4', 'E4', 'Gb4', 'Ab4', 'Bb4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "SuperLocrian('C4')")

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


class TestChromaticScale(TestScaleBase):

    def test_Chromatic_on_C4(self):
        scale = Chromatic(Note('C4'))
        in_scale = ['C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4',
                    'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Chromatic('C4')")


class TestAlteredInterval(unittest.TestCase):

    def setUp(self):
        self.scale = Altered('C')

    def test_Altered_generate_interval_raises(self):
        self.assertRaises(Exception, self.scale._generate_intervals, 0)
        self.assertRaises(Exception, self.scale._generate_intervals, 8)

    def test_Altered_generate_interval_mode_one(self):
        out = self.scale._generate_intervals(1)
        expected = [0, 1, 3, 4, 6, 8, 10, 12]
        self.assertEqual(out, expected)


class TestAlteredScale(TestScaleBase):

    def test_Altered_on_C4(self):
        scale = Altered(Note('C4'))
        in_scale = ['C4', 'Db4', 'Eb4', 'E4', 'Gb4', 'Ab4', 'Bb4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "Altered('C4')")

    def test_Altered_is_SuperLocrian(self):
        self.assertEqual(Altered('C4'), SuperLocrian('C4'))


class TestOctatonicInterval(unittest.TestCase):

    def setUp(self):
        self.scale = Octatonic('C')

    def test_Octatonic_generate_interval_raises(self):
        self.assertRaises(Exception, self.scale._generate_intervals, 0)
        self.assertRaises(Exception, self.scale._generate_intervals, 3)

    def test_Octatonic_generate_interval_mode_one(self):
        out = self.scale._generate_intervals(1)
        expected = [0, 1, 3, 4, 6, 7, 9, 10, 12]
        self.assertEqual(out, expected)

    def test_Octatonic_generate_interval_mode_two(self):
        out = self.scale._generate_intervals(2)
        expected = [0, 2, 3, 5, 6, 8, 9, 11, 12]
        self.assertEqual(out, expected)


class TestOctatonicScale(TestScaleBase):

    def test_OctatonicModeOne_on_C4(self):
        scale = OctatonicModeOne(Note('C4'))
        in_scale = ['C4', 'Db4', 'Eb4', 'E4', 'Gb4', 'G4', 'A4', 'Bb4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "OctatonicModeOne('C4')")

    def test_HalfWholeDiminished_on_C4(self):
        scale = HalfWholeDiminished(Note('C4'))
        in_scale = ['C4', 'Db4', 'Eb4', 'E4', 'Gb4', 'G4', 'A4', 'Bb4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "HalfWholeDiminished('C4')")

    def test_OctatonicModeOne_is_symmetric(self):
        def compare_symmetric_with_mode_one(scale1_root, scale2_root):
            scale1 = OctatonicModeOne(scale1_root)
            scale2 = OctatonicModeOne(scale2_root)
            self.assertEqual(scale1, scale2)

        def compare_symmetric_with_mode_two(scale1_root, scale2_root):
            scale1 = OctatonicModeOne(scale1_root)
            scale2 = OctatonicModeTwo(scale2_root)
            self.assertEqual(scale1, scale2)
        compare_symmetric_with_mode_two('C4', 'Db4')
        compare_symmetric_with_mode_one('C4', 'Eb4')
        compare_symmetric_with_mode_two('C4', 'E4')
        compare_symmetric_with_mode_one('C4', 'Gb4')
        compare_symmetric_with_mode_two('C4', 'G4')
        compare_symmetric_with_mode_one('C4', 'A4')
        compare_symmetric_with_mode_two('C4', 'Bb4')
        compare_symmetric_with_mode_one('C4', 'C5')

    def test_OctatonicModeTwo_on_C4(self):
        scale = OctatonicModeTwo(Note('C4'))
        in_scale = ['C4', 'D4', 'Eb4', 'F4', 'Gb4', 'Ab4', 'A4', 'B4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "OctatonicModeTwo('C4')")

    def test_WholeHalfDiminished_on_C4(self):
        scale = WholeHalfDiminished(Note('C4'))
        in_scale = ['C4', 'D4', 'Eb4', 'F4', 'Gb4', 'Ab4', 'A4', 'B4', 'C5']
        self._scale_tester(scale, in_scale)
        self.assertEqual(repr(scale), "WholeHalfDiminished('C4')")

    def test_OctatonicModeTwo_is_symmetric(self):
        def compare_symmetric_with_mode_two(scale1_root, scale2_root):
            scale1 = OctatonicModeTwo(scale1_root)
            scale2 = OctatonicModeTwo(scale2_root)
            self.assertEqual(scale1, scale2)

        def compare_symmetric_with_mode_one(scale1_root, scale2_root):
            scale1 = OctatonicModeTwo(scale1_root)
            scale2 = OctatonicModeOne(scale2_root)
            self.assertEqual(scale1, scale2)
        compare_symmetric_with_mode_one('C4', 'D4')
        compare_symmetric_with_mode_two('C4', 'Eb4')
        compare_symmetric_with_mode_one('C4', 'F4')
        compare_symmetric_with_mode_two('C4', 'Gb4')
        compare_symmetric_with_mode_one('C4', 'Ab4')
        compare_symmetric_with_mode_two('C4', 'A4')
        compare_symmetric_with_mode_one('C4', 'B4')
        compare_symmetric_with_mode_two('C4', 'C5')


class TestCircles(unittest.TestCase):

    def test_circle_of_fifths(self):
        out = circle_of_fifths()
        expected = [Major('C4'),
                    Major('G4'),
                    Major('D4'),
                    Major('A4'),
                    Major('E4'),
                    Major('B4'),
                    Major('F#4'),
                    Major('C#4')]
        self.assertEqual(out, expected)

    def test_circle_of_fourths(self):
        out = circle_of_fourths()
        expected = [Major('C4'),
                    Major('F4'),
                    Major('Bb4'),
                    Major('Eb4'),
                    Major('Ab4'),
                    Major('Db4'),
                    Major('Gb4'),
                    Major('Cb4')]
        self.assertEqual(out, expected)


class TestScaleHelpers(unittest.TestCase):

    def test_scale_creator(self):
        out = _scale_creator(Major)
        expected = [Major('C4'),
                    Major('Db4'),
                    Major('D4'),
                    Major('Eb4'),
                    Major('E4'),
                    Major('F4'),
                    Major('Gb4'),
                    Major('G4'),
                    Major('Ab4'),
                    Major('A4'),
                    Major('Bb4'),
                    Major('B4')]
        self.assertEqual(out, expected)

    def test_dorian_scales(self):
        out = dorian_scales()
        expected = [Dorian('C4'),
                    Dorian('Db4'),
                    Dorian('D4'),
                    Dorian('Eb4'),
                    Dorian('E4'),
                    Dorian('F4'),
                    Dorian('Gb4'),
                    Dorian('G4'),
                    Dorian('Ab4'),
                    Dorian('A4'),
                    Dorian('Bb4'),
                    Dorian('B4')]
        self.assertEqual(out, expected)

    def test_mixolydian_scales(self):
        out = mixolydian_scales()
        expected = [Mixolydian('C4'),
                    Mixolydian('Db4'),
                    Mixolydian('D4'),
                    Mixolydian('Eb4'),
                    Mixolydian('E4'),
                    Mixolydian('F4'),
                    Mixolydian('Gb4'),
                    Mixolydian('G4'),
                    Mixolydian('Ab4'),
                    Mixolydian('A4'),
                    Mixolydian('Bb4'),
                    Mixolydian('B4')]
        self.assertEqual(out, expected)

    def test_major_scales(self):
        out = major_scales()
        expected = [Major('C4'),
                    Major('Db4'),
                    Major('D4'),
                    Major('Eb4'),
                    Major('E4'),
                    Major('F4'),
                    Major('Gb4'),
                    Major('G4'),
                    Major('Ab4'),
                    Major('A4'),
                    Major('Bb4'),
                    Major('B4')]
        self.assertEqual(out, expected)

    def test_minor_scales(self):
        out = minor_scales(root='A4')
        expected = [Minor('A4'),
                    Minor('Bb4'),
                    Minor('B4'),
                    Minor('C5'),
                    Minor('C#5'),
                    Minor('D5'),
                    Minor('Eb5'),
                    Minor('E5'),
                    Minor('F5'),
                    Minor('F#5'),
                    Minor('G5'),
                    Minor('G#5')]
        self.assertEqual(out, expected)

    def test_major_equals_minor(self):
        for major, minor in zip(major_scales(), minor_scales(root='A4')):
            self.assertEqual(major, minor)

    def test_major_pentatonic_scales(self):
        out = major_pentatonic_scales()
        expected = [MajorPentatonic('C4'),
                    MajorPentatonic('Db4'),
                    MajorPentatonic('D4'),
                    MajorPentatonic('Eb4'),
                    MajorPentatonic('E4'),
                    MajorPentatonic('F4'),
                    MajorPentatonic('Gb4'),
                    MajorPentatonic('G4'),
                    MajorPentatonic('Ab4'),
                    MajorPentatonic('A4'),
                    MajorPentatonic('Bb4'),
                    MajorPentatonic('B4')]
        self.assertEqual(out, expected)

    def test_minor_pentatonic_scales(self):
        out = minor_pentatonic_scales()
        expected = [MinorPentatonic('C4'),
                    MinorPentatonic('Db4'),
                    MinorPentatonic('D4'),
                    MinorPentatonic('Eb4'),
                    MinorPentatonic('E4'),
                    MinorPentatonic('F4'),
                    MinorPentatonic('Gb4'),
                    MinorPentatonic('G4'),
                    MinorPentatonic('Ab4'),
                    MinorPentatonic('A4'),
                    MinorPentatonic('Bb4'),
                    MinorPentatonic('B4')]
        self.assertEqual(out, expected)

    def test_major_blues_scales(self):
        out = major_blues_scales()
        expected = [MajorBlues('C4'),
                    MajorBlues('Db4'),
                    MajorBlues('D4'),
                    MajorBlues('Eb4'),
                    MajorBlues('E4'),
                    MajorBlues('F4'),
                    MajorBlues('Gb4'),
                    MajorBlues('G4'),
                    MajorBlues('Ab4'),
                    MajorBlues('A4'),
                    MajorBlues('Bb4'),
                    MajorBlues('B4')]
        self.assertEqual(out, expected)

    def test_minor_blues_scales(self):
        out = minor_blues_scales()
        expected = [MinorBlues('C4'),
                    MinorBlues('Db4'),
                    MinorBlues('D4'),
                    MinorBlues('Eb4'),
                    MinorBlues('E4'),
                    MinorBlues('F4'),
                    MinorBlues('Gb4'),
                    MinorBlues('G4'),
                    MinorBlues('Ab4'),
                    MinorBlues('A4'),
                    MinorBlues('Bb4'),
                    MinorBlues('B4')]
        self.assertEqual(out, expected)


class TestSongScales(unittest.TestCase):

    def test_blue_bossa(self):
        self.assertEqual(Dorian('D'), Major('C'))
        self.assertEqual(Dorian('G'), Major('F'))
        self.assertEqual(Locrian('E'), Major('F'))
        self.assertEqual(DiminishedWholeTone('A'), SuperLocrian('A'))
        self.assertEqual(Dorian('F'), Major('Eb'))
        self.assertEqual(Mixolydian('Bb'), Major('Eb'))

    def test_canteloupe_island(self):
        self.assertEqual(Dorian('G'), Major('F'))
        self.assertEqual(Lydian('Eb').generic_notes,
                         set(['D#', 'F', 'G', 'A', 'A#', 'C', 'D']))
        self.assertEqual(Dorian('E'), Major('D'))

    def test_freddie_freeloader(self):
        self.assertEqual(Mixolydian('C'), Major('F'))
        self.assertEqual(Mixolydian('F'), Major('Bb'))
        self.assertEqual(Mixolydian('G'), Major('C'))
        self.assertEqual(Mixolydian('Bb'), Major('Eb'))

    def test_so_what_scales(self):
        self.assertEqual(Dorian('E'), Major('D'))
        self.assertEqual(Dorian('F'), Major('Eb'))
