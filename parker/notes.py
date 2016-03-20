from .constants import LOOKUP_FLATS
from .constants import LOOKUP_SHARPS
from .constants import NOTE_MATCHER
from .constants import NOTE_OFFSETS
from .mixins import AugmentDiminishMixin
from .mixins import Aug
from .mixins import Dim
from .mixins import CommonEqualityMixin
from .mixins import NotesMixin
from .mixins import TransposeMixin


class Note(TransposeMixin, CommonEqualityMixin,
           AugmentDiminishMixin):
    """Representation of a single note."""
    _base_name = 'A'
    _octave = 4
    _accidentals = 0

    def __init__(self, note=None, use_sharps=True):
        self.set_note(note, use_sharps=use_sharps)

    def __str__(self):
        accidentals = self.get_accidentals_as_string()
        return "{}{}{:d}".format(self._base_name, accidentals, self._octave)

    def __repr__(self):
        return "{}('{}')".format(type(self).__name__, str(self))

    def __int__(self):
        result = (int(self._octave) + 1) * 12
        result += NOTE_OFFSETS[self._base_name]
        result += self._accidentals
        return int(result)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.__dict__ == other.__dict__:
            return True
        # Notes are identical if their integer value is the same regardless
        # of the base_name, accidentals, and octave.
        if int(self) == int(other):
            return True
        return False

    def set_note(self, note, use_sharps):
        if isinstance(note, int):
            self.set_from_int(note, use_sharps)
        elif isinstance(note, str):
            self.set_from_string(note)
        elif isinstance(note, Note):
            self.set_from_note(note)
        elif note is None:
            self.set_from_string('A4')

    def set_from_int(self, note, use_sharps=True):
        """
        Set the Note from an integer representation

        Example: 60 should return middle C on a piano
                 integer:     60
                 octave:      4
                 offset:      0
                 base_name:   C
                 accidentals: 0
        """
        self._octave = int((note // 12) - 1)
        offset = note - (self._octave + 1) * 12
        lookup = LOOKUP_SHARPS if use_sharps else LOOKUP_FLATS

        # The lookup table only works from 0 - 11, so make sure
        # that the offset matches
        offset = offset % 12
        self._base_name, self._accidentals = lookup[offset]

    def set_from_string(self, note):
        """
        Set the Note from a string representation

        Example: C4 should return middle C on a piano
                 string:      C4
                 octave:      4
                 offset:      0
                 base_name:   C
                 accidentals: 0
        """
        m = NOTE_MATCHER.match(note)
        if m is not None:
            name, accidentals, octave = m.group(1), m.group(2), m.group(3)
            self._base_name = name
            try:
                self._octave = int(octave)
            except (NameError, ValueError):
                self._octave = 4
            self._accidentals = sum(1 if acc == '#' else -1
                                    for acc in accidentals)
            return
        raise Exception("Unknown note format: {}".format(note))

    def set_from_note(self, note):
        """Set the Note from a Note object"""
        self._base_name = note._base_name
        self._octave = note._octave
        self._accidentals = note._accidentals

    def get_base_name(self):
        return self._base_name

    def set_base_name(self, base_name):
        if base_name in 'ABCDEFG':
            self._base_name = base_name
        else:
            raise Exception('Unkown base name: {}'.format(base_name))

    def get_accidentals(self):
        return self._accidentals

    def get_accidentals_as_string(self):
        return ('#' if self._accidentals > 0 else 'b') * abs(self._accidentals)

    def get_frequency(self, ndigits=None):
        """
        Return the frequency of the note.

        This uses the forumula f = f0 * (a ** n)

        f0 - the reference frequency, which is A4 at 440 Hz
        a  - the twelth root of 2, or 2 ** (1/12)
        n  - the number of half steps between notes

        Should rounding be required you can set the number of digits to
        round to in the method.

        Reference:
          - http://www.phy.mtu.edu/~suits/NoteFreqCalcs.html
          - https://en.wikipedia.org/wiki/Scientific_pitch_notation
          - https://en.wikipedia.org/wiki/Music_and_mathematics
        """
        reference = Note('A4')
        if self == reference:
            return 440.0
        ref_freq = reference.get_frequency()
        steps = int(self) - int(reference)
        a = 2.0 ** (1.0 / 12.0)
        note_freq = ref_freq * (a ** steps)

        if isinstance(ndigits, int):
            return round(note_freq, ndigits)
        return note_freq

    def generalize(self):
        """
        Return the note without the octave component.

        Example: C4    -> C
                 Cbb4  -> Cbb
                 C###4 -> C###
        """
        accidentals = self.get_accidentals_as_string()
        return "{}{}".format(self._base_name, accidentals)

    def normalize(self, use_sharps=None):
        """
        Return the note normalized and without the octave component.
        Set use_sharps to control the output.

        Example: C4    -> C
                 Cbb4  -> Bb
                 Cbb4  -> A# (use_sharps=True)
                 C###4 -> D#
                 C###4 => Eb (use_sharps=False)
        """
        if use_sharps is None:
            if 'b' in str(self):
                use_sharps = False
            else:
                use_sharps = True
        return Note(int(self), use_sharps).generalize()

    def set_accidentals(self, accidentals):
        self._accidentals = int(accidentals)

    def get_octave(self):
        return self._octave

    def set_octave(self, octave):
        if not isinstance(octave, int):
            try:
                octave = int(octave)
            except ValueError:
                raise Exception("Unknown octave format: {}".format(octave))
        if not (0 < octave < 9):
            raise Exception("Octave must be 0 through 9")
        self._octave = octave

    def set_transpose(self, amount):
        acc = self._accidentals
        transpose_amount = None
        if isinstance(amount, int):
            transpose_amount = amount
        elif isinstance(amount, (Aug, Dim)):
            transpose_amount = amount.amount
        else:
            raise Exception("Cannot transpose from '{}'".format(amount))
        use_sharps = transpose_amount % 12 in [0, 2, 4, 7, 9, 11]
        self.set_from_int(int(self) - acc + transpose_amount, use_sharps)
        self._accidentals += acc

        # The amount to update could given by a Aug or Dim class
        if isinstance(amount, (Aug, Dim)):
            amount.update(self)
        return self

    def set_augment(self):
        self._accidentals += 1
        return self

    def set_diminish(self):
        self._accidentals -= 1
        return self


class NotesParser(object):
    """
    Parse notes of any type into a list of notes.
    Valid notes are: Note, NoteGroup, int, str, list, tuple, set.
    """

    @staticmethod
    def parse(notes):
        if isinstance(notes, Note):
            return [notes.clone()]
        elif isinstance(notes, NoteGroup):
            return notes.clone().notes
        elif isinstance(notes, (int, str)):
            return [Note(notes)]
        elif isinstance(notes, (list, tuple, set)):
            result = []
            for n in notes:
                result.extend(NotesParser.parse(n))
            return result
        elif notes is None:
            return []
        raise Exception("Cannot parse notes: {}".format(str(notes)))


class NoteGroupBase(TransposeMixin, CommonEqualityMixin,
                    AugmentDiminishMixin, NotesMixin):
    """
    Representation of a set of notes to be played at the same time.
    An example of a NoteGroup would be a chord (1, 3, 5) played on a piano.

    The base class does not let you add notes.
    """
    notes = []

    def set_transpose(self, amount):
        return self.walk(lambda n: n.set_transpose(amount))

    def set_augment(self):
        return self.walk(lambda n: n.set_augment())

    def set_diminish(self):
        return self.walk(lambda n: n.set_diminish())

    def get_notes(self):
        return sorted(self.notes, key=int)

    def __getitem__(self, key):
        return self.notes[key]

    def __str__(self):
        return str(self.notes)

    def __repr__(self):
        return "{}({})".format(type(self).__name__, str(self))

    def __len__(self):
        return len(self.notes)


class NoteGroup(NoteGroupBase):
    """
    A mutable set of notes to be played at the same time.
    """

    def __init__(self, notes=None):
        self.notes = []
        self.add(notes)

    def add(self, notes):
        self.notes.extend(NotesParser.parse(notes))
        return self

    def append(self, item):
        return self.add(item)
