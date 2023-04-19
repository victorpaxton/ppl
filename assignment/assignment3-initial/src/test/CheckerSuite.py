import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    #     def test_0(self):
    #         input = """x: integer;"""
    #         expect = """No entry point"""
    #         self.assertTrue(TestChecker.test(input, expect, 400))

    #     def test_1(self):
    #         input = """x: integer;
    # main: function void () {}
    # x: integer;
    #         """
    #         expect = """Redeclared Variable: x"""
    #         self.assertTrue(TestChecker.test(input, expect, 401))

    #     def test_2(self):
    #         input = """x: integer;
    # inc: function integer (i: integer) {
    #     return i + 1;
    # }
    # inc: function integer (i: integer) {
    #     return i - 1;
    # }
    # main: function void () {
    # }
    #         """
    #         expect = """Redeclared Function: inc"""
    #         self.assertTrue(TestChecker.test(input, expect, 402))

    #     def test_3(self):
    #         input = """x: integer;
    # inc: function integer (i: integer) {
    #     return i + 1;
    # }
    # x: function integer (i: integer) {
    #     return i - 1;
    # }
    # main: function void () {
    # }
    #         """
    #         expect = """Redeclared Function: x"""
    #         self.assertTrue(TestChecker.test(input, expect, 403))

    #     def test_4(self):
    #         input = """x: auto;
    #         main: function void () {

    #         }
    #         """
    #         expect = """Invalid Variable: x"""
    #         self.assertTrue(TestChecker.test(input, expect, 404))

    #     def test_5(self):
    #         input = """x: auto = 1;
    #         y: boolean = !x;
    #         x: integer;
    #         main: function void () {

    # }        """
    #         expect = """Type mismatch in expression: UnExpr(!, Id(x))"""
    #         self.assertTrue(TestChecker.test(input, expect, 405))

    #     def test_6(self):
    #         input = """x: auto = true;
    #         y: boolean = !x;
    #         x: integer;
    #         main: function void () {

    #         }
    #         """
    #         expect = """Redeclared Variable: x"""
    #         self.assertTrue(TestChecker.test(input, expect, 406))

    #     def test_7(self):
    #         input = """
    #         x: float = 1;
    #         y: float = x + 1;
    #         z: integer = 3.8;
    #         main: function void () {}
    #         """
    #         expect = """Type mismatch in Variable Declaration: VarDecl(z, IntegerType, FloatLit(3.8))"""
    #         self.assertTrue(TestChecker.test(input, expect, 407))

    #     def test_8(self):
    #         input = """
    #         x: auto = "hello";
    #         y: auto = " world";
    #         z: string = x::y;
    #         t: auto = x + y;
    #         main: function void () {}
    #         """
    #         expect = """Type mismatch in expression: BinExpr(+, Id(x), Id(y))"""
    #         self.assertTrue(TestChecker.test(input, expect, 408))

    #     def test_9(self):
    #         input = """
    #         x: auto = a < 10;
    #         y: boolean = !x;
    #         main: function void () {}
    #         """
    #         expect = """Undeclared Identifier: a"""
    #         self.assertTrue(TestChecker.test(input, expect, 409))

    #     def test_10(self):
    #         input = """
    #         a: auto = "hello";
    #         x: auto = a < 10;
    #         y: boolean = !x;
    #         main: function void () {}
    #         """
    #         expect = """Type mismatch in expression: BinExpr(<, Id(a), IntegerLit(10))"""
    #         self.assertTrue(TestChecker.test(input, expect, 410))

    #     def test_11(self):
    #         input = """
    #         a: auto = 2023.5;
    #         x: auto = a < 10;
    #         y: boolean = x < 1;
    #         main: function void () {}
    #         """
    #         expect = """Type mismatch in expression: BinExpr(<, Id(x), IntegerLit(1))"""
    #         self.assertTrue(TestChecker.test(input, expect, 411))

    #     def test_12(self):
    #         input = """
    #         x: integer = 5/7;
    #         main: function void () {}
    #         """
    #         expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, BinExpr(/, IntegerLit(5), IntegerLit(7)))"""
    #         self.assertTrue(TestChecker.test(input, expect, 412))

    #     def test_13(self):
    #         input = """
    #         a: auto = "hello";
    #         x: auto = a < 10;
    #         y: boolean = !x;
    #         """
    #         expect = """Type mismatch in expression: BinExpr(<, Id(a), IntegerLit(10))"""
    #         self.assertTrue(TestChecker.test(input, expect, 413))

    #     def test_14(self):
    #         input = """
    #         a: auto = 50;
    #         x: auto = a < 10;
    #         y: boolean;
    #         main: function void () {

    #         }
    #         foo: function integer () inherit goo {}
    #         """
    #         expect = """Undeclared Function: goo"""
    #         self.assertTrue(TestChecker.test(input, expect, 414))

    #     def test_15(self):
    #         input = """
    #         main: function void () {

    #         }
    #         foo: function integer (b: integer, c: integer) inherit goo {}
    #         goo: function integer (inherit a: integer, a: integer) {}
    #         """
    #         expect = """Redeclared Parameter: a"""
    #         self.assertTrue(TestChecker.test(input, expect, 415))

    #     def test_16(self):
    #         input = """
    #         main: function void () {

    #         }
    #         foo: function integer (a: integer, c: integer) inherit goo {}
    #         goo: function integer (inherit a: integer) {}
    #         """
    #         expect = """Invalid Parameter: a"""
    #         self.assertTrue(TestChecker.test(input, expect, 416))

    #     def test_17(self):
    #         input = """
    #         a: integer = 3;
    #         main: function void () {

    #         }
    #         foo: function integer (a: integer, c: integer) inherit goo {}
    #         goo: function integer (inherit a: integer, a: integer) {}
    #         """
    #         expect = """Redeclared Parameter: a"""
    #         self.assertTrue(TestChecker.test(input, expect, 417))

    #     def test_18(self):
    #         input = """
    #         a: integer = 3;
    #         main: function void () {

    #         }
    #         foo: function integer (a: integer, c: integer) inherit goo {
    #             super(3, 4, 5);
    #         }
    #         goo: function integer (inherit b: integer, d: float) {}
    #         """
    #         expect = """Type mismatch in expression: IntegerLit(5)"""
    #         self.assertTrue(TestChecker.test(input, expect, 418))

    #     def test_19(self):
    #         input = """
    #         a: integer = 3;
    #         foo: function integer (b: integer) inherit a {
    #             super("abc");
    #         }
    #         a: function string (inherit c: string) {}
    #         """
    #         expect = """Redeclared Function: a"""
    #         self.assertTrue(TestChecker.test(input, expect, 419))

    #     def test_20(self):
    #         input = """
    #         a: integer = 3;
    #         main: function void () {

    #         }
    #         foo: function integer (a: integer, c: integer) inherit goo {
    #             super("abc", 4);
    #         }
    #         goo: function integer (inherit b: integer, d: float) {}
    #         """
    #         expect = """Type mismatch in expression: StringLit(abc)"""
    #         self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """
        a: integer = 3;
        main: function void () {

        }
        foo: function integer (a: integer, c: integer) inherit goo {
            super();
        }
        goo: function integer (inherit b: integer, d: float) {}
        """
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input, expect, 421))

        #     def test_22(self):
        #         input = """
        #         a: integer = 3;
        #         main: function void () {

        #         }
        #         foo: function integer (a: integer, c: integer) inherit goo {
        #         }
        #         goo: function integer () inherit hoo {}
        #         hoo: function void (inherit d: integer) {}
        #         """
        #         expect = """Invalid statement in function: goo"""
        #         self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        input = """
        a: integer = 3;
        main: function void () {

        }
        foo: function integer (a: integer, c: integer) inherit goo {
            super("abc");
        }
        goo: function integer (d: string) inherit hoo {}
        hoo: function void (inherit d: integer) {}
        """
        expect = """Invalid Parameter: d"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    # def test_24(self):
    #     input = """
    #         a: integer = 3;
    #         main: function void () {

    #         }
    #         hoo: function void () {}
    #         foo: function integer (a: integer, c: integer) inherit goo {
    #             hoo();
    #             a = a + 1;
    #         }
    #         goo: function integer (d: string)  {}

    #     """
    #     expect = """Invalid statement in function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 424))

    # def test_25(self):
    #     input = """
    #         a: integer = 3;
    #         main: function void () {

    #         }
    #         foo: function integer (a: integer, c: integer) inherit goo {
    #         }
    #         goo: function integer ()  {}
    #         goo: function void () {}
    #     """
    #     expect = """Redeclared Function: goo"""
    #     self.assertTrue(TestChecker.test(input, expect, 425))

    # def test_26(self):
    #     input = """
    #     a: integer;
    #     b: float;
    #     main: function void () {
    #         b = 6;
    #         a = 5.6;
    #     }
    #     """
    #     expect = """Type mismatch in statement: AssignStmt(Id(a), FloatLit(5.6))"""
    #     self.assertTrue(TestChecker.test(input, expect, 426))

    # def test_27(self):
    #     input = """
    #     foo: function integer () {}
    #     main: function void () {
    #         foo = 5.6;
    #     }
    #     """
    #     expect = """Undeclared Identifier: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 427))

    # def test_28(self):
    #     input = """
    #     foo: function integer () {}
    #     main: function void () {
    #         i: integer = 0;
    #         for (i = 1, i < 5, i+1) {
    #             a: integer = 3;
    #             if (a < 10) {}
    #         }
    #     }
    #     """
    #     expect = """Undeclared Identifier: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 428))

    # def test_29(self):
    #     input = """
    #     x: integer = 1;
    #     a: integer;
    #     foo: function float () {
    #         return 2023;
    #     }
    #     main: function void () {
    #         a = foo(4);
    #     }
    #     """
    #     expect = """Type mismatch in expression: FuncCall(foo, [IntegerLit(4)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 429))

    # def test_30(self):
    #     input = """
    #     x: integer = 1;
    #     foo: function float (x: integer) {
    #         x = x + 1;
    #     }
    #     main: function void () {
    #         foo("ab");
    #     }
    #     """
    #     expect = """Type mismatch in statement: CallStmt(foo, StringLit(ab))"""
    #     self.assertTrue(TestChecker.test(input, expect, 430))

    # def test_31(self):
    #     input = """
    #     x: integer = 1;
    #     foo: function float (x: integer) {
    #         x = x + 1;
    #     }
    #     main: function void () {
    #         foo(5);
    #         goo("ab");
    #     }
    #     """
    #     expect = """Undeclared Function: goo"""
    #     self.assertTrue(TestChecker.test(input, expect, 431))

    # def test_32(self):
    #     input = """
    #     a: integer = 3;
    #     main: function void () {

    #     }
    #     foo: function integer (c: integer) inherit goo {
    #         super(6);
    #         a: integer;
    #     }
    #     goo: function integer (inherit a: integer) {}
    #     """
    #     expect = """Redeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 432))

    # def test_33(self):
    #     input = """
    #     x: integer = 1;
    #     a: integer;
    #     foo: function float (x: integer) {
    #         return 2023;
    #     }
    #     main: function void () {
    #         a = foo();
    #     }
    #     """
    #     expect = """Type mismatch in expression: FuncCall(foo, [])"""
    #     self.assertTrue(TestChecker.test(input, expect, 433))

    # def test_34(self):
    #     input = """
    #     x: integer = 1;
    #     foo: function float (x: integer) {
    #         x = x + 1;
    #     }
    #     main: function void () {
    #         foo();
    #     }
    #     """
    #     expect = """Type mismatch in statement: CallStmt(foo, )"""
    #     self.assertTrue(TestChecker.test(input, expect, 434))

    # def test_35(self):
    #     input = """
    #     x: integer = 1;
    #     foo: function float (x: integer) {
    #         x = x + 1;
    #     }
    #     main: function void () {
    #         foo(5, 6);
    #     }
    #     """
    #     expect = """Type mismatch in statement: CallStmt(foo, IntegerLit(5), IntegerLit(6))"""
    #     self.assertTrue(TestChecker.test(input, expect, 435))

    # def test_36(self):
    #     input = """main: function void () {
    #     x: integer;
    #     for (i = 1, i < 10, i + 1) {
    #         writeInteger(i);
    #     }
    # }"""
    #     expect = """Undeclared Identifier: i"""
    #     self.assertTrue(TestChecker.test(input, expect, 436))

    # def test_37(self):
    #     input = """main: function void () {
    #     i: integer;
    #     for (i = 1, i < 10, i + 1) {
    #         readInteger();
    #         printInteger(i + 5.5);
    #     }
    # }"""
    #     expect = """Type mismatch in statement: CallStmt(printInteger, BinExpr(+, Id(i), FloatLit(5.5)))"""
    #     self.assertTrue(TestChecker.test(input, expect, 437))

    # def test_38(self):
    #     input = """main: function void () {
    #     i: integer;
    #     for (i = 1, i < 10, i + 1) {
    #         readInteger();
    #         printFloat(i);
    #         printString("abc");
    #         printBoolean(true);
    #         readFloat();
    #         readBoolean();
    #         readString();
    #         readInteger(3);
    #     }
    # }"""
    #     expect = """Type mismatch in statement: CallStmt(readInteger, IntegerLit(3))"""
    #     self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = """main: function void () {
        i: integer;
        for (i = 6.7, i < 10, i + 1) {
            readInteger();
            printFloat(i);
        }
    }"""
        expect = """Type mismatch in statement: AssignStmt(Id(i), FloatLit(6.7))"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        input = """main: function void () {
        i: string;
        for (i = "abc", i < 10, i + 1) {
            readInteger();
            printFloat(i);
        }
    }"""
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), StringLit(abc)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(readInteger, ), CallStmt(printFloat, Id(i))]))"""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        input = """main: function void () {
        i: integer;
        for (i = 6, i + 10, i + 1) {
            readInteger();
            printFloat(i);
        }
    }"""
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(6)), BinExpr(+, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(readInteger, ), CallStmt(printFloat, Id(i))]))"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """main: function void () {
        i: integer;
        for (i = 6, i < 10, i + 2.0) {
            readInteger();
            printFloat(i);
        }
    }"""
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(6)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), FloatLit(2.0)), BlockStmt([CallStmt(readInteger, ), CallStmt(printFloat, Id(i))]))"""
        self.assertTrue(TestChecker.test(input, expect, 442))


#     def test_full_vardecl(self):
#         input = """x, y, z: integer = 1, 2, 3;"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(1))
# 	VarDecl(y, IntegerType, IntegerLit(2))
# 	VarDecl(z, IntegerType, IntegerLit(3))
# ])"""
#         self.assertTrue(TestChecker.test(input, expect, 401))

#     def test_vardecls(self):
#         input = """x, y, z: integer = 1, 2, 3;
#         a, b: float;"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(1))
# 	VarDecl(y, IntegerType, IntegerLit(2))
# 	VarDecl(z, IntegerType, IntegerLit(3))
# 	VarDecl(a, FloatType)
# 	VarDecl(b, FloatType)
# ])"""
#         self.assertTrue(TestChecker.test(input, expect, 402))

#     def test_simple_program(self):
#         """Simple program"""
#         input = """main: function void () {
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestChecker.test(input, expect, 403))

#     def test_more_complex_program(self):
#         """More complex program"""
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestChecker.test(input, expect, 404))
