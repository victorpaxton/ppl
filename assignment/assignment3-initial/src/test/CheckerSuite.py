import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_0(self):
        input = """x: integer;"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_1(self):
        input = """x: integer;
main: function void () {}
x: integer;
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """x: integer;
inc: function integer (i: integer) {
    return i + 1;
}
inc: function integer (i: integer) {
    return i - 1;
}
main: function void () {
}
        """
        expect = """Redeclared Function: inc"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        input = """x: integer;
inc: function integer (i: integer) {
    return i + 1;
}
x: function integer (i: integer) {
    return i - 1;
}
main: function void () {
}
        """
        expect = """Redeclared Function: x"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """x: auto;
        main: function void () {

        }
        """
        expect = """Invalid Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5(self):
        input = """x: auto = 1;
        y: boolean = !x;
        x: integer;
        main: function void () {

}        """
        expect = """Type mismatch in expression: UnExpr(!, Id(x))"""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_6(self):
        input = """x: auto = true;
        y: boolean = !x;
        x: integer;
        main: function void () {

        }
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_7(self):
        input = """
        x: float = 1;
        y: float = x + 1;
        z: integer = 3.8;
        main: function void () {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(z, IntegerType, FloatLit(3.8))"""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        input = """
        x: auto = "hello";
        y: auto = " world";
        z: string = x::y;
        t: auto = x + y;
        main: function void () {}
        """
        expect = """Type mismatch in expression: BinExpr(+, Id(x), Id(y))"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_9(self):
        input = """
        x: auto = a < 10;
        y: boolean = !x;
        main: function void () {}
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_10(self):
        input = """
        a: auto = "hello";
        x: auto = a < 10;
        y: boolean = !x;
        main: function void () {}
        """
        expect = """Type mismatch in expression: BinExpr(<, Id(a), IntegerLit(10))"""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """
        a: auto = 2023.5;
        x: auto = a < 10;
        y: boolean = x < 1;
        main: function void () {}
        """
        expect = """Type mismatch in expression: BinExpr(<, Id(x), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        input = """
        x: integer = 5/7;
        main: function void () {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, BinExpr(/, IntegerLit(5), IntegerLit(7)))"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """
        a: auto = "hello";
        x: auto = a < 10;
        y: boolean = !x;
        """
        expect = """Type mismatch in expression: BinExpr(<, Id(a), IntegerLit(10))"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_14(self):
        input = """
        a: auto = 50;
        x: auto = a < 10;
        y: boolean;
        main: function void () {

        }
        foo: function integer () inherit goo {}
        """
        expect = """Undeclared Function: goo"""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = """
        main: function void () {

        }
        foo: function integer (b: integer, c: integer) inherit goo {}
        goo: function integer (inherit a: integer, a: integer) {}
        """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_16(self):
        input = """
        main: function void () {

        }
        foo: function integer (a: integer, c: integer) inherit goo {}
        goo: function integer (inherit a: integer) {}
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """
        a: integer = 3;
        main: function void () {

        }
        foo: function integer (a: integer, c: integer) inherit goo {}
        goo: function integer (inherit a: integer, a: integer) {}
        """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        input = """
        a: integer = 3;
        main: function void () {

        }
        foo: function integer (a: integer, c: integer) inherit goo {
            super(3, 4, 5);
        }
        goo: function integer (inherit b: integer, d: float) {}
        """
        expect = """Type mismatch in expression: IntegerLit(5)"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """
        a: integer = 3;
        foo: function integer (b: integer) inherit a {
            super("abc");
        }
        a: function string (inherit c: string) {}
        """
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """
        a: integer = 3;
        main: function void () {

        }
        foo: function integer (a: integer, c: integer) inherit goo {
            super("abc", 4);
        }
        goo: function integer (inherit b: integer, d: float) {}
        """
        expect = """Type mismatch in expression: StringLit(abc)"""
        self.assertTrue(TestChecker.test(input, expect, 420))

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

    def test_22(self):
        input = """
        a: integer = 3;
        main: function void () {

        }
        foo: function integer (a: integer, c: integer) inherit goo {
        }
        goo: function integer () inherit hoo {}
        hoo: function void (inherit d: integer) {}
        """
        expect = """Invalid statement in function: goo"""
        self.assertTrue(TestChecker.test(input, expect, 422))

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

    def test_24(self):
        input = """
            a: integer = 3;
            main: function void () {

            }
            hoo: function void () {}
            foo: function integer (a: integer, c: integer) inherit goo {
                hoo();
                a = a + 1;
            }
            goo: function integer (d: string)  {}

        """
        expect = """Invalid statement in function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        input = """
            a: integer = 3;
            main: function void () {

            }
            foo: function integer (a: integer, c: integer) inherit goo {
            }
            goo: function integer ()  {}
            goo: function void () {}
        """
        expect = """Redeclared Function: goo"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        input = """
        a: integer;
        b: float;
        main: function void () {
            b = 6;
            a = 5.6;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), FloatLit(5.6))"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """
        foo: function integer () {}
        main: function void () {
            foo = 5.6;
        }
        """
        expect = """Undeclared Identifier: foo"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """
        foo: function integer () {}
        main: function void () {
            i: integer = 0;
            for (i = 1, i < 5, i+1) {
                a: integer = 3;
                if (a < 10) {printInteger(foo);}
            }
        }
        """
        expect = """Undeclared Identifier: foo"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        input = """
        x: integer = 1;
        a: integer;
        foo: function float () {
            return 2023;
        }
        main: function void () {
            a = foo(4);
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [IntegerLit(4)])"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input = """
        x: integer = 1;
        foo: function float (x: integer) {
            x = x + 1;
        }
        main: function void () {
            foo("ab");
        }
        """
        expect = """Type mismatch in statement: CallStmt(foo, StringLit(ab))"""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        input = """
        x: integer = 1;
        foo: function float (x: integer) {
            x = x + 1;
        }
        main: function void () {
            foo(5);
            goo("ab");
        }
        """
        expect = """Undeclared Function: goo"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        input = """
        a: integer = 3;
        main: function void () {

        }
        foo: function integer (c: integer) inherit goo {
            super(6);
            a: integer;
        }
        goo: function integer (inherit a: integer) {}
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        input = """
        x: integer = 1;
        a: integer;
        foo: function float (x: integer) {
            return 2023;
        }
        main: function void () {
            a = foo();
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_34(self):
        input = """
        x: integer = 1;
        foo: function float (x: integer) {
            x = x + 1;
        }
        main: function void () {
            foo();
        }
        """
        expect = """Type mismatch in statement: CallStmt(foo, )"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        input = """
        x: integer = 1;
        foo: function float (x: integer) {
            x = x + 1;
        }
        main: function void () {
            foo(5, 6);
        }
        """
        expect = """Type mismatch in statement: CallStmt(foo, IntegerLit(5), IntegerLit(6))"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input = """main: function void () {
        x: integer;
        for (i = 1, i < 10, i + 1) {
            writeInteger(i);
        }
    }"""
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """main: function void () {
        i: integer;
        for (i = 1, i < 10, i + 1) {
            readInteger();
            printInteger(i + 5.5);
        }
    }"""
        expect = """Type mismatch in statement: CallStmt(printInteger, BinExpr(+, Id(i), FloatLit(5.5)))"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        input = """main: function void () {
        i: integer;
        for (i = 1, i < 10, i + 1) {
            readInteger();
            printFloat(i);
            printString("abc");
            printBoolean(true);
            readFloat();
            readBoolean();
            readString();
            readInteger(3);
        }
    }"""
        expect = """Type mismatch in statement: CallStmt(readInteger, IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input, expect, 438))

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

    def test_43(self):
        input = """x: integer = 2;
        main: function void () {
            if (x>0) {
                if (x % 2 == 0) {
                    printString("Even positive number");
                }
                else
                    printString("Odd positive number");
            }
            else if (x + 0)
                printString("Negative number") ;
            }"""
        expect = """Type mismatch in statement: IfStmt(BinExpr(+, Id(x), IntegerLit(0)), CallStmt(printString, StringLit(Negative number)))"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        input = """x: boolean = true && false && 5 == 7;
        main: function void () {
            if (x) {
            }
            else if (x > 0)
                printString("Negative number") ;
        }"""
        expect = """Type mismatch in expression: BinExpr(&&, BinExpr(&&, BooleanLit(True), BooleanLit(False)), IntegerLit(5))"""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        input = """x: boolean = true && false && (5 == 7);
        main: function void () {
            if (x) {
            }
            else if (x > 0)
                printString("Negative number") ;
        }"""
        expect = """Type mismatch in expression: BinExpr(>, Id(x), IntegerLit(0))"""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        input = """
        main: function void () {
            i: integer = 1;
            while (i < 10) {
                printInteger(i);
                i = i + 1;
                if (i == 5) break;
                printString(5);
                }}
        """
        expect = """Type mismatch in statement: CallStmt(printString, IntegerLit(5))"""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        input = """
        main: function void () {
            while (i < 10) {
                i: integer = 1;
                printInteger(i);
                i = i + 1;
                if (i == 5) break;
                printString(5);
                }}
        """
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_48(self):
        input = """
        main: function void () {
            i: integer = 1;
            while (i < 10) {
                printInteger(i);
                i = i + 1;
                }
            if (i == 5) break;
        }

        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_49(self):
        input = """
        main: function void () {
            i: integer = 1;
            while (i < 10) {
                printInteger(i);
                i = i + 1;
                continue;
                }
            if (i == 5) continue;
        }

        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        input = """
        inc: function integer (num: integer, delta: integer) {
                    return num + delta;
                }
        main: function void () {
            result: float = inc(2022, 1);
            printInteger(result);
        }
        """
        expect = """Type mismatch in statement: CallStmt(printInteger, Id(result))"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
        input = """
        inc: function integer (num: integer, delta: integer) {
                    return num + delta;
                }
        main: function void () {
            result: float = inc;
            printInteger(result);
        }
        """
        expect = """Undeclared Identifier: inc"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_52(self):
        input = """
        inc: function integer (num: integer, delta: integer) {
                    return num + delta;
                }
        main: function void () {
            inc: integer = 5;
            result: integer = inc(2023, 1);
            printInteger(result);
        }

        """
        expect = """Undeclared Function: inc"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        input = """
        inc : function void (out n : integer, n: float) inherit foo{
        super(0.1, 1);
        n: string = 124;
}
foo : function auto (inherit n: float, b: integer){}
        """
        expect = """Redeclared Parameter: n"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_54(self):
        input = """
        foo: function void (b: auto, c: auto){
    a: string = b % c;
}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(%, Id(b), Id(c)))"""
        self.assertTrue(TestChecker.test(input, expect, 454))

    # ?????????????????????????
    # b,c -> int/float type or b,c still auto type

    def test_55(self):
        input = """
        foo: function void (b: auto, c: auto){
    a: string = b / c;
}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(/, Id(b), Id(c)))"""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_56(self):
        input = """
        // This is a comment
        main: function void () {
            myPI: float = 3.14;
            r, s: integer;
            r = 2;
            s = r * r * myPI;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI)))"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        input = """
        concatString: function string (s1: string, s2: string) {
                return s1::s2;
                return s1 + s2;
                res: string = s1::s2;
                return res;
                res: string = s1 + s2;
            }
            main: function void () {
                printString(concatString("abc","def"));
                }
        """
        expect = """Redeclared Variable: res"""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_58(self):
        input = """
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n / fact(n - 1);
        }
        main: function void() {
            delta: integer = fact(3);
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(BinExpr(/, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))])))"""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_59(self):
        input = """
        check: function boolean (n: integer){
    sum, i: integer = 0, 1;//khai bao biem sum
    for(i=1,i<=n/2,i+1){
        if(n%i==0) sum = sum+i;
    }
    if(sum==n) return 1; // tra ve true
    return 0;
}
main: function void () {

}
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_60(self):
        input = """
    check: function boolean (n: integer) {
        sum, i: integer = 0, 1;//khai bao biem sum
        for(i=1,i<=n/2,i+1){
            if(n%i==0) sum = sum+i;
        }
        if(sum==n) return true; // tra ve true
        return false;
    }

    main: function void () {
        n: integer;
        printString("Nhap n: ");
        n = readInteger();
        if(check(n))
            printString("n la so hoan hao");
        else
            printString("n khong phai la so hoan hao.");
        return 2023;
    }
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(2023))"""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input = """

        getSum: function integer(n: integer)
    {
        sum: integer = 0;
        while (n != 0) {
            sum = sum + n % 10;
            n = n / 10;
        }
        return sum;
    }
    main: function void () {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(n), BinExpr(/, Id(n), IntegerLit(10)))"""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_62(self):
        input = """

checkYear: function boolean (year: integer)
{
    // If a year is multiple of 400,
    // then it is a leap year
    if (year % 400 == 0)
        return true;

    // Else If a year is multiple of 100,
    // then it is not a leap year
    if (year % 100 == 0)
        return false;

    // Else If a year is multiple of 4,
    // then it is a leap year
    if (year % 4 == 0)
        return true;
    return false;
}

main: function void () {
    year: integer = 2023;
    printBoolean(checkYear(year));
    return 23;
}
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(23))"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_63(self):
        input = """
