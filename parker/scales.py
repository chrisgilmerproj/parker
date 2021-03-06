from .mixins import Aug
from .mixins import Dim
from .mixins import OctaveMixin
from .notes import Note
from .notes import NoteGroupBase


class Scale(NoteGroupBase, OctaveMixin):
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
            raise Exception("Order must be one of: {0}".format(
                            self.ORDER_CHOICES))
        self.build_scale()

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        if self.order == self.DESCENDING:
            return "{0}('{1}', order='{2}')".format(type(self).__name__,
                                                    str(self), self.DESCENDING)
        else:
            return "{0}('{1}')".format(type(self).__name__, str(self))

    def __eq__(self, other):
        # Scales must be of the same class or derived from the Scale class
        if not (isinstance(other, self.__class__) or isinstance(other, Scale)):
            return False
        if self.__dict__ == other.__dict__:
            return True
        # Scales are identical if their generic notes are also identical
        if self.generic_notes == other.generic_notes:
            return True
        return False

    def build_scale(self):
        intervals = self.intervals
        self.notes = self.root.transpose_list(intervals)
        if self.order == self.DESCENDING:
            self.notes.reverse()

        # Get a list of the notes without the octave
        generic_notes = [n.normalize(use_sharps=True)
                         for n in self.notes]
        self.generic_notes = set(generic_notes)

    @property
    def intervals(self):
        return [0]

    def get_whole_half_construction(self):
        intervals = self.intervals
        if len(intervals) < 2:
            return []

        wh = []
        current = intervals[0]
        for i in intervals[1:]:
            if isinstance(i, Aug):
                diff = i.amount + 1 - current
                current = i.amount + 1
            elif isinstance(i, Dim):
                diff = i.amount - 1 - current
                current = i.amount - 1
            else:
                diff = i - current
                current = i
            if diff == 2:
                wh.append('W')
            elif diff == 1:
                wh.append('H')
            else:
                wh.append(diff)
        return wh

    def get_tone_semitone_construction(self):
        wh = self.get_whole_half_construction()
        ts = []
        for current in wh:
            if current == 'W':
                ts.append('T')
            elif current == 'H':
                ts.append('s')
            else:
                ts.append(current)
        return ts

    def is_generic_note_in_scale(self, note):
        if isinstance(note, str):
            return note in self.generic_notes
        if isinstance(note, Note):
            gen_note = Note(int(note)).generalize()
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
    @property
    def intervals(self):
        return self._generate_intervals(1)


class Major(Ionian):
    pass


class HarmonicMajor(Major):
    @property
    def intervals(self):
        intervals = self._generate_intervals(1)
        intervals[6] -= 1
        return intervals


class Dorian(Diatonic):
    @property
    def intervals(self):
        return self._generate_intervals(2)


class Phrygian(Diatonic):
    @property
    def intervals(self):
        return self._generate_intervals(3)


class PhrygianDominant(Diatonic):
    @property
    def intervals(self):
        intervals = self._generate_intervals(3)
        intervals[2] += 1
        return intervals


class MedievalLydian(Diatonic):
    @property
    def intervals(self):
        return self._generate_intervals(4)


class Lydian(Diatonic):
    """
    The Lydian scale can be described as a major scale with the fourth scale
    degree raised a semitone, e.g., a C-major scale with an F# rather than
    F-natural.

    Source: https://en.wikipedia.org/wiki/Lydian_mode
    """
    @property
    def intervals(self):
        return self._generate_intervals(4, aug_dim_cls=[(3, Aug)])


class Mixolydian(Diatonic):
    @property
    def intervals(self):
        return self._generate_intervals(5)


class Dominant(Mixolydian):
    pass


class Aeolian(Diatonic):
    @property
    def intervals(self):
        return self._generate_intervals(6)


class Minor(Aeolian):
    pass


class NaturalMinor(Minor):
    pass


class HarmonicMinor(Minor):
    @property
    def intervals(self):
        intervals = self._generate_intervals(6)
        intervals[6] += 1
        return intervals


