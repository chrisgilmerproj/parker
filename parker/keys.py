from .constants import MAJOR_KEYS
from .constants import MINOR_KEYS
from .constants import ORDER_OF_FLATS
from .constants import ORDER_OF_SHARPS
from .constants import SIGN_FLAT
from .constants import SIGN_SHARP
from .notes import Note
from .scales import Major
from .scales import Minor


class Key(object):
    """
    Reference: https://en.wikipedia.org/wiki/Key_(music)
    """
    MAJOR = 'major'
    MINOR = 'minor'

    def __init__(self, key='C'):
        self.key = key

        self.mode = self.MINOR if key.islower() else self.MAJOR
        if self.mode == self.MAJOR:
            self.signature = MAJOR_KEYS[self.key]
        elif self.mode == self.MINOR:
            self.signature = MINOR_KEYS[self.key]

        if self.signature >= 0:
            self.sign = SIGN_SHARP
            self.accidentals = ORDER_OF_SHARPS[:abs(self.signature)]
        elif self.signature < 0:
            self.sign = SIGN_FLAT
            self.accidentals = ORDER_OF_FLATS[:abs(self.signature)]

    def __str__(self):
        return "{0} {1}".format(self.key, self.mode)

    def __repr__(self):
        return "{0}('{1}')".format(type(self).__name__, str(self.key))

    def is_major(self):
        return self.mode == self.MAJOR

    def is_minor(self):
        return self.mode == self.MINOR

    def get_accidental_notes(self):
        return [Note('{0}{1}'.format(n, self.sign)) for n in self.accidentals]

    def get_scale(self):
        if self.is_major():
            return Major(self.key)
        else:
            return Minor(self.key.upper())