/* Returns 1 if n is a lucky no.
otherwise returns 0*/
isLucky: function boolean (n: integer)
{
    counter: integer = 2;

    if (counter > n)
        return true;
    if (n % counter == 0)
        return false;

    /*calculate next position of input no.
        Variable "next_position" is just for
    readability of the program we can
    remove it and update in "n" only */
    next_position: integer = n - (n / counter);

    counter = counter + 1;
    return isLucky(next_position);
}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(next_position, IntegerType, BinExpr(-, Id(n), BinExpr(/, Id(n), Id(counter))))"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_64(self):
        input = """
        squareRoot: function float (n: float)
    {
        /*We are using n itself as initial approximation
            This can definitely be improved */
        x, y, e: float = n, 1.0, 0.000001;
        while (x - y > e) {
            x = (x + y) / 2;
            y = n / x;
        }
        return x;
    }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_65(self):
        input = """
        x: integer = 2023;
        main: function void () {
            printInteger(inc(2023, 2024));
            inc: integer = 2023;
            return inc;
        }
        inc: function integer (value: integer, delta: integer) {
            res: integer = value + delta;
            return res;
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(Id(inc))"""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_66(self):
        input = """
        arr: array [2, 3] of integer = {{5, 7, 5}, {4, 5, {7}}};
        main: function void () {

        }
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(5), IntegerLit(7), IntegerLit(5)]), ArrayLit([IntegerLit(4), IntegerLit(5), ArrayLit([IntegerLit(7)])])])"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_67(self):
        input = """
        arr: array [2] of integer = {{5}, {6}};
        main: function void () {

        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(5)]), ArrayLit([IntegerLit(6)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_68(self):
        input = """
        arr: array [2, 3, 2] of integer = {{{4, 8},{2, 4},{1, 6}}, {{3, 6},{5, 4},{9, 3}}};
        arr2: array [2, 1] of float = {{1.0},{2.0}};
        arr3: array [2, 1] of float = {{1.0},{2}};
        main: function void () {

        }
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([IntegerLit(2)])])"""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_69(self):
        input = """
        arr: array [2, 3, 2] of integer = {{{4, 8},{2, 4},{1, 6}}, {{3, 6},{5, 4},{9, 3}}};
        main: function void () {
            temp: integer = arr[1, 2, 1];
            temp1: array [2] of integer = arr[1, 2];
            temp2: array [3, 2] of integer = arr[1];
            temp4: auto = arr[];
            temp3: auto = arr[1, 2, 3, 4];
        }
        """
        expect = """Type mismatch in expression: ArrayCell(arr, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        input = """
        main: function void () {
            arr: array [2,3,2] of integer = {{{4, 8},{2, 4},{1, 6}}, {{3, 6},{5, 4},{9, 3}}};
            i, j, k: integer;
            for (i = 0, i < 2, i+1)
                for (j = 0, j < 3, j+1)
                    for (k = 0, k < 2, k + 1) {
                        printInteger(arr[i, j, k]);
                        continue;
                    }

            break;
        }
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_71(self):
        input = """
        // function to return sum of elements
// in an array of size n
sum: function integer (arr: array [4] of integer, n: integer)
{
    sum, i: integer = 0, 0; // initialize sum

    // Iterate through all elements
    // and add them to sum
    for (i = 0, i < n, i+1)
        sum = sum + arr[i];

    return sum;
}

main: function void ()
{
    arr: array [4] of integer = { 12, 3, 4, 15 };
    n: integer = 4;
    printInteger(sum(arr, n));

    arr2: array [5] of integer = { 12, 3, 4, 15, 5 };
    res: integer = sum(arr2, 5);
}
        """
        expect = """Type mismatch in expression: FuncCall(sum, [Id(arr2), IntegerLit(5)])"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_72(self):
        input = """
        // C function to find maximum in arr[] of size n
largest: function integer (arr: array [4] of integer, n: integer)
{
    i: integer;

    // Initialize maximum element
    max: integer = arr[0];

    // Traverse array elements from second and
    // compare every element with current max
    for (i = 1, i < n, i+1)
        if (arr[i] > max)
            max = arr[i];

    return max;
}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_73(self):
        input = """
        // Recursive function to search x in arr[]
elmntSrch: function integer (arr: array [4] of integer, size: integer, x: integer) {
    rec: integer;

    size = size - 1;

    if (size >= 0) {
        if (arr[size] == x)
            return size;
        else
            rec = elmntSrch(arr, size, x);
    }
    else
        return -1;

    return rec;
}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_74(self):
        input = """
        mulMat: function void (mat1: array [2, 2] of integer, mat2: array [2, 2] of integer)
{
    rslt: array [2, 2] of integer;

    printString("Multiplication of given two matrices is:\\n");

    i, j ,k : integer = 0, 0, 0;
    for (i = 0, i < 2, i+1) {
        for (j = 0, j < 2, j+1) {
            rslt[i, j] = 0;

            for (k = 0, k < 2, k+1) {
                rslt[i,j] = rslt[i,j] + mat1[i,k] * mat2[k,j];
            }

            printInteger(rslt[i, j]);
        }
        printString("\\n");
        printInteger(rslt[i]);
    }
}
        """
        expect = """Type mismatch in statement: CallStmt(printInteger, ArrayCell(rslt, [Id(i)]))"""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_75(self):
        input = """
    /* prints element and NGE pair for all elements of
    arr[] of size n */
    printNGE: function void (arr: array [4] of integer, n: integer)
    {
        next, i, j: integer;
        for (i = 0, i < n, i+1) {
            next = -1;
            for (j = i + 1, j < n, j+1) {
                if (arr[i] < arr[j]) {
                    next = arr[j];
                    break;
                }
            }
            printInteger(arr[i]);
            printInteger(next);
        }
    }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_76(self):
        input = """
    binarySearch: function integer (arr: array [4] of integer, l: integer, r:integer, x:integer)
    {
        if (r >= l) {
            mid: float = l + (r - l) / 2;

            // If the element is present at the middle
            // itself
            if (arr[mid] == x)
                return mid;

            // If element is smaller than mid, then
            // it can only be present in left subarray
            if (arr[mid] > x)
                return binarySearch(arr, l, mid - 1, x);

            // Else the element can only be present
            // in right subarray
            return binarySearch(arr, mid + 1, r, x);
        }

        // We reach here when element is not
        // present in array
        return -1;
    }
        """
        expect = """Type mismatch in expression: ArrayCell(arr, [Id(mid)])"""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self):
        input = """
            /* Function to sort an array using insertion sort*/
    insertionSort: function void (arr: array [4] of integer, n: integer)
    {
        i, key, j: integer;
        for (i = 1, i < n, i+1) {
            key = arr[i];
            j = i - 1;

            /* Move elements of arr[0..i-1], that are
                greater than key, to one position ahead
                of their current position */
            while ((j >= 0 )&& (arr[j] > key)) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_78(self):
        input = """
        foo: function auto () {
            
        }
        a: integer = foo();
        b: string = foo();
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, StringType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_79(self):
        input = """
        a: function auto (b: integer)  {
            return b;
        }
        foo: function auto (c: auto) {
            return c;
        }
        goo: function auto (p: auto) {
            return p;
        }
        main: function void () {
            res: integer = foo(a(2023));
            res2: float = goo("abc") + 3.5;
        }
        """

        expect = """Type mismatch in expression: BinExpr(+, FuncCall(goo, [StringLit(abc)]), FloatLit(3.5))"""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_80(self):
        input = """
        foo: function integer () inherit goo {
        }
        goo: function integer () {
            super();
        }
        """
        expect = """Undeclared Function: super"""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input = """
        foo: function auto (b: auto){
            return b;
}
main: function void () {
    x: string = foo(2);

}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(x, StringType, FuncCall(foo, [IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_82(self):
        input = """
        sum: function float (n: integer)
{
    i, s: float = 0.0, 0.0;
    for (i = 1, i <= n, i+1)
    s = s + 1/i;
    return s;
}
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(s), BinExpr(+, Id(s), BinExpr(/, IntegerLit(1), Id(i)))))"""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        input = """
// Function to check whether number is palindrome or not
isPalindrome: function integer (num: integer)
{
    // Declaring variables
    n, k, rev: integer = 0,0,0;
    // storing num in n so that we can compare it later
    n = num;
    // while num is not 0 we find its reverse and store in
    // rev
    while (num != 0) {
        k = num % 10;
        rev = (rev * 10) + k;
        num = num / 10;
    }
    // check if num and its reverse are same
    if (n == rev) {
        return 1;
    }
    else {
        return 0;
    }
}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(num), BinExpr(/, Id(num), IntegerLit(10)))"""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_84(self):
        input = """
        // function to return sum of elements
// in an array of size n
sum: function integer (arr: array [4] of integer, n: integer)
{
    sum, i: integer = 0, 0; // initialize sum

    // Iterate through all elements
    // and add them to sum
    for (i = 0, i < n, i+1)
        sum = sum + arr[i];

    return sum;
}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_85(self):
        input = """
        main: function void ()
{
    arr: array [4] of integer = { 12, 3, 4, 15 };
    n: integer = 4;
    printInteger(sum(arr, n));
}
        """
        expect = """Undeclared Function: sum"""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_86(self):
        input = """
// function to return sum of elements
// in an array of size n
sum: function integer (arr: array [4] of integer, n: integer)
{
    sum, i: integer = 0, 0; // initialize sum

    // Iterate through all elements
    // and add them to sum
    for (i = 0, i < n, i+1)
        sum = sum + arr[i];

    return sum;
}

main: function void ()
{
    arr: array [4] of integer = { 12, 3, 4, 15 };
    n: integer = 4;
    printInteger(sum(arr, n));
    break;
}
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        input = """
// C function to find maximum in arr[] of size n
largest: function integer (arr: array [4] of integer, n: integer)
{
    i: integer;

    // Initialize maximum element
    max: integer = arr[0];

    // Traverse array elements from second and
    // compare every element with current max
    for (i = 1, i < n, i+1)
        if (arr[i] > max)
            max = arr[i];

    return max;
}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        input = """
    // Recursive function to search x in arr[]
    elmntSrch: function integer (arr: array [4] of integer, size: integer, x: integer) {
        rec: integer;

        size = size - 1;

        if (size >= 0) {
            if (arr[size] == x)
                return size;
            else
                rec = elmntSrch(arr, size, x);
        }
        else
            return -1;

        return rec;
    }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        input = """
mulMat: function void (mat1: array [2, 2] of integer, mat2: array [2, 2] of integer)
{
    rslt: array [2, 2] of integer;

    printString("Multiplication of given two matrices is:\\n");

    i, j ,k : integer = 0, 0, 0;
    for (i = 0, i < 2, i+1) {
        for (j = 0, j < 2, j+1) {
            rslt[i, j] = 0;

            for (k = 0, k < 2, k+1) {
                rslt[i,j] = rslt[i,j] + mat1[i,k] * mat2[k,j];
            }

            printInteger(rslt[i, j]);
        }

        printString("\\n");
    }
}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        input = """
    /* prints element and NGE pair for all elements of
    arr[] of size n */
    printNGE: function void (arr: array [4] of integer, n: integer)
    {
        next, i, j: integer;
        for (i = 0, i < n, i+1) {
            next = -1;
            for (j = i + 1, j < n, j+1) {
                if (arr[i] < arr[j]) {
                    next = arr[j];
                    break;
                }
            }
            printInteger(arr[i]);
            printInteger(next);
        }
    }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        input = """
        foo: function void (x: auto) {
            x = 20;
            x = "abc";
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(x), StringLit(abc))"""
        self.assertTrue(TestChecker.test(input, expect, 491))


# def test_92(self):
#     input = """
#     """
#     expect = """"""
#     self.assertTrue(TestChecker.test(input, expect, 492))

# def test_93(self):
#     input = """
#     """
#     expect = """"""
#     self.assertTrue(TestChecker.test(input, expect, 493))

# def test_94(self):
#     input = """
#     """
#     expect = """"""
#     self.assertTrue(TestChecker.test(input, expect, 494))

# def test_95(self):
#     input = """
#     """
#     expect = """"""
#     self.assertTrue(TestChecker.test(input, expect, 495))

# def test_96(self):
#     input = """
#     """
#     expect = """"""
#     self.assertTrue(TestChecker.test(input, expect, 496))

# def test_97(self):
#     input = """
#     """
#     expect = """"""
#     self.assertTrue(TestChecker.test(input, expect, 497))

# def test_98(self):
#     input = """
#     """
#     expect = """"""
#     self.assertTrue(TestChecker.test(input, expect, 498))

# def test_99(self):
#     input = """
#     """
#     expect = """"""
#     self.assertTrue(TestChecker.test(input, expect, 499))
