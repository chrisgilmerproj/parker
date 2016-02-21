import unittest

from parker.chords import Chord
from parker.chords import produce_all_chords
from parker.notes import Note


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

    def test_constructor_raises_with_no_input(self):
        with self.assertRaises(Exception):
            Chord()

    def test_constructor_raises_with_bad_chord(self):
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

    def test_transpose_chord(self):
        chord = Chord('C4')
        self.assertEqual(chord.notes, [Note('C4'),
                                       Note('E4'),
                                       Note('G4')])
        self.assertEqual(chord.extension, 'M')
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

        new_chord = chord.transpose(5)
        self.assertEqual(new_chord.notes, [Note('F4'),
                                           Note('A4'),
                                           Note('C5')])
        self.assertEqual(new_chord.extension, 'M')
        self._chord_tester(new_chord, ['F4', 'A4', 'C5'])


class TestAllChords(unittest.TestCase):

    def setUp(self):
        self.chord_info = produce_all_chords('C4')

    def test_produce_all_chords(self):
        expected = {'dominant_flat_ninth': Chord('C47b9'), 'minor_sixth': Chord('C4m6'), 'suspended_fourth_ninth': Chord('C4sus4b9'), 'major_ninth': Chord('C4M9'), 'eleventh': Chord('C411'), 'suspended_seventh': Chord('C4sus47'), 'minor_major_seventh': Chord('C4m/M7'), 'minor_seventh_flat_five': Chord('C4m7b5'), 'augmented_major_seventh': Chord('C4M7+'), 'major_sixth': Chord('C4M6'), 'suspended_triad': Chord('C4sus'), 'hendrix_chord': Chord('C47b12'), 'dominant_sharp_ninth': Chord('C47#9'), 'minor_seventh': Chord('C4m7'), 'major_seventh': Chord('C4M7'), 'sixth_ninth': Chord('C469'), 'suspended_fourth_triad': Chord('C4sus4'), 'major_thirteenth': Chord('C4M13'), 'diminished_triad': Chord('C4dim'), 'dominant_ninth': Chord('C49'), 'dominant_thirteenth': Chord('C413'), 'half_diminished_seventh': Chord('C4m7b5'), 'dominant_seventh': Chord('C4dom7'), 'dominant_flat_five': Chord('C47b5'), 'minor_thirteenth': Chord('C4m13'), 'augmented_triad': Chord('C4aug'), 'augmented_minor_seventh': Chord('C4m7+'), 'minor_triad': Chord('C4m'), 'suspended_second_triad': Chord('C4sus2'), 'minor_ninth': Chord('C4m9'), 'dominant_sixth': Chord('C467'), 'minor_eleventh': Chord('C4m11'), 'diminished_seventh': Chord('C4dim7'), 'lydian_dominant_seventh': Chord('C47#11'), 'major_triad': Chord('C4M')}
        self.assertEqual(self.chord_info, expected)
