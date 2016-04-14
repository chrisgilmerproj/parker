

from .notes import Note
from .keys import Key


# Reference: https://en.wikipedia.org/wiki/Clef
CLEF_G_TREBLE = 'g_treble'
CLEF_G_FRENCH_VIOLIN = 'g_french_violin'
CLEF_F_BASS = 'f_bass'
CLEF_F_BARITONE = 'f_baritone'
CLEF_F_SUB_BASS = 'f_sub_bass'
CLEF_C_ALTO = 'c_alto'
CLEF_C_TENOR = 'c_tenor'
CLEF_C_BARITONE = 'c_baritone'
CLEF_C_MEZZO_SOPRANO = 'c_mezzo_soprano'
CLEF_C_SOPRANO = 'c_saprano'
CLEF_OCTAVE = 'octave'
CLEF_NEUTRAL = 'neutral'
CLEF_TABULATURE = 'tabulature'

CLEF_TREBLE = CLEF_G_TREBLE
CLEF_BASS = CLEF_F_BASS


class Instrument(object):
    """
    Instrument descriptor
    """
    name = 'Instrument'
    _note_range = (Note('C0'), Note('C8'))
    clef = CLEF_TREBLE
    key = Key('C')
    dist_to_c = -9

    def __str__(self):
        return self.name

    def __repr__(self):
        return "{0}()".format(type(self).__name__)

    @property
    def note_range(self):
        return self._note_range

    @note_range.setter
    def note_range(self, note_range):
        """Set the range of the instrument.

        A range is a tuple of two Notes or note strings.
        """
        low_note, high_note = note_range
        self._note_range = (Note(low_note), Note(high_note))

    def in_range(self, note):
        return self.note_range[0] <= Note(note) <= self.note_range[1]


class BbInstrument(Instrument):
    name = 'BbInstrument'
    key = Key('Bb')


class EbInstrument(Instrument):
    name = 'EbInstrument'
    key = Key('Eb')


class FInstrument(Instrument):
    name = 'FInstrument'
    key = Key('F')


class BassClefInstrument(Instrument):
    name = 'BassClefInstrument'
    clef = CLEF_BASS


class TenorSaxophone(BbInstrument):
    name = 'TenorSaxophone'
    _note_range = (Note('Bb2'), Note('F#5'))
