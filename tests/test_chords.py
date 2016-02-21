import unittest

from parker.chords import Chord
from parker.notes import Note
from parker.notes import NoteGroup


class TestChord(unittest.TestCase):

    def _chord_tester(self, chord, notes):
        self.assertEqual(len(chord), len(notes))
        for ix, note in enumerate(notes):
            self.assertEqual(chord[ix], Note(note),
                             msg="Note {} of {} should be {}".format(
                                 ix, str(chord), note))

    def test_constructor(self):
        chord = Chord('C4')
        self.assertEqual(chord.note, Note('C4'))
        self.assertEqual(chord.chord, 'C4')
        self.assertEqual(chord.group, NoteGroup([Note('C4'),
                                                 Note('E4'),
                                                 Note('G4')]))
        self.assertEqual(chord.extension, '')
        self._chord_tester(chord.group, ['C4', 'E4', 'G4'])

    def test_major_triad(self):
        chord = Chord('C4')
        chord = chord.major_triad()
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

#    def test_major_triad_on_Note(self):
#        chord = Chord(Note('C4')).major_triad()
#        self._chord_tester(chord, ['C4', 'E4', 'G4'])
#
#    def test_major_triad_on_int(self):
#        chord = Chord(60).major_triad()
#        self._chord_tester(chord, ['C4', 'E4', 'G4'])

    def test_minor_triad(self):
        chord = Chord('C4').minor_triad()
        self._chord_tester(chord, ['C4', 'Eb4', 'G4'])

    def test_diminished_triad(self):
        chord = Chord('C4').diminished_triad()
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4'])

    def test_augmented_triad(self):
        chord = Chord('C4').augmented_triad()
        self._chord_tester(chord, ['C4', 'E4', 'G#4'])

    def test_augmented_minor_seventh(self):
        chord = Chord('C4').augmented_minor_seventh()
        self._chord_tester(chord, ['C4', 'E4', 'G#4', 'Bb4'])

    def test_augmented_major_seventh(self):
        chord = Chord('C4').augmented_major_seventh()
        self._chord_tester(chord, ['C4', 'E4', 'G#4', 'B4'])

    def test_suspended_triad(self):
        chord = Chord('C4').suspended_triad()
        self._chord_tester(chord, ['C4', 'F4', 'G4'])

    def test_suspended_fourth_triad(self):
        chord = Chord('C4').suspended_fourth_triad()
        self._chord_tester(chord, ['C4', 'F4', 'G4'])

    def test_suspended_second_triad(self):
        chord = Chord('C4').suspended_second_triad()
        self._chord_tester(chord, ['C4', 'D4', 'G4'])

    def test_suspended_seventh(self):
        chord = Chord('C4').suspended_seventh()
        self._chord_tester(chord, ['C4', 'F4', 'G4', 'Bb4'])

    def test_suspended_fourth_ninth(self):
        chord = Chord('C4').suspended_fourth_ninth()
        self._chord_tester(chord, ['C4', 'F4', 'G4', 'Db5'])

    def test_eleventh(self):
        chord = Chord('C4').eleventh()
        self._chord_tester(chord, ['C4', 'G4', 'Bb4', 'F5'])

    def test_minor_eleventh(self):
        chord = Chord('C4').minor_eleventh()
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'F5'])

    def test_lydian_dominant_seventh(self):
        chord = Chord('C4').lydian_dominant_seventh()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'F#5'])

    def test_minor_thirteenth(self):
        chord = Chord('C4').minor_thirteenth()
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'D5', 'A5'])

    def test_major_thirteenth(self):
        chord = Chord('C4').major_thirteenth()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'B4', 'D5', 'A5'])

    def test_dominant_thirteenth(self):
        chord = Chord('C4').dominant_thirteenth()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D5', 'A5'])

    def test_major_seventh(self):
        chord = Chord('C4').major_seventh()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'B4'])

    def test_minor_seventh(self):
        chord = Chord('C4').minor_seventh()
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4'])

    def test_dominant_seventh(self):
        chord = Chord('C4').dominant_seventh()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4'])

    def test_diminished_seventh(self):
        chord = Chord('C4').diminished_seventh()
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bbb4'])

    def test_half_diminished_seventh(self):
        chord = Chord('C4').half_diminished_seventh()
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bb4'])

    def test_minor_seventh_flat_five(self):
        chord = Chord('C4').minor_seventh_flat_five()
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bb4'])

    def test_minor_major_seventh(self):
        chord = Chord('C4').minor_major_seventh()
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'B4'])

    def test_minor_sixth(self):
        chord = Chord('C4').minor_sixth()
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Ab4'])

    def test_major_sixth(self):
        chord = Chord('C4').major_sixth()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4'])

    def test_dominant_sixth(self):
        chord = Chord('C4').dominant_sixth()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4', 'Bb4'])

    def test_sixth_ninth(self):
        chord = Chord('C4').sixth_ninth()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4', 'D5'])

    def test_minor_ninth(self):
        chord = Chord('C4').minor_ninth()
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'D5'])

    def test_dominant_ninth(self):
        chord = Chord('C4').dominant_ninth()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D5'])

    def test_dominant_flat_ninth(self):
        chord = Chord('C4').dominant_flat_ninth()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'Db5'])

    def test_dominant_sharp_ninth(self):
        chord = Chord('C4').dominant_sharp_ninth()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D#5'])

    def test_dominant_flat_five(self):
        chord = Chord('C4').dominant_flat_five()
        self._chord_tester(chord, ['C4', 'E4', 'Gb4', 'Bb4'])

    def test_hendrix_chord(self):
        chord = Chord('C4').hendrix_chord()
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'Eb5'])

    def test_from_string(self):
        self._chord_tester(Chord('Cmaj7').group, ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chord('C4maj7').group, ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chord('CM7').group, ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chord('Cm7').group, ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('Cmin7').group, ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('Cmi7').group, ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('C-7').group, ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('C3-7').group, ['C3', 'Eb3', 'G3', 'Bb3'])
