from mixins import Aug
from mixins import Dim
from notes import Note
from notes import NoteGroupBase


def diatonic_interval(tonic):
    """
    Create the diatonic interval from the tonic.
    This uses the interavl T-T-s-T-T-T-s (or W-W-h-W-W-W-h) as the basis
    for creating a diatonic scale.  It returns only 7 notes instead of
    the full octave.

    Source: https://en.wikipedia.org/wiki/Diatonic_scale#Modes
    """
    if tonic not in xrange(1, 8):
        raise Exception("Tonic must be a number between 1 and 7")
    rot = tonic - 1
    tonal_sequence = [2, 2, 1, 2, 2, 2, 1]
    seq = tonal_sequence[rot:] + tonal_sequence[:rot]
    interval = [0]
    for i, s in enumerate(seq):
        interval.append(s + interval[i])
    return interval[:-1]


# def octatonic_interval(tonic):
#     """
#     Source: https://en.wikipedia.org/wiki/Octatonic_scale
#     """
#     tonal_sequence = [2, 1, 2, 1, 2, 1, 2, 1]


class Scale(NoteGroupBase):
    """
    Source: https://en.wikipedia.org/wiki/Scale_(music)
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


class Ionian(Scale):
    intervals = diatonic_interval(1)


class Major(Ionian):
    pass


class Dorian(Scale):
    intervals = diatonic_interval(2)


class Phrygian(Scale):
    intervals = diatonic_interval(3)


class Lydian(Scale):
    # intervals = diatonic_interval(4)
    intervals = [0, 2, 4, Aug(5), 7, 9, 11]


class Mixolydian(Scale):
    intervals = diatonic_interval(5)


class Dominant(Mixolydian):
    pass


class Aeolian(Scale):
    intervals = diatonic_interval(6)


class Minor(Aeolian):
    pass


class Locrian(Scale):
    intervals = diatonic_interval(7)


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
