from mixins import Aug
from mixins import Dim
from notes import Note
from notes import NoteGroupBase


class Scale(NoteGroupBase):
    """
    Source Material: https://en.wikipedia.org/wiki/Scale_(music)
    """
    intervals = [0]

    def __init__(self, root):
        """
        Create scales
        """
        self.notes = []
        self.build_scale(Note(root))

    def __str__(self):
        return str(self.notes[0])

    def __repr__(self):
        return "{}('{}')".format(type(self).__name__, str(self))

    def build_scale(self, note):
        self.notes = note.transpose_list(self.intervals)


class Diatonic(Scale):
    intervals = [0, 2, 4, 5, 7, 9, 11]


class Ionian(Diatonic):
    pass


class Major(Diatonic):
    pass


class Dorian(Scale):
    intervals = [0, 2, 3, 5, 7, 9, 10]


class Phrygian(Scale):
    intervals = [0, 1, 3, 5, 7, 8, 10]


class Lydian(Scale):
    intervals = [0, 2, 4, Aug(5), 7, 9, 11]


class Mixolydian(Scale):
    intervals = [0, 2, 4, 5, 7, 9, 10]


class Dominant(Mixolydian):
    pass


class Aeolian(Scale):
    intervals = [0, 2, 3, 5, 7, 8, 10]


class NaturalMinor(Aeolian):
    pass


class Locrian(Scale):
    intervals = [0, 1, 3, 5, 6, 8, 10]


class Chromatic(Scale):
    intervals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


class MajorPentatonic(Scale):
    intervals = [0, 2, 4, 7, 9]


class MinorPentatonic(Scale):
    intervals = [0, 3, 5, 7, 10]


class MajorBlues(Scale):
    intervals = [0, 2, Dim(4), 4, 7, 9]


class MinorBlues(Scale):
    intervals = [0, 3, 5, Aug(5), 7, 10]