class MelodicMinor(Minor):
    @property
    def intervals(self):
        intervals = self._generate_intervals(6)
        intervals[5] += 1
        intervals[6] += 1
        return intervals


class Locrian(Diatonic):
    @property
    def intervals(self):
        return self._generate_intervals(7)


class SuperLocrian(Diatonic):
    @property
    def intervals(self):
        intervals = self._generate_intervals(7)
        intervals[3] -= 1
        return intervals


class MajorPentatonic(Major):
    """
    Major Pentatonic drops 4th and 7th from the Diatonic Major and
    consists of only 5 notes.
    """

    @property
    def intervals(self):
        intervals = super(MajorPentatonic, self).intervals
        intervals.pop(6)
        intervals.pop(3)
        return intervals[0:5]


class MinorPentatonic(Minor):
    """
    Minor Pentatonic drops 2nd and 6th from the Diatonic Minor and
    consists of only 5 notes.
    """

    @property
    def intervals(self):
        intervals = super(MinorPentatonic, self).intervals
        intervals.pop(5)
        intervals.pop(1)
        return intervals[0:5]


class MajorBlues(MajorPentatonic):
    """
    Major Blues is the same as the Major Pentatonic but it adds a
    diminished 4th and consists of 6 notes.
    """

    @property
    def intervals(self):
        intervals = super(MajorBlues, self).intervals
        intervals.insert(2, Dim(4))
        return intervals


class MinorBlues(MinorPentatonic):
    """
    Minor Blues is the same as the Minor Pentatonic but it adds an
    augmented 5th and consists of 6 notes.
    """

    @property
    def intervals(self):
        intervals = super(MinorBlues, self).intervals
        intervals.insert(3, Aug(5))
        return intervals


class Altered(Scale):

    @classmethod
    def _generate_intervals(cls, tonic):
        """
        Source: https://en.wikipedia.org/wiki/Altered_scale

        s-T-s-T-T-T-T
        """
        if tonic not in range(1, 8):
            raise Exception("Tonic must be a number between 1 and 7")
        rot = tonic - 1
        tonal_sequence = [1, 2, 1, 2, 2, 2, 2]
        seq = tonal_sequence[rot:] + tonal_sequence[:rot]
        interval = [0]
        for i, s in enumerate(seq):
            interval.append(s + interval[i])
        return interval

    @property
    def intervals(self):
        return self._generate_intervals(1)


class DiminishedWholeTone(Altered):
    pass


class Chromatic(Scale):
    @property
    def intervals(self):
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
    @property
    def intervals(self):
        return self._generate_intervals(1)


class HalfWholeDiminished(OctatonicModeOne):
    pass


class OctatonicModeTwo(Octatonic):
    @property
    def intervals(self):
        return self._generate_intervals(2)


class WholeHalfDiminished(OctatonicModeTwo):
    pass


def circle_of_fifths():
    root = 'C'
    scales = []
    while len(scales) < 8:
        scale = Major(Note(root))
        scales.append(scale)
        root = scale[4].generalize()
    return scales


def circle_of_fourths():
    root = 'C'
    scales = []
    while len(scales) < 8:
        scale = Major(Note(root))
        scales.append(scale)
        root = scale[3].generalize()
    return scales


def _scale_creator(scale_cls, root='C4'):
    scale = Chromatic(root)
    scales = []
    for note in scale.notes[:-1]:
        scales.append(scale_cls(note))
    return scales


def dorian_scales(root='C4'):
    return _scale_creator(Dorian, root=root)


def mixolydian_scales(root='C4'):
    return _scale_creator(Mixolydian, root=root)


def major_scales(root='C4'):
    return _scale_creator(Major, root=root)


def minor_scales(root='C4'):
    return _scale_creator(Minor, root=root)


def major_pentatonic_scales(root='C4'):
    return _scale_creator(MajorPentatonic, root=root)


def minor_pentatonic_scales(root='C4'):
    return _scale_creator(MinorPentatonic, root=root)


def major_blues_scales(root='C4'):
    return _scale_creator(MajorBlues, root=root)


def minor_blues_scales(root='C4'):
    return _scale_creator(MinorBlues, root=root)
