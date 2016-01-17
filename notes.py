"""
This is mostly a reconstruction of work from another library so I can
understand how it was done.  All credit here:

https://github.com/bspaans/python-mingus/blob/mingus-oo/mingus/notes.py
"""

import copy
import re

# Notes should be formated with three pieces of information
# The first group is the note, always capitalized from A to G
# The second group is the accidentals, any number of # or b symbols
# The third group is the octave, which must be a digit between 0 and 9
NOTE_MATCHER = re.compile("^(A|B|C|D|E|F|G)([#|b]*)([0-9]*)$")

# 
NOTE_OFFSETS = {
    'C': 0,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 7,
    'A': 9,
    'B': 11
}

# A lookup hash for notes with sharps when working from an offset from a given
# octave.  If the note is middle C on a piano, C4, then the integer would be
# 60 and the offset would be 0.  So the return here would be the note 'C' and
# the number of accidentals would be 0.  If the note was D#4 then then the
# integer would be 63, the offset would be 3, returning the note 'D' and the
# number of accidentals would be 1.
LOOKUP_SHARPS = {
  0: ('C', 0),
  1: ('C', 1),
  2: ('D', 0),
  3: ('D', 1),
  4: ('E', 0),
  5: ('F', 0),
  6: ('F', 1),
  7: ('G', 0),
  8: ('G', 1),
  9: ('A', 0),
  10: ('A', 1),
  11: ('B', 0),
}

# Simliar to LOOKUP_SHARPS, this will return the same information except for
# flats.  An example would be D#4, which is also Eb4.  If the integer is 63
# then the offset would be 3, returning 'E' and the number of accidentals
# would be -1.
LOOKUP_FLATS = {
  0: ('C', 0),
  1: ('D', -1),
  2: ('D', 0),
  3: ('E', -1),
  4: ('E', 0),
  5: ('F', 0),
  6: ('G', -1),
  7: ('G', 0),
  8: ('A', -1),
  9: ('A', 0),
  10: ('B', -1),
  11: ('C', -1),
}


class Note(object):
    _base_name = 'A'
    _octave = 4
    _accidentals = 0
    _duration = 0

    def __init__(self, note=None):
        self.set_note(note)

    def __str__(self):
        accidentals = self.get_accidentals_as_string()
        return "{}{}{}".format(self._base_name, accidentals, self._octave)

    def __repr__(self):
        return str(self)

    def __int__(self):
        result = (int(self._octave) + 1) * 12
        result += NOTE_OFFSETS[self._base_name]
        result += self._accidentals
        return result

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def clone(self):
        return copy.deepcopy(self)

    def set_note(self, note):
        if type(note) == int:
            self.set_from_int(note)
        elif type(note) == str:
            self.set_from_string(note)
        elif isinstance(note, Note):
            self.set_from_note(note)

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
        self._octave = (note / 12) - 1
        offset = note - (self._octave + 1) * 12
        lookup = LOOKUP_SHARPS if use_sharps else LOOKUP_FLATS
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
            octave = octave if octave.isdigit() else "4"
            self._octave = int(octave)
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
        self._base_name = base_name

    def get_accidentals(self):
        return self._accidentals

    def get_accidentals_as_string(self):
        return ('#' if self._accidentals > 0 else 'b') * abs(self._accidentals)

    def set_accidentals(self, accidentals):
        self._accidentals = accidentals

    def get_octave(self):
        return self._octave

    def set_octave(self, octave):
        if not type(octave, int):
            try:
                octave = int(octave)
            except NameError:
                raise Exception("Unknown octave format: {}".format(octave))
        if not (0 < octave < 9):
            raise Exception("Octave must be 0 through 9")
        self._octave = octave

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    def augment(self):
        self._accidentals += 1
        return self

    def diminish(self):
        self._accidentals -= 1
        return self
