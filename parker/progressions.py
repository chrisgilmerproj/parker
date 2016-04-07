

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

    def _get_chord_triad(self, lookup):
        note = self.scale.notes[lookup]
        sc_type = PROGRESSION_LOOKUP[lookup]
        ch_str = '{}{}'.format(note.generalize(), sc_type)
        return Chord(ch_str)

    def _get_chord_seventh(self, lookup):
        note = self.scale.notes[lookup]
        sc_type = PROGRESSION_LOOKUP[lookup]
        ch_str = '{}{}7'.format(note.generalize(), sc_type)
        return Chord(ch_str)

    def I(self):
        return self._get_chord_triad(0)

    def II(self):
        return self._get_chord_triad(1)

    def III(self):
        return self._get_chord_triad(2)

    def IV(self):
        return self._get_chord_triad(3)

    def V(self):
        return self._get_chord_triad(4)

    def VI(self):
        return self._get_chord_triad(5)

    def VII(self):
        return self._get_chord_triad(6)

    def I7(self):
        return self._get_chord_seventh(0)

    def II7(self):
        return self._get_chord_seventh(1)

    def III7(self):
        return self._get_chord_seventh(2)

    def IV7(self):
        return self._get_chord_seventh(3)

    def V7(self):
        return self._get_chord_seventh(4)

    def VI7(self):
        return self._get_chord_seventh(5)

    def VII7(self):
        return self._get_chord_seventh(6)

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
