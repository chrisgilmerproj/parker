from mixins import Aug
from notes import Note
from notes import NoteGroupBase


class Scale(NoteGroupBase):
    """
    Source Material:
    """

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


class Aeolian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 3, 5, 7, 8, 10], note)


class Locrian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 1, 3, 5, 6, 8, 10], note)
