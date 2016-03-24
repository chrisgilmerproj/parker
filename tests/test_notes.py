import unittest

from parker.mixins import Aug
from parker.mixins import Dim
from parker.notes import Note
from parker.notes import NoteGroup
from parker.notes import is_valid_note
from parker.notes import note_from_frequency


class TestNoteMethods(unittest.TestCase):

    def test_is_valid_note(self):
        self.assertTrue(is_valid_note('C'))
        self.assertTrue(is_valid_note('C4'))
        self.assertTrue(is_valid_note('C#4'))
        self.assertTrue(is_valid_note('C10'))
        self.assertTrue(is_valid_note('B-1'))
        self.assertTrue(is_valid_note('Bb-53'))

    def test_is_not_valid_note(self):
        self.assertFalse(is_valid_note('c'))
        self.assertFalse(is_valid_note('H'))
        self.assertFalse(is_valid_note('C$'))
        self.assertFalse(is_valid_note('C$'))
        self.assertFalse(is_valid_note('CC'))
        self.assertFalse(is_valid_note('C#+1'))

    def test_note_from_frequency(self):
        self.assertEquals(Note('A2'), note_from_frequency(110.0))
        self.assertEquals(Note('A4'), note_from_frequency(440.0))
        self.assertEquals(Note('C5'), note_from_frequency(523.251))
        self.assertEquals(Note('B10'), note_from_frequency(31608.531))


