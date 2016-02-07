import unittest

from parker.notes import Note


class TestNote(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

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

#    def test_Note_transpose(self):
#        n = Note('C4')
#        assert_that(n.perfect_fourth_up(), equal_to(Note('F4')))
#        assert_that(n.perfect_fourth_down(), equal_to(Note('G3')))
#        assert_that(n, equal_to(Note('C4')))
#    
#        n = Note('C#4')
#        assert_that(n.perfect_fourth_up(), equal_to(Note('F#4')))
#        assert_that(n.perfect_fourth_down(), equal_to(Note('G#3')))
#    
#        n = Note('C##4')
#        assert_that(n.perfect_fourth_up(), equal_to(Note('F##4')))
#        assert_that(n.perfect_fourth_down(), equal_to(Note('G##3')))
#    
#        n = Note('C###4')
#        assert_that(n.perfect_fourth_up(), equal_to(Note('F###4')))
#        assert_that(n.perfect_fourth_down(), equal_to(Note('G###3')))
#    
#        n = Note('Cb4')
#        assert_that(n.perfect_fourth_up(), equal_to(Note('Fb4')))
#        assert_that(n.perfect_fourth_down(), equal_to(Note('Gb3')))
#    
#        n = Note('Cbb4')
#        assert_that(n.perfect_fourth_up(), equal_to(Note('Fbb4')))
#        assert_that(n.perfect_fourth_down(), equal_to(Note('Gbb3')))
#    
#        n = Note('Cbbb4')
#        assert_that(n.perfect_fourth_up(), equal_to(Note('Fbbb4')))
#        assert_that(n.perfect_fourth_down(), equal_to(Note('Gbbb3')))
#    
#    def test_Note_transpose_up_no_accidentals():
#        assert_that(Note('C4').minor_second_up(), equal_to(Note('Db4')))
#        assert_that(Note('C4').major_second_up(), equal_to(Note('D4')))
#        assert_that(Note('C4').minor_third_up(), equal_to(Note('Eb4')))
#        assert_that(Note('C4').major_third_up(), equal_to(Note('E4')))
#        assert_that(Note('C4').major_fourth_up(), equal_to(Note('F4')))
#        assert_that(Note('C4').minor_fifth_up(), equal_to(Note('Gb4')))
#        assert_that(Note('C4').major_fifth_up(), equal_to(Note('G4')))
#        assert_that(Note('C4').minor_sixth_up(), equal_to(Note('Ab4')))
#        assert_that(Note('C4').major_sixth_up(), equal_to(Note('A4')))
#        assert_that(Note('C4').minor_seventh_up(), equal_to(Note('Bb4')))
#        assert_that(Note('C4').major_seventh_up(), equal_to(Note('B4')))
#        assert_that(Note('C4').octave_up(), equal_to(Note('C5')))
#    
#    def test_Note_transpose_up_no_accidentals():
#        assert_that(Note('G4').minor_second_up(), equal_to(Note('Ab4')))
#        assert_that(Note('G4').major_second_up(), equal_to(Note('A4')))
#        assert_that(Note('G4').minor_third_up(), equal_to(Note('Bb4')))
#        assert_that(Note('G4').major_third_up(), equal_to(Note('B4')))
#        assert_that(Note('G4').major_fourth_up(), equal_to(Note('C5')))
#        assert_that(Note('G4').minor_fifth_up(), equal_to(Note('Db5')))
#        assert_that(Note('G4').major_fifth_up(), equal_to(Note('D5')))
#        assert_that(Note('G4').minor_sixth_up(), equal_to(Note('Eb5')))
#        assert_that(Note('G4').major_sixth_up(), equal_to(Note('E5')))
#        assert_that(Note('G4').minor_seventh_up(), equal_to(Note('F5')))
#        assert_that(Note('G4').major_seventh_up(), equal_to(Note('F#5')))
#        assert_that(Note('G4').octave_up(), equal_to(Note('G5')))
#    
#    def test_Note_transpose_up_no_accidentals():
#        assert_that(Note('F4').minor_second_up(), equal_to(Note('Gb4')))
#        assert_that(Note('F4').major_second_up(), equal_to(Note('G4')))
#        assert_that(Note('F4').minor_third_up(), equal_to(Note('Ab4')))
#        assert_that(Note('F4').major_third_up(), equal_to(Note('A4')))
#        assert_that(Note('F4').major_fourth_up(), equal_to(Note('Bb4')))
#        assert_that(Note('Bb4').minor_fifth_up(), equal_to(Note('Fb5')))
#        assert_that(Note('F4').minor_fifth_up(), equal_to(Note('Cb4')))
#        assert_that(Note('F4').major_fifth_up(), equal_to(Note('C5')))
#        assert_that(Note('F4').minor_sixth_up(), equal_to(Note('Db5')))
#        assert_that(Note('F4').major_sixth_up(), equal_to(Note('D5')))
#        assert_that(Note('F4').minor_seventh_up(), equal_to(Note('Eb5')))
#        assert_that(Note('F4').major_seventh_up(), equal_to(Note('E5')))
#        assert_that(Note('F4').octave_up(), equal_to(Note('F5')))
#    
#    def test_Note_transpose_up_sharp():
#        assert_that(Note('C#4').minor_second_up(), equal_to(Note('Db#4')))
#        assert_that(Note('C#4').major_second_up(), equal_to(Note('D#4')))
#        assert_that(Note('C#4').minor_third_up(), equal_to(Note('Eb#4')))
#        assert_that(Note('C#4').major_third_up(), equal_to(Note('E#4')))
#        assert_that(Note('C#4').major_fourth_up(), equal_to(Note('F#4')))
#        assert_that(Note('C#4').minor_fifth_up(), equal_to(Note('Gb#4')))
#        assert_that(Note('C#4').major_fifth_up(), equal_to(Note('G#4')))
#        assert_that(Note('C#4').minor_sixth_up(), equal_to(Note('Ab#4')))
#        assert_that(Note('C#4').major_sixth_up(), equal_to(Note('A#4')))
#        assert_that(Note('C#4').minor_seventh_up(), equal_to(Note('Bb#4')))
#        assert_that(Note('C#4').major_seventh_up(), equal_to(Note('B#4')))
#        assert_that(Note('C#4').octave_up(), equal_to(Note('C#5')))
#    
#    def test_Note_transpose_up_flat():
#        assert_that(Note('Cb4').minor_second_up(), equal_to(Note('Dbb4')))
#        assert_that(Note('Cb4').major_second_up(), equal_to(Note('Db4')))
#        assert_that(Note('Cb4').minor_third_up(), equal_to(Note('Ebb4')))
#        assert_that(Note('Cb4').major_third_up(), equal_to(Note('Eb4')))
#        assert_that(Note('Cb4').major_fourth_up(), equal_to(Note('Fb4')))
#        assert_that(Note('Cb4').minor_fifth_up(), equal_to(Note('Gbb4')))
#        assert_that(Note('Cb4').major_fifth_up(), equal_to(Note('Gb4')))
#        assert_that(Note('Cb4').minor_sixth_up(), equal_to(Note('Abb4')))
#        assert_that(Note('Cb4').major_sixth_up(), equal_to(Note('Ab4')))
#        assert_that(Note('Cb4').minor_seventh_up(), equal_to(Note('Bbb4')))
#        assert_that(Note('Cb4').major_seventh_up(), equal_to(Note('Bb4')))
#        assert_that(Note('Cb4').octave_up(), equal_to(Note('Cb5')))
#    
#    def test_Note_transpose_by_int():
#        assert_that(Note('C4').transpose(0), equal_to(Note('C4')))
#        assert_that(Note('C4').transpose(1), equal_to(Note('Db4')))
#        assert_that(Note('C4').transpose(2), equal_to(Note('D4')))
#        assert_that(Note('C4').transpose(3), equal_to(Note('Eb4')))
#        assert_that(Note('C4').transpose(4), equal_to(Note('E4')))
#        assert_that(Note('C4').transpose(5), equal_to(Note('F4')))
#        assert_that(Note('C4').transpose(6), equal_to(Note('Gb4')))
#        assert_that(Note('C4').transpose(7), equal_to(Note('G4')))
#        assert_that(Note('C4').transpose(8), equal_to(Note('Ab4')))
#        assert_that(Note('C4').transpose(9), equal_to(Note('A4')))
#        assert_that(Note('C4').transpose(10), equal_to(Note('Bb4')))
#        assert_that(Note('C4').transpose(11), equal_to(Note('B4')))
#        assert_that(Note('C4').transpose(12), equal_to(Note('C5')))
#    
#    def test_Note_set_transpose():
#        n = Note(60)
#        assert_that(n.set_transpose(5), equal_to(Note(65)))
#        assert_that(n.set_transpose(-10), equal_to(Note(55)))
#        assert_that(n, equal_to(Note(55)))
