from .constants import CHORD_MATCHER
from .notes import Note
from .notes import NoteGroupBase
from .mixins import Aug
from .mixins import Dim


SHORTHAND = {
    # Triads
    'm': [0, 3, 7],
    'M': [0, 4, 7],
    'dim': [0, 3, 6],
    # Augmented
    'aug': [0, 4, Aug(7)],
    'm7+': [0, 4, Aug(7), 10],
    'M7+': [0, 4, Aug(7), 11],
    # Suspended
    'sus47': [0, 5, 7, 10],
    'sus4': [0, 5, 7],
    'sus2': [0, 2, 7],
    'sus4b9': [0, 5, 7, 13],
    # Sevenths
    'm7': [0, 3, 7, 10],
    'M7': [0, 4, 7, 11],
    '7': [0, 4, 7, 10],
    'm7b5': [0, 3, 6, 10],
    'dim7': [0, 3, 6, Dim(10)],
    'mM7': [0, 3, 7, 11],
    # Sixths
    'm6': [0, 3, 7, 9],
    'M6': [0, 4, 7, 9],
    '67': [0, 4, 7, 9, 10],
    # Ninths
    '69': [0, 4, 7, 9, 14],
    '9': [0, 4, 7, 10, 14],
    '7b9': [0, 4, 7, 10, 13],
    '7#9': [0, 4, 7, 10, Aug(14)],
    'M9': [0, 4, 7, 11, 14],
    'm9': [0, 3, 7, 10, 14],
    'add9': [0, 4, 7, 14],
    # Elevenths
    '11': [0, 7, 10, 17],
    'm11': [0, 3, 7, 10, 17],
    '7#11': [0, 4, 7, 10, Aug(17)],
    # Thirteenths
    'M13': [0, 4, 7, 11, 14, 21],
    'm13': [0, 3, 7, 10, 14, 21],
    '13': [0, 4, 7, 10, 14, 21],
    # Altered chords
    '7b5': [0, 4, 6, 10],
    '7b12': [0, 4, 7, 10, 15],
}

CHORD_TO_SHORTHAND = {
    # Triads
    'minor_triad': 'm',
    'major_triad': 'M',
    'diminished_triad': 'dim',
    # Augmented
    'augmented_triad': 'aug',
    'augmented_minor_seventh': 'm7+',
    'augmented_major_seventh': 'M7+',
    # Suspended
    'suspended_fourth_triad': 'sus4',
    'suspended_second_triad': 'sus2',
    'suspended_seventh': 'sus47',
    'suspended_fourth_ninth': 'sus4b9',
    # Sevenths
    'minor_seventh': 'm7',
    'major_seventh': 'M7',
    'dominant_seventh': '7',
    'minor_seventh_flat_five': 'm7b5',
    'diminished_seventh': 'dim7',
    'minor_major_seventh': 'mM7',
    # Sixths
    'minor_sixth': 'm6',
    'major_sixth': 'M6',
    'dominant_sixth': '67',
    # Ninths
    'sixth_ninth': '69',
    'dominant_ninth': '9',
    'dominant_flat_ninth': '7b9',
    'dominant_sharp_ninth': '7#9',
    'major_ninth': 'M9',
    'minor_ninth': 'm9',
    'added_ninth': 'add9',
    # Elevenths
    'eleventh': '11',
    'minor_eleventh': 'm11',
    'lydian_dominant_seventh': '7#11',
    # Thirteenths
    'major_thirteenth': 'M13',
    'minor_thirteenth': 'm13',
    'dominant_thirteenth': '13',
    # Altered chords
    'dominant_flat_five': '7b5',
    'hendrix_chord': '7b12',
}


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
        return '{}{}'.format(self.notes[0].generalize() if self.notes else '',
                             self.extension)

    def __repr__(self):
        rep_str = "{}('{}'".format(type(self).__name__, str(self))
        if self._octave:
            rep_str = "{}, octave={}".format(rep_str, self._octave)
        return "{})".format(rep_str)

    def _set_from_string(self, chord):
        m = CHORD_MATCHER.match(chord)
        if m is None:
            raise Exception("Unknown chord format: {}".format(chord))

        root, extension = m.group(1), m.group(2)
        if self._octave:
            root = "{}{}".format(root, self._octave)
        self.extension = self.normalize_extension(extension)

        transpose_list = self._get_shorthand(self.extension)
        self.notes = Note(root).transpose_list(transpose_list)

    @staticmethod
    def normalize_extension(extension):
        extension = extension.replace("min", "m")
        extension = extension.replace("mi", "m")
        extension = extension.replace("-", "m")
        extension = extension.replace("maj", "M")
        extension = extension.replace("ma", "M")
        return extension

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
    for name, shorthand in CHORD_TO_SHORTHAND.items():
        chord_name = '{}{}'.format(root, shorthand)
        chord = Chord(chord_name)
        chord_info[name] = chord
    return chord_info
