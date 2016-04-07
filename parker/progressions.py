

from .chords import Chord
from .scales import Major


PROGRESSION_LOOKUP = {
    0: 'M',
    1: 'm',
    2: 'm',
    3: 'M',
    4: 'M',
    5: 'm',
    6: 'dim',
}


class Progression(object):

    def __init__(self, scale):
        self.scale = Major(scale)

    def _get_chord(self, lookup, extension=''):
        """
        Get chord for progression from a lookup index number.

        The extension helps determine the dominant.
        """
        note = self.scale.notes[lookup]
        sc_type = PROGRESSION_LOOKUP[lookup]
        ch_str = '{}{}{}'.format(note.generalize(), sc_type, extension)
        return Chord(ch_str)

    def I(self):
        return self._get_chord(0)

    def II(self):
        return self._get_chord(1)

    def III(self):
        return self._get_chord(2)

    def IV(self):
        return self._get_chord(3)

    def V(self):
        return self._get_chord(4)

    def VI(self):
        return self._get_chord(5)

    def VII(self):
        return self._get_chord(6)

    def I7(self):
        return self._get_chord(0, '7')

    def II7(self):
        return self._get_chord(1, '7')

    def III7(self):
        return self._get_chord(2, '7')

    def IV7(self):
        return self._get_chord(3, '7')

    def V7(self):
        return self._get_chord(4, '7')

    def VI7(self):
        return self._get_chord(5, '7')

    def VII7(self):
        return self._get_chord(6, '7')

    def all_progressions(self):
        return {'I': self.I(),
                'II': self.II(),
                'III': self.III(),
                'IV': self.IV(),
                'V': self.V(),
                'VI': self.VI(),
                'VII': self.VII(),
                'I7': self.I7(),
                'II7': self.II7(),
                'III7': self.III7(),
                'IV7': self.IV7(),
                'V7': self.V7(),
                'VI7': self.VI7(),
                'VII7': self.VII7(),
                }
