import collections
import random
import re


# Reference: https://en.wikipedia.org/wiki/Scientific_pitch_notation
# Notes should be formated with three pieces of information
# The first group is the note, always capitalized from A to G
# The second group is the accidentals, any number of # or b symbols
# The third group is the octave, which must be a digit between 0 and 9
NOTE_MATCHER = re.compile("^([A|B|C|D|E|F|G]{1})([#|b]*)(-?[0-9]*)$")

# Chords are formatted like notes but include a trailing group
# which defines the type of chord
CHORD_MATCHER = re.compile("^([A|B|C|D|E|F|G]{1}[#|b]*[0-9]{0,1})(.*)$")

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

ORDER_OF_SHARPS = ['F', 'C', 'G', 'D', 'A', 'E', 'B']
ORDER_OF_FLATS = ORDER_OF_SHARPS[::-1]

MNEMONIC_ORDER_OF_SHARPS = random.choice([
    "Fat Cats Go Down Alleys Eating Birds",
    "Father Charles Goes Down And Ends Battle",
])
MNEMONIC_ORDER_OF_FLATS = random.choice([
    "Boys Eat All Day Girls Can Fly",
    "Battle Ends And Down Goes Charles' Father",
])
MNEMONIC_CIRCLE_OF_FIFTHS = random.choice([
    "Caroline Goes Down And Eats Butter Fly Costumes",
])
MNEMONIC_CIRCLE_OF_FOURTHS = random.choice([
    "Caroline Finds B E A Ds Gone Cold",
])

MAJOR_KEYS = collections.OrderedDict(sorted({
    'Cb': -7,
    'Gb': -6,
    'Db': -5,
    'Ab': -4,
    'Eb': -3,
    'Bb': -2,
    'F': -1,
    'C': 0,
    'G': 1,
    'D': 2,
    'A': 3,
    'E': 4,
    'B': 5,
    'F#': 6,
    'C#': 7,
    }.items(), key=lambda n: n[1]))

MINOR_KEYS = collections.OrderedDict(sorted({
    'ab': -7,
    'eb': -6,
    'bb': -5,
    'f': -4,
    'c': -3,
    'g': -2,
    'd': -1,
    'a': 0,
    'e': 1,
    'b': 2,
    'f#': 3,
    'c#': 4,
    'g#': 5,
    'd#': 6,
    'a#': 7,
    }.items(), key=lambda n: n[1]))
