import unittest

from parker.mixins import AugmentDiminishMixin
from parker.mixins import Aug
from parker.mixins import Dim
from parker.mixins import CloneMixin
from parker.mixins import CommonEqualityMixin
from parker.mixins import NotesMixin
from parker.mixins import TransposeMixin
from parker.notes import Note


class TestAugmentDiminishMixin(unittest.TestCase):

    def test_set_augment_raises(self):
        ad = AugmentDiminishMixin()
        with self.assertRaises(NotImplementedError):
            ad.set_augment()

    def test_augment_raises(self):
        ad = AugmentDiminishMixin()
        with self.assertRaises(NotImplementedError):
            ad.augment()

    def test_set_diminish_raises(self):
        ad = AugmentDiminishMixin()
        with self.assertRaises(NotImplementedError):
            ad.set_diminish()

    def test_diminish_raises(self):
        ad = AugmentDiminishMixin()
        with self.assertRaises(NotImplementedError):
            ad.diminish()


class TestAug(unittest.TestCase):

    def test_constructor(self):
        aug = Aug(7)
        self.assertEqual(aug.amount, 7)

    def test_update(self):
        n = Note()
        aug = Aug(7)
        aug.update(n)
        self.assertEqual(int(n), 70)


class TestDim(unittest.TestCase):

    def test_constructor(self):
        dim = Dim(7)
        self.assertEqual(dim.amount, 7)

    def test_update(self):
        n = Note()
        dim = Dim(7)
        dim.update(n)
        self.assertEqual(int(n), 68)


class TestCloneMixin(unittest.TestCase):

    def test_clone(self):
        class A(CloneMixin):
            pass
        a = A()
        b = a.clone()
        self.assertNotEqual(id(a), id(b))


class TestCommonEqualityMixin(unittest.TestCase):

    def setUp(self):
        class CEM(CommonEqualityMixin):
            def __init__(self, val):
                self.val = val
        self.cem1 = CEM('C4')
        self.cem2 = CEM('C4')
        self.cem3 = CEM('F4')

    def test_equality(self):
        self.assertTrue(self.cem1 == self.cem2)

    def test_inequality(self):
        self.assertTrue(self.cem1 != self.cem3)


class TestNotesMixin(unittest.TestCase):
    def setUp(self):
        class NewNote(NotesMixin):
            def get_notes(self):
                return ['C4', 'F4']
        self.nn = NewNote()

    def test_get_notes_raises(self):
        nm = NotesMixin()
        with self.assertRaises(NotImplementedError):
            nm.get_notes()

    def test_lowest_note(self):
        self.assertEqual(self.nn.lowest_note(), 'C4')

    def test_highest_note(self):
        self.assertEqual(self.nn.highest_note(), 'F4')

    def test_walk(self):
        ob = self.nn.walk(str)
        self.assertEqual(ob, self.nn)


class TestTransposeMixin(unittest.TestCase):

    def test_set_transpose_raises(self):
        tm = TransposeMixin()
        with self.assertRaises(NotImplementedError):
            tm.set_transpose(7)
