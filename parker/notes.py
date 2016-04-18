import math

from .constants import LOOKUP_FLATS
from .constants import LOOKUP_SHARPS
from .constants import NOTE_MATCHER
from .constants import NOTE_OFFSETS
from .constants import SIGN_FLAT
from .constants import SIGN_HALF_FLAT
from .constants import SIGN_HALF_SHARP
from .constants import SIGN_SHARP
from .constants import VALID_NOTES
from .mixins import AugmentDiminishMixin
from .mixins import Aug
from .mixins import Dim
from .mixins import CommonEqualityMixin
from .mixins import NotesMixin
from .mixins import TransposeMixin


def is_valid_note(note):
    """
    Determine if a note is valid from a given string representation.
    """
    m = NOTE_MATCHER.match(note)
    if m is not None:
        return True
    return False


class Accidental(CommonEqualityMixin):

    def __init__(self, acc=''):
        self._name = ''
        self._alter = 0.0
        self.set_from_str(acc)

    def set_from_str(self, acc):
        alter = 0.0
        for char in acc:
            if char == SIGN_SHARP:
                alter += 1.0
            elif char == SIGN_FLAT:
                alter -= 1.0
            elif char == SIGN_HALF_SHARP:
                alter += 0.5
            elif char == SIGN_HALF_FLAT:
                alter -= 0.5
        self.set_from_num(alter)

    def set_from_num(self, alter):
        self.alter = float(alter)
        full = ''
        if self.alter > 0:
            full = SIGN_SHARP * int(abs(math.floor(self.alter)))
        else:
            full = SIGN_FLAT * int(abs(math.ceil(self.alter)))
        half = ''
        if self._alter % 1:
            half = (SIGN_HALF_SHARP if self.alter > 0 else SIGN_HALF_FLAT)
        self.name = '{0}{1}'.format(full, half)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "{0}('{1}')".format(type(self).__name__, str(self))

    def __int__(self):
        return int(self._alter)

    def __float__(self):
        return self._alter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def alter(self):
        return self._alter

    @alter.setter
    def alter(self, value):
        self._alter = value

    def set_augment(self):
        alter = self.alter + 1
        self.set_from_num(alter)
        return self

    def set_diminish(self):
        alter = self.alter - 1
        self.set_from_num(alter)
        return self


class Note(TransposeMixin, CommonEqualityMixin,
           AugmentDiminishMixin):
    """Representation of a single note."""
    _base_name = 'A'
    _octave = 4
    _accidentals = 0

    def __init__(self, note=None, use_sharps=True):
        self._set_note(note, use_sharps=use_sharps)

    def __str__(self):
        return "{0}{1}{2:d}".format(self._base_name,
                                    self.accidentals,
                                    self._octave)

    def __repr__(self):
        return "{0}('{1}')".format(type(self).__name__, str(self))

    def __int__(self):
        return int(float(self))

    def __float__(self):
        result = (float(self._octave) + 1) * 12
        result += float(NOTE_OFFSETS[self._base_name])
        if self._base_name == 'C' and int(self.accidentals) == -1:
            result += 12
        result += float(self.accidentals)
        return result

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.__dict__ == other.__dict__:
            return True
        # Notes are identical if their integer value is the same regardless
        # of the base_name, accidentals, and octave.
        if float(self) == float(other):
            return True
        return False

    def __le__(self, other):
        if float(self) <= float(other):
            return True
        return False

    def __lt__(self, other):
        if float(self) < float(other):
            return True
        return False

    def __ge__(self, other):
        if float(self) >= float(other):
            return True
        return False

    def __gt__(self, other):
        if float(self) > float(other):
            return True
        return False

    def __add__(self, other):
        """
        Addition is a function of semitones and simply returns the sum
        of the semitones of each Note object.
        """
        return float(self) + float(other)

    def __sub__(self, other):
        """
        Addition is a function of semitones and simply returns the difference
        of the semitones of each Note object.
        """
        return float(self) - float(other)

    def _set_note(self, note, use_sharps):
        if isinstance(note, (int, float)):
            self._set_from_num(note, use_sharps)
        elif isinstance(note, str):
            self._set_from_string(note)
        elif isinstance(note, Note):
            self._set_from_note(note)
        elif note is None:
            self._set_from_string('A4')

    def _set_from_num(self, note, use_sharps=True):
        """
        Set the Note from an integer representation

        Example:
                 60 should return middle C on a piano
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
        offset_remainder = offset % 1
        offset = math.floor(offset % 12)
        self._base_name, acc_lookup = lookup[offset]
        self.accidentals = acc_lookup + offset_remainder

    def _set_from_string(self, note):
        """
        Set the Note from a string representation

        Example:
                 C4 should return middle C on a piano
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
            self.accidentals = accidentals
            return
        raise Exception("Unknown note format: {0}".format(note))

    def _set_from_note(self, note):
        """Set the Note from a Note object"""
        self._base_name = note._base_name
        self._octave = note._octave
        self.accidentals = note.accidentals

    @property
    def base_name(self):
        return self._base_name

    @base_name.setter
    def base_name(self, base_name):
        if base_name in VALID_NOTES:
            self._base_name = base_name
        else:
            raise Exception('Unkown base name: {0}'.format(base_name))

    @property
    def accidentals(self):
        return self._accidentals

    @accidentals.setter
    def accidentals(self, accidentals):
        if isinstance(accidentals, Accidental):
            self._accidentals = accidentals
        elif isinstance(accidentals, (int, float)):
            acc = Accidental()
            acc.set_from_num(accidentals)
            self._accidentals = acc
        else:
            self._accidentals = Accidental(accidentals)

    @property
    def octave(self):
        return self._octave

    @octave.setter
    def octave(self, octave):
        if not isinstance(octave, int):
            try:
                octave = int(octave)
            except ValueError:
                raise Exception("Unknown octave format: {0}".format(octave))
        if not (0 < octave < 9):
            raise Exception("Octave must be 0 through 9")
        self._octave = octave

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
        steps = self - reference
        a = 2.0 ** (1.0 / 12.0)
        note_freq = ref_freq * (a ** steps)

        if isinstance(ndigits, int):
            return round(note_freq, ndigits)
        return note_freq

    def generalize(self):
        """
        Return the note without the octave component.

        Example:
                 C4    -> C
                 Cbb4  -> Cbb
                 C###4 -> C###
        """
        return "{0}{1}".format(self._base_name, self.accidentals)

    def normalize(self, use_sharps=None):
        """
        Return the note normalized and without the octave component.
        Set use_sharps to control the output.

        Example:
                 C4    -> C
                 Cbb4  -> Bb
                 Cbb4  -> A# (use_sharps=True)
                 C###4 -> D#
                 C###4 => Eb (use_sharps=False)
        """
        if use_sharps is None:
            if SIGN_FLAT in str(self):
                use_sharps = False
            else:
                use_sharps = True
        return Note(float(self), use_sharps).generalize()

    def set_transpose(self, amount):
        """
        Modify the note by a given number of semitones.

        In some instances the letters 't' or 'A' may be used to designate a
        change of 10 pitch classes.  Similarly 'e' or 'B' may be used to
        designate a change of 11 pitch classes.

        References:
          - https://en.wikipedia.org/wiki/Pitch_class
          - https://en.wikipedia.org/wiki/List_of_chords
        """
        transpose_amount = None
        if isinstance(amount, (int, float)):
            transpose_amount = amount
        elif isinstance(amount, str):
            if amount in 'tA':
                transpose_amount = 10
            elif amount in 'eB':
                transpose_amount = 11
            else:
                raise Exception("Cannot transpose from '{0}'".format(amount))
        elif isinstance(amount, (Aug, Dim)):
            transpose_amount = amount.amount
        else:
            raise Exception("Cannot transpose from '{0}'".format(amount))
        use_sharps = transpose_amount % 12 in [0, 2, 4, 7, 9, 11]
        self._set_from_num(float(self) + transpose_amount, use_sharps)

        # The amount to update could given by a Aug or Dim class
        if isinstance(amount, (Aug, Dim)):
            amount.update(self)
        return self

    def set_augment(self):
        self.accidentals.set_augment()
        return self

    def set_diminish(self):
        self.accidentals.set_diminish()
        return self