class TestNote(unittest.TestCase):

    def test_constructor_from_int(self):
        self.assertEqual(Note(), Note(69))
        self.assertEqual(Note('C0'), Note(12))
        self.assertEqual(Note('C1'), Note(24))
        self.assertEqual(Note('C2'), Note(36))
        self.assertEqual(Note('C3'), Note(48))
        self.assertEqual(Note('C4'), Note(60))
        self.assertEqual(Note('C#4'), Note(61))
        self.assertEqual(Note('D4'), Note(62))
        self.assertEqual(Note('D#4'), Note(63))
        self.assertEqual(Note('E4'), Note(64))
        self.assertEqual(Note('F4'), Note(65))
        self.assertEqual(Note('F#4'), Note(66))
        self.assertEqual(Note('G4'), Note(67))
        self.assertEqual(Note('G#4'), Note(68))
        self.assertEqual(Note('A4'), Note(69))
        self.assertEqual(Note('A#4'), Note(70))
        self.assertEqual(Note('B4'), Note(71))
        self.assertEqual(Note('C5'), Note(72))
        self.assertEqual(Note('C6'), Note(84))
        self.assertEqual(Note('C7'), Note(96))

    def test_constructor_from_int_sharps_flats(self):
        self.assertEqual(str(Note(61, use_sharps=True)), 'C#4')
        self.assertEqual(str(Note(61, use_sharps=False)), 'Db4')

    def test_constructor_from_int_negative_octave(self):
        self.assertEqual(int(Note('B-1')), int(Note(11)))
        self.assertEqual(Note('B-1'), Note(11))

    def test_constructor_from_int_blackhole_note(self):
        self.assertEqual(int(Note('Bb-53')), int(Note(-614)))
        self.assertEqual(Note('Bb-53'), Note(-614))

    def test_constructor_from_Note(self):
        self.assertEqual(Note(Note('B9')), Note('B9'))

    def test_constructor_raises(self):
        with self.assertRaises(Exception):
            Note('H$5')

    def test_flat_sharp_enharmonics(self):
        self.assertEqual(Note('Cb4'), Note('B3'))
        self.assertEqual(Note('C4'), Note('B#3'))
        self.assertEqual(Note('Db4'), Note('C#4'))
        self.assertEqual(Note('Eb4'), Note('D#4'))
        self.assertEqual(Note('Fb4'), Note('E4'))
        self.assertEqual(Note('F4'), Note('E#4'))
        self.assertEqual(Note('Gb4'), Note('F#4'))
        self.assertEqual(Note('Ab4'), Note('G#4'))
        self.assertEqual(Note('Bb4'), Note('A#4'))

    def test_Note_to_str(self):
        self.assertEqual(str(Note()), 'A4')
        self.assertEqual(str(Note('C0')), 'C0')
        self.assertEqual(str(Note('C1')), 'C1')
        self.assertEqual(str(Note('C2')), 'C2')
        self.assertEqual(str(Note('C3')), 'C3')
        self.assertEqual(str(Note('C4')), 'C4')
        self.assertEqual(str(Note('C#4')), 'C#4')
        self.assertEqual(str(Note('D4')), 'D4')
        self.assertEqual(str(Note('D#4')), 'D#4')
        self.assertEqual(str(Note('E4')), 'E4')
        self.assertEqual(str(Note('F4')), 'F4')
        self.assertEqual(str(Note('F#4')), 'F#4')
        self.assertEqual(str(Note('G4')), 'G4')
        self.assertEqual(str(Note('G#4')), 'G#4')
        self.assertEqual(str(Note('A4')), 'A4')
        self.assertEqual(str(Note('A#4')), 'A#4')
        self.assertEqual(str(Note('B4')), 'B4')
        self.assertEqual(str(Note('C5')), 'C5')
        self.assertEqual(str(Note('C6')), 'C6')
        self.assertEqual(str(Note('C7')), 'C7')

    def test_Note_to_repr(self):
        self.assertEqual(repr(Note()), "Note('A4')")

    def test_Note_equality(self):
        self.assertFalse(Note() == NoteGroup())

    def test_Note_inequality(self):
        self.assertTrue(Note('C4') != Note('F4'))

    def test_Note_addition(self):
        self.assertEquals(Note('C5') + Note('A4'), 141)

    def test_Note_subtraction(self):
        self.assertEquals(Note('C5') - Note('A4'), 3)

    def test_clone(self):
        note = Note('C4')
        self.assertNotEqual(id(note), id(note.clone()))
        self.assertEqual(note, note.clone())

    def test_get_base_name(self):
        note = Note('C4')
        self.assertEqual(note.base_name, 'C')

    def test_set_base_name(self):
        note = Note('C4')
        note.base_name = 'D'
        self.assertEqual(note.base_name, 'D')
        self.assertEqual(str(note), 'D4')

    def test_set_base_name_raises(self):
        note = Note('C4')
        with self.assertRaises(Exception):
            note.base_name = 'H'

    def test_get_accidentals(self):
        note = Note('C4')
        self.assertEquals(note.accidentals, 0)

    def test_set_accidentals(self):
        note = Note('C4')
        note.accidentals = 2
        self.assertEquals(note.accidentals, 2)
        self.assertEquals(str(note), 'C##4')

    def test__get_accidentals_as_string(self):
        note = Note('Cbb4')
        self.assertEquals(note.accidentals, -2)
        self.assertEquals(note._get_accidentals_as_string(), 'bb')
        note = Note('C###4')
        self.assertEquals(note.accidentals, 3)
        self.assertEquals(note._get_accidentals_as_string(), '###')

    def test_get_frequency(self):
        self.assertEquals(round(Note('A2').get_frequency(), 0), 110.0)
        self.assertEquals(Note('A4').get_frequency(ndigits=3), 440.0)
        self.assertEquals(Note('C5').get_frequency(ndigits=3), 523.251)
        self.assertEquals(Note('B10').get_frequency(ndigits=3), 31608.531)

    def test_get_frequency_human_range(self):
        """
        Humans should be able to hear from about 20Hz to 20kHz.  For most
        applications C0 to C10 is valid but its more like E0 to E10.
        """
        self.assertEquals(Note('C0').get_frequency(ndigits=3), 16.352)
        self.assertEquals(Note('E0').get_frequency(ndigits=3), 20.602)
        self.assertEquals(Note('C10').get_frequency(ndigits=3), 16744.036)
        self.assertEquals(Note('E10').get_frequency(ndigits=3), 21096.164)

    def test_generalize(self):
        note = Note('C4')
        self.assertEquals(note.generalize(), 'C')
        note = Note('Cbb4')
        self.assertEquals(note.generalize(), 'Cbb')
        note = Note('C###4')
        self.assertEquals(note.generalize(), 'C###')

    def test_normalize(self):
        note = Note('C4')
        self.assertEquals(note.normalize(), 'C')
        note = Note('Cbb4')
        self.assertEquals(note.normalize(), 'Bb')
        note = Note('Cbb4')
        self.assertEquals(note.normalize(use_sharps=True), 'A#')
        note = Note('C###4')
        self.assertEquals(note.normalize(), 'D#')
        note = Note('C###4')
        self.assertEquals(note.normalize(use_sharps=False), 'Eb')

    def test_get_octave(self):
        self.assertEqual(Note('C4').octave, 4)
        self.assertEqual(Note('B4').octave, 4)
        self.assertEqual(Note('Cb5').octave, 5)

    def test_set_octave_from_int(self):
        n = Note('C4')
        self.assertEqual(n.octave, 4)
        n.octave = 3
        self.assertEqual(n.octave, 3)
        self.assertEqual(str(n), 'C3')

    def test_set_octave_from_str(self):
        n = Note('C4')
        self.assertEqual(n.octave, 4)
        n.octave = '3'
        self.assertEqual(n.octave, 3)
        self.assertEqual(str(n), 'C3')

    def test_set_octave_from_bad_value(self):
        n = Note('C4')
        self.assertEqual(n.octave, 4)
        with self.assertRaises(Exception):
            n.octave = '3b'

    def test_set_octave_from_int_outside_range(self):
        n = Note('C4')
        self.assertEqual(n.octave, 4)
        with self.assertRaises(Exception):
            n.octave = 12

    def test_transpose(self):
        n = Note('C4')
        self.assertEqual(n.perfect_fourth_up(), Note('F4'))
        self.assertEqual(n.perfect_fourth_down(), Note('G3'))
        self.assertEqual(n, Note('C4'))

        n = Note('C#4')
        self.assertEqual(n.perfect_fourth_up(), Note('F#4'))
        self.assertEqual(n.perfect_fourth_down(), Note('G#3'))

        n = Note('C##4')
        self.assertEqual(n.perfect_fourth_up(), Note('F##4'))
        self.assertEqual(n.perfect_fourth_down(), Note('G##3'))

        n = Note('C###4')
        self.assertEqual(n.perfect_fourth_up(), Note('F###4'))
        self.assertEqual(n.perfect_fourth_down(), Note('G###3'))

        n = Note('Cb4')
        self.assertEqual(n.perfect_fourth_up(), Note('Fb4'))
        self.assertEqual(n.perfect_fourth_down(), Note('Gb3'))

        n = Note('Cbb4')
        self.assertEqual(n.perfect_fourth_up(), Note('Fbb4'))
        self.assertEqual(n.perfect_fourth_down(), Note('Gbb3'))

        n = Note('Cbbb4')
        self.assertEqual(n.perfect_fourth_up(), Note('Fbbb4'))
        self.assertEqual(n.perfect_fourth_down(), Note('Gbbb3'))

    def test_transpose_up_no_accidentals_Bb4(self):
        self.assertEqual(Note('Bb4').minor_second_up(), Note('Cb5'))
        self.assertEqual(Note('Bb4').major_second_up(), Note('C5'))
        self.assertEqual(Note('Bb4').minor_third_up(), Note('Db5'))
        self.assertEqual(Note('Bb4').major_third_up(), Note('D5'))
        self.assertEqual(Note('Bb4').major_fourth_up(), Note('Eb5'))
        self.assertEqual(Note('Bb4').minor_fifth_up(), Note('Fb5'))
        self.assertEqual(Note('Bb4').major_fifth_up(), Note('F5'))
        self.assertEqual(Note('Bb4').perfect_fifth_up(), Note('F5'))
        self.assertEqual(Note('Bb4').minor_sixth_up(), Note('Gb5'))
        self.assertEqual(Note('Bb4').major_sixth_up(), Note('G5'))
        self.assertEqual(Note('Bb4').minor_seventh_up(), Note('Ab5'))
        self.assertEqual(Note('Bb4').major_seventh_up(), Note('A5'))
        self.assertEqual(Note('Bb4').octave_up(), Note('Bb5'))

    def test_transpose_up_no_accidentals_C4(self):
        self.assertEqual(Note('C4').minor_second_up(), Note('Db4'))
        self.assertEqual(Note('C4').major_second_up(), Note('D4'))
        self.assertEqual(Note('C4').minor_third_up(), Note('Eb4'))
        self.assertEqual(Note('C4').major_third_up(), Note('E4'))
        self.assertEqual(Note('C4').major_fourth_up(), Note('F4'))
        self.assertEqual(Note('C4').minor_fifth_up(), Note('Gb4'))
        self.assertEqual(Note('C4').major_fifth_up(), Note('G4'))
        self.assertEqual(Note('C4').perfect_fifth_up(), Note('G4'))
        self.assertEqual(Note('C4').minor_sixth_up(), Note('Ab4'))
        self.assertEqual(Note('C4').major_sixth_up(), Note('A4'))
        self.assertEqual(Note('C4').minor_seventh_up(), Note('Bb4'))
        self.assertEqual(Note('C4').major_seventh_up(), Note('B4'))
        self.assertEqual(Note('C4').octave_up(), Note('C5'))

    def test_transpose_up_no_accidentals_C4_compound(self):
        self.assertEqual(Note('C4').minor_ninth_up(), Note('Db5'))
        self.assertEqual(Note('C4').compound_minor_second_up(), Note('Db5'))
        self.assertEqual(Note('C4').major_ninth_up(), Note('D5'))
        self.assertEqual(Note('C4').compound_major_second_up(), Note('D5'))
        self.assertEqual(Note('C4').augmented_ninth_up(), Note('Eb5'))
        self.assertEqual(Note('C4').minor_tenth_up(), Note('Eb5'))
        self.assertEqual(Note('C4').compound_augmented_second_up(),
                         Note('Eb5'))
        self.assertEqual(Note('C4').compound_minor_third_up(), Note('Eb5'))
        self.assertEqual(Note('C4').major_tenth_up(), Note('E5'))
        self.assertEqual(Note('C4').compound_major_third_up(), Note('E5'))
        self.assertEqual(Note('C4').major_eleventh_up(), Note('F5'))
        self.assertEqual(Note('C4').compound_perfect_fourth_up(), Note('F5'))
        self.assertEqual(Note('C4').augmented_eleventh_up(), Note('Gb5'))
        self.assertEqual(Note('C4').compound_augmented_fourth_up(),
                         Note('Gb5'))
        self.assertEqual(Note('C4').minor_thirteenth_up(), Note('Ab5'))
        self.assertEqual(Note('C4').compound_minor_sixth_up(), Note('Ab5'))
        self.assertEqual(Note('C4').major_thirteenth_up(), Note('A5'))
        self.assertEqual(Note('C4').compound_major_sixth_up(), Note('A5'))

    def test_transpose_up_no_accidentals_F4(self):
        self.assertEqual(Note('F4').minor_second_up(), Note('Gb4'))
        self.assertEqual(Note('F4').major_second_up(), Note('G4'))
        self.assertEqual(Note('F4').minor_third_up(), Note('Ab4'))
        self.assertEqual(Note('F4').major_third_up(), Note('A4'))
        self.assertEqual(Note('F4').major_fourth_up(), Note('Bb4'))
        self.assertEqual(Note('F4').minor_fifth_up(), Note('Cb4'))
        self.assertEqual(Note('F4').major_fifth_up(), Note('C5'))
        self.assertEqual(Note('F4').perfect_fifth_up(), Note('C5'))
        self.assertEqual(Note('F4').minor_sixth_up(), Note('Db5'))
        self.assertEqual(Note('F4').major_sixth_up(), Note('D5'))
        self.assertEqual(Note('F4').minor_seventh_up(), Note('Eb5'))
        self.assertEqual(Note('F4').major_seventh_up(), Note('E5'))
        self.assertEqual(Note('F4').octave_up(), Note('F5'))

    def test_transpose_up_no_accidentals_G4(self):
        self.assertEqual(Note('G4').minor_second_up(), Note('Ab4'))
        self.assertEqual(Note('G4').major_second_up(), Note('A4'))
        self.assertEqual(Note('G4').minor_third_up(), Note('Bb4'))
        self.assertEqual(Note('G4').major_third_up(), Note('B4'))
        self.assertEqual(Note('G4').major_fourth_up(), Note('C5'))
        self.assertEqual(Note('G4').minor_fifth_up(), Note('Db5'))
        self.assertEqual(Note('G4').major_fifth_up(), Note('D5'))
        self.assertEqual(Note('G4').perfect_fifth_up(), Note('D5'))
        self.assertEqual(Note('G4').minor_sixth_up(), Note('Eb5'))
        self.assertEqual(Note('G4').major_sixth_up(), Note('E5'))
        self.assertEqual(Note('G4').minor_seventh_up(), Note('F5'))
        self.assertEqual(Note('G4').major_seventh_up(), Note('F#5'))
        self.assertEqual(Note('G4').octave_up(), Note('G5'))

    def test_transpose_down_no_accidentals_Bb4(self):
        self.assertEqual(Note('Bb4').minor_second_down(), Note('A4'))
        self.assertEqual(Note('Bb4').major_second_down(), Note('Ab4'))
        self.assertEqual(Note('Bb4').minor_third_down(), Note('G4'))
        self.assertEqual(Note('Bb4').major_third_down(), Note('Gb4'))
        self.assertEqual(Note('Bb4').major_fourth_down(), Note('F4'))
        self.assertEqual(Note('Bb4').minor_fifth_down(), Note('Fb4'))
        self.assertEqual(Note('Bb4').major_fifth_down(), Note('Eb4'))
        self.assertEqual(Note('Bb4').perfect_fifth_down(), Note('Eb4'))
        self.assertEqual(Note('Bb4').minor_sixth_down(), Note('D4'))
        self.assertEqual(Note('Bb4').major_sixth_down(), Note('Db4'))
        self.assertEqual(Note('Bb4').minor_seventh_down(), Note('C4'))
        self.assertEqual(Note('Bb4').major_seventh_down(), Note('Cb4'))
        self.assertEqual(Note('Bb4').octave_down(), Note('Bb3'))

    def test_transpose_down_no_accidentals_C4(self):
        self.assertEqual(Note('C4').minor_second_down(), Note('B3'))
        self.assertEqual(Note('C4').major_second_down(), Note('Bb3'))
        self.assertEqual(Note('C4').minor_third_down(), Note('A3'))
        self.assertEqual(Note('C4').major_third_down(), Note('Ab3'))
        self.assertEqual(Note('C4').major_fourth_down(), Note('G3'))
        self.assertEqual(Note('C4').minor_fifth_down(), Note('Gb3'))
        self.assertEqual(Note('C4').major_fifth_down(), Note('F3'))
        self.assertEqual(Note('C4').perfect_fifth_down(), Note('F3'))
        self.assertEqual(Note('C4').minor_sixth_down(), Note('E3'))
        self.assertEqual(Note('C4').major_sixth_down(), Note('Eb3'))
        self.assertEqual(Note('C4').minor_seventh_down(), Note('D3'))
        self.assertEqual(Note('C4').major_seventh_down(), Note('Db3'))
        self.assertEqual(Note('C4').octave_down(), Note('C3'))

    def test_transpose_down_no_accidentals_C4_compound(self):
        self.assertEqual(Note('C4').minor_ninth_down(), Note('B2'))
        self.assertEqual(Note('C4').compound_minor_second_down(), Note('B2'))
        self.assertEqual(Note('C4').major_ninth_down(), Note('Bb2'))
        self.assertEqual(Note('C4').compound_major_second_down(), Note('Bb2'))
        self.assertEqual(Note('C4').augmented_ninth_down(), Note('A2'))
        self.assertEqual(Note('C4').minor_tenth_down(), Note('A2'))
        self.assertEqual(Note('C4').compound_augmented_second_down(),
                         Note('A2'))
        self.assertEqual(Note('C4').compound_minor_third_down(), Note('A2'))
        self.assertEqual(Note('C4').major_tenth_down(), Note('Ab2'))
        self.assertEqual(Note('C4').compound_major_third_down(), Note('Ab2'))
        self.assertEqual(Note('C4').major_eleventh_down(), Note('G2'))
        self.assertEqual(Note('C4').compound_perfect_fourth_down(), Note('G2'))
        self.assertEqual(Note('C4').augmented_eleventh_down(), Note('Gb2'))
        self.assertEqual(Note('C4').compound_augmented_fourth_down(),
                         Note('Gb2'))
        self.assertEqual(Note('C4').minor_thirteenth_down(), Note('E2'))
        self.assertEqual(Note('C4').compound_minor_sixth_down(), Note('E2'))
        self.assertEqual(Note('C4').major_thirteenth_down(), Note('Eb2'))
        self.assertEqual(Note('C4').compound_major_sixth_down(), Note('Eb2'))

    def test_transpose_down_no_accidentals_F4(self):
        self.assertEqual(Note('F4').minor_second_down(), Note('E4'))
        self.assertEqual(Note('F4').major_second_down(), Note('Eb4'))
        self.assertEqual(Note('F4').minor_third_down(), Note('D4'))
        self.assertEqual(Note('F4').major_third_down(), Note('Db4'))
        self.assertEqual(Note('F4').major_fourth_down(), Note('C4'))
        self.assertEqual(Note('F4').minor_fifth_down(), Note('Cb3'))
        self.assertEqual(Note('F4').major_fifth_down(), Note('Bb3'))
        self.assertEqual(Note('F4').perfect_fifth_down(), Note('Bb3'))
        self.assertEqual(Note('F4').minor_sixth_down(), Note('A3'))
        self.assertEqual(Note('F4').major_sixth_down(), Note('Ab3'))
        self.assertEqual(Note('F4').minor_seventh_down(), Note('G3'))
        self.assertEqual(Note('F4').major_seventh_down(), Note('Gb3'))
        self.assertEqual(Note('F4').octave_down(), Note('F3'))

    def test_transpose_down_no_accidentals_G4(self):
        self.assertEqual(Note('G4').minor_second_down(), Note('F#4'))
        self.assertEqual(Note('G4').major_second_down(), Note('F4'))
        self.assertEqual(Note('G4').minor_third_down(), Note('E4'))
        self.assertEqual(Note('G4').major_third_down(), Note('Eb4'))
        self.assertEqual(Note('G4').major_fourth_down(), Note('D4'))
        self.assertEqual(Note('G4').minor_fifth_down(), Note('Db4'))
        self.assertEqual(Note('G4').major_fifth_down(), Note('C4'))
        self.assertEqual(Note('G4').perfect_fifth_down(), Note('C4'))
        self.assertEqual(Note('G4').minor_sixth_down(), Note('B3'))
        self.assertEqual(Note('G4').major_sixth_down(), Note('Bb3'))
        self.assertEqual(Note('G4').minor_seventh_down(), Note('A3'))
        self.assertEqual(Note('G4').major_seventh_down(), Note('Ab3'))
        self.assertEqual(Note('G4').octave_down(), Note('G3'))

    def test_transpose_up_sharp(self):
        self.assertEqual(Note('C#4').minor_second_up(), Note('Db#4'))
        self.assertEqual(Note('C#4').major_second_up(), Note('D#4'))
        self.assertEqual(Note('C#4').minor_third_up(), Note('Eb#4'))
        self.assertEqual(Note('C#4').major_third_up(), Note('E#4'))
        self.assertEqual(Note('C#4').major_fourth_up(), Note('F#4'))
        self.assertEqual(Note('C#4').minor_fifth_up(), Note('Gb#4'))
        self.assertEqual(Note('C#4').major_fifth_up(), Note('G#4'))
        self.assertEqual(Note('C#4').minor_sixth_up(), Note('Ab#4'))
        self.assertEqual(Note('C#4').major_sixth_up(), Note('A#4'))
        self.assertEqual(Note('C#4').minor_seventh_up(), Note('Bb#4'))
        self.assertEqual(Note('C#4').major_seventh_up(), Note('B#4'))
        self.assertEqual(Note('C#4').octave_up(), Note('C#5'))

    def test_transpose_up_flat(self):
        self.assertEqual(Note('Cb4').minor_second_up(), Note('Dbb4'))
        self.assertEqual(Note('Cb4').major_second_up(), Note('Db4'))
        self.assertEqual(Note('Cb4').minor_third_up(), Note('Ebb4'))
        self.assertEqual(Note('Cb4').major_third_up(), Note('Eb4'))
        self.assertEqual(Note('Cb4').major_fourth_up(), Note('Fb4'))
        self.assertEqual(Note('Cb4').minor_fifth_up(), Note('Gbb4'))
        self.assertEqual(Note('Cb4').major_fifth_up(), Note('Gb4'))
        self.assertEqual(Note('Cb4').minor_sixth_up(), Note('Abb4'))
        self.assertEqual(Note('Cb4').major_sixth_up(), Note('Ab4'))
        self.assertEqual(Note('Cb4').minor_seventh_up(), Note('Bbb4'))
        self.assertEqual(Note('Cb4').major_seventh_up(), Note('Bb4'))
        self.assertEqual(Note('Cb4').octave_up(), Note('Cb5'))

    def test_transpose_by_int(self):
        self.assertEqual(Note('C4').transpose(0), Note('C4'))
        self.assertEqual(Note('C4').transpose(1), Note('Db4'))
        self.assertEqual(Note('C4').transpose(2), Note('D4'))
        self.assertEqual(Note('C4').transpose(3), Note('Eb4'))
        self.assertEqual(Note('C4').transpose(4), Note('E4'))
        self.assertEqual(Note('C4').transpose(5), Note('F4'))
        self.assertEqual(Note('C4').transpose(6), Note('Gb4'))
        self.assertEqual(Note('C4').transpose(7), Note('G4'))
        self.assertEqual(Note('C4').transpose(8), Note('Ab4'))
        self.assertEqual(Note('C4').transpose(9), Note('A4'))
        self.assertEqual(Note('C4').transpose(10), Note('Bb4'))
        self.assertEqual(Note('C4').transpose(11), Note('B4'))
        self.assertEqual(Note('C4').transpose(12), Note('C5'))

    def test_set_transpose(self):
        n = Note(60)
        self.assertEqual(n.set_transpose(5), Note(65))
        self.assertEqual(n.set_transpose(-10), Note(55))
        self.assertEqual(n, Note(55))

    def test_set_transpose_Aug_and_Dim(self):
        n = Note(60)
        self.assertEqual(n.set_transpose(Aug(4)), Note(65))
        self.assertEqual(n.set_transpose(Dim(4)), Note(68))
        self.assertEqual(n, Note(68))

    def test_set_transpose_letters(self):
        n = Note(60)
        self.assertEqual(n.set_transpose('t'), Note(70))
        n = Note(60)
        self.assertEqual(n.set_transpose('A'), Note(70))
        n = Note(60)
        self.assertEqual(n.set_transpose('e'), Note(71))
        n = Note(60)
        self.assertEqual(n.set_transpose('B'), Note(71))

    def test_set_transpose_letters_raises(self):
        n = Note(60)
        with self.assertRaises(Exception):
            n.set_transpose('C')

    def test_set_transpose_raises(self):
        n = Note(60)
        with self.assertRaises(Exception):
            n.set_transpose({5})

    def test_augment(self):
        n = Note('C4')
        self.assertEqual(n._accidentals, 0)
        n2 = n.augment()
        self.assertEqual(n._accidentals, 0)
        self.assertEqual(n2._accidentals, 1)

    def test_set_augment(self):
        n = Note('C4')
        self.assertEqual(n._accidentals, 0)
        n.set_augment()
        self.assertEqual(n._accidentals, 1)

    def test_diminish(self):
        n = Note('C4')
        self.assertEqual(n._accidentals, 0)
        n2 = n.diminish()
        self.assertEqual(n._accidentals, 0)
        self.assertEqual(n2._accidentals, -1)

    def test_set_diminish(self):
        n = Note('C4')
        self.assertEqual(n._accidentals, 0)
        n.set_diminish()
        self.assertEqual(n._accidentals, -1)

    def test_all_transpositions(self):
        n = Note('C4')
        out = n.all_transpositions()
        expected = {
            'augmented_eleventh_down': Note('Gb2'),
            'augmented_eleventh_up': Note('Gb5'),
            'augmented_ninth_down': Note('A2'),
            'augmented_ninth_up': Note('Eb5'),
            'compound_augmented_fourth_down': Note('Gb2'),
            'compound_augmented_fourth_up': Note('Gb5'),
            'compound_augmented_second_down': Note('A2'),
            'compound_augmented_second_up': Note('Eb5'),
            'compound_major_second_down': Note('Bb2'),
            'compound_major_second_up': Note('D5'),
            'compound_major_sixth_down': Note('Eb2'),
            'compound_major_sixth_up': Note('A5'),
            'compound_major_third_down': Note('Ab2'),
            'compound_major_third_up': Note('E5'),
            'compound_minor_second_down': Note('B2'),
            'compound_minor_second_up': Note('Db5'),
            'compound_minor_sixth_down': Note('E2'),
            'compound_minor_sixth_up': Note('Ab5'),
            'compound_minor_third_down': Note('A2'),
            'compound_minor_third_up': Note('Eb5'),
            'compound_perfect_fourth_down': Note('G2'),
            'compound_perfect_fourth_up': Note('F5'),
            'major_eleventh_down': Note('G2'),
            'major_eleventh_up': Note('F5'),
            'major_fifth_down': Note('F3'),
            'major_fifth_up': Note('G4'),
            'major_fourth_down': Note('G3'),
            'major_fourth_up': Note('F4'),
            'major_ninth_down': Note('Bb2'),
            'major_ninth_up': Note('D5'),
            'major_second_down': Note('Bb3'),
            'major_second_up': Note('D4'),
            'major_seventh_down': Note('Db3'),
            'major_seventh_up': Note('B4'),
            'major_sixth_down': Note('Eb3'),
            'major_sixth_up': Note('A4'),
            'major_tenth_down': Note('Ab2'),
            'major_tenth_up': Note('E5'),
            'major_third_down': Note('Ab3'),
            'major_third_up': Note('E4'),
            'major_thirteenth_down': Note('Eb2'),
            'major_thirteenth_up': Note('A5'),
            'minor_fifth_down': Note('Gb3'),
            'minor_fifth_up': Note('Gb4'),
            'minor_ninth_down': Note('B2'),
            'minor_ninth_up': Note('Db5'),
            'minor_second_down': Note('B3'),
            'minor_second_up': Note('Db4'),
            'minor_seventh_down': Note('D3'),
            'minor_seventh_up': Note('Bb4'),
            'minor_sixth_down': Note('E3'),
            'minor_sixth_up': Note('Ab4'),
            'minor_tenth_down': Note('A2'),
            'minor_tenth_up': Note('Eb5'),
            'minor_third_down': Note('A3'),
            'minor_third_up': Note('Eb4'),
            'minor_thirteenth_down': Note('E2'),
            'minor_thirteenth_up': Note('Ab5'),
            'octave_down': Note('C3'),
            'octave_up': Note('C5'),
            'perfect_fifth_down': Note('F3'),
            'perfect_fifth_up': Note('G4'),
            'perfect_fourth_down': Note('G3'),
            'perfect_fourth_up': Note('F4')}
        self.assertEquals(out, expected)


