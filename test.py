import generate
import unittest
import json
import os


class TestGenerateHtml(unittest.TestCase):

    def test_read(self):

        expected = ({"layout": "base.html",
                     "title": "Contact us!"
                     },
                    'Write an email to contact@example.com.')
        result = generate.read_file('test/source/contact.rst')
        self.assertEqual(result[0]['title'], expected[0]['title'])
        self.assertEqual(result[0]['layout'], expected[0]['layout'])
        self.assertEqual(result[1], expected[1])

    def test_empty_read(self):

        file = open('empty_file.rst', 'w')
        file.write('{}')
        f = file.close()
        result = generate.read_file('empty_file.rst')
        expected = ({}, '')
        self.assertEqual(result[0], expected[0])
        self.assertEqual(result[1], expected[1])

    def test_list(self):
        result = [x for x in generate.list_files('test/source')]
        expected = [('test/source/contact.rst', 'contact'),
                    ('test/source/index.rst', 'index')
                    ]
        self.assertEqual(result, expected)

    def test_list_with_no_rst_file(self):
        expected = [('test/source/contact.rst', 'contact'),
                    ('test/source/index.rst', 'index')]
        file = open('test/source/no_rst.txt', 'w')
        f = file.close()
        result = [x for x in generate.list_files('test/source')]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
