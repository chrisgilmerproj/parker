import unittest

from parker.notes import Note
from parker.instruments import CLEF_TREBLE
from parker.instruments import AltoSaxophone
from parker.instruments import BaritoneSaxophone
from parker.instruments import Instrument
from parker.instruments import SopranoSaxophone
from parker.instruments import TenorSaxophone
from parker.keys import Key


class TestInstruments(unittest.TestCase):

    def test_constructor(self):
        inst = Instrument()
        self.assertEqual(inst.name, 'Instrument')
        self.assertEqual(inst._note_range, (Note('C0'), Note('C8')))
        self.assertEqual(inst.clef, CLEF_TREBLE)
        self.assertEqual(inst.key, Key('C'))
        self.assertEqual(inst._dist_to_c, 0)

    def test_str(self):
        inst = Instrument()
        self.assertEqual(str(inst), 'Instrument')

    def test_repr(self):
        inst = Instrument()
        self.assertEqual(repr(inst), 'Instrument()')

    def test_set_note_range(self):
        inst = Instrument()
        self.assertEqual(inst._note_range, (Note('C0'), Note('C8')))
        inst.note_range = (Note('C1'), Note('C9'))
        self.assertEqual(inst._note_range, (Note('C1'), Note('C9')))

    def test_in_range(self):
        inst = Instrument()
        self.assertTrue(inst.in_range('C4'))

    def test_transpose_note(self):
        inst = TenorSaxophone()
        self.assertEquals(inst.transpose_note('D4'), Note('C3'))
        self.assertEquals(inst.transpose_note('D4', Key('Bb')), Note('D2'))
        self.assertEquals(inst.transpose_note('D4', Key('Eb')), Note('A2'))
        self.assertEquals(inst.transpose_note('D4', Key('F')), Note('G2'))

    def test_transpose_to_c(self):
        self.assertEquals(SopranoSaxophone().transpose_to_c(),
                          [Note('Ab2'), Note('E5')])
        self.assertEquals(AltoSaxophone().transpose_to_c(),
                          [Note('Db3'), Note('Ab4')])
        self.assertEquals(TenorSaxophone().transpose_to_c(),
                          [Note('Ab1'), Note('E4')])
        self.assertEquals(BaritoneSaxophone().transpose_to_c(),
                          [Note('D1'), Note('A#3')])
