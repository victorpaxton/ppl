import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: float = .e2, 1.0, 3.0;"""
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(0.0))
	VarDecl(y, FloatType, FloatLit(1.0))
	VarDecl(z, FloatType, FloatLit(3.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
                    a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """
            foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

            main: function void () {
                printInteger(4);
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """x:integer = 2023;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2023))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """x: auto = 2023;"""
        expect = """Program([
	VarDecl(x, AutoType, IntegerLit(2023))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """x: array [2,3] of integer;"""
        expect = """Program([
	VarDecl(x, ArrayType([2, 3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = """a: auto = "abc"; b: string = "abc"; """
        expect = """Program([
	VarDecl(a, AutoType, StringLit(abc))
	VarDecl(b, StringType, StringLit(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = """a: auto = true; b: boolean = false; """
        expect = """Program([
	VarDecl(a, AutoType, BooleanLit(True))
	VarDecl(b, BooleanType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = """arr: array [3] of integer = {1,2,3};"""
        expect = """Program([
	VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = """x: integer = arr[0]; y: integer = a[2,3];"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayCell(arr, [IntegerLit(0)]))
	VarDecl(y, IntegerType, ArrayCell(a, [IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """arr: array [2, 3] of integer = {1, 2, 3, 4, 5, 6};"""
        expect = """Program([
	VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """a: auto = 1.234; b: string = 1_456.2e5; """
        expect = """Program([
	VarDecl(a, AutoType, FloatLit(1.234))
	VarDecl(b, StringType, FloatLit(145620000.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """inc: function integer (n: integer , delta: integer) inherit fact {}"""
        expect = """Program([
	FuncDecl(inc, IntegerType, [Param(n, IntegerType), Param(delta, IntegerType)], fact, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """x, y, z, t: auto = 45 + 2, "abc"::"abc", !true, a[0] + 5; """
        expect = """Program([
	VarDecl(x, AutoType, BinExpr(+, IntegerLit(45), IntegerLit(2)))
	VarDecl(y, AutoType, BinExpr(::, StringLit(abc), StringLit(abc)))
	VarDecl(z, AutoType, UnExpr(!, BooleanLit(True)))
	VarDecl(t, AutoType, BinExpr(+, ArrayCell(a, [IntegerLit(0)]), IntegerLit(5)))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """inc: function integer (n: integer , delta: integer) {} x: integer = inc(5, 3);"""
        expect = """Program([
	FuncDecl(inc, IntegerType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([]))
	VarDecl(x, IntegerType, FuncCall(inc, [IntegerLit(5), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = """x: integer = -3; y: boolean = (x > 1) && (x < 5);"""
        expect = """Program([
	VarDecl(x, IntegerType, UnExpr(-, IntegerLit(3)))
	VarDecl(y, BooleanType, BinExpr(&&, BinExpr(>, Id(x), IntegerLit(1)), BinExpr(<, Id(x), IntegerLit(5))))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """fact : function integer (n : integer ) {
                if (n == 0) return 1 ;
    else return n * fact (n - 1 );
    }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """x: integer = 2023; inc: function void (out n: integer , delta: integer) {} main: function void () {delta: integer = 3; inc(x, delta);}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2023))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, IntegerLit(3)), CallStmt(inc, Id(x), Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """main: function void () {foo(2); foo(5 + 6);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(2)), CallStmt(foo, BinExpr(+, IntegerLit(5), IntegerLit(6)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """main: function void () {delta: integer; x, y: integer = 3, 5;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType), VarDecl(x, IntegerType, IntegerLit(3)), VarDecl(y, IntegerType, IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """main: function void () {
            x: integer;
            x = 5 + 7;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(+, IntegerLit(5), IntegerLit(7)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """main: function void () {
        x: integer;
        for (i = 1, i < 10, i + 1) {
            writeInteger(i);
        }
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = """x: integer = 2;
        main: function void () {
            if (x>0) {
                if (x % 2 == 0) {
                    printString("Even positive number");
                }
                else 
                    printString("Odd positive number");
            }
            else
                printString("Negative number") ; 
            }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(Even positive number))]), CallStmt(printString, StringLit(Odd positive number)))]), CallStmt(printString, StringLit(Negative number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """x: boolean = true && false && 5 == 7;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(==, BinExpr(&&, BinExpr(&&, BooleanLit(True), BooleanLit(False)), IntegerLit(5)), IntegerLit(7)))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input = """x: integer = 10 - 20 - 15 * 5 + 120 / 10; """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, BinExpr(-, BinExpr(-, IntegerLit(10), IntegerLit(20)), BinExpr(*, IntegerLit(15), IntegerLit(5))), BinExpr(/, IntegerLit(120), IntegerLit(10))))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = """i: integer = 1;
        main: function void () {
            while (i < 10) {
                printInteger(i);
                i = i + 1;
                }}"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = """i: integer = 1;
        main: function void () {
            while (i < 10) {
                printInteger(i);
                i = i + 1;
                if (i == 5) break;
                }}"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), IfStmt(BinExpr(==, Id(i), IntegerLit(5)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input = """main: function void() {
            i: integer;
            for (i = 2023, i >= 0, i - 1) {
                printInteger(i);
                if (i == 1000) continue;
                }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(2023)), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i)), IfStmt(BinExpr(==, Id(i), IntegerLit(1000)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = """i: integer = 2023;
        main: function void () {
            do {
                printInteger(i);
                i = i - 1;
            } while (i > 0);
            }"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(2023))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input = """i: integer = 2023;
        main: function void () {
            do {
                printInteger(i);
                if (i == 1000) continue;
                i = i - 1;
            } while (i > 0);
            }"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(2023))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(i)), IfStmt(BinExpr(==, Id(i), IntegerLit(1000)), ContinueStmt()), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = """inc: function integer (num: integer, delta: integer) {
                return num + delta;
            }"""
        expect = """Program([
	FuncDecl(inc, IntegerType, [Param(num, IntegerType), Param(delta, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(num), Id(delta)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = """
        inc: function integer (num: integer, delta: integer) {
                    return num + delta;
                }
        main: function void () {
            result: integer = inc(2022, 1);
            printInteger(result);
        }        
        """
        expect = """Program([
	FuncDecl(inc, IntegerType, [Param(num, IntegerType), Param(delta, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(num), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(result, IntegerType, FuncCall(inc, [IntegerLit(2022), IntegerLit(1)])), CallStmt(printInteger, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = """arr: array [2,3] of integer = {1, 2, 3, 4, 5, 6};
        i: integer;
        main: function void () {
            for (i = 0, i < 2, i+1) {
                for (j = 0, j < 3, j+1) 
                    printInteger(arr[i, j]);
            }
        }
        
        """
        expect = """Program([
	VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
	VarDecl(i, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), CallStmt(printInteger, ArrayCell(arr, [Id(i), Id(j)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        input = """main: function void () {
            for (i = 0, i < 2, i+1) {
                for (j = 0, j < 3, j+1) 
                    if (arr[i, j] % 2 == 0) 
                        printInteger(arr[i,j]);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i), Id(j)]), IntegerLit(2)), IntegerLit(0)), CallStmt(printInteger, ArrayCell(arr, [Id(i), Id(j)]))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        input = """
        // This is a comment
        main: function void () {
            r, s: integer;
            r = 2.0;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;  
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input = """main: function void () {
            if (i > 0) {
                for (j = i, j >= 0, j - 1) {
                    printInteger(j);
                }
            } else {
                return;
            }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([ForStmt(AssignStmt(Id(j), Id(i)), BinExpr(>=, Id(j), IntegerLit(0)), BinExpr(-, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(j))]))]), BlockStmt([ReturnStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input = """
        arr1, arr2: array [2] of integer = {1, 2}, {5, 6};
        """
        expect = """Program([
	VarDecl(arr1, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(arr2, ArrayType([2], IntegerType), ArrayLit([IntegerLit(5), IntegerLit(6)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input = """concatString: function string (s1: string, s2: string) {
                return s1::s2;
            }
            main: function void () {
                printString(concatString("abc","def"));
                }"""
        expect = """Program([
	FuncDecl(concatString, StringType, [Param(s1, StringType), Param(s2, StringType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(s1), Id(s2)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, FuncCall(concatString, [StringLit(abc), StringLit(def)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = """main: function void () {
            while (true) {
                while (true) {
                    while (true) {
                        return;
                    }
                }
            }
            
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([ReturnStmt()]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
        input = """x: integer = 2;
main: function void () {
    for (i = 1, i < 10, i + 1) {
        j: integer = i*i;
        if (j % 2 == 0) printInteger(i);
    }
}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(j, IntegerType, BinExpr(*, Id(i), Id(i))), IfStmt(BinExpr(==, BinExpr(%, Id(j), IntegerLit(2)), IntegerLit(0)), CallStmt(printInteger, Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
        input = """x: integer = 2;
main: function void () {
    for (i = 1, i < 10, i + 1) {
        j: integer = i*i;
        if (j % 2 == 0) printInteger(i);
        else {
            while (j < 50)
                printInteger(j);
        }
    }
}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(j, IntegerType, BinExpr(*, Id(i), Id(i))), IfStmt(BinExpr(==, BinExpr(%, Id(j), IntegerLit(2)), IntegerLit(0)), CallStmt(printInteger, Id(i)), BlockStmt([WhileStmt(BinExpr(<, Id(j), IntegerLit(50)), CallStmt(printInteger, Id(j)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
        input = """
check: function boolean (n: integer){
    sum, i: integer = 0, 1;//khai bao biem sum
    for(i=1,i<=n/2,i+1){
        if(n%i==0) sum = sum+i;
    }
    if(sum==n) return true; // tra ve true
    return false;
}
        """
        expect = """Program([
	FuncDecl(check, BooleanType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(i, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))))])), IfStmt(BinExpr(==, Id(sum), Id(n)), ReturnStmt(BooleanLit(True))), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input = """
main: function void () {
    n: integer;
    printString("Nhap n: ");
    n = readInteger();
    if(check(n))
        printString("n la so hoan hao");
    else
        printString("n khong phai la so hoan hao.",n);
    return;
}        
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(printString, StringLit(Nhap n: )), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(FuncCall(check, [Id(n)]), CallStmt(printString, StringLit(n la so hoan hao)), CallStmt(printString, StringLit(n khong phai la so hoan hao.), Id(n))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input = """
    check: function boolean (n: integer){
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
            printString("n khong phai la so hoan hao.",n);
        return;
    }    
        """
        expect = """Program([
	FuncDecl(check, BooleanType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(i, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))))])), IfStmt(BinExpr(==, Id(sum), Id(n)), ReturnStmt(BooleanLit(True))), ReturnStmt(BooleanLit(False))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(printString, StringLit(Nhap n: )), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(FuncCall(check, [Id(n)]), CallStmt(printString, StringLit(n la so hoan hao)), CallStmt(printString, StringLit(n khong phai la so hoan hao.), Id(n))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
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
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(arr, ArrayType([4], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        input = """
main: function void ()
{
    arr: array [4] of integer = { 12, 3, 4, 15 };
    n: integer = 4;
    printInteger(sum(arr, n));
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([4], IntegerType), ArrayLit([IntegerLit(12), IntegerLit(3), IntegerLit(4), IntegerLit(15)])), VarDecl(n, IntegerType, IntegerLit(4)), CallStmt(printInteger, FuncCall(sum, [Id(arr), Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
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
}
        """
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(arr, ArrayType([4], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([4], IntegerType), ArrayLit([IntegerLit(12), IntegerLit(3), IntegerLit(4), IntegerLit(15)])), VarDecl(n, IntegerType, IntegerLit(4)), CallStmt(printInteger, FuncCall(sum, [Id(arr), Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
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
        expect = """Program([
	FuncDecl(largest, IntegerType, [Param(arr, ArrayType([4], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(max, IntegerType, ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(max)), AssignStmt(Id(max), ArrayCell(arr, [Id(i)])))), ReturnStmt(Id(max))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
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
        expect = """Program([
	FuncDecl(elmntSrch, IntegerType, [Param(arr, ArrayType([4], IntegerType)), Param(size, IntegerType), Param(x, IntegerType)], None, BlockStmt([VarDecl(rec, IntegerType), AssignStmt(Id(size), BinExpr(-, Id(size), IntegerLit(1))), IfStmt(BinExpr(>=, Id(size), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [Id(size)]), Id(x)), ReturnStmt(Id(size)), AssignStmt(Id(rec), FuncCall(elmntSrch, [Id(arr), Id(size), Id(x)])))]), ReturnStmt(UnExpr(-, IntegerLit(1)))), ReturnStmt(Id(rec))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
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
        expect = """Program([
	FuncDecl(mulMat, VoidType, [Param(mat1, ArrayType([2, 2], IntegerType)), Param(mat2, ArrayType([2, 2], IntegerType))], None, BlockStmt([VarDecl(rslt, ArrayType([2, 2], IntegerType)), CallStmt(printString, StringLit(Multiplication of given two matrices is:\\n)), VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(0)), VarDecl(k, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(rslt, [Id(i), Id(j)]), IntegerLit(0)), ForStmt(AssignStmt(Id(k), IntegerLit(0)), BinExpr(<, Id(k), IntegerLit(2)), BinExpr(+, Id(k), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(rslt, [Id(i), Id(j)]), BinExpr(+, ArrayCell(rslt, [Id(i), Id(j)]), BinExpr(*, ArrayCell(mat1, [Id(i), Id(k)]), ArrayCell(mat2, [Id(k), Id(j)]))))])), CallStmt(printInteger, ArrayCell(rslt, [Id(i), Id(j)]))])), CallStmt(printString, StringLit(\\n))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
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
        expect = """Program([
	FuncDecl(printNGE, VoidType, [Param(arr, ArrayType([4], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(next, IntegerType), VarDecl(i, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(next), UnExpr(-, IntegerLit(1))), ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(j)])), BlockStmt([AssignStmt(Id(next), ArrayCell(arr, [Id(j)])), BreakStmt()]))])), CallStmt(printInteger, ArrayCell(arr, [Id(i)])), CallStmt(printInteger, Id(next))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = """
    binarySearch: function integer (arr: array [4] of integer, l: integer, r:integer, x:integer)
    {
        if (r >= l) {
            mid: integer = l + (r - l) / 2;

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
        expect = """Program([
	FuncDecl(binarySearch, IntegerType, [Param(arr, ArrayType([4], IntegerType)), Param(l, IntegerType), Param(r, IntegerType), Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(r), Id(l)), BlockStmt([VarDecl(mid, IntegerType, BinExpr(+, Id(l), BinExpr(/, BinExpr(-, Id(r), Id(l)), IntegerLit(2)))), IfStmt(BinExpr(==, ArrayCell(arr, [Id(mid)]), Id(x)), ReturnStmt(Id(mid))), IfStmt(BinExpr(>, ArrayCell(arr, [Id(mid)]), Id(x)), ReturnStmt(FuncCall(binarySearch, [Id(arr), Id(l), BinExpr(-, Id(mid), IntegerLit(1)), Id(x)]))), ReturnStmt(FuncCall(binarySearch, [Id(arr), BinExpr(+, Id(mid), IntegerLit(1)), Id(r), Id(x)]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
        input = """
// A function to implement bubble sort
bubbleSort: function void (arr: array [4] of integer, n: integer)
{
    i, j: integer;
    for (i = 0, i < n - 1, i+1)
 
        // Last i elements are already in place
        for (j = 0, j < n - i - 1, j+1)
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
}
        """
        expect = """Program([
	FuncDecl(bubbleSort, VoidType, [Param(arr, ArrayType([4], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), IfStmt(BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), CallStmt(swap, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
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
        expect = """Program([
	FuncDecl(insertionSort, VoidType, [Param(arr, ArrayType([4], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(key, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(key), ArrayCell(arr, [Id(i)])), AssignStmt(Id(j), BinExpr(-, Id(i), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(>=, Id(j), IntegerLit(0)), BinExpr(>, ArrayCell(arr, [Id(j)]), Id(key))), BlockStmt([AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), ArrayCell(arr, [Id(j)])), AssignStmt(Id(j), BinExpr(-, Id(j), IntegerLit(1)))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(key))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input = """
/* For a given array arr[], 
   returns the maximum j - i such
   that arr[j] > arr[i] */
maxIndexDiff: function integer(arr: array [4] of integer, n: integer)
{
    maxDiff:integer = -1;
    i, j: integer;
  
    for (i = 0, i < n, i+1) {
        for (j = n - 1, j > i, j-1) {
            if ((arr[j] > arr[i]) && (maxDiff < (j - i)))
                maxDiff = j - i;
        }
    }
  
    return maxDiff;
}    
        """
        expect = """Program([
	FuncDecl(maxIndexDiff, IntegerType, [Param(arr, ArrayType([4], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(maxDiff, IntegerType, UnExpr(-, IntegerLit(1))), VarDecl(i, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [Id(i)])), BinExpr(<, Id(maxDiff), BinExpr(-, Id(j), Id(i)))), AssignStmt(Id(maxDiff), BinExpr(-, Id(j), Id(i))))]))])), ReturnStmt(Id(maxDiff))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = """
// function to find the maximum element
findMaximum: function integer (arr: array [4] of integer, low: integer, high: integer)
{
    max: integer = arr[low];
    i: integer;
    for (i = low+1,i <= high, i+1)
    {
        if (arr[i] > max)
            max = arr[i];
    // break when once an element is smaller than
    // the max then it will go on decreasing
    // and no need to check after that
        else
            break;
    }
    return max;
}
        """
        expect = """Program([
	FuncDecl(findMaximum, IntegerType, [Param(arr, ArrayType([4], IntegerType)), Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([VarDecl(max, IntegerType, ArrayCell(arr, [Id(low)])), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), BinExpr(+, Id(low), IntegerLit(1))), BinExpr(<=, Id(i), Id(high)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(max)), AssignStmt(Id(max), ArrayCell(arr, [Id(i)])), BreakStmt())])), ReturnStmt(Id(max))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
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
        """
        expect = """Program([
	FuncDecl(getSum, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(!=, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), BinExpr(%, Id(n), IntegerLit(10)))), AssignStmt(Id(n), BinExpr(/, Id(n), IntegerLit(10)))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
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
        """
        expect = """Program([
	FuncDecl(checkYear, BooleanType, [Param(year, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(year), IntegerLit(400)), IntegerLit(0)), ReturnStmt(BooleanLit(True))), IfStmt(BinExpr(==, BinExpr(%, Id(year), IntegerLit(100)), IntegerLit(0)), ReturnStmt(BooleanLit(False))), IfStmt(BinExpr(==, BinExpr(%, Id(year), IntegerLit(4)), IntegerLit(0)), ReturnStmt(BooleanLit(True))), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = """
printNos: function void (n: integer)
{
    if(n > 0)
    {
        printNos(n - 1);
        printInteger(n);
    }
    return;
}
        """
        expect = """Program([
	FuncDecl(printNos, VoidType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([CallStmt(printNos, BinExpr(-, Id(n), IntegerLit(1))), CallStmt(printInteger, Id(n))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = """
// Utility function to find minimum of two integers
min: function integer(x: integer, y: integer)
{
    if (x < y) return x;
    return y;
     
}
        """
        expect = """Program([
	FuncDecl(min, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(x), Id(y)), ReturnStmt(Id(x))), ReturnStmt(Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """main: function void () {
            // validate the input
    if ((h <0) || (m < 0) || (h >12) || (m > 60)) printString("Wrong input");
            
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(<, Id(h), IntegerLit(0)), BinExpr(<, Id(m), IntegerLit(0))), BinExpr(>, Id(h), IntegerLit(12))), BinExpr(>, Id(m), IntegerLit(60))), CallStmt(printString, StringLit(Wrong input)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = """main: function void () {
            if (h == 12) h = 0;
    if (m == 60)
     {
      m = 0;
      h = h+ 1;
       if(h>12)
        h = h-12;
     }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(h), IntegerLit(12)), AssignStmt(Id(h), IntegerLit(0))), IfStmt(BinExpr(==, Id(m), IntegerLit(60)), BlockStmt([AssignStmt(Id(m), IntegerLit(0)), AssignStmt(Id(h), BinExpr(+, Id(h), IntegerLit(1))), IfStmt(BinExpr(>, Id(h), IntegerLit(12)), AssignStmt(Id(h), BinExpr(-, Id(h), IntegerLit(12))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = """main: function void () {
            hour_angle: float = 0.5 * (h * 60 + m);
    minute_angle: float = 6 * m;
    angle: float = abs(hour_angle - minute_angle);
    angle = min(360 - angle, angle);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(hour_angle, FloatType, BinExpr(*, FloatLit(0.5), BinExpr(+, BinExpr(*, Id(h), IntegerLit(60)), Id(m)))), VarDecl(minute_angle, FloatType, BinExpr(*, IntegerLit(6), Id(m))), VarDecl(angle, FloatType, FuncCall(abs, [BinExpr(-, Id(hour_angle), Id(minute_angle))])), AssignStmt(Id(angle), FuncCall(min, [BinExpr(-, IntegerLit(360), Id(angle)), Id(angle)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input = """
/* Returns 1 if n is a lucky no.
otherwise returns 0*/
isLucky: function boolean (n: integer)
{
    counter: integer = 2;
 
    if (counter > n)
        return 1;
    if (n % counter == 0)
        return 0;
 
    /*calculate next position of input no.
      Variable "next_position" is just for
    readability of the program we can
    remove it and update in "n" only */
    next_position: integer = n - (n / counter);
 
    counter = counter + 1;
    return isLucky(next_position);
}
"""
        expect = """Program([
	FuncDecl(isLucky, BooleanType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(counter, IntegerType, IntegerLit(2)), IfStmt(BinExpr(>, Id(counter), Id(n)), ReturnStmt(IntegerLit(1))), IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(counter)), IntegerLit(0)), ReturnStmt(IntegerLit(0))), VarDecl(next_position, IntegerType, BinExpr(-, Id(n), BinExpr(/, Id(n), Id(counter)))), AssignStmt(Id(counter), BinExpr(+, Id(counter), IntegerLit(1))), ReturnStmt(FuncCall(isLucky, [Id(next_position)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
        input = """main: function void () {
            x: integer = 5;
 
    // Function call
    if (isLucky(x))
        printString(" is a lucky no.");
    else
        printString(" is not a lucky no.");
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), IfStmt(FuncCall(isLucky, [Id(x)]), CallStmt(printString, StringLit( is a lucky no.)), CallStmt(printString, StringLit( is not a lucky no.)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
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
        expect = """Program([
	FuncDecl(squareRoot, FloatType, [Param(n, FloatType)], None, BlockStmt([VarDecl(x, FloatType, Id(n)), VarDecl(y, FloatType, FloatLit(1.0)), VarDecl(e, FloatType, FloatLit(1e-06)), WhileStmt(BinExpr(>, BinExpr(-, Id(x), Id(y)), Id(e)), BlockStmt([AssignStmt(Id(x), BinExpr(/, BinExpr(+, Id(x), Id(y)), IntegerLit(2))), AssignStmt(Id(y), BinExpr(/, Id(n), Id(x)))])), ReturnStmt(Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = """
main: function void () {
            x: integer = 5;
            printFloat(squareRoot(x));
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), CallStmt(printFloat, FuncCall(squareRoot, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = """
fib: function integer (n: integer)
{
    if (n <= 1)
        return n;
    return fib(n - 1) + fib(n - 2);
}        
"""
        expect = """Program([
	FuncDecl(fib, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(1)), ReturnStmt(Id(n))), ReturnStmt(BinExpr(+, FuncCall(fib, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fib, [BinExpr(-, Id(n), IntegerLit(2))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = """
main: function void () {
            x: integer = 5;
            printInteger(fib(x));
}
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), CallStmt(printInteger, FuncCall(fib, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = """
findArea: function float (a: float, b: float, c: float) 
{ 
    // Length of sides must be positive 
    // and sum of any two sides 
    // must be smaller than third side. 
    if ((a < 0) || (b < 0) || (c < 0) || 
       (a + b <= c) || (a + c <= b) || 
                       (b + c <= a)) 
    { 
        printString("Not a valid triangle"); 
        return;
    } 
    s: float = (a + b + c) / 2; 
    return sqrt(s * (s - a) * (s - b) * (s - c)); 
} 
        """
        expect = """Program([
	FuncDecl(findArea, FloatType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(<, Id(a), IntegerLit(0)), BinExpr(<, Id(b), IntegerLit(0))), BinExpr(<, Id(c), IntegerLit(0))), BinExpr(<=, BinExpr(+, Id(a), Id(b)), Id(c))), BinExpr(<=, BinExpr(+, Id(a), Id(c)), Id(b))), BinExpr(<=, BinExpr(+, Id(b), Id(c)), Id(a))), BlockStmt([CallStmt(printString, StringLit(Not a valid triangle)), ReturnStmt()])), VarDecl(s, FloatType, BinExpr(/, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c)), IntegerLit(2))), ReturnStmt(FuncCall(sqrt, [BinExpr(*, BinExpr(*, BinExpr(*, Id(s), BinExpr(-, Id(s), Id(a))), BinExpr(-, Id(s), Id(b))), BinExpr(-, Id(s), Id(c)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = """main: function void () {
            x: integer = 5;
            i: integer;
             for(i = 0, i < n, i+1)
    {
        printInteger(fibonacci_numbers(i));
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, FuncCall(fibonacci_numbers, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = """
fibonacci_numbers: function integer(n: integer)
{
    if(n == 0){
        return 0;
    }
    else if(n == 1){
        return 1;
    }
    else{
        return fibonacci_numbers(n-2) + fibonacci_numbers(n-1);
    }
}
        """
        expect = """Program([
	FuncDecl(fibonacci_numbers, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))]), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(fibonacci_numbers, [BinExpr(-, Id(n), IntegerLit(2))]), FuncCall(fibonacci_numbers, [BinExpr(-, Id(n), IntegerLit(1))])))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = """
nPr: function integer (n: integer, r: integer)
{
    return fact(n)/fact(n-r);
}
        """
        expect = """Program([
	FuncDecl(nPr, IntegerType, [Param(n, IntegerType), Param(r, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, FuncCall(fact, [Id(n)]), FuncCall(fact, [BinExpr(-, Id(n), Id(r))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = """
binomialCoeff: function integer(n: integer, k: integer)
{
    res: integer = 1;
    i: integer;
    if (k > n - k)
    k = n - k;
    for (i = 0, i < k, i+1)
    {
        res =res * (n - i);
        res =res/ (i + 1);
    }
     
    return res;
}        
        """
        expect = """Program([
	FuncDecl(binomialCoeff, IntegerType, [Param(n, IntegerType), Param(k, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType, IntegerLit(1)), VarDecl(i, IntegerType), IfStmt(BinExpr(>, Id(k), BinExpr(-, Id(n), Id(k))), AssignStmt(Id(k), BinExpr(-, Id(n), Id(k)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(k)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(res), BinExpr(*, Id(res), BinExpr(-, Id(n), Id(i)))), AssignStmt(Id(res), BinExpr(/, Id(res), BinExpr(+, Id(i), IntegerLit(1))))])), ReturnStmt(Id(res))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = """
printPascal: function void (n: integer)
{
    // Iterate through every line and
    // print entries in it
    line: integer;
    for (line = 0, line < n, line+1)
    {
        // Every line has number of
        // integers equal to line
        // number
        i: integer;
        for (i = 0, i <= line, i+1)
            printInteger(binomialCoeff(line, i));
        printString("\\n");
    }
}
        """
        expect = """Program([
	FuncDecl(printPascal, VoidType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(line, IntegerType), ForStmt(AssignStmt(Id(line), IntegerLit(0)), BinExpr(<, Id(line), Id(n)), BinExpr(+, Id(line), IntegerLit(1)), BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), Id(line)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, FuncCall(binomialCoeff, [Id(line), Id(i)]))), CallStmt(printString, StringLit(\\n))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = """
// A function to print all prime
// factors of a given number n
primeFactors: function void (n: integer)
{
    // Print the number of 2s that divide n
    while (n % 2 == 0)
    {
        printInteger(2);
        n = n/2;
    }
 
    // n must be odd at this point. So we can skip
    // one element (Note i = i +2)
    i: integer;
    for (i = 3, i <= sqrt(n), i + 2)
    {
        // While i divides n, print i and divide n
        while (n % i == 0)
        {
            printInteger(i);
            n = n/i;
        }
    }
 
    // This condition is to handle the case when n
    // is a prime number greater than 2
    if (n > 2)
        printInteger(n);
}
        """
        expect = """Program([
	FuncDecl(primeFactors, VoidType, [Param(n, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(==, BinExpr(%, Id(n), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printInteger, IntegerLit(2)), AssignStmt(Id(n), BinExpr(/, Id(n), IntegerLit(2)))])), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(<=, Id(i), FuncCall(sqrt, [Id(n)])), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([WhileStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(n), BinExpr(/, Id(n), Id(i)))]))])), IfStmt(BinExpr(>, Id(n), IntegerLit(2)), CallStmt(printInteger, Id(n)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = """
sum: function float (n: integer)
{
    i, s: float = 0.0, 0.0;
    for (i = 1, i <= n, i+1)
    s = s + 1/i;
    return s;
}
        """
        expect = """Program([
	FuncDecl(sum, FloatType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(i, FloatType, FloatLit(0.0)), VarDecl(s, FloatType, FloatLit(0.0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(s), BinExpr(+, Id(s), BinExpr(/, IntegerLit(1), Id(i))))), ReturnStmt(Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
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
        expect = """Program([
	FuncDecl(isPalindrome, IntegerType, [Param(num, IntegerType)], None, BlockStmt([VarDecl(n, IntegerType, IntegerLit(0)), VarDecl(k, IntegerType, IntegerLit(0)), VarDecl(rev, IntegerType, IntegerLit(0)), AssignStmt(Id(n), Id(num)), WhileStmt(BinExpr(!=, Id(num), IntegerLit(0)), BlockStmt([AssignStmt(Id(k), BinExpr(%, Id(num), IntegerLit(10))), AssignStmt(Id(rev), BinExpr(+, BinExpr(*, Id(rev), IntegerLit(10)), Id(k))), AssignStmt(Id(num), BinExpr(/, Id(num), IntegerLit(10)))])), IfStmt(BinExpr(==, Id(n), Id(rev)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(IntegerLit(0))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = """
main: function void () {
    n: integer;
    printString("Nhap n: ");
    n = readInteger();
    if(check(n))
        printString("n la so hoan hao");
    else
        printString("n khong phai la so hoan hao.",n);
    return;
}        
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(printString, StringLit(Nhap n: )), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(FuncCall(check, [Id(n)]), CallStmt(printString, StringLit(n la so hoan hao)), CallStmt(printString, StringLit(n khong phai la so hoan hao.), Id(n))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = """inc: function integer (num: integer, delta: integer) {
                return num + delta;
            }"""
        expect = """Program([
	FuncDecl(inc, IntegerType, [Param(num, IntegerType), Param(delta, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(num), Id(delta)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = """i: integer = 1;
        main: function void () {
            while (i < 10) {
                printInteger(i);
                i = i + 1;
                if (i == 5) break;
                }}"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), IfStmt(BinExpr(==, Id(i), IntegerLit(5)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = """main: function void () {foo(2); foo(5 + 6);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(2)), CallStmt(foo, BinExpr(+, IntegerLit(5), IntegerLit(6)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input = """main: function void () {delta: integer; x, y: integer = 3, 5;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType), VarDecl(x, IntegerType, IntegerLit(3)), VarDecl(y, IntegerType, IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input = """main: function void () {
            x: integer;
            x = 5 + 7;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(+, IntegerLit(5), IntegerLit(7)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input = """main: function void () {
        x: integer;
        for (i = 1, i < 10, i + 1) {
            writeInteger(i);
        }
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = """x: integer = 2;
        main: function void () {
            if (x>0) {
                if (x % 2 == 0) {
                    printString("Even positive number");
                }
                else 
                    printString("Odd positive number");
            }
            else
                printString("Negative number") ; 
            }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(Even positive number))]), CallStmt(printString, StringLit(Odd positive number)))]), CallStmt(printString, StringLit(Negative number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = """x: boolean = true && false && 5 == 7;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(==, BinExpr(&&, BinExpr(&&, BooleanLit(True), BooleanLit(False)), IntegerLit(5)), IntegerLit(7)))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = """x: integer = 10 - 20 - 15 * 5 + 120 / 10; """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, BinExpr(-, BinExpr(-, IntegerLit(10), IntegerLit(20)), BinExpr(*, IntegerLit(15), IntegerLit(5))), BinExpr(/, IntegerLit(120), IntegerLit(10))))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """i: integer = 1;
        main: function void () {
            while (i < 10) {
                printInteger(i);
                i = i + 1;
                }}"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = """i: integer = 1;
        main: function void () {
            while (i < 10) {
                printInteger(i);
                i = i + 1;
                if (i == 5) break;
                }}"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), IfStmt(BinExpr(==, Id(i), IntegerLit(5)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = """main: function void() {
            i: integer;
            for (i = 2023, i >= 0, i - 1) {
                printInteger(i);
                if (i == 1000) continue;
                }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(2023)), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i)), IfStmt(BinExpr(==, Id(i), IntegerLit(1000)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = """i: integer = 2023;
        main: function void () {
            do {
                printInteger(i);
                i = i - 1;
            } while (i > 0);
            }"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(2023))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = """i: integer = 2023;
        main: function void () {
            do {
                printInteger(i);
                if (i == 1000) continue;
                i = i - 1;
            } while (i > 0);
            }"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(2023))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(i)), IfStmt(BinExpr(==, Id(i), IntegerLit(1000)), ContinueStmt()), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = """inc: function integer (num: integer, delta: integer) {
                return num + delta;
            }"""
        expect = """Program([
	FuncDecl(inc, IntegerType, [Param(num, IntegerType), Param(delta, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(num), Id(delta)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = """
        inc: function integer (num: integer, delta: integer) {
                    return num + delta;
                }
        main: function void () {
            result: integer = inc(2022, 1);
            printInteger(result);
        }        
        """
        expect = """Program([
	FuncDecl(inc, IntegerType, [Param(num, IntegerType), Param(delta, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(num), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(result, IntegerType, FuncCall(inc, [IntegerLit(2022), IntegerLit(1)])), CallStmt(printInteger, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input = """arr: array [2,3] of integer = {1, 2, 3, 4, 5, 6};
        i: integer;
        main: function void () {
            for (i = 0, i < 2, i+1) {
                for (j = 0, j < 3, j+1) 
                    printInteger(arr[i, j]);
            }
        }
        
        """
        expect = """Program([
	VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
	VarDecl(i, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), CallStmt(printInteger, ArrayCell(arr, [Id(i), Id(j)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
