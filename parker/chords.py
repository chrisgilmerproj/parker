from .constants import CHORD_MATCHER
from .notes import Note
from .notes import NoteGroupBase
from .mixins import Aug
from .mixins import Dim


# References:
# - http://www.cs.cmu.edu/~scottd/chords_and_scales/music.html
# - https://en.wikipedia.org/wiki/List_of_chords

# The CHORD_MAP is a dictionary where the chord name is mapped to a list of
# shorthand notations and the corresponding transpose list to create the
# chord given a root note.  The shorthand list order is not consequential
# except that when producing all the chords the first element in the list
# is chosen as the desired shorthand notation.
CHORD_MAP = {
    # Triads
    'major_triad': {'shorthand': ['M', '', 'maj', 'ma', 'major'],
                    'transpose_list': [0, 4, 7]},
    'minor_triad': {'shorthand': ['m', 'min', 'mi', '-', 'minor'],
                    'transpose_list': [0, 3, 7]},
    # Augmented
    'augmented_triad': {'shorthand': ['aug'],
                        'transpose_list': [0, 4, Aug(7)]},
    'augmented_major_seventh': {'shorthand': ['M7+'],
                                'transpose_list': [0, 4, Aug(7), 'e']},
    'augmented_minor_seventh': {'shorthand': ['m7+'],
                                'transpose_list': [0, 4, Aug(7), 't']},
    'lydian_dominant_seventh': {'shorthand': ['7#11'],
                                'transpose_list': [0, 4, 7, 't', Aug(17)]},
    # Diminished
    'diminished_major_seventh': {'shorthand': ['dimM7'],
                                 'transpose_list': [0, 3, 6, 'e']},
    'diminished_seventh': {'shorthand': ['dim7'],
                           'transpose_list': [0, 3, 6, Dim(10)]},
    'diminished_triad': {'shorthand': ['dim', 'o'],
                         'transpose_list': [0, 3, 6]},
    # Suspended
    'suspended_fourth_ninth': {'shorthand': ['sus4b9'],
                               'transpose_list': [0, 5, 7, 13]},
    'suspended_fourth_triad': {'shorthand': ['sus4', 'sus'],
                               'transpose_list': [0, 5, 7]},
    'suspended_second_triad': {'shorthand': ['sus2'],
                               'transpose_list': [0, 2, 7]},
    'suspended_seventh': {'shorthand': ['sus47', '7sus4'],
                          'transpose_list': [0, 5, 7, 10]},
    # Fifths
    'major_fifth': {'shorthand': ['5'],
                    'transpose_list': [0, 7]},
    # Sixths
    'major_sixth': {'shorthand': ['M6', '6', 'maj6'],
                    'transpose_list': [0, 4, 7, 9]},
    'minor_sixth': {'shorthand': ['m6', 'min6'],
                    'transpose_list': [0, 3, 7, 9]},
    'sixth_ninth': {'shorthand': ['69', '6/9'],
                    'transpose_list': [0, 4, 7, 9, 14]},
    'dominant_sixth': {'shorthand': ['67'],
                       'transpose_list': [0, 4, 7, 9, 10]},
    # Sevenths
    'dominant_seventh': {'shorthand': ['7'],
                         'transpose_list': [0, 4, 7, 10]},
    'major_seventh': {'shorthand': ['M7', 'maj7', 'ma7'],  # delta7 and delta
                      'transpose_list': [0, 4, 7, 11]},
    'major_seventh_sharp_five': {'shorthand': ['M7#5', 'M7+5'],
                                 'transpose_list': [0, 4, 8, 11]},
    'major_seventh_flat_five': {'shorthand': ['M7b5', 'M7-5'],
                                'transpose_list': [0, 4, 6, 11]},
    'minor_major_seventh': {'shorthand': ['mM7', 'm/M7', 'm/maj7'],
                            'transpose_list': [0, 3, 7, 11]},
    'minor_seventh': {'shorthand': ['m7', 'min7', 'mi7', '-7'],
                      'transpose_list': [0, 3, 7, 10]},
    'minor_seventh_sharp_five': {'shorthand': ['m7#5', 'm7+5'],
                                 'transpose_list': [0, 3, 8, 10]},
    'minor_seventh_flat_five': {'shorthand': ['m7b5', 'm7-5'],
                                'transpose_list': [0, 3, 6, 10]},
    # Ninths
    'added_ninth': {'shorthand': ['add9'],
                    'transpose_list': [0, 4, 7, 14]},
    'minor_added_ninth': {'shorthand': ['madd9'],
                          'transpose_list': [0, 3, 7, 14]},
    'dominant_ninth': {'shorthand': ['9'],
                       'transpose_list': [0, 4, 7, 10, 14]},
    'dominant_ninth_flat_five': {'shorthand': ['9b5', '9-5'],
                                 'transpose_list': [0, 4, 6, 10, 14]},
    'dominant_ninth_sharp_five': {'shorthand': ['9#5', '9+5'],
                                  'transpose_list': [0, 4, 8, 10, 14]},
    'dominant_flat_ninth': {'shorthand': ['7b9', '7-9'],
                            'transpose_list': [0, 4, 7, 10, 13]},
    'dominant_sharp_ninth': {'shorthand': ['7#9', '7+9'],
                             'transpose_list': [0, 4, 7, 10, Aug(14)]},
    'dominant_sharp_ninth_flat_five': {'shorthand': ['7#9b5', '7+9-5'],
                                       'transpose_list': [0, 4, 6, 10,
                                                          Aug(14)]},
    'major_ninth': {'shorthand': ['M9', 'maj9', 'ma9'],
                    'transpose_list': [0, 4, 7, 11, 14]},
    'minor_ninth': {'shorthand': ['m9', 'min9', 'mi9'],
                    'transpose_list': [0, 3, 7, 10, 14]},
    'minor_ninth_flat_five': {'shorthand': ['m9b5', 'm9-5'],
                              'transpose_list': [0, 3, 6, 10, 14]},
    # Elevenths
    'eleventh': {'shorthand': ['11'],
                 'transpose_list': [0, 7, 10, 17]},
    'minor_eleventh': {'shorthand': ['m11'],
                       'transpose_list': [0, 3, 7, 10, 17]},
    # Thirteenths
    'dominant_thirteenth': {'shorthand': ['13'],
                            'transpose_list': [0, 4, 7, 10, 14, 21]},
    'major_thirteenth': {'shorthand': ['M13', 'maj13'],
                         'transpose_list': [0, 4, 7, 11, 14, 21]},
    'minor_thirteenth': {'shorthand': ['m13'],
                         'transpose_list': [0, 3, 7, 10, 14, 21]},
    # Altered
    'dominant_flat_five': {'shorthand': ['7b5', '7-5'],
                           'transpose_list': [0, 4, 6, 't']},
    'dominant_sharp_five': {'shorthand': ['7#5', '7+5'],
                            'transpose_list': [0, 4, 8, 't']},
    # Atonal
    'ode_to_napoleon': {'shorthand': ['napoleon'],
                        'transpose_list': [0, 1, 4, 5, 8, 9]},
    'farben': {'shorthand': ['farben'],
               'transpose_list': [0, 8, 'e', 16, 21]},
    'mystic': {'shorthand': ['mystic'],
               'transpose_list': [0, 6, 't', 16, 21, 26]},
    'northern_lights': {'shorthand': ['northern'],
                        'transpose_list': [1, 2, 8, 12, 15, 18,
                                           19, 22, 23, 28, 31]},
    'viennese_trichord': {'shorthand': ['viennese'],
                          'transpose_list': [0, 1, 6]},
    # Bitonal
    'elektra': {'shorthand': ['elektra'],
                'transpose_list': [0, 7, 9, 13, 16]},
    'so_what': {'shorthand': ['so_what'],
                'transpose_list': [0, 5, 't', 15, 19]},
    # Mixed
    'hendrix_chord': {'shorthand': ['7b12', 'hendrix'],
                      'transpose_list': [0, 4, 7, 't', 15]},
    'petrushka': {'shorthand': ['petrushka'],
                  'transpose_list': [0, 1, 4, 6, 7, 't']},
    # Predominant
    'augmented_sixth': {'shorthand': ['aug6'],
                        'transpose_list': [0, 6, 8]},
    'tristan': {'shorthand': ['tristan'],
                'transpose_list': [0, 3, 6, 't']},
}

