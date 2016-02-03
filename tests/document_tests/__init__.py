from __future__ import unicode_literals

from prompt_toolkit.document import Document

import unittest


class DocumentTest(unittest.TestCase):
    def setUp(self):
        self.document = Document(
            'line 1\n' +
            'line 2\n' +
            'line 3\n' +
            'line 4\n',
            len('line 1\n' + 'lin')
        )

    def test_current_char(self):
        self.assertEqual(self.document.current_char, 'e')

    def test_text_before_cursor(self):
        self.assertEqual(self.document.text_before_cursor, 'line 1\nlin')

    def test_text_after_cursor(self):
        self.assertEqual(self.document.text_after_cursor,
                         'e 2\n' +
                         'line 3\n' +
                         'line 4\n')

    def test_lines(self):
        self.assertEqual(self.document.lines, [
                         'line 1',
                         'line 2',
                         'line 3',
                         'line 4', ''])

    def test_line_count(self):
        self.assertEqual(self.document.line_count, 5)

    def test_current_line_before_cursor(self):
        self.assertEqual(self.document.current_line_before_cursor, 'lin')

    def test_current_line_after_cursor(self):
        self.assertEqual(self.document.current_line_after_cursor, 'e 2')

    def test_current_line(self):
        self.assertEqual(self.document.current_line, 'line 2')

    def test_cursor_position(self):
        self.assertEqual(self.document.cursor_position_row, 1)
        self.assertEqual(self.document.cursor_position_col, 3)

        d = Document('', 0)
        self.assertEqual(d.cursor_position_row, 0)
        self.assertEqual(d.cursor_position_col, 0)

    def test_translate_index_to_position(self):
        pos = self.document.translate_index_to_position(
            len('line 1\nline 2\nlin'))

        self.assertEqual(pos[0], 2)
        self.assertEqual(pos[1], 3)

        pos = self.document.translate_index_to_position(0)
        self.assertEqual(pos, (0, 0))

    def test_getitem(self):
        d = Document('line1\nline2\nline3')
        self.assertEqual(d.lines, ['line1', 'line2', 'line3'])
        self.assertEqual(d._line_start_indexes, [0, 6, 12])

        d2 = d[:10]
        self.assertEqual(d2.text, 'line1\nline')
        self.assertEqual(d2.lines, ['line1', 'line'])
        self.assertEqual(d2._line_start_indexes, [0, 6])

        d3 = d[3:10]
        self.assertEqual(d3.text, 'e1\nline')
        self.assertEqual(d3.lines, ['e1', 'line'])
        self.assertEqual(d3._line_start_indexes, [0, 3])

    def test_concatenate(self):
        d = Document('line1\nline2\nline3')
        self.assertEqual(d.lines, ['line1', 'line2', 'line3'])
        self.assertEqual(d._line_start_indexes, [0, 6, 12])

        d2 = Document('line4\nline5\nline6')
        self.assertEqual(d2.lines, ['line4', 'line5', 'line6'])
        self.assertEqual(d2._line_start_indexes, [0, 6, 12])

        d3 = d + d2
        self.assertEqual(d3.lines, [
            'line1', 'line2', 'line3line4', 'line5', 'line6'])
        self.assertEqual(d3._line_start_indexes, [0, 6, 12, 23, 29])
