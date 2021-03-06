"""
Data structures for the selection.
"""
from __future__ import unicode_literals

__all__ = (
    'SelectionType',
    'SelectionState',
)


class SelectionType(object):
    """
    Type of selection.
    """
    #: Characters. (Visual in Vi.)
    CHARACTERS = 'characters'

    #: Whole lines. (Visual-Line in Vi.)
    LINES = 'lines'

    #: A block selection. (Visual-Block in Vi.)
    BLOCK = 'block'


class SelectionState(object):
    """
    State of the current selection.

    :param original_cursor_position: int
    :param type: :class:`~.SelectionType`
    """
    def __init__(self, original_cursor_position=0, type=SelectionType.CHARACTERS):
        self.original_cursor_position = original_cursor_position
        self.type = type

    def __repr__(self):
        return '{0!s}(original_cursor_position={1!r}, type={2!r})'.format(
            self.__class__.__name__,
            self.original_cursor_position, self.type)
