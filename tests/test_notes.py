import unittest

from parker.mixins import Aug
from parker.mixins import Dim
from parker.notes import Note
from parker.notes import NoteGroup


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

    def test_constructor_from_Note(self):
        self.assertEqual(Note(Note('B9')), Note('B9'))

    def test_constructor_raises(self):
        with self.assertRaises(Exception):
            Note('H$5')

    def test_flat_sharp_difference(self):
        self.assertNotEqual(Note('Db4'), Note('C#4'))
        self.assertNotEqual(Note('Eb4'), Note('D#4'))
        self.assertNotEqual(Note('Gb4'), Note('F#4'))
        self.assertNotEqual(Note('Ab4'), Note('G#4'))
        self.assertNotEqual(Note('Bb4'), Note('A#4'))

    def test_flat_enharmonics(self):
        self.assertEqual(int(Note('Cb4')), int(Note('B3')))
        self.assertEqual(int(Note('C4')), int(Note('B#3')))
        self.assertEqual(int(Note('Db4')), int(Note('C#4')))
        self.assertEqual(int(Note('Eb4')), int(Note('D#4')))
        self.assertEqual(int(Note('Fb4')), int(Note('E4')))
        self.assertEqual(int(Note('F4')), int(Note('E#4')))
        self.assertEqual(int(Note('Gb4')), int(Note('F#4')))
        self.assertEqual(int(Note('Ab4')), int(Note('G#4')))
        self.assertEqual(int(Note('Bb4')), int(Note('A#4')))

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

    def test_clone(self):
        note = Note('C4')
        self.assertNotEqual(id(note), id(note.clone()))
        self.assertEqual(note, note.clone())

    def test_get_base_name(self):
        note = Note('C4')
        self.assertEqual(note.get_base_name(), 'C')

    def test_set_base_name(self):
        note = Note('C4')
        note.set_base_name('D')
        self.assertEqual(note.get_base_name(), 'D')
        self.assertEqual(str(note), 'D4')

    def test_set_base_name_raises(self):
        note = Note('C4')
        with self.assertRaises(Exception):
            note.set_base_name('H')

    def test_get_accidentals(self):
        note = Note('C4')
        self.assertEquals(note.get_accidentals(), 0)

    def test_get_accidentals_as_string(self):
        note = Note('Cbb4')
        self.assertEquals(note.get_accidentals(), -2)
        note = Note('C###4')
        self.assertEquals(note.get_accidentals(), 3)

    def test_set_accidentals(self):
        note = Note('C4')
        note.set_accidentals(2)
        self.assertEquals(note.get_accidentals(), 2)
        self.assertEquals(str(note), 'C##4')

    def test_get_octave(self):
        self.assertEqual(Note('C4').get_octave(), 4)
        self.assertEqual(Note('B4').get_octave(), 4)
        self.assertEqual(Note('Cb5').get_octave(), 5)

    def test_set_octave_from_int(self):
        n = Note('C4')
        self.assertEqual(n.get_octave(), 4)
        n.set_octave(3)
        self.assertEqual(n.get_octave(), 3)
        self.assertEqual(str(n), 'C3')

    def test_set_octave_from_str(self):
        n = Note('C4')
        self.assertEqual(n.get_octave(), 4)
        n.set_octave('3')
        self.assertEqual(n.get_octave(), 3)
        self.assertEqual(str(n), 'C3')

    def test_set_octave_from_bad_value(self):
        n = Note('C4')
        self.assertEqual(n.get_octave(), 4)
        with self.assertRaises(Exception):
            n.set_octave('3b')

    def test_set_octave_from_int_outside_range(self):
        n = Note('C4')
        self.assertEqual(n.get_octave(), 4)
        with self.assertRaises(Exception):
            n.set_octave(12)

    def test_get_duration(self):
        n = Note('C4')
        self.assertEqual(n.get_duration(), 0)

    def test_set_duration(self):
        n = Note('C4')
        n.set_duration(500)
        self.assertEqual(n.get_duration(), 500)

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
        n.set_transpose(Aug(4))
        self.assertEqual(int(n), 65)
        n.set_transpose(Dim(4))
        self.assertEqual(int(n), 68)
        self.assertEqual(n, Note(68))

    def test_set_transpose_raises(self):
        n = Note(60)
        with self.assertRaises(Exception):
            n.set_transpose('5')

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

    def test_notes_are_sorted(self):
        n1 = Note('G4')
        n2 = Note('C4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(ng.get_notes()[0], n2)
        self.assertEqual(ng.get_notes()[1], n1)
        self.assertEqual(ng[0], n2)
        self.assertEqual(ng[1], n1)

    def test_NoteGroup_to_str(self):
        n1 = Note('G4')
        n2 = Note('C4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(str(ng), "[Note('C4'), Note('G4')]")

    def test_NoteGroup_to_repr(self):
        n1 = Note('G4')
        n2 = Note('C4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(repr(ng), "NoteGroup([Note('C4'), Note('G4')])")

    def test_highest_lowest_notes(self):
        n1 = Note('G4')
        n2 = Note('C4')
        ng = NoteGroup([n1, n2])
        self.assertEqual(ng.lowest_note(), n2)
        self.assertEqual(ng.highest_note(), n1)
