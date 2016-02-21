from constants import CHORD_MATCHER
from notes import Note
from notes import NoteGroup
from mixins import Aug
from mixins import Dim


class Chord(object):
    note = None
    chord = None
    group = None
    extension = None

    def __init__(self, chord=None):
        if chord:
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
        self.group = self._get_shorthand(self.extension)(self.note)

    @staticmethod
    def normalize_extension(extension):
        extension = extension.replace("min", "m")
        extension = extension.replace("mi", "m")
        extension = extension.replace("-", "m")
        extension = extension.replace("maj", "M")
        extension = extension.replace("ma", "M")
        return extension

    @staticmethod
    def _create_chord(root, transpose_list):
        note = Note(root)
        group = NoteGroup(note.transpose_list(transpose_list))
        return group

    @classmethod
    def major_triad(cls, root):
        return cls._create_chord(root, [0, 4, 7])

    @classmethod
    def minor_triad(cls, root):
        return cls._create_chord(root, [0, 3, 7])

    @classmethod
    def diminished_triad(cls, root):
        return cls._create_chord(root, [0, 3, 6])

    @classmethod
    def augmented_triad(cls, root):
        return cls._create_chord(root, [0, 4, Aug(7)])

    @classmethod
    def augmented_minor_seventh(cls, root):
        return cls._create_chord(root, [0, 4, Aug(7), 10])

    @classmethod
    def augmented_major_seventh(cls, root):
        return cls._create_chord(root, [0, 4, Aug(7), 11])

    @classmethod
    def suspended_triad(cls, root):
        return cls._create_chord(root, [0, 5, 7])

    @classmethod
    def suspended_fourth_triad(cls, root):
        return cls._create_chord(root, [0, 5, 7])

    @classmethod
    def suspended_second_triad(cls, root):
        return cls._create_chord(root, [0, 2, 7])

    @classmethod
    def suspended_seventh(cls, root):
        return cls._create_chord(root, [0, 5, 7, 10])

    @classmethod
    def suspended_fourth_ninth(cls, root):
        return cls._create_chord(root, [0, 5, 7, 13])

    @classmethod
    def major_seventh(cls, root):
        return cls._create_chord(root, [0, 4, 7, 11])

    @classmethod
    def minor_seventh(cls, root):
        return cls._create_chord(root, [0, 3, 7, 10])

    @classmethod
    def dominant_seventh(cls, root):
        return cls._create_chord(root, [0, 4, 7, 10])

    @classmethod
    def diminished_seventh(cls, root):
        return cls._create_chord(root, [0, 3, 6, Dim(10)])

    @classmethod
    def half_diminished_seventh(cls, root):
        return cls._create_chord(root, [0, 3, 6, 10])

    @classmethod
    def minor_seventh_flat_five(cls, root):
        return cls._create_chord(root, [0, 3, 6, 10])

    @classmethod
    def minor_major_seventh(cls, root):
        return cls._create_chord(root, [0, 3, 7, 11])

    @classmethod
    def minor_sixth(cls, root):
        return cls._create_chord(root, [0, 3, 7, 8])

    @classmethod
    def major_sixth(cls, root):
        return cls._create_chord(root, [0, 4, 7, 9])

    @classmethod
    def dominant_sixth(cls, root):
        return cls._create_chord(root, [0, 4, 7, 9, 10])

    @classmethod
    def sixth_ninth(cls, root):
        return cls._create_chord(root, [0, 4, 7, 9, 14])

    @classmethod
    def minor_ninth(cls, root):
        return cls._create_chord(root, [0, 3, 7, 10, 14])

    @classmethod
    def major_ninth(cls, root):
        return cls._create_chord(root, [0, 4, 7, 11, 14])

    @classmethod
    def dominant_ninth(cls, root):
        return cls._create_chord(root, [0, 4, 7, 10, 14])

    @classmethod
    def dominant_flat_ninth(cls, root):
        return cls._create_chord(root, [0, 4, 7, 10, 13])

    @classmethod
    def dominant_sharp_ninth(cls, root):
        return cls._create_chord(root, [0, 4, 7, 10, Aug(14)])

    @classmethod
    def eleventh(cls, root):
        return cls._create_chord(root, [0, 7, 10, 17])

    @classmethod
    def minor_eleventh(cls, root):
        return cls._create_chord(root, [0, 3, 7, 10, 17])

    @classmethod
    def lydian_dominant_seventh(cls, root):
        return cls._create_chord(root, [0, 4, 7, 10, Aug(17)])

    @classmethod
    def minor_thirteenth(cls, root):
        return cls._create_chord(root, [0, 3, 7, 10, 14, 21])

    @classmethod
    def major_thirteenth(cls, root):
        return cls._create_chord(root, [0, 4, 7, 11, 14, 21])

    @classmethod
    def dominant_thirteenth(cls, root):
        return cls._create_chord(root, [0, 4, 7, 10, 14, 21])

    @classmethod
    def dominant_flat_five(cls, root):
        return cls._create_chord(root, [0, 4, 6, 10])

    @classmethod
    def hendrix_chord(cls, root):
        return cls._create_chord(root, [0, 4, 7, 10, 15])

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