SHORTHAND = {}
for name, data in CHORD_MAP.items():
    for short in data['shorthand']:
        SHORTHAND[short] = data['transpose_list']


class Chord(NoteGroupBase):
    """
    Source Material: https://en.wikipedia.org/wiki/Chord_(music)
    """

    def __init__(self, chord=None, octave=None):
        """
        Create chords from a chord name and an optional octave.
        """
        self._octave = octave
        if isinstance(chord, str):
            self._set_from_string(chord)
        else:
            raise Exception('Must instantiate Chord() object with a '
                            'chord name')

    def __str__(self):
        return '{}{}'.format(self.root.generalize() if self.notes else '',
                             self.extension)

    def __repr__(self):
        rep_str = "{}('{}'".format(type(self).__name__, str(self))
        if self._octave:
            rep_str = "{}, octave={}".format(rep_str, self._octave)
        return "{})".format(rep_str)

    def __eq__(self, other):
        # Chords must be of the same class or derived from the Chord class
        if not (isinstance(other, self.__class__) or isinstance(other, Chord)):
            return False
        if self.__dict__ == other.__dict__:
            return True
        # Scales are identical if their generic notes are also identical
        if self.notes == other.notes:
            return True
        return False

    def _set_from_string(self, chord):
        m = CHORD_MATCHER.match(chord)
        if m is None:
            raise Exception("Unknown chord format: {}".format(chord))

        root, self.extension = m.group(1), m.group(2)
        if self._octave:
            root = "{}{}".format(root, self._octave)

        transpose_list = self._get_shorthand(self.extension)
        self.root = Note(root)
        self.notes = self.root.transpose_list(transpose_list)

    @classmethod
    def _get_shorthand(cls, shorthand):
        if shorthand not in SHORTHAND:
            raise Exception("Unknown chord extensions: {}".format(shorthand))
        return SHORTHAND[shorthand]


def produce_all_chords(root):
    """
    Produce all chords given a root note.

    Returns a dictionary of chord names as the key and the chord object
    as the value.
    """

    chord_info = {}
    for name, data in CHORD_MAP.items():
        shorthand = data['shorthand'][0]
        chord_name = '{}{}'.format(root, shorthand)
        chord = Chord(chord_name)
        chord_info[name] = chord
    return chord_info
