Tutorial 01 - Notes
===================

The basic building block of any music is the note.  A note is defined by its
name, octave, and accidentals.  Let's play with notes:

>>> from parker.notes import Note


----


Notes objects
-------------

A note can be easily constructed from a valid note name.  Let's try a few:


>>> n = Note('C4')
>>> print(n)
C4
>>> repr(n)
"Note('C4')"


You'll notice immediately that the note that was returned says `C4` instead of
`C`.  This is because the default octave will be the middle or fourth (4)
octave of the scale.  It also has no accidentals (sharps or flats).

There are a lot of valid notes that you can construct:


>>> note_list = ['C', 'C4', 'C#4', 'Cbb4']
>>> print([Note(note) for note in note_list])
[Note('C4'), Note('C4'), Note('C#4'), Note('Cbb4')]


Suprisingly you can use some very interesting notes:


>>> Note('C######bb')
Note('C####4')
>>> Note('C#b#bb##b##bb')
Note('C4')


Notes as Integers
-----------------

Notes can also be represented as integers:


>>> int(Note('C4'))
60


Constructing Notes
------------------

You can construct notes using strings, integers, and other Note objects.


Modifying Notes
---------------

Augmenting or Diminishing Notes


Other Reprentations
-------------------

Normalization vs Generalization


