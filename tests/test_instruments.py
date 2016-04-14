import unittest

from parker.notes import Note
from parker.instruments import CLEF_TREBLE
from parker.instruments import Instrument
from parker.keys import Key


class TestInstruments(unittest.TestCase):

    def test_constructor(self):
        inst = Instrument()
        self.assertEqual(inst.name, 'Instrument')
        self.assertEqual(inst._note_range, (Note('C0'), Note('C8')))
        self.assertEqual(inst.clef, CLEF_TREBLE)
        self.assertEqual(inst.key, Key('C'))
        self.assertEqual(inst.dist_to_c, -9)

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
