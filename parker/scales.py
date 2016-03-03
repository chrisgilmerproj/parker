from .mixins import Aug
from .mixins import Dim
from .notes import Note
from .notes import NoteGroupBase


class Scale(NoteGroupBase):
    """
    Source: https://en.wikipedia.org/wiki/Scale_(music)
    """
    ASCENDING = 'ascending'
    DESCENDING = 'descending'
    ORDER_CHOICES = [ASCENDING, DESCENDING]
    generic_notes = []

    def __init__(self, root, order=None):
        """
        Create scales
        """
        self.notes = []
        self.root = Note(root)
        if not order:
            self.order = self.ASCENDING
        elif order in self.ORDER_CHOICES:
            self.order = order
        else:
            raise Exception("Order must be one of: {}".format(
                            self.ORDER_CHOICES))
        self.build_scale()

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        if self.order == self.DESCENDING:
            return "{}('{}', order='{}')".format(type(self).__name__,
                                                 str(self), self.DESCENDING)
        else:
            return "{}('{}')".format(type(self).__name__, str(self))

    def build_scale(self):
        intervals = self.get_intervals()
        self.notes = self.root.transpose_list(intervals)
        if self.order == self.DESCENDING:
            self.notes.reverse()

        # Get a list of the notes without the octave
        generic_notes = [Note(int(n)).get_note_without_octave()
                         for n in self.notes]
        self.generic_notes = set(generic_notes)

    def get_intervals(self):
        return [0]

    def is_generic_note_in_scale(self, note):
        if isinstance(note, str):
            return note in self.generic_notes
        if isinstance(note, Note):
            gen_note = Note(int(note)).get_note_without_octave()
            return gen_note in self.generic_notes


class Diatonic(Scale):

    @classmethod
    def _generate_intervals(cls, tonic, aug_dim_cls=None):
        """
        Create the diatonic interval from the tonic.
        This uses the interavl T-T-s-T-T-T-s (or W-W-h-W-W-W-h) as the basis
        for creating a diatonic scale.  It returns only 7 notes instead of
        the full octave.

        aug_dim_cls - a list of tuples that includes the index and the class
        to apply.  For instance, in Lydian scales you want to Augment the 4th
        note, so you'd give the tuple (3, Aug) in the list.

        Source: https://en.wikipedia.org/wiki/Diatonic_scale#Modes
        """
        if tonic not in range(1, 8):
            raise Exception("Tonic must be a number between 1 and 7")
        rot = tonic - 1
        tonal_sequence = [2, 2, 1, 2, 2, 2, 1]
        seq = tonal_sequence[rot:] + tonal_sequence[:rot]
        interval = [0]
        for i, s in enumerate(seq):
            interval.append(s + interval[i])

        # Apply Aug and Dim classes
        # This logic is a bit convoluted and should be cleaned up
        if not aug_dim_cls:
            aug_dim_cls = []
        for i, cls in aug_dim_cls:
            if cls == Aug:
                interval[i] = cls(interval[i] - 1)
            elif cls == Dim:
                interval[i] = cls(interval[i] + 1)
            else:
                msg = "Must use Aug or Dim classes for modifying intervals"
                raise Exception(msg)
        return interval


class Ionian(Diatonic):
    def get_intervals(self):
        return self._generate_intervals(1)


class Major(Ionian):
    pass


class Dorian(Diatonic):
    def get_intervals(self):
        return self._generate_intervals(2)


class Phrygian(Diatonic):
    def get_intervals(self):
        return self._generate_intervals(3)


class MedievalLydian(Diatonic):
    def get_intervals(self):
        return self._generate_intervals(4)


class Lydian(Diatonic):
    """
    The Lydian scale can be described as a major scale with the fourth scale
    degree raised a semitone, e.g., a C-major scale with an F# rather than
    F-natural.

    Source: https://en.wikipedia.org/wiki/Lydian_mode
    """
    def get_intervals(self):
        return self._generate_intervals(4, aug_dim_cls=[(3, Aug)])


class Mixolydian(Diatonic):
    def get_intervals(self):
        return self._generate_intervals(5)


class Dominant(Mixolydian):
    pass


class Aeolian(Diatonic):
    def get_intervals(self):
        return self._generate_intervals(6)


class Minor(Aeolian):
    pass


class Locrian(Diatonic):
    def get_intervals(self):
        return self._generate_intervals(7)


class MajorPentatonic(Major):
    """
    Major Pentatonic drops 4th and 7th from the Diatonic Major and
    consists of only 5 notes.
    """

    def get_intervals(self):
        intervals = super(MajorPentatonic, self).get_intervals()
        intervals.pop(6)
        intervals.pop(3)
        return intervals[0:5]


class MinorPentatonic(Minor):
    """
    Minor Pentatonic drops 2nd and 6th from the Diatonic Minor and
    consists of only 5 notes.
    """

    def get_intervals(self):
        intervals = super(MinorPentatonic, self).get_intervals()
        intervals.pop(5)
        intervals.pop(1)
        return intervals[0:5]


class MajorBlues(MajorPentatonic):
    """
    Major Blues is the same as the Major Pentatonic but it adds a
    diminished 4th and consists of 6 notes.
    """

    def get_intervals(self):
        intervals = super(MajorBlues, self).get_intervals()
        intervals.insert(2, Dim(4))
        return intervals


class MinorBlues(MinorPentatonic):
    """
    Minor Blues is the same as the Minor Pentatonic but it adds an
    augmented 5th and consists of 6 notes.
    """

    def get_intervals(self):
        intervals = super(MinorBlues, self).get_intervals()
        intervals.insert(3, Aug(5))
        return intervals


class Chromatic(Scale):
    def get_intervals(self):
        return range(0, 13)


class Octatonic(Scale):

    @classmethod
    def _generate_intervals(cls, tonic):
        """
        Source: https://en.wikipedia.org/wiki/Octatonic_scale
        """
        if tonic not in range(1, 3):
            raise Exception("Tonic must be a number between 1 and 2")
        rot = tonic - 1
        tonal_sequence = [1, 2, 1, 2, 1, 2, 1, 2]
        seq = tonal_sequence[rot:] + tonal_sequence[:rot]
        interval = [0]
        for i, s in enumerate(seq):
            interval.append(s + interval[i])
        return interval


class OctatonicModeOne(Octatonic):
    def get_intervals(self):
        return self._generate_intervals(1)


class OctatonicModeTwo(Octatonic):
    def get_intervals(self):
        return self._generate_intervals(2)


def circle_of_fifths():
    root = 'C'
    scales = []
    while len(scales) < 8:
        scale = Major(Note(root))
        scales.append(scale)
        root = scale[4].get_note_without_octave()
    return scales


def circle_of_fourths():
    root = 'C'
    scales = []
    while len(scales) < 8:
        scale = Major(Note(root))
        scales.append(scale)
        root = scale[3].get_note_without_octave()
    return scales


def major_scales():
    scale = Chromatic('C4')
    scales = []
    for note in scale.notes[:-1]:
        scales.append(Major(note))
    return scales


def minor_scales():
    scale = Chromatic('A4')
    scales = []
    for note in scale.notes[:-1]:
        scales.append(Minor(note))
    return scales