def note_from_frequency(freq):
    """
    Return the closest note given a frequency value in Hz

    This uses the forumula f = f0 * (a ** n)

    f0 - the reference frequency, which is A4 at 440 Hz
    a  - the twelth root of 2, or 2 ** (1/12)
    n  - the number of half steps between notes

    Here we want the value of n, or the integer value
    of half steps distance from the reference note.

    n = log(f / f0) / log(a)

    This does not take into account out of tune notes. In the future it might
    make sense to return the cents above or below the note.
    """
    reference = Note('A4')
    ref_freq = reference.get_frequency()
    a = 2.0 ** (1.0 / 12.0)
    steps = math.log(freq / ref_freq) / math.log(a)
    steps = int(round(steps))
    note_int = reference + steps
    return Note(note_int)


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
        elif isinstance(notes, (int, float, str)):
            return [Note(notes)]
        elif isinstance(notes, (list, tuple, set)):
            result = []
            for n in notes:
                result.extend(NotesParser.parse(n))
            return result
        elif notes is None:
            return []
        raise Exception("Cannot parse notes: {0}".format(str(notes)))


class NoteGroupBase(TransposeMixin, CommonEqualityMixin,
                    AugmentDiminishMixin, NotesMixin):
    """
    Representation of a set of notes to be played at the same time.
    An example of a NoteGroup would be a chord (1, 3, 5) played on a piano.

    The base class does not let you add notes.
    """
    root = None
    notes = []

    def set_transpose(self, amount):
        return self.walk(lambda n: n.set_transpose(amount))

    def set_augment(self):
        return self.walk(lambda n: n.set_augment())

    def set_diminish(self):
        return self.walk(lambda n: n.set_diminish())

    def get_notes(self):
        return sorted(self.notes, key=float)

    def __getitem__(self, key):
        return self.notes[key]

    def __str__(self):
        return str(self.notes)

    def __repr__(self):
        return "{0}({1})".format(type(self).__name__, str(self))

    def __len__(self):
        return len(self.notes)


class NoteGroup(NoteGroupBase):
    """
    A mutable set of notes to be played at the same time.
    """

    def __init__(self, notes=None):
        self.notes = []
        self.add(notes)
        if len(self.notes) > 0:
            self.root = self.notes[0].clone()

    def add(self, notes):
        self.notes.extend(NotesParser.parse(notes))
        return self

    def append(self, item):
        return self.add(item)
