
from .keys import Key
from .notes import Note

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
    _dist_to_c = 0
    clef = CLEF_TREBLE
    key = Key('C')

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

    def transpose_note(self, note, key=None):
        if not key:
            key = Key('C')
        note_to_c = Note(note).transpose(self._dist_to_c)
        note_to_key = note_to_c.transpose(Note('C4') - Note(key.key))
        return note_to_key

    def transpose_to_c(self):
        return [note.transpose(self._dist_to_c) for note in self.note_range]


class TrebleClefInstrument(Instrument):
    name = 'TrebleClefInstrument'
    clef = CLEF_TREBLE


class BassClefInstrument(Instrument):
    name = 'BassClefInstrument'
    clef = CLEF_BASS


class CInstrument(TrebleClefInstrument):
    name = 'CInstrument'


class BbInstrument(TrebleClefInstrument):
    name = 'BbInstrument'
    key = Key('Bb')


class EbInstrument(TrebleClefInstrument):
    name = 'EbInstrument'
    key = Key('Eb')


class FInstrument(TrebleClefInstrument):
    name = 'FInstrument'
    key = Key('F')


class SopranoSaxophone(BbInstrument):
    name = 'SopranoSaxophone'
    _dist_to_c = -2
    _note_range = (Note('Bb2'), Note('F#5'))


class AltoSaxophone(EbInstrument):
    name = 'AltoSaxophone'
    _dist_to_c = -9
    _note_range = (Note('Bb3'), Note('F5'))


class TenorSaxophone(BbInstrument):
    name = 'TenorSaxophone'
    _dist_to_c = -14
    _note_range = (Note('Bb2'), Note('F#5'))


class BaritoneSaxophone(EbInstrument):
    name = 'BaritoneSaxophone'
    _dist_to_c = -20
    _note_range = (Note('Bb2'), Note('F#5'))
