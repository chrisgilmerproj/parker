from mixins import Aug
from mixins import Dim
from notes import Note
from notes import NoteGroupBase


class Scale(NoteGroupBase):
    """
    Source Material: https://en.wikipedia.org/wiki/Scale_(music)
    """
    tonal_sequence = [2, 2, 1, 2, 2, 2, 1]

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

    def _notes_to_scale_representation(self, intervals, root):
        self.notes = root.transpose_list(intervals)

    def build_scale(self, note):
        self._notes_to_scale_representation([0], note)


class Diatonic(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 4, 5, 7, 9, 11], note)


class Ionian(Diatonic):
    pass


class Major(Diatonic):
    pass


class Dorian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 3, 5, 7, 9, 10], note)


class Phrygian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 1, 3, 5, 7, 8, 10], note)


class Lydian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 4, Aug(5), 7, 9, 11], note)


class Mixolydian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 4, 5, 7, 9, 10], note)


class Dominant(Mixolydian):
    pass


class Aeolian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 3, 5, 7, 8, 10], note)


class NaturalMinor(Aeolian):
    pass


class Locrian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 1, 3, 5, 6, 8, 10], note)


class Chromatic(Scale):
    def build_scale(self, note):
        intervals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self._notes_to_scale_representation(intervals, note)


class MajorPentatonic(Scale):
    def build_scale(self, note):
        intervals = [0, 2, 4, 7, 9]
        self._notes_to_scale_representation(intervals, note)


class MinorPentatonic(Scale):
    def build_scale(self, note):
        intervals = [0, 3, 5, 7, 10]
        self._notes_to_scale_representation(intervals, note)


class MajorBlues(Scale):
    def build_scale(self, note):
        intervals = [0, 2, Dim(4), 4, 7, 9]
        self._notes_to_scale_representation(intervals, note)


class MinorBlues(Scale):
    def build_scale(self, note):
        intervals = [0, 3, 5, Aug(5), 7, 10]
        self._notes_to_scale_representation(intervals, note)
