import unittest

from parker.chords import Chords
from parker.notes import Note


class TestChords(unittest.TestCase):

    def _chord_tester(self, chord, notes):
        self.assertEqual(len(chord), len(notes))
        for ix, note in enumerate(notes):
            self.assertEqual(chord[ix], Note(note))
                # "Note %d of %s should be %s" % (ix, str(chord), note))

    def test_Chord_major_triad(self):
        chord = Chords.major_triad('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

    def test_Chord_major_triad_on_Note(self):
        chord = Chords.major_triad(Note('C4'))
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

    def test_Chord_major_triad_on_int(self):
        chord = Chords.major_triad(60)
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

    def test_Chord_minor_triad(self):
        chord = Chords.minor_triad('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4'])

    def test_Chord_diminished_triad(self):
        chord = Chords.diminished_triad('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4'])

    def test_Chord_augmented_triad(self):
        chord = Chords.augmented_triad('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G#4'])

    def test_Chord_augmented_minor_seventh(self):
        chord = Chords.augmented_minor_seventh('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G#4', 'Bb4'])

    def test_Chord_augmented_major_seventh(self):
        chord = Chords.augmented_major_seventh('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G#4', 'B4'])

    def test_Chord_suspended_triad(self):
        chord = Chords.suspended_triad('C4')
        self._chord_tester(chord, ['C4', 'F4', 'G4'])

    def test_Chord_suspended_fourth_triad(self):
        chord = Chords.suspended_fourth_triad('C4')
        self._chord_tester(chord, ['C4', 'F4', 'G4'])

    def test_Chord_suspended_second_triad(self):
        chord = Chords.suspended_second_triad('C4')
        self._chord_tester(chord, ['C4', 'D4', 'G4'])

    def test_Chord_suspended_seventh(self):
        chord = Chords.suspended_seventh('C4')
        self._chord_tester(chord, ['C4', 'F4', 'G4', 'Bb4'])

    def test_Chord_suspended_fourth_ninth(self):
        chord = Chords.suspended_fourth_ninth('C4')
        self._chord_tester(chord, ['C4', 'F4', 'G4', 'Db5'])

    def test_Chord_eleventh(self):
        chord = Chords.eleventh('C4')
        self._chord_tester(chord, ['C4', 'G4', 'Bb4', 'F5'])

    def test_Chord_minor_eleventh(self):
        chord = Chords.minor_eleventh('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'F5'])

    def test_Chord_lydian_dominant_seventh(self):
        chord = Chords.lydian_dominant_seventh('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'F#5'])

    def test_Chord_minor_thirteenth(self):
        chord = Chords.minor_thirteenth('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'D5', 'A5'])

    def test_Chord_major_thirteenth(self):
        chord = Chords.major_thirteenth('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'B4', 'D5', 'A5'])

    def test_Chord_dominant_thirteenth(self):
        chord = Chords.dominant_thirteenth('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D5', 'A5'])

    def test_Chord_major_seventh(self):
        chord = Chords.major_seventh('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'B4'])

    def test_Chord_minor_seventh(self):
        chord = Chords.minor_seventh('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4'])

    def test_Chord_dominant_seventh(self):
        chord = Chords.dominant_seventh('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4'])

    def test_Chord_diminished_seventh(self):
        chord = Chords.diminished_seventh('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bbb4'])

    def test_Chord_half_diminished_seventh(self):
        chord = Chords.half_diminished_seventh('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bb4'])

    def test_Chord_minor_seventh_flat_five(self):
        chord = Chords.minor_seventh_flat_five('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bb4'])

    def test_Chord_minor_major_seventh(self):
        chord = Chords.minor_major_seventh('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'B4'])

    def test_Chord_minor_sixth(self):
        chord = Chords.minor_sixth('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Ab4'])

    def test_Chord_major_sixth(self):
        chord = Chords.major_sixth('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4'])

    def test_Chord_dominant_sixth(self):
        chord = Chords.dominant_sixth('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4', 'Bb4'])

    def test_Chord_sixth_ninth(self):
        chord = Chords.sixth_ninth('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4', 'D5'])

    def test_Chord_minor_ninth(self):
        chord = Chords.minor_ninth('C4')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'D5'])

    def test_Chord_dominant_ninth(self):
        chord = Chords.dominant_ninth('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D5'])

    def test_Chord_dominant_flat_ninth(self):
        chord = Chords.dominant_flat_ninth('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'Db5'])

    def test_Chord_dominant_sharp_ninth(self):
        chord = Chords.dominant_sharp_ninth('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D#5'])

    def test_Chord_dominant_flat_five(self):
        chord = Chords.dominant_flat_five('C4')
        self._chord_tester(chord, ['C4', 'E4', 'Gb4', 'Bb4'])

    def test_Chord_hendrix_chord(self):
        chord = Chords.hendrix_chord('C4')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'Eb5'])

    def test_Chord_from_string(self):
        self._chord_tester(Chords.from_string('Cmaj7'), ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chords.from_string('C4maj7'), ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chords.from_string('CM7'), ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chords.from_string('Cm7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chords.from_string('Cmin7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chords.from_string('Cmi7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chords.from_string('C-7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chords.from_string('C3-7'), ['C3', 'Eb3', 'G3', 'Bb3'])
