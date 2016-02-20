import unittest

from parker.notes import Note


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

    def test_clone(self):
        note = Note('C4')
        self.assertNotEqual(id(note), id(note.clone()))
        self.assertEqual(note, note.clone())

    def test_get_octave(self):
        self.assertEqual(Note('C4').get_octave(), 4)
        self.assertEqual(Note('B4').get_octave(), 4)
        self.assertEqual(Note('Cb5').get_octave(), 5)

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

    def test_transpose_up_no_accidentals_C4(self):
        self.assertEqual(Note('C4').minor_second_up(), Note('Db4'))
        self.assertEqual(Note('C4').major_second_up(), Note('D4'))
        self.assertEqual(Note('C4').minor_third_up(), Note('Eb4'))
        self.assertEqual(Note('C4').major_third_up(), Note('E4'))
        self.assertEqual(Note('C4').major_fourth_up(), Note('F4'))
        self.assertEqual(Note('C4').minor_fifth_up(), Note('Gb4'))
        self.assertEqual(Note('C4').major_fifth_up(), Note('G4'))
        self.assertEqual(Note('C4').minor_sixth_up(), Note('Ab4'))
        self.assertEqual(Note('C4').major_sixth_up(), Note('A4'))
        self.assertEqual(Note('C4').minor_seventh_up(), Note('Bb4'))
        self.assertEqual(Note('C4').major_seventh_up(), Note('B4'))
        self.assertEqual(Note('C4').octave_up(), Note('C5'))

    def test_transpose_up_no_accidentals_G4(self):
        self.assertEqual(Note('G4').minor_second_up(), Note('Ab4'))
        self.assertEqual(Note('G4').major_second_up(), Note('A4'))
        self.assertEqual(Note('G4').minor_third_up(), Note('Bb4'))
        self.assertEqual(Note('G4').major_third_up(), Note('B4'))
        self.assertEqual(Note('G4').major_fourth_up(), Note('C5'))
        self.assertEqual(Note('G4').minor_fifth_up(), Note('Db5'))
        self.assertEqual(Note('G4').major_fifth_up(), Note('D5'))
        self.assertEqual(Note('G4').minor_sixth_up(), Note('Eb5'))
        self.assertEqual(Note('G4').major_sixth_up(), Note('E5'))
        self.assertEqual(Note('G4').minor_seventh_up(), Note('F5'))
        self.assertEqual(Note('G4').major_seventh_up(), Note('F#5'))
        self.assertEqual(Note('G4').octave_up(), Note('G5'))

    def test_transpose_up_no_accidentals_F4(self):
        self.assertEqual(Note('F4').minor_second_up(), Note('Gb4'))
        self.assertEqual(Note('F4').major_second_up(), Note('G4'))
        self.assertEqual(Note('F4').minor_third_up(), Note('Ab4'))
        self.assertEqual(Note('F4').major_third_up(), Note('A4'))
        self.assertEqual(Note('F4').major_fourth_up(), Note('Bb4'))
        self.assertEqual(Note('Bb4').minor_fifth_up(), Note('Fb5'))
        self.assertEqual(Note('F4').minor_fifth_up(), Note('Cb4'))
        self.assertEqual(Note('F4').major_fifth_up(), Note('C5'))
        self.assertEqual(Note('F4').minor_sixth_up(), Note('Db5'))
        self.assertEqual(Note('F4').major_sixth_up(), Note('D5'))
        self.assertEqual(Note('F4').minor_seventh_up(), Note('Eb5'))
        self.assertEqual(Note('F4').major_seventh_up(), Note('E5'))
        self.assertEqual(Note('F4').octave_up(), Note('F5'))

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