class TestNoteGroup(unittest.TestCase):

    def test_constructor(self):
        ng = NoteGroup()
        self.assertEqual(ng.get_notes(), [])

    def test_constructor_from_Note(self):
        note = Note(30)
        self.assertEqual(NoteGroup(note).get_notes()[0], note)
        self.assertNotEqual(id(NoteGroup(note).get_notes()[0]), id(note))

    def test_clone(self):
        ng = NoteGroup(['C4', 'G4'])
        self.assertNotEqual(id(ng), id(ng.clone()))
        self.assertEqual(ng, ng.clone())

    def test_constructor_from_NoteGroup(self):
        n1 = Note(30)
        n2 = Note(35)
        ng = NoteGroup(NoteGroup([n1, n2]))
        self.assertEqual(ng.get_notes()[0], n1)

    def test_constructor_from_mixed_types(self):
        notes = [Note(60), 60, 'C4']
        self.assertEqual(str(NoteGroup(notes).get_notes()),
                         "[Note('C4'), Note('C4'), Note('C4')]")

    def test_constructor_raises(self):
        with self.assertRaises(Exception):
            NoteGroup({'C': 4})

    def test_add(self):
        n1 = Note('C4')
        n2 = Note('G4')
        n3 = Note('F4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(len(ng), 2)
        self.assertFalse(n3 in ng.get_notes())
        ng.add(n3)
        self.assertEqual(len(ng), 3)
        self.assertTrue(n3 in ng.get_notes())

    def test_append(self):
        n1 = Note('C4')
        n2 = Note('G4')
        n3 = Note('F4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(len(ng), 2)
        self.assertFalse(n3 in ng.get_notes())
        ng.append(n3)
        self.assertEqual(len(ng), 3)
        self.assertTrue(n3 in ng.get_notes())

    def test_transpose(self):
        n1 = Note('C4')
        n2 = Note('G4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(ng.transpose(5).get_notes()[0], Note('F4'))
        self.assertEqual(ng.perfect_fourth_up().get_notes()[0], Note('F4'))
        self.assertEqual(ng.transpose(5).get_notes()[1], Note('C5'))
        self.assertEqual(ng.transpose(-5).get_notes()[0], Note('G3'))
        self.assertEqual(ng.transpose(-5).get_notes()[1], Note('D4'))
        self.assertEqual(n1, Note('C4'))
        self.assertEqual(n2, Note('G4'))

    def test_set_transpose(self):
        ng = NoteGroup([20, 'C4'])
        self.assertEqual(ng.set_transpose(5).get_notes()[0], Note(25))
        self.assertEqual(ng.get_notes()[0], Note(25))
        self.assertEqual(ng.get_notes()[1], Note(65))

    def test_set_augment(self):
        ng = NoteGroup(['A3', 'C4'])
        ng.set_augment()
        self.assertEqual(ng.get_notes()[0], Note('A#3'))
        self.assertEqual(ng.get_notes()[1], Note('C#4'))

    def test_set_diminish(self):
        ng = NoteGroup(['A3', 'C4'])
        ng.set_diminish()
        self.assertEqual(ng.get_notes()[0], Note('Ab3'))
        self.assertEqual(ng.get_notes()[1], Note('Cb4'))

    def test_get_notes_are_sorted(self):
        n1 = Note('G4')
        n2 = Note('C4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(ng.get_notes()[0], n2)
        self.assertEqual(ng.get_notes()[1], n1)

    def test_NoteGroup_to_str(self):
        n1 = Note('G4')
        n2 = Note('C4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(str(ng), "[Note('G4'), Note('C4')]")

    def test_NoteGroup_to_repr(self):
        n1 = Note('G4')
        n2 = Note('C4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(repr(ng), "NoteGroup([Note('G4'), Note('C4')])")

    def test_highest_lowest_notes(self):
        n1 = Note('G4')
        n2 = Note('C4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(ng.lowest_note(), n2)
        self.assertEqual(ng.highest_note(), n1)
