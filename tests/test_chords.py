import unittest

from parker.chords import Chord
from parker.notes import Note
from parker.notes import NoteGroup


class TestChord(unittest.TestCase):

    def _chord_tester(self, chord, notes):
        self.assertEqual(len(chord), len(notes))
        for ix, note in enumerate(notes):
            self.assertEqual(chord[ix], Note(note),
                    msg="Note {} of {} doesn't match.\n{} != {}\nGiv: {}\nExp: {}".format(
                                 ix, str(chord), chord[ix], note, [str(n) for n in chord.notes], notes))

    def test_constructor(self):
        chord = Chord('C4')
        self.assertEqual(chord.notes, [Note('C4'),
                                       Note('E4'),
                                       Note('G4')])
        self.assertEqual(chord.extension, 'M')
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

    def test_constructor_from_shorthand(self):
        self._chord_tester(Chord('Cmaj7'), ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chord('C4maj7'), ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chord('CM7'), ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chord('Cm7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('Cmin7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('Cmi7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('C-7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('C3-7'), ['C3', 'Eb3', 'G3', 'Bb3'])

    def test_constructor_raises(self):
        with self.assertRaises(Exception):
            Chord('_C4%G6')

    def test_Chord_to_str(self):
        self.assertEqual(str(Chord('Cmaj7')), 'C4M7')

    def test_Chord_to_repr(self):
        self.assertEqual(repr(Chord('Cmaj7')), "Chord('C4M7')")
        self.assertEqual(repr(Chord('C4maj7')), "Chord('C4M7')")
        self.assertEqual(repr(Chord('CM7')), "Chord('C4M7')")
        self.assertEqual(repr(Chord('Cm7')), "Chord('C4m7')")
        self.assertEqual(repr(Chord('Cmin7')), "Chord('C4m7')")
        self.assertEqual(repr(Chord('Cmi7')), "Chord('C4m7')")
        self.assertEqual(repr(Chord('C-7')), "Chord('C4m7')")
        self.assertEqual(repr(Chord('C3-7')), "Chord('C3m7')")

    def test_get_shorthand_raises(self):
        with self.assertRaises(Exception):
            Chord._get_shorthand('fail')

    def test_major_triad(self):
        chord = Chord.major_triad('C4')
        self.assertEqual(str(chord), 'C4M')
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

    def test_major_triad_on_Note(self):
        chord = Chord.major_triad(Note('C4'))
        self.assertEqual(str(chord), 'C4M')
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

    def test_major_triad_on_int(self):
        chord = Chord.major_triad(60)
        self.assertEqual(str(chord), 'C4M')
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

    def test_minor_triad(self):
        chord = Chord.minor_triad('C4')
        self.assertEqual(str(chord), 'C4m')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4'])

    def test_diminished_triad(self):
        chord = Chord.diminished_triad('C4')
        self.assertEqual(str(chord), 'C4dim')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4'])

    def test_augmented_triad(self):
        chord = Chord.augmented_triad('C4')
        self.assertEqual(str(chord), 'C4aug')
        self._chord_tester(chord, ['C4', 'E4', 'G#4'])

    def test_augmented_minor_seventh(self):
        chord = Chord.augmented_minor_seventh('C4')
        self.assertEqual(str(chord), 'C4m7+')
        self._chord_tester(chord, ['C4', 'E4', 'G#4', 'Bb4'])

    def test_augmented_major_seventh(self):
        chord = Chord.augmented_major_seventh('C4')
        self.assertEqual(str(chord), 'C4M7+')
        self._chord_tester(chord, ['C4', 'E4', 'G#4', 'B4'])

    def test_suspended_triad(self):
        chord = Chord.suspended_triad('C4')
        self.assertEqual(str(chord), 'C4sus')
        self._chord_tester(chord, ['C4', 'F4', 'G4'])

    def test_suspended_fourth_triad(self):
        chord = Chord.suspended_fourth_triad('C4')
        self.assertEqual(str(chord), 'C4sus4')
        self._chord_tester(chord, ['C4', 'F4', 'G4'])

    def test_suspended_second_triad(self):
        chord = Chord.suspended_second_triad('C4')
        self.assertEqual(str(chord), 'C4sus2')
        self._chord_tester(chord, ['C4', 'D4', 'G4'])

    def test_suspended_seventh(self):
        chord = Chord.suspended_seventh('C4')
        self.assertEqual(str(chord), 'C4sus47')
        self._chord_tester(chord, ['C4', 'F4', 'G4', 'Bb4'])

    def test_suspended_fourth_ninth(self):
        chord = Chord.suspended_fourth_ninth('C4')
        self.assertEqual(str(chord), 'C4sus4b9')
        self._chord_tester(chord, ['C4', 'F4', 'G4', 'Db5'])

    def test_eleventh(self):
        chord = Chord.eleventh('C4')
        self.assertEqual(str(chord), 'C411')
        self._chord_tester(chord, ['C4', 'G4', 'Bb4', 'F5'])

    def test_minor_eleventh(self):
        chord = Chord.minor_eleventh('C4')
        self.assertEqual(str(chord), 'C4m11')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'F5'])

    def test_lydian_dominant_seventh(self):
        chord = Chord.lydian_dominant_seventh('C4')
        self.assertEqual(str(chord), 'C47#11')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'F#5'])

    def test_minor_thirteenth(self):
        chord = Chord.minor_thirteenth('C4')
        self.assertEqual(str(chord), 'C4m13')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'D5', 'A5'])

    def test_major_thirteenth(self):
        chord = Chord.major_thirteenth('C4')
        self.assertEqual(str(chord), 'C4M13')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'B4', 'D5', 'A5'])

    def test_dominant_thirteenth(self):
        chord = Chord.dominant_thirteenth('C4')
        self.assertEqual(str(chord), 'C413')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D5', 'A5'])

    def test_major_seventh(self):
        chord = Chord.major_seventh('C4')
        self.assertEqual(str(chord), 'C4M7')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'B4'])

    def test_minor_seventh(self):
        chord = Chord.minor_seventh('C4')
        self.assertEqual(str(chord), 'C4m7')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4'])

    def test_dominant_seventh(self):
        chord = Chord.dominant_seventh('C4')
        self.assertEqual(str(chord), 'C4dom7')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4'])

    def test_diminished_seventh(self):
        chord = Chord.diminished_seventh('C4')
        self.assertEqual(str(chord), 'C4dim7')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bbb4'])

    def test_half_diminished_seventh(self):
        chord = Chord.half_diminished_seventh('C4')
        self.assertEqual(str(chord), 'C4m7b5')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bb4'])

    def test_minor_seventh_flat_five(self):
        chord = Chord.minor_seventh_flat_five('C4')
        self.assertEqual(str(chord), 'C4m7b5')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bb4'])

    def test_minor_major_seventh(self):
        chord = Chord.minor_major_seventh('C4')
        self.assertEqual(str(chord), 'C4m/M7')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'B4'])

    def test_minor_sixth(self):
        chord = Chord.minor_sixth('C4')
        self.assertEqual(str(chord), 'C4m6')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Ab4'])

    def test_major_sixth(self):
        chord = Chord.major_sixth('C4')
        self.assertEqual(str(chord), 'C4M6')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4'])

    def test_dominant_sixth(self):
        chord = Chord.dominant_sixth('C4')
        self.assertEqual(str(chord), 'C467')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4', 'Bb4'])

    def test_sixth_ninth(self):
        chord = Chord.sixth_ninth('C4')
        self.assertEqual(str(chord), 'C469')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4', 'D5'])

    def test_minor_ninth(self):
        chord = Chord.minor_ninth('C4')
        self.assertEqual(str(chord), 'C4m9')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'D5'])

    def test_major_ninth(self):
        chord = Chord.major_ninth('C4')
        self.assertEqual(str(chord), 'C4M9')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'B4', 'D5'])

    def test_dominant_ninth(self):
        chord = Chord.dominant_ninth('C4')
        self.assertEqual(str(chord), 'C49')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D5'])

    def test_dominant_flat_ninth(self):
        chord = Chord.dominant_flat_ninth('C4')
        self.assertEqual(str(chord), 'C47b9')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'Db5'])

    def test_dominant_sharp_ninth(self):
        chord = Chord.dominant_sharp_ninth('C4')
        self.assertEqual(str(chord), 'C47#9')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D#5'])

    def test_dominant_flat_five(self):
        chord = Chord.dominant_flat_five('C4')
        self.assertEqual(str(chord), 'C47b5')
        self._chord_tester(chord, ['C4', 'E4', 'Gb4', 'Bb4'])

    def test_hendrix_chord(self):
        chord = Chord.hendrix_chord('C4')
        self.assertEqual(str(chord), 'C47b12')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'Eb5'])
