import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_abc", "_abc,<EOF>", 101))

    def test_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_a", "_a,<EOF>", 102))

    def test_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1a", "Error Token 1", 103))

    def test_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc?svn", "abc,Error Token ?", 104))

    def test_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("duy.tran2903", "duy,Error Token .", 105))

    def test_6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("A", "A,<EOF>", 106))

    def test_7(self):
        """test comment"""
        self.assertTrue(TestLexer.test("//abc", "//abc,<EOF>", 107))

    def test_8(self):
        """test comment"""
        self.assertTrue(TestLexer.test("//ab\nc", "//ab,c,<EOF>", 108))

    def test_9(self):
        """test comment"""
        self.assertTrue(TestLexer.test("/*abc */", "/*abc */,<EOF>", 109))

    def test_10(self):
        """test comment"""
        self.assertTrue(TestLexer.test("/*   @756  abc */   */", "/*   @756  abc */,*/,<EOF>", 110))

    def test_11(self):
        """test intlit"""
        self.assertTrue(TestLexer.test("1_2_34_567", "1234567,<EOF>", 111))

    def test_12(self):
        """test intlit"""
        self.assertTrue(TestLexer.test("1__2_34_5_67", "1234567,<EOF>", 112))

    def test_13(self):
        """test floatlit"""
        self.assertTrue(TestLexer.test("1.234", "1.234,<EOF>", 113))

    def test_14(self):
        """test floatlit"""
        self.assertTrue(TestLexer.test("1.2e3", "1.2e3,<EOF>", 114))

    def test_15(self):
        """test floatlit"""
        self.assertTrue(TestLexer.test("7E-10", "7E-10,<EOF>", 115))

    def test_16(self):
        """test floatlit"""
        self.assertTrue(TestLexer.test("1_234.567e+2", "1234.567e+2,<EOF>", 116))

    def test_17(self):
        """test floatlit"""
        self.assertTrue(TestLexer.test("1_234.", "1234.,<EOF>", 117))

    def test_18(self):
        """test stringlit"""
        self.assertTrue(
            TestLexer.test('"This\'s a string containing tab?"', "This's a string containing tab?,<EOF>", 118)
        )

    def test_19(self):
        """test stringlit"""
        self.assertTrue(TestLexer.test('"...\mbc"', "Illegal Escape In String: ...\mbc,<EOF>", 119))

    def test_20(self):
        """test stringlit"""
        self.assertTrue(TestLexer.test('"...ac@?/"def"', "...ac@?/,Error Token d,<EOF>", 120))

    def test_21(self):
        """test stringlit"""
        self.assertTrue(TestLexer.test('"...a\c@?/"def"', "Illegal Escape In String: ...a\c", 121))

    def test_22(self):
        """test stringlit"""
        self.assertTrue(TestLexer.test('"abdfh - fhgj', "Unclose String: abdfh - fhgj", 122))

    def test_23(self):
        """test stringlit"""
        self.assertTrue(TestLexer.test("?", "Error Token: ?", 123))

    def test_23(self):
        """test stringlit"""
        self.assertTrue(
            TestLexer.test(
                """a, b, c, d: integer = 3, 4, 6;""",
                "",
                124,
            )
        )
