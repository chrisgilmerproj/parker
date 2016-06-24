from .chords import Chord
from .constants import PROG_LOOKUP
from .constants import PROG_MATCHER
from .constants import SIGN_FLAT
from .constants import SIGN_SHARP
from .notes import Note
from .scales import Major


def is_valid_progression(note):
    """
    Determine if a progression is valid from a given string representation.
    """
    m = PROG_MATCHER.match(note)
    if m is not None:
        return True
    return False


class Progression(object):
    """
    Reference: https://en.wikipedia.org/wiki/Roman_numeral_analysis
    """

    def __init__(self, root, scale_cls=Major):
        self.root = Note(root)
        self.scale_cls = scale_cls
        self.scale = scale_cls(self.root)

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        if self.scale_cls != Major:
            return "{0}('{1}', scale_cls={2})".format(type(self).__name__,
                                                      str(self),
                                                      self.scale_cls.__name__)
        else:
            return "{0}('{1}')".format(type(self).__name__, str(self))

    def __call__(self, progression):
        """
        From an instantiated class call the from_string() method directly
        """
        return self.from_string(progression)

    def _get_chord(self, lookup, extension='', accidental=None):
        """
        Get chord for progression from a lookup index number.

        The extension helps determine the format.
        """
        note = self.scale.notes[lookup]
        if accidental == SIGN_FLAT:
            note.set_diminish()
        elif accidental == SIGN_SHARP:
            note.set_augment()
        ch_str = '{0}{1}'.format(note.generalize(), extension)
        return Chord(ch_str)

    def standard_triads(self):
        prog_list = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii']
        return self.from_list(prog_list, as_map=True)

    def standard_sevenths(self):
        prog_list = ['I7', 'ii7', 'iii7', 'IV7', 'V7', 'vi7', 'vii7']
        return self.from_list(prog_list, as_map=True)

    def all_progressions(self):
        p_types = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
        extensions = ['', '7']
        progressions = {}
        for p in p_types:
            for ext in extensions:
                prog_str = '{0}{1}'.format(p, ext)
                progressions[prog_str] = self.from_string(prog_str)
                prog_str = prog_str.lower()
                progressions[prog_str] = self.from_string(prog_str)
        return progressions

    def from_string(self, progression):
        """
        Take a string representation of a progression and return the chord
        that it represents.
        """
        m = PROG_MATCHER.match(progression)
        if not m:
            msg = "Progression '{0}' not recognized".format(progression)
            raise Exception(msg)
        accidental, prog, extension = m.groups()

        index = PROG_LOOKUP[prog.upper()]
        ch_type = ''
        if not extension:
            if prog in ['VII', 'vii']:
                ch_type = 'dim'
            elif prog.isupper():
                ch_type = 'M'
            elif prog.islower():
                ch_type = 'm'
        else:
            if prog.islower():
                ch_type = 'm'
        ch_str = '{0}{1}'.format(ch_type, extension)
        return self._get_chord(index, ch_str, accidental=accidental)

    def from_list(self, prog_list, as_map=False):
        """
        Take a list of progressions and return the list of chords.

        Setting `as_map` to True will return the progressions as a dictionary
        where the keys are the progressions passed in and the values are the
        chords.
        """
        if as_map:
            return dict(zip(prog_list, self.from_list(prog_list)))
        return [self.from_string(prog) for prog in prog_list]
