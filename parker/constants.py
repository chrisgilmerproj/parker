import re


# Notes should be formated with three pieces of information
# The first group is the note, always capitalized from A to G
# The second group is the accidentals, any number of # or b symbols
# The third group is the octave, which must be a digit between 0 and 9
NOTE_MATCHER = re.compile(r"^(A|B|C|D|E|F|G)([#|b]*)([0-9]*)$")

# Chords are formatted like notes but include a trailing group
# which defines the type of chord
CHORD_MATCHER = re.compile(r"^([A|B|C|D|E|F|G][#|b]*[0-9]*)(.*)$")

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
