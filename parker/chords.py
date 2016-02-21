from constants import CHORD_MATCHER
from notes import Note
from notes import NoteGroup
from mixins import Aug
from mixins import Dim


def create_chord(root, chord_name):
    pass


class Chord(object):
    note = None
    chord = None
    group = None
    extension = None

    def __init__(self, chord):
        self.set_from_string(chord)

    def __len__(self):
        return len(self.group)

    def set_from_string(self, chord):
        self.chord = chord
        m = CHORD_MATCHER.match(chord)
        if m is None:
            raise Exception("Unknown chord format: {}".format(chord))

        base_name, accidentals, octave, extension = (m.group(1), m.group(2),
                                                     m.group(3), m.group(4))
        self.extension = self.normalize_extension(extension)

        self.note = Note("%s%s%s" % (base_name, accidentals, octave))
        self.group = self._get_shorthand(self.extension)()

    @staticmethod
    def normalize_extension(extension):
        extension = extension.replace("min", "m")
        extension = extension.replace("mi", "m")
        extension = extension.replace("-", "m")
        extension = extension.replace("maj", "M")
        extension = extension.replace("ma", "M")
        return extension

    def _create_chord(self, transpose_list):
        return NoteGroup(Note(self.note).transpose_list(transpose_list))

    def major_triad(self):
        return self._create_chord([0, 4, 7])

    def minor_triad(self):
        return self._create_chord([0, 3, 7])

    def diminished_triad(self):
        return self._create_chord([0, 3, 6])

    def augmented_triad(self):
        return self._create_chord([0, 4, Aug(7)])

    def augmented_minor_seventh(self):
        return self._create_chord([0, 4, Aug(7), 10])

    def augmented_major_seventh(self):
        return self._create_chord([0, 4, Aug(7), 11])

    def suspended_triad(self):
        return self._create_chord([0, 5, 7])

    def suspended_fourth_triad(self):
        return self._create_chord([0, 5, 7])

    def suspended_second_triad(self):
        return self._create_chord([0, 2, 7])

    def suspended_seventh(self):
        return self._create_chord([0, 5, 7, 10])

    def suspended_fourth_ninth(self):
        return self._create_chord([0, 5, 7, 13])

    def major_seventh(self):
        return self._create_chord([0, 4, 7, 11])

    def minor_seventh(self):
        return self._create_chord([0, 3, 7, 10])

    def dominant_seventh(self):
        return self._create_chord([0, 4, 7, 10])

    def diminished_seventh(self):
        return self._create_chord([0, 3, 6, Dim(10)])

    def half_diminished_seventh(self):
        return self._create_chord([0, 3, 6, 10])

    def minor_seventh_flat_five(self):
        return self._create_chord([0, 3, 6, 10])

    def minor_major_seventh(self):
        return self._create_chord([0, 3, 7, 11])

    def minor_sixth(self):
        return self._create_chord([0, 3, 7, 8])

    def major_sixth(self):
        return self._create_chord([0, 4, 7, 9])

    def dominant_sixth(self):
        return self._create_chord([0, 4, 7, 9, 10])

    def sixth_ninth(self):
        return self._create_chord([0, 4, 7, 9, 14])

    def minor_ninth(self):
        return self._create_chord([0, 3, 7, 10, 14])

    def major_ninth(self):
        return self._create_chord([0, 4, 7, 11, 14])

    def dominant_ninth(self):
        return self._create_chord([0, 4, 7, 10, 14])

    def dominant_flat_ninth(self):
        return self._create_chord([0, 4, 7, 10, 13])

    def dominant_sharp_ninth(self):
        return self._create_chord([0, 4, 7, 10, Aug(14)])

    def eleventh(self):
        return self._create_chord([0, 7, 10, 17])

    def minor_eleventh(self):
        return self._create_chord([0, 3, 7, 10, 17])

    def lydian_dominant_seventh(self):
        return self._create_chord([0, 4, 7, 10, Aug(17)])

    def minor_thirteenth(self):
        return self._create_chord([0, 3, 7, 10, 14, 21])

    def major_thirteenth(self):
        return self._create_chord([0, 4, 7, 11, 14, 21])

    def dominant_thirteenth(self):
        return self._create_chord([0, 4, 7, 10, 14, 21])

    def dominant_flat_five(self):
        return self._create_chord([0, 4, 6, 10])

    def hendrix_chord(self):
        return self._create_chord([0, 4, 7, 10, 15])

    def _get_shorthand(self, shorthand):
        SHORTHAND = {
            # Triads
            'm': self.minor_triad,
            'M': self.major_triad,
            '': self.major_triad,
            'dim': self.diminished_triad,
            # Augmented
            'aug': self.augmented_triad,
            '+': self.augmented_triad,
            '7#5': self.augmented_minor_seventh,
            'M7+5': self.augmented_minor_seventh,
            'M7+': self.augmented_major_seventh,
            'm7+': self.augmented_minor_seventh,
            '7+': self.augmented_major_seventh,
            # Suspended
            'sus47': self.suspended_seventh,
            'sus4': self.suspended_fourth_triad,
            'sus2': self.suspended_second_triad,
            'sus': self.suspended_triad,
            'sus4b9': self.suspended_fourth_ninth,
            'susb9': self.suspended_fourth_ninth,
            # Sevenths
            'm7': self.minor_seventh,
            'M7': self.major_seventh,
            '7': self.dominant_seventh,
            'dom7': self.dominant_seventh,
            'm7b5': self.minor_seventh_flat_five,
            'dim7': self.diminished_seventh,
            'm/M7': self.minor_major_seventh,
            'mM7': self.minor_major_seventh,
            # Sixths
            'm6': self.minor_sixth,
            'M6': self.major_sixth,
            '6': self.major_sixth,
            '6/7': self.dominant_sixth,
            '67': self.dominant_sixth,
            # Ninths
            '6/9': self.sixth_ninth,
            '69': self.sixth_ninth,
            '9': self.dominant_ninth,
            '7b9': self.dominant_flat_ninth,
            '7#9': self.dominant_sharp_ninth,
            'M9': self.major_ninth,
            'm9': self.minor_ninth,
            # Elevenths
            '11': self.eleventh,
            'm11': self.minor_eleventh,
            '7#11': self.lydian_dominant_seventh,
            # Thirteenths
            'M13': self.major_thirteenth,
            'm13': self.minor_thirteenth,
            '13': self.dominant_thirteenth,
            # Altered chords
            '7b5': self.dominant_flat_five,
            'hendrix': self.hendrix_chord,
            '7b12': self.hendrix_chord,
        }
        if shorthand not in SHORTHAND:
            raise Exception("Unknown chord extensions: {}".format(shorthand))
        return SHORTHAND[shorthand]
