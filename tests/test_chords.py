import unittest

from parker.chords import Chord
from parker.chords import produce_all_chords
from parker.notes import Note


class TestChord(unittest.TestCase):

    def _chord_tester(self, chord, notes):
        self.assertEqual(len(chord), len(notes))
        for ix, note in enumerate(notes):
            msg = ("Note {} of {} doesn't match.\n"
                   "{} != {}\nGiv: {}\nExp: {}".format(
                    ix, str(chord), chord[ix], note,
                    [str(n) for n in chord.notes], notes))
            self.assertEqual(chord[ix], Note(note), msg)

    def test_constructor(self):
        chord = Chord('CM')
        self.assertEqual(chord.notes, [Note('C4'),
                                       Note('E4'),
                                       Note('G4')])
        self.assertEqual(chord.extension, 'M')
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

    def test_constructor_from_shorthand(self):
        self._chord_tester(Chord('Cmaj7'), ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chord('CM7'), ['C4', 'E4', 'G4', 'B4'])
        self._chord_tester(Chord('Cm7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('Cmin7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('Cmi7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('C-7'), ['C4', 'Eb4', 'G4', 'Bb4'])
        self._chord_tester(Chord('C-7', octave=3), ['C3', 'Eb3', 'G3', 'Bb3'])

    def test_constructor_raises_with_no_input(self):
        with self.assertRaises(Exception):
            Chord()

    def test_constructor_raises_with_bad_chord(self):
        with self.assertRaises(Exception):
            Chord('_C%G6')

    def test_Chord_to_str(self):
        self.assertEqual(str(Chord('Cmaj7')), 'Cmaj7')

    def test_Chord_to_repr(self):
        self.assertEqual(repr(Chord('Cmaj7')), "Chord('Cmaj7')")
        self.assertEqual(repr(Chord('CM7')), "Chord('CM7')")
        self.assertEqual(repr(Chord('Cm7')), "Chord('Cm7')")
        self.assertEqual(repr(Chord('Cmin7')), "Chord('Cmin7')")
        self.assertEqual(repr(Chord('Cmi7')), "Chord('Cmi7')")
        self.assertEqual(repr(Chord('C-7')), "Chord('C-7')")
        self.assertEqual(repr(Chord('C-7', octave=3)),
                         "Chord('C-7', octave=3)")

    def test_get_shorthand_raises(self):
        with self.assertRaises(Exception):
            Chord._get_shorthand('fail')

    def test_major_triad(self):
        chord = Chord('CM')
        self.assertEqual(str(chord), 'CM')
        self._chord_tester(chord, ['C4', 'E4', 'G4'])

        # Alternative representations
        self.assertEqual(chord, Chord('C'))

    def test_minor_triad(self):
        chord = Chord('Cm')
        self.assertEqual(str(chord), 'Cm')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4'])

    def test_diminished_triad(self):
        chord = Chord('Cdim')
        self.assertEqual(str(chord), 'Cdim')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4'])

        # Alternative representations
        self.assertEqual(chord, Chord('Co'))

    def test_augmented_triad(self):
        chord = Chord('Caug')
        self.assertEqual(str(chord), 'Caug')
        self._chord_tester(chord, ['C4', 'E4', 'G#4'])

    def test_augmented_minor_seventh(self):
        chord = Chord('Cm7+')
        self.assertEqual(str(chord), 'Cm7+')
        self._chord_tester(chord, ['C4', 'E4', 'G#4', 'Bb4'])

    def test_augmented_major_seventh(self):
        chord = Chord('CM7+')
        self.assertEqual(str(chord), 'CM7+')
        self._chord_tester(chord, ['C4', 'E4', 'G#4', 'B4'])

    def test_suspended_fourth_triad(self):
        chord = Chord('Csus4')
        self.assertEqual(str(chord), 'Csus4')
        self._chord_tester(chord, ['C4', 'F4', 'G4'])

        # Alternative representations
        self.assertEqual(chord, Chord('Csus'))

    def test_suspended_second_triad(self):
        chord = Chord('Csus2')
        self.assertEqual(str(chord), 'Csus2')
        self._chord_tester(chord, ['C4', 'D4', 'G4'])

    def test_suspended_seventh(self):
        chord = Chord('Csus47')
        self.assertEqual(str(chord), 'Csus47')
        self._chord_tester(chord, ['C4', 'F4', 'G4', 'Bb4'])

    def test_suspended_fourth_ninth(self):
        chord = Chord('Csus4b9')
        self.assertEqual(str(chord), 'Csus4b9')
        self._chord_tester(chord, ['C4', 'F4', 'G4', 'Db5'])

    def test_eleventh(self):
        chord = Chord('C11')
        self.assertEqual(str(chord), 'C11')
        self._chord_tester(chord, ['C4', 'G4', 'Bb4', 'F5'])

    def test_minor_eleventh(self):
        chord = Chord('Cm11')
        self.assertEqual(str(chord), 'Cm11')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'F5'])

    def test_lydian_dominant_seventh(self):
        chord = Chord('C7#11')
        self.assertEqual(str(chord), 'C7#11')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'F#5'])

    def test_minor_thirteenth(self):
        chord = Chord('Cm13')
        self.assertEqual(str(chord), 'Cm13')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'D5', 'A5'])

    def test_major_thirteenth(self):
        chord = Chord('CM13')
        self.assertEqual(str(chord), 'CM13')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'B4', 'D5', 'A5'])

    def test_dominant_thirteenth(self):
        chord = Chord('C13')
        self.assertEqual(str(chord), 'C13')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D5', 'A5'])

    def test_major_seventh(self):
        chord = Chord('CM7')
        self.assertEqual(str(chord), 'CM7')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'B4'])

    def test_minor_seventh(self):
        chord = Chord('Cm7')
        self.assertEqual(str(chord), 'Cm7')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4'])

    def test_dominant_seventh(self):
        chord = Chord('C7')
        self.assertEqual(str(chord), 'C7')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4'])

    def test_diminished_seventh(self):
        chord = Chord('Cdim7')
        self.assertEqual(str(chord), 'Cdim7')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bbb4'])

    def test_minor_seventh_flat_five(self):
        chord = Chord('Cm7b5')
        self.assertEqual(str(chord), 'Cm7b5')
        self._chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bb4'])

    def test_minor_major_seventh(self):
        chord = Chord('CmM7')
        self.assertEqual(str(chord), 'CmM7')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'B4'])

        # Alternative representations
        self.assertEqual(chord, Chord('Cm/M7'))

    def test_minor_sixth(self):
        chord = Chord('Cm6')
        self.assertEqual(str(chord), 'Cm6')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'A4'])

    def test_major_sixth(self):
        chord = Chord('CM6')
        self.assertEqual(str(chord), 'CM6')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4'])

    def test_dominant_sixth(self):
        chord = Chord('C67')
        self.assertEqual(str(chord), 'C67')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4', 'Bb4'])

    def test_sixth_ninth(self):
        chord = Chord('C69')
        self.assertEqual(str(chord), 'C69')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'A4', 'D5'])

    def test_minor_ninth(self):
        chord = Chord('Cm9')
        self.assertEqual(str(chord), 'Cm9')
        self._chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'D5'])

    def test_major_ninth(self):
        chord = Chord('CM9')
        self.assertEqual(str(chord), 'CM9')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'B4', 'D5'])

    def test_added_ninth(self):
        chord = Chord('Cadd9')
        self.assertEqual(str(chord), 'Cadd9')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'D5'])

    def test_dominant_ninth(self):
        chord = Chord('C9')
        self.assertEqual(str(chord), 'C9')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D5'])

    def test_dominant_flat_ninth(self):
        chord = Chord('C7b9')
        self.assertEqual(str(chord), 'C7b9')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'Db5'])

    def test_dominant_sharp_ninth(self):
        chord = Chord('C7#9')
        self.assertEqual(str(chord), 'C7#9')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D#5'])

    def test_dominant_flat_five(self):
        chord = Chord('C7b5')
        self.assertEqual(str(chord), 'C7b5')
        self._chord_tester(chord, ['C4', 'E4', 'Gb4', 'Bb4'])

    def test_hendrix_chord(self):
        chord = Chord('C7b12')
        self.assertEqual(str(chord), 'C7b12')
        self._chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'Eb5'])

    def test_transpose_chord(self):
        chord = Chord('CM')
        self.assertEqual(chord.notes, [Note('C'),
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
        self.chord_info = produce_all_chords('C')

    def test_produce_all_chords(self):

        expected = {'added_ninth': Chord('Cadd9'),
                    'augmented_major_seventh': Chord('CM7+'),
                    'augmented_minor_seventh': Chord('Cm7+'),
                    'augmented_triad': Chord('Caug'),
                    'diminished_seventh': Chord('Cdim7'),
                    'diminished_triad': Chord('Cdim'),
                    'dominant_flat_five': Chord('C7b5'),
                    'dominant_flat_ninth': Chord('C7b9'),
                    'dominant_ninth': Chord('C9'),
                    'dominant_ninth_flat_five': Chord('C9b5'),
                    'dominant_ninth_sharp_five': Chord('C9#5'),
                    'dominant_seventh': Chord('C7'),
                    'dominant_sharp_five': Chord('C7#5'),
                    'dominant_sharp_ninth': Chord('C7#9'),
                    'dominant_sharp_ninth_flat_five': Chord('C7#9b5'),
                    'dominant_sixth': Chord('C67'),
                    'dominant_thirteenth': Chord('C13'),
                    'eleventh': Chord('C11'),
                    'hendrix_chord': Chord('C7b12'),
                    'lydian_dominant_seventh': Chord('C7#11'),
                    'major_fifth': Chord('C5'),
                    'major_ninth': Chord('CM9'),
                    'major_seventh': Chord('CM7'),
                    'major_seventh_flat_five': Chord('CM7b5'),
                    'major_seventh_sharp_five': Chord('CM7#5'),
                    'major_sixth': Chord('CM6'),
                    'major_thirteenth': Chord('CM13'),
                    'major_triad': Chord('CM'),
                    'minor_added_ninth': Chord('Cmadd9'),
                    'minor_eleventh': Chord('Cm11'),
                    'minor_major_seventh': Chord('CmM7'),
                    'minor_ninth': Chord('Cm9'),
                    'minor_ninth_flat_five': Chord('Cm9b5'),
                    'minor_seventh': Chord('Cm7'),
                    'minor_seventh_flat_five': Chord('Cm7b5'),
                    'minor_seventh_sharp_five': Chord('Cm7#5'),
                    'minor_sixth': Chord('Cm6'),
                    'minor_thirteenth': Chord('Cm13'),
                    'minor_triad': Chord('Cm'),
                    'sixth_ninth': Chord('C69'),
                    'suspended_fourth_ninth': Chord('Csus4b9'),
                    'suspended_fourth_triad': Chord('Csus4'),
                    'suspended_second_triad': Chord('Csus2'),
                    'suspended_seventh': Chord('Csus47')}
        self.assertEqual(self.chord_info, expected)
