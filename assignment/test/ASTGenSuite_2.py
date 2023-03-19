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
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
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
        input = """a,b,c:integer;"""
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """a,b,c:auto = 1,2,3;"""
        expect = """Program([
	VarDecl(a, AutoType, IntegerLit(1))
	VarDecl(b, AutoType, IntegerLit(2))
	VarDecl(c, AutoType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """a,b,c:integer = "abc","abc","abc";"""
        expect = """Program([
	VarDecl(a, IntegerType, StringLit(abc))
	VarDecl(b, IntegerType, StringLit(abc))
	VarDecl(c, IntegerType, StringLit(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = """a,b,c: float = 1.2E10, {1,2}, True ;"""
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(12000000000.0))
	VarDecl(b, FloatType, ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(c, FloatType, Id(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = """a,b,c: boolean = {1,2,3},2,3;"""
        expect = """Program([
	VarDecl(a, BooleanType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, BooleanType, IntegerLit(2))
	VarDecl(c, BooleanType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = """a,b,c:integer = "ABCD"+3213,2,3;"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, StringLit(ABCD), IntegerLit(3213)))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = """a:array[3] of float;"""
        expect = """Program([
	VarDecl(a, ArrayType([3], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """arr: array [2, 3] of integer = {1, 2, 3, 4, 5, 6};"""
        expect = """Program([
	VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """a:array[3,4] of string = {"a","b","c"};"""
        expect = """Program([
	VarDecl(a, ArrayType([3, 4], StringType), ArrayLit([StringLit(a), StringLit(b), StringLit(c)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """a,b,c,d: auto = 1,3,4,true;"""
        expect = """Program([
	VarDecl(a, AutoType, IntegerLit(1))
	VarDecl(b, AutoType, IntegerLit(3))
	VarDecl(c, AutoType, IntegerLit(4))
	VarDecl(d, AutoType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """fact: function integer (n: integer) {
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """inc: function void(out n: integer, delta: integer) {}"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = """inc: function void( inherit out n: integer, inherit delta: integer) {}"""
        expect = """Program([
	FuncDecl(inc, VoidType, [InheritOutParam(n, IntegerType), InheritParam(delta, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """inc: function void( inherit out n: integer, out delta: integer) {}
        abc: function void( inherit n: string, out  delta: integer) {}"""
        expect = """Program([
	FuncDecl(inc, VoidType, [InheritOutParam(n, IntegerType), OutParam(delta, IntegerType)], None, BlockStmt([]))
	FuncDecl(abc, VoidType, [InheritParam(n, StringType), OutParam(delta, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """inc: function void( inherit out n: integer, out delta: integer) {
            a=2;
        } """
        expect = """Program([
	FuncDecl(inc, VoidType, [InheritOutParam(n, IntegerType), OutParam(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """inc: function void( inherit out n: integer, out delta: integer) {
            a=2;
            b=3;
            c=4;
            a: integer;
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [InheritOutParam(n, IntegerType), OutParam(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), IntegerLit(3)), AssignStmt(Id(c), IntegerLit(4)), VarDecl(a, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """inc: function void( inherit out n: integer, out delta: integer) {
            a=2;
            a: integer = 1;
            b,c,d: string = "2","3","4";
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [InheritOutParam(n, IntegerType), OutParam(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, StringType, StringLit(2)), VarDecl(c, StringType, StringLit(3)), VarDecl(d, StringType, StringLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """main: function void () {
            a= 1>2 %3;
            b=!(3*4);
            a=a+b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, IntegerLit(1), BinExpr(%, IntegerLit(2), IntegerLit(3)))), AssignStmt(Id(b), UnExpr(!, BinExpr(*, IntegerLit(3), IntegerLit(4)))), AssignStmt(Id(a), BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """main: function void () {
            a= -a + b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, UnExpr(-, Id(a)), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = """inc: function void( inherit out n: integer, out delta: integer) {
            a: array[3] of integer;
            a[0]=1;
            a[1]=2;a[3]=4;
        } """
        expect = """Program([
	FuncDecl(inc, VoidType, [InheritOutParam(n, IntegerType), OutParam(delta, IntegerType)], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(2)), AssignStmt(ArrayCell(a, [IntegerLit(3)]), IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """x: integer =3;
        inc: function void( inherit out n: integer, out delta: integer) {
            a = x*x+x-X;
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(3))
	FuncDecl(inc, VoidType, [InheritOutParam(n, IntegerType), OutParam(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, BinExpr(*, Id(x), Id(x)), Id(x)), Id(X)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input = """x: integer = 10 - 20 - 15 * 5 + 120 / 10; """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, BinExpr(-, BinExpr(-, IntegerLit(10), IntegerLit(20)), BinExpr(*, IntegerLit(15), IntegerLit(5))), BinExpr(/, IntegerLit(120), IntegerLit(10))))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = """fact: function integer (n: integer) {
            if (n == 1 || (n==2)) {
                return 6;
                {
                    return 1+2;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), BinExpr(||, IntegerLit(1), BinExpr(==, Id(n), IntegerLit(2)))), BlockStmt([ReturnStmt(IntegerLit(6)), BlockStmt([ReturnStmt(BinExpr(+, IntegerLit(1), IntegerLit(2)))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) {
                return 1;
            }else{
                return 2;
            }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(IntegerLit(2))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) {
                return 1;
            }else{
                if(n==2){
                    return 3;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(IntegerLit(3))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = """main: function void () {
            a= foo(3) + foo(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, FuncCall(foo, [IntegerLit(3)]), FuncCall(foo, [IntegerLit(4)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) {
                if(n==0){
                    n=1;
                }else{
                    n=2;
                }
            }else{
                n=3;
            }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(n), IntegerLit(1))]), BlockStmt([AssignStmt(Id(n), IntegerLit(2))]))]), BlockStmt([AssignStmt(Id(n), IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) {
                a=1+1+1;
                b=foo(4);
                c=a+b;
            }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(1)), IntegerLit(1))), AssignStmt(Id(b), FuncCall(foo, [IntegerLit(4)])), AssignStmt(Id(c), BinExpr(+, Id(a), Id(b)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) {
                a=1+1+1;
                b=foo(4);
                if(a!=3){
                    c=c+3;
                }
                c=a+b;
            }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(1)), IntegerLit(1))), AssignStmt(Id(b), FuncCall(foo, [IntegerLit(4)])), IfStmt(BinExpr(!=, Id(a), IntegerLit(3)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(3)))])), AssignStmt(Id(c), BinExpr(+, Id(a), Id(b)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = """fact: function integer (n: integer) {
            if (n == 0 || (a==3)) {
                a=1+1+1;
            }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), BinExpr(||, IntegerLit(0), BinExpr(==, Id(a), IntegerLit(3)))), BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(1)), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        input = """inc: function void( inherit out n: integer, out delta: integer) {
            if(a==b){}else{
                {
                    a=3;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [InheritOutParam(n, IntegerType), OutParam(delta, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([]), BlockStmt([BlockStmt([AssignStmt(Id(a), IntegerLit(3))])]))]))
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
        input = """fact: function void (){
              for (i = 5, i < 10, i > 1) {
                    a = a+2;
                    b=c+d;
                }
          }"""
        expect = """Program([
	FuncDecl(fact, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(5)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(>, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))), AssignStmt(Id(b), BinExpr(+, Id(c), Id(d)))]))]))
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
        input = """fact: function integer (){
              for (i = 5, i > 10.E19, i + 1) {
                    a=2;
                    if(a==2){
                        return 0;
                    }
                }
          }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(5)), BinExpr(>, Id(i), FloatLit(1e+20)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(2)), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([ReturnStmt(IntegerLit(0))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = """fact: function integer (){
              for (i = 5, i > 10.E19, i + 1) {
                    for(a=5,a<5,a+2){
                        a=a+i;
                    }
                }
          }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(5)), BinExpr(>, Id(i), FloatLit(1e+20)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(5)), BinExpr(<, Id(a), IntegerLit(5)), BinExpr(+, Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))]))]))]))
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
        input = """fact: function integer (){
              for (i = 5, i > 10.E19, i + 1) {
                    if(a-b==0){
                        for(a=5,a<5,a+2){
                            a=a+i;
                        }
                    }
                }
          }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(5)), BinExpr(>, Id(i), FloatLit(1e+20)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(-, Id(a), Id(b)), IntegerLit(0)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(5)), BinExpr(<, Id(a), IntegerLit(5)), BinExpr(+, Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))]))]))]))]))
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
        input = """fact: function integer (){
              for (i = 5, i > 10.E19, i + 1) {
                    if(a-b==0){
                        for(a=5,a<5,a+2){
                            a=a+i;
                        }
                        for(a=5,a<0,a+2){
                            
                        }
                    }
                }
          }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(5)), BinExpr(>, Id(i), FloatLit(1e+20)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(-, Id(a), Id(b)), IntegerLit(0)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(5)), BinExpr(<, Id(a), IntegerLit(5)), BinExpr(+, Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))])), ForStmt(AssignStmt(Id(a), IntegerLit(5)), BinExpr(<, Id(a), IntegerLit(0)), BinExpr(+, Id(a), IntegerLit(2)), BlockStmt([]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input = """a:integer;
          fact: function integer (){
              while(1+2)
              a=2;
              a: integer;
              return "123";
              a=2;
              return "123";
          }"""
        expect = """Program([
	VarDecl(a, IntegerType)
	FuncDecl(fact, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(+, IntegerLit(1), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(2))), VarDecl(a, IntegerType), ReturnStmt(StringLit(123)), AssignStmt(Id(a), IntegerLit(2)), ReturnStmt(StringLit(123))]))
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
    }    
        """
        expect = """Program([
	FuncDecl(check, BooleanType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(i, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))))])), IfStmt(BinExpr(==, Id(sum), Id(n)), ReturnStmt(BooleanLit(True))), ReturnStmt(BooleanLit(False))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        input = """a:integer;
          fact: function integer (){
            while(1+2)
                a=2;
            while(true){
                a=2;
            }
          }"""
        expect = """Program([
	VarDecl(a, IntegerType)
	FuncDecl(fact, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(+, IntegerLit(1), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(2))), WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), IntegerLit(2))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        input = """fact: function integer (){
            while(1+2)
                a=2;
            while(true){
                a=2;
                for(i=2,i<10,i+1)
                    a=a+2;
            }
          }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(+, IntegerLit(1), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(2))), WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), IntegerLit(2)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        input = """fact: function integer (){
            while(1+2)
                a=2;
            while(true){
                if(a==2){
                    a=a+2;
                }
                for(i=2,i<10,i+1)
                    a=a+2;
            }
          }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(+, IntegerLit(1), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(2))), WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2)))])), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))))]))]))
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
        input = """fact: function integer (){
            if(a==2)
            while(a==2){
                a=a+2;
                b=b+2;
            }
          }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(2)), WhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))), AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(2)))])))]))
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
        }
  
        printString("\\n");
    }
}
        
        """
        expect = """Program([
	FuncDecl(mulMat, VoidType, [Param(mat1, ArrayType([2, 2], IntegerType)), Param(mat2, ArrayType([2, 2], IntegerType))], None, BlockStmt([VarDecl(rslt, ArrayType([2, 2], IntegerType)), CallStmt(printString, StringLit(Multiplication of given two matrices is:\\n)), VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(0)), VarDecl(k, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(rslt, [Id(i), Id(j)]), IntegerLit(0))])), CallStmt(printString, StringLit(\\n))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input = """fact: function void (){
            do {a=a+2;} 
            while(a==2);
          }"""
        expect = """Program([
	FuncDecl(fact, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = """fact: function void (){
            do{
                if(a==1){
                    continue;
                }
            } while(a<2);
          }"""
        expect = """Program([
	FuncDecl(fact, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([ContinueStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
        input = """fact: function void (){
            do{
                if(a==1){
                    continue;
                }else{
                    break;
                }
            } while(a<2);
          }"""
        expect = """Program([
	FuncDecl(fact, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([ContinueStmt()]), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
        input = """fact: function void (){
            do{
                if(a==1){
                    continue;
                }
            } while(a<2);
          }"""
        expect = """Program([
	FuncDecl(fact, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([ContinueStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input = """fact: function void (){
            do{
                if(a==1){
                    continue;
                }else{
                    a=a+2;
                    return 2;
                }
            } while(a<2);
          }"""
        expect = """Program([
	FuncDecl(fact, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([ContinueStmt()]), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))), ReturnStmt(IntegerLit(2))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = """fact: function integer (){
            while(1+2)
                a = foo(2,2);
                foo(2,2);
          }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(+, IntegerLit(1), IntegerLit(2)), AssignStmt(Id(a), FuncCall(foo, [IntegerLit(2), IntegerLit(2)]))), CallStmt(foo, IntegerLit(2), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input = """fact: function integer (){
                if(a==2){
                    return 1;
                }else return 0;
          }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([ReturnStmt(IntegerLit(1))]), ReturnStmt(IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
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
        input = """fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
            for(i=0,i<10,i+10)
                return (3*24+312)/2;
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))])))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(10)), ReturnStmt(BinExpr(/, BinExpr(+, BinExpr(*, IntegerLit(3), IntegerLit(24)), IntegerLit(312)), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = """inc: function void(out n: integer, delta: integer) {
            a: array[5] of string;
            a[0]="abc";
            n = n + delta;
            return a[0];
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([VarDecl(a, ArrayType([5], StringType)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(abc)), AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ReturnStmt(ArrayCell(a, [IntegerLit(0)]))]))
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
        input = """main: function void() {
            for(i = 0,i<10,i+2){
                continue;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input = """x: integer = 65;
        func1: function integer (n: integer) {
            x : array[3] of integer = {1,2,3};
            x[0]=x[0]+1;
            return x[0] < x[1];
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(func1, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(ArrayCell(x, [IntegerLit(0)]), BinExpr(+, ArrayCell(x, [IntegerLit(0)]), IntegerLit(1))), ReturnStmt(BinExpr(<, ArrayCell(x, [IntegerLit(0)]), ArrayCell(x, [IntegerLit(1)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = """main: function void() {
            readInt(x);
            inc(x,1);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(readInt, Id(x)), CallStmt(inc, Id(x), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            r, s: integer;
            r = 2.0;
            a, b: array [5] of string;
            }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], StringType)), VarDecl(b, ArrayType([5], StringType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = """fact: function integer (n: integer) {
            r, s: integer;
            r = 2.0;
            a, b: array [4] of integer;
            s = r * r * myPI;
            a[0] = s;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([4], IntegerType)), VarDecl(b, ArrayType([4], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
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
        input = """inc: function void(out n: integer, delta: integer) {
            a=2;
            b=3;
            return a+b;
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), IntegerLit(3)), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = """main: function void() {
            for(i = 0,i<10,i+2){
                if(a==0){
                    break;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = """x: integer = 65;
        func1: function integer (n: integer) {
            x : array[3] of integer;
            x[0]=x[0]+1;
            return x[0] != x[1];
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(func1, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType)), AssignStmt(ArrayCell(x, [IntegerLit(0)]), BinExpr(+, ArrayCell(x, [IntegerLit(0)]), IntegerLit(1))), ReturnStmt(BinExpr(!=, ArrayCell(x, [IntegerLit(0)]), ArrayCell(x, [IntegerLit(1)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = """inc: function void(out n: integer, delta: integer) {
            return 1;
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            _asd123 = 3;
            return _asd123;
            }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(_asd123), IntegerLit(3)), ReturnStmt(Id(_asd123))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = """inc: function void(out n: integer, delta: integer) {
            while(a<10){
                a = 5;
            }
            return 5;
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), IntegerLit(5))])), ReturnStmt(IntegerLit(5))]))
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
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            x=1;y=2;z=3;
            return x+y+z;
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(x), IntegerLit(1)), AssignStmt(Id(y), IntegerLit(2)), AssignStmt(Id(z), IntegerLit(3)), ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = """inc: function void(out n: integer, delta: integer) {
            return foo(3);
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([ReturnStmt(FuncCall(foo, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = """x: integer = 65;
        func1: function integer (n: integer) {
            x : array[3] of integer;
            x[0]=x[0]+y-z;
            return 25;
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(func1, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType)), AssignStmt(ArrayCell(x, [IntegerLit(0)]), BinExpr(-, BinExpr(+, ArrayCell(x, [IntegerLit(0)]), Id(y)), Id(z))), ReturnStmt(IntegerLit(25))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = """main: function void() {
            readInt(x);
            inc(x,1);
            return IamDone(Ass1);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(readInt, Id(x)), CallStmt(inc, Id(x), IntegerLit(1)), ReturnStmt(FuncCall(IamDone, [Id(Ass1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = """main: function void () {
            { }
            if (x>2) x=3;
            { if (x>2) x=3;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([]), IfStmt(BinExpr(>, Id(x), IntegerLit(2)), AssignStmt(Id(x), IntegerLit(3))), BlockStmt([IfStmt(BinExpr(>, Id(x), IntegerLit(2)), AssignStmt(Id(x), IntegerLit(3)))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input = """main: function void () {delta: integer; x, y: integer = 3, 5;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType), VarDecl(x, IntegerType, IntegerLit(3)), VarDecl(y, IntegerType, IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input = """
                foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
                main: function void () {
                    printInteger(4);
}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input = """ func: function integer(){
            a[1,2,3,"a"]=4.5;
            a = a==b::c==d;
            }"""
        expect = """Program([
	FuncDecl(stage, AutoType, [], None, BlockStmt([IfStmt(UnExpr(!, FuncCall(isDead, [])), BlockStmt([AssignStmt(Id(stage), BinExpr(+, Id(stage), IntegerLit(1)))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = """func: function array [1,2,3] of integer (){
            a[1,2,3]=(4.5+8*9)+10;
            }"""
        expect = """Program([
	FuncDecl(func, ArrayType([1, 2, 3], IntegerType), [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, BinExpr(+, FloatLit(4.5), BinExpr(*, IntegerLit(8), IntegerLit(9))), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = """func: function integer(){
            do{
                a=2;
                a,b,c:integer=1,2,3;
                a=a+1;
            }
            while(a<10);
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), IntegerLit(2)), VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = """func: function integer(inherit out a:array [1,2,3] of integer){
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [InheritOutParam(a, ArrayType([1, 2, 3], IntegerType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """
        a:string;
        b:float;
        c:integer;
        d:boolean;
        e:array[1,2,3] of string;
        f:auto;
        """
        expect = """Program([
	VarDecl(a, StringType)
	VarDecl(b, FloatType)
	VarDecl(c, IntegerType)
	VarDecl(d, BooleanType)
	VarDecl(e, ArrayType([1, 2, 3], StringType))
	VarDecl(f, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = """
        a,b,c:string="1","2","3";
        b,c,d:float = {1,2,3},a==b,a::(b::c>=d);
        c,d,e:integer;
        d,e,f:boolean;
        e,f,g:array[1,2,3] of string;
        f,g,h:auto;"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(1))
	VarDecl(b, StringType, StringLit(2))
	VarDecl(c, StringType, StringLit(3))
	VarDecl(b, FloatType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(c, FloatType, BinExpr(==, Id(a), Id(b)))
	VarDecl(d, FloatType, BinExpr(::, Id(a), BinExpr(::, Id(b), BinExpr(>=, Id(c), Id(d)))))
	VarDecl(c, IntegerType)
	VarDecl(d, IntegerType)
	VarDecl(e, IntegerType)
	VarDecl(d, BooleanType)
	VarDecl(e, BooleanType)
	VarDecl(f, BooleanType)
	VarDecl(e, ArrayType([1, 2, 3], StringType))
	VarDecl(f, ArrayType([1, 2, 3], StringType))
	VarDecl(g, ArrayType([1, 2, 3], StringType))
	VarDecl(f, AutoType)
	VarDecl(g, AutoType)
	VarDecl(h, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = """func: function void(a:integer){
                  a=!(!(!(-3)));
            }  """
        expect = """Program([
	FuncDecl(func, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(Id(a), UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(-, IntegerLit(3))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = """ main:function void()
        {if(a == 1){_ID_=3;}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(_ID_), IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = """main:function void(){a=true::{1,2,3};}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BooleanLit(True), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = """ main:function void(){
                        a=1;
                        if(a == 1) 
                            a=3;
                        else
                            a=4;   
                        while(x>3) print(x);
                        do {
                            a=a+2;
                            b=a;
                        }
                        while(a<10);
            } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(3)), AssignStmt(Id(a), IntegerLit(4))), WhileStmt(BinExpr(>, Id(x), IntegerLit(3)), CallStmt(print, Id(x))), DoWhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))), AssignStmt(Id(b), Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = """  main:function void(){
                        if(a == 1  && true && false) 
                           {
                               a=2;
                           }
                        else
                            {a=4;} }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), BinExpr(&&, BinExpr(&&, IntegerLit(1), BooleanLit(True)), BooleanLit(False))), BlockStmt([AssignStmt(Id(a), IntegerLit(2))]), BlockStmt([AssignStmt(Id(a), IntegerLit(4))]))]))
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

    def test_388(self):
        input = """arr: array [2,3] of integer = {1, 2, 3, 4, 5, 6};
        i: integer;
        
        """
        expect = """Program([
	VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
	VarDecl(i, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
