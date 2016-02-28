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
