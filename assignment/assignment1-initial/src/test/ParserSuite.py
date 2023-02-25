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

    def test_simple_program(self):
        """Simple program: int main() {}"""
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else {
                a: string = "123";
                return n * fact(n - 1);
            }
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
