import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {}"""
    #     input = """main: function void() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 201))

    def test_simple_program(self):
        """Simple program: int main() {}"""
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 202))
