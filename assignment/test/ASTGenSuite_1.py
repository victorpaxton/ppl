import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """x,y: integer;y,z:float;a:auto;b:array[1,2,3] of integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(y, FloatType)
	VarDecl(z, FloatType)
	VarDecl(a, AutoType)
	VarDecl(b, ArrayType([1, 2, 3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test2(self):
        input = """x,y,z: string = "aa","bb","cc";"""
        expect = """Program([
	VarDecl(x, StringType, StringLit(aa))
	VarDecl(y, StringType, StringLit(bb))
	VarDecl(z, StringType, StringLit(cc))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test3(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;
        A, B: string;
        C, D: boolean = true, false;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(A, StringType)
	VarDecl(B, StringType)
	VarDecl(C, BooleanType, BooleanLit(True))
	VarDecl(D, BooleanType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4(self):
        input = """main: function void () {
            { }
            if (x>2) x=3;
            { if (x>2) x=3;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([]), IfStmt(BinExpr(>, Id(x), IntegerLit(2)), AssignStmt(Id(x), IntegerLit(3))), BlockStmt([IfStmt(BinExpr(>, Id(x), IntegerLit(2)), AssignStmt(Id(x), IntegerLit(3)))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test5(self):
        input = """
                foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
                main: function void () {
                    printInteger(4);
}"""
        expect = """Program([
\tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test6(self):
        input = """
        a:integer;
        main: function void () {
            a:integer;
            printInteger(4);
        }
        a,b,c:integer;
        a,b,c:float = 1_2.2,2_2.3,3_3.4;"""
        expect = """Program([
	VarDecl(a, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), CallStmt(printInteger, IntegerLit(4))]))
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	VarDecl(a, FloatType, FloatLit(12.2))
	VarDecl(b, FloatType, FloatLit(22.3))
	VarDecl(c, FloatType, FloatLit(33.4))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test7(self):
        input = """
        a:array[3] of string = {"a","b","c"};"""
        expect = """Program([
	VarDecl(a, ArrayType([3], StringType), ArrayLit([StringLit(a), StringLit(b), StringLit(c)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test8(self):
        input = """ func: function integer(){
            a[1,2,3,"a"]=4.5;
            a = a==b::c==d;
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), StringLit(a)]), FloatLit(4.5)), AssignStmt(Id(a), BinExpr(::, BinExpr(==, Id(a), Id(b)), BinExpr(==, Id(c), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test9(self):
        input = """func: function integer(){
            a[1,2,3]= a!=(b==c);
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(!=, Id(a), BinExpr(==, Id(b), Id(c))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test10(self):
        input = """ a : integer = {1,2,3,a==b,a::(b::c>=d)}; """
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), BinExpr(==, Id(a), Id(b)), BinExpr(::, Id(a), BinExpr(::, Id(b), BinExpr(>=, Id(c), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test11(self):
        input = """func: function array [1,2,3] of integer (){
            a[1,2,3]=(4.5+8*9)+10;
            }"""
        expect = """Program([
	FuncDecl(func, ArrayType([1, 2, 3], IntegerType), [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, BinExpr(+, FloatLit(4.5), BinExpr(*, IntegerLit(8), IntegerLit(9))), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test12(self):
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
        self.assertTrue(TestAST.test(input, expect, 312))

    def test13(self):
        input = """func: function integer(inherit out a:array [1,2,3] of integer){
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [InheritOutParam(a, ArrayType([1, 2, 3], IntegerType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test14(self):
        input = """func: function integer(inherit a:auto,inherit out b:string,out c:array[1,2,3] of integer){
            a= {1,2_3,2_3.4,"aa",true,{1,2}};
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [InheritParam(a, AutoType), InheritOutParam(b, StringType), OutParam(c, ArrayType([1, 2, 3], IntegerType))], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(23), FloatLit(23.4), StringLit(aa), BooleanLit(True), ArrayLit([IntegerLit(1), IntegerLit(2)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test15(self):
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
        self.assertTrue(TestAST.test(input, expect, 315))

    def test16(self):
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
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        input = """func: function integer(){
            a={1,2,3}/4;
            print(5);
            while(a<10)a=3;
            {
                while({true,false,"aa",_a}) a=4;
            }
            } """
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(/, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(4))), CallStmt(print, IntegerLit(5)), WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), AssignStmt(Id(a), IntegerLit(3))), BlockStmt([WhileStmt(ArrayLit([BooleanLit(True), BooleanLit(False), StringLit(aa), Id(_a)]), AssignStmt(Id(a), IntegerLit(4)))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test18(self):
        input = """func: function void(a:integer){
                  a=-(-(-(-3)));
            } """
        expect = """Program([
	FuncDecl(func, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(Id(a), UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(3))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        input = """func: function void(a:integer){
                  a=!(!(!(-3)));
            }  """
        expect = """Program([
	FuncDecl(func, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(Id(a), UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(-, IntegerLit(3))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        input = """ main:function void(){
            a=!true &&false ||false;
            } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(&&, UnExpr(!, BooleanLit(True)), BooleanLit(False)), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test21(self):
        input = """ main:function void()
        {if(a == 1){_ID_=3;}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(_ID_), IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test22(self):
        input = """main:function void(){a=true::{1,2,3};}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BooleanLit(True), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test23(self):
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
        self.assertTrue(TestAST.test(input, expect, 323))

    def test24(self):
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
        self.assertTrue(TestAST.test(input, expect, 324))

    def test25(self):
        input = """
        a:boolean=true;
        b,c,d:array[1,2,3] of boolean= {true,false,true},true,false;
        main:function void(){
                        if(a == 1) 
                            a=3;
                        if(true && false)
                            x=y-4;
                        else
                            a=4;   
            } """
        expect = """Program([
	VarDecl(a, BooleanType, BooleanLit(True))
	VarDecl(b, ArrayType([1, 2, 3], BooleanType), ArrayLit([BooleanLit(True), BooleanLit(False), BooleanLit(True)]))
	VarDecl(c, ArrayType([1, 2, 3], BooleanType), BooleanLit(True))
	VarDecl(d, ArrayType([1, 2, 3], BooleanType), BooleanLit(False))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(3))), IfStmt(BinExpr(&&, BooleanLit(True), BooleanLit(False)), AssignStmt(Id(x), BinExpr(-, Id(y), IntegerLit(4))), AssignStmt(Id(a), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test26(self):
        input = """ main:function void(){
                    for(i = 1, i < 4, i + 1) {
                    break;
                    return;
                    continue;
                    return {1,2,3};}
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([BreakStmt(), ReturnStmt(), ContinueStmt(), ReturnStmt(ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test27(self):
        input = """ 
        main:function void(){
            a = a::b==c&&d+e/!-f;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, Id(a), BinExpr(==, Id(b), BinExpr(&&, Id(c), BinExpr(+, Id(d), BinExpr(/, Id(e), UnExpr(!, UnExpr(-, Id(f)))))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test28(self):
        input = """ main:function void(){\n
                     while(true){
                         x[1,2]=3;
                     }
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(1), IntegerLit(2)]), IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test29(self):
        input = """
        main:function void (){
                if (x) 
                    if(y) return 1; 
                    else return 2;
                    for(x=2,x<10,x+1){
                        a,b,c:integer=1,2,3;
                    }
            }
            """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(x), IfStmt(Id(y), ReturnStmt(IntegerLit(1)), ReturnStmt(IntegerLit(2)))), ForStmt(AssignStmt(Id(x), IntegerLit(2)), BinExpr(<, Id(x), IntegerLit(10)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test30(self):
        input = """ main:function void(){\n
                     while(true){
                         a={1,2,{"a","b"},a::b,"a"::"b"};
                     }
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([StringLit(a), StringLit(b)]), BinExpr(::, Id(a), Id(b)), BinExpr(::, StringLit(a), StringLit(b))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test31(self):
        input = """ main:function void(){\n
                     while(x<6){
                        {{}
                        a=print(print(print(x,y,z)),t);}
                     }
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(6)), BlockStmt([BlockStmt([BlockStmt([]), AssignStmt(Id(a), FuncCall(print, [FuncCall(print, [FuncCall(print, [Id(x), Id(y), Id(z)])]), Id(t)]))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test32(self):
        input = """ main:function void(){\n
                        x:integer;
                        x=x+1;
                        print(x);
                        y: array[3] of integer;
                        y={1,2,3};
                        x=y[0];
                        print(x);
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), CallStmt(print, Id(x)), VarDecl(y, ArrayType([3], IntegerType)), AssignStmt(Id(y), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(Id(x), ArrayCell(y, [IntegerLit(0)])), CallStmt(print, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        input = """ main:function void(){\n
                    do{
                        x:integer;
                        x=x+1;
                    }while(x==1);
                        
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test34(self):
        input = """ foo:function integer(){
            return 1;
            }
                    main:function void(){
            while(a == 2){
                a=-foo();
            }
            } """
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), UnExpr(-, FuncCall(foo, [])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test35(self):
        input = """inc: function void(out n: integer, delta: integer) inherit abc {
            if(--a[foo(8,{"aa","bb",{}}),a[b[c[_5]]]]) return;
            else 
                if (_1) return a==_2+_3; 
                else return true;
        }   """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], abc, BlockStmt([IfStmt(UnExpr(-, UnExpr(-, ArrayCell(a, [FuncCall(foo, [IntegerLit(8), ArrayLit([StringLit(aa), StringLit(bb), ArrayLit([])])]), ArrayCell(a, [ArrayCell(b, [ArrayCell(c, [Id(_5)])])])]))), ReturnStmt(), IfStmt(Id(_1), ReturnStmt(BinExpr(==, Id(a), BinExpr(+, Id(_2), Id(_3)))), ReturnStmt(BooleanLit(True))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test36(self):
        input = """main:function void(){\n
                    while(a==3){
                        if(x==1){
                            break;
                        }
                        print(-a,-b,c,!d,a::(b::d));
                    }
                        
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([BreakStmt()])), CallStmt(print, UnExpr(-, Id(a)), UnExpr(-, Id(b)), Id(c), UnExpr(!, Id(d)), BinExpr(::, Id(a), BinExpr(::, Id(b), Id(d))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test37(self):
        input = """main:function void(){\n
                    while(a==3){
                        if(x==1){
                            continue;
                        }
                    }
                        
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([ContinueStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test38(self):
        input = """  main:function void(){
            while(a==3){
                do {{}}
                    while(a[0] == 2);
            }            
                    }  """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([DoWhileStmt(BinExpr(==, ArrayCell(a, [IntegerLit(0)]), IntegerLit(2)), BlockStmt([BlockStmt([])]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test39(self):
        input = """ 
        kiemtra: function integer (n: integer){
                if (n==1) return 1;
                else return 0;
                if (n==0) return;
                else return n :: fibo(a::(b::c&&d));
            } """
        expect = """Program([
	FuncDecl(kiemtra, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1)), ReturnStmt(IntegerLit(0))), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(), ReturnStmt(BinExpr(::, Id(n), FuncCall(fibo, [BinExpr(::, Id(a), BinExpr(::, Id(b), BinExpr(&&, Id(c), Id(d))))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test40(self):
        input = """ main:function void(){
        a= _abc[{true,false}];} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(_abc, [ArrayLit([BooleanLit(True), BooleanLit(False)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test41(self):
        input = """ main:function void(){
                for(i = 1, i < 4, i + 1){
                    if (i == 1) {{\n}}}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(1)), BlockStmt([BlockStmt([])]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test42(self):
        input = """main:function void(){\n
                    while(a==3){
                        if(x==1){
                            return 0;
                        }
                    }
                        
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(0))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test43(self):
        input = """ main:function void(){
                    for(i = 1, i < 4, i + 1) 
                        for(j = 1, j < 5, j+1){}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    #     def test44(self):
    #         input = """ main:function void(){
    #             for(i = 1, i < 4, i + 1)
    #             {\n a= a + 1; \n a = 1;
    #              for(i=1,i<4,i-1){
    #                  for(i[i]=i,i<i,i--i){}}}} """
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(a), IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(ArrayCell(i, [Id(i)]), Id(i)), BinExpr(<, Id(i), Id(i)), BinExpr(-, Id(i), UnExpr(-, Id(i))), BlockStmt([]))]))]))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 344))

    def test45(self):
        input = """ a:integer = a[1];
            b: string = {foo(a[9999]),_1[111],"string"};
            sum: function integer(a:integer, b:integer) inherit _print{
                return (a+b);
            }  """
        expect = """Program([
	VarDecl(a, IntegerType, ArrayCell(a, [IntegerLit(1)]))
	VarDecl(b, StringType, ArrayLit([FuncCall(foo, [ArrayCell(a, [IntegerLit(9999)])]), ArrayCell(_1, [IntegerLit(111)]), StringLit(string)]))
	FuncDecl(sum, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], _print, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test46(self):
        input = """ main:function void(){\n
                    for(i = 1, i < 4, i + 1) 
                        while(true){\n 
                            a:integer = 1; \n 
                                if(true) 
                                    break;
                                else continue;
                    a = a + 1;}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), WhileStmt(BooleanLit(True), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), IfStmt(BooleanLit(True), BreakStmt(), ContinueStmt()), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test47(self):
        input = """x,y: integer=2,0;
        x,y,z: integer=2,0,1;
        x,y,z,t: integer=2,0,1,5;
        x,y,z,t,u: integer=2,0,1,5,0;
        x,y,z,t,u,v: integer=2,0,1,5,0,4;
        x,y,z,t,u,v,w: integer=2,0,1,5,0,4,3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2))
	VarDecl(y, IntegerType, IntegerLit(0))
	VarDecl(x, IntegerType, IntegerLit(2))
	VarDecl(y, IntegerType, IntegerLit(0))
	VarDecl(z, IntegerType, IntegerLit(1))
	VarDecl(x, IntegerType, IntegerLit(2))
	VarDecl(y, IntegerType, IntegerLit(0))
	VarDecl(z, IntegerType, IntegerLit(1))
	VarDecl(t, IntegerType, IntegerLit(5))
	VarDecl(x, IntegerType, IntegerLit(2))
	VarDecl(y, IntegerType, IntegerLit(0))
	VarDecl(z, IntegerType, IntegerLit(1))
	VarDecl(t, IntegerType, IntegerLit(5))
	VarDecl(u, IntegerType, IntegerLit(0))
	VarDecl(x, IntegerType, IntegerLit(2))
	VarDecl(y, IntegerType, IntegerLit(0))
	VarDecl(z, IntegerType, IntegerLit(1))
	VarDecl(t, IntegerType, IntegerLit(5))
	VarDecl(u, IntegerType, IntegerLit(0))
	VarDecl(v, IntegerType, IntegerLit(4))
	VarDecl(x, IntegerType, IntegerLit(2))
	VarDecl(y, IntegerType, IntegerLit(0))
	VarDecl(z, IntegerType, IntegerLit(1))
	VarDecl(t, IntegerType, IntegerLit(5))
	VarDecl(u, IntegerType, IntegerLit(0))
	VarDecl(v, IntegerType, IntegerLit(4))
	VarDecl(w, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test48(self):
        input = """main:function void(){\n
                    x:float=2.015043;
                    print(x);
                    x= print(x);
                    a:integer = print({1,2,3},a[1,2,3]);
                    return 0;                       
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(2.015043)), CallStmt(print, Id(x)), AssignStmt(Id(x), FuncCall(print, [Id(x)])), VarDecl(a, IntegerType, FuncCall(print, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test49(self):
        input = """ main:function void(){\n
                    x:float=1.3;
                    print(x,"abv");
                    return 0;                       
                    }
                    main:function void(){\n                    
                    }
                    int : integer = 1;
                    bool : boolean = true;
                    int,bool: array[2] of integer= {1,2},{true,false};
                    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.3)), CallStmt(print, Id(x), StringLit(abv)), ReturnStmt(IntegerLit(0))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	VarDecl(int, IntegerType, IntegerLit(1))
	VarDecl(bool, BooleanType, BooleanLit(True))
	VarDecl(int, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(bool, ArrayType([2], IntegerType), ArrayLit([BooleanLit(True), BooleanLit(False)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test50(self):
        input = """ main:function void(){\n
                    x:float=2.015043;
                    print(x,"abc",_d,____e,_f__,true,a[1,2]);
                    continue;
                    break;
                    x:array[3] of string = {"aa","bb","cc"};           
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(2.015043)), CallStmt(print, Id(x), StringLit(abc), Id(_d), Id(____e), Id(_f__), BooleanLit(True), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])), ContinueStmt(), BreakStmt(), VarDecl(x, ArrayType([3], StringType), ArrayLit([StringLit(aa), StringLit(bb), StringLit(cc)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test51(self):
        input = """ a,b,c,d,e,f,g :integer = 2,0,1,5,0,4,3;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	VarDecl(b, IntegerType, IntegerLit(0))
	VarDecl(c, IntegerType, IntegerLit(1))
	VarDecl(d, IntegerType, IntegerLit(5))
	VarDecl(e, IntegerType, IntegerLit(0))
	VarDecl(f, IntegerType, IntegerLit(4))
	VarDecl(g, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test52(self):
        input = """ a,b :auto; """
        expect = """Program([
	VarDecl(a, AutoType)
	VarDecl(b, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test53(self):
        input = """
        foo:function void(){
            a=a[1,2];
            a={1,2};
            a=a::b;
            a=a::b&&c;
            a={1,2,a[1,{1,2}]};}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])), AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2)])), AssignStmt(Id(a), BinExpr(::, Id(a), Id(b))), AssignStmt(Id(a), BinExpr(::, Id(a), BinExpr(&&, Id(b), Id(c)))), AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), ArrayCell(a, [IntegerLit(1), ArrayLit([IntegerLit(1), IntegerLit(2)])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test54(self):
        input = """ a,b,c,d,e : integer = 1+2,1-2,1*2,1/2,1+2-1*1/2; """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
	VarDecl(b, IntegerType, BinExpr(-, IntegerLit(1), IntegerLit(2)))
	VarDecl(c, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(d, IntegerType, BinExpr(/, IntegerLit(1), IntegerLit(2)))
	VarDecl(e, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(1)), IntegerLit(2))))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test55(self):
        input = """x,y:string;
                    a,b,c:float=1,2,4.e5;
                    d: array[1,2] of integer;"""
        expect = """Program([
	VarDecl(x, StringType)
	VarDecl(y, StringType)
	VarDecl(a, FloatType, IntegerLit(1))
	VarDecl(b, FloatType, IntegerLit(2))
	VarDecl(c, FloatType, FloatLit(400000.0))
	VarDecl(d, ArrayType([1, 2], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test56(self):
        input = """ main:function void(inherit out x:float){\n
                    foo(x);
                    return 1;
                    return ;
                    x,y:integer;
                    x,y,z:float=1.2,3.2,4.2;
                    x:float;
                    return a[0,1];
                    return {1,2,3};
                    return {1,2,a[3]};
                    return a[0,{1,2,3}];
                    return 0;                       
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(x, FloatType)], None, BlockStmt([CallStmt(foo, Id(x)), ReturnStmt(IntegerLit(1)), ReturnStmt(), VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(x, FloatType, FloatLit(1.2)), VarDecl(y, FloatType, FloatLit(3.2)), VarDecl(z, FloatType, FloatLit(4.2)), VarDecl(x, FloatType), ReturnStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(1)])), ReturnStmt(ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), ReturnStmt(ArrayLit([IntegerLit(1), IntegerLit(2), ArrayCell(a, [IntegerLit(3)])])), ReturnStmt(ArrayCell(a, [IntegerLit(0), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test57(self):
        input = """ main:function void( out x:float,y:integer){\n
                    print(x);                     
                    }
                    _x_,__y,___z : float= 1.2,1_2.3,{1.2,2.3};"""
        expect = """Program([
	FuncDecl(main, VoidType, [OutParam(x, FloatType), Param(y, IntegerType)], None, BlockStmt([CallStmt(print, Id(x))]))
	VarDecl(_x_, FloatType, FloatLit(1.2))
	VarDecl(__y, FloatType, FloatLit(12.3))
	VarDecl(___z, FloatType, ArrayLit([FloatLit(1.2), FloatLit(2.3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test58(self):
        input = """ main:function void(inherit x:float,y:integer){\n
                    do{
                        while(x<3){
                            print(x);
                        }
                        for(x=1,x<3,x+1){
                            
                        }
                        if(x==3) print(x);
                        else {}
                    }
                    while(x>3);          
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritParam(x, FloatType), Param(y, IntegerType)], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(3)), BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(3)), BlockStmt([CallStmt(print, Id(x))])), ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(<, Id(x), IntegerLit(3)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([])), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), CallStmt(print, Id(x)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test59(self):
        input = """ a,b : auto = {1,2,3},2;
        _c,_d_:integer=1,2;
        _foo: function integer(inherit out _foo:array[3] of integer,out x:auto){}"""
        expect = """Program([
	VarDecl(a, AutoType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, AutoType, IntegerLit(2))
	VarDecl(_c, IntegerType, IntegerLit(1))
	VarDecl(_d_, IntegerType, IntegerLit(2))
	FuncDecl(_foo, IntegerType, [InheritOutParam(_foo, ArrayType([3], IntegerType)), OutParam(x, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test60(self):
        input = """ a, b,c : auto= {1,2,3},4,(1); """
        expect = """Program([
	VarDecl(a, AutoType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, AutoType, IntegerLit(4))
	VarDecl(c, AutoType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test61(self):
        input = """main:function void(){\nfor(i = 1, i < 4, i + 1) break;
        return;
        continue;
        break;
        a:integer = 1;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), ReturnStmt(), ContinueStmt(), BreakStmt(), VarDecl(a, IntegerType, IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test62(self):
        input = """ main : function void(){
                    print(1);
                    a = main(1,2,3,_,{_,_,_1});}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, IntegerLit(1)), AssignStmt(Id(a), FuncCall(main, [IntegerLit(1), IntegerLit(2), IntegerLit(3), Id(_), ArrayLit([Id(_), Id(_), Id(_1)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        input = """  inc : function void (out n : integer , delta : integer)
        {
            _:integer = _ + _ - _ / _;
            _[1,2,3]=_[1,2,3];
            } """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([VarDecl(_, IntegerType, BinExpr(-, BinExpr(+, Id(_), Id(_)), BinExpr(/, Id(_), Id(_)))), AssignStmt(ArrayCell(_, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayCell(_, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test64(self):
        input = """x: integer = 65;
                inc: function void(out n: array [5] of integer, delta: integer) inherit _ {
                    n = n + delta;\n}
                main: function void(inherit n:integer,out delta:integer) inherit abc {
                        delta: integer = fact(3);\
                        inc(x, delta);
                        printInteger(x);\n}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(inc, VoidType, [OutParam(n, ArrayType([5], IntegerType)), Param(delta, IntegerType)], _, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [InheritParam(n, IntegerType), OutParam(delta, IntegerType)], abc, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test65(self):
        input = """ 
        a:integer;
        b:float;
        x,y,z,t,_ : integer = 1,2,3,4,5;
        main : function void(){
            \n \nreturn 0;\n } """
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, FloatType)
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(t, IntegerType, IntegerLit(4))
	VarDecl(_, IntegerType, IntegerLit(5))
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test66(self):
        input = """ func: function integer(){\nbreak;\n}"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test67(self):
        input = """ a: float=a>(b>c)::d==e;"""
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(::, BinExpr(>, Id(a), BinExpr(>, Id(b), Id(c))), BinExpr(==, Id(d), Id(e))))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test68(self):
        input = """ main : function void(){
                    foo(2 + x, 4.0 / y,z[0],foo({1,2,3}));
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y)), ArrayCell(z, [IntegerLit(0)]), FuncCall(foo, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test69(self):
        input = """a,b,c,d,e,f,e,g,e,d : integer = 1,2,3,4,5,6,7,8,9,10;
        main : function void(){
                continue;
                break;
                return;
                for(i = 1, i < 4, i + 1) 
                if(i==4) 
                    while(true){}
                else
                    if(i==4){}
                if(i==4) 
                    while(true){}
                else
                    if(i==4){}
                do{
                        x,y:integer;
                        x=3;
                    }
                    while(x<10);
                while(x<10){x:integer;}
                if(i==4) 
                    while(true){}
                else
                    if(i==4){}
                while(x<10){x:integer;}
                }
                   a: array[3] of integer= {1,2,3};
                   main : function void(){
                }
                   """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(d, IntegerType, IntegerLit(4))
	VarDecl(e, IntegerType, IntegerLit(5))
	VarDecl(f, IntegerType, IntegerLit(6))
	VarDecl(e, IntegerType, IntegerLit(7))
	VarDecl(g, IntegerType, IntegerLit(8))
	VarDecl(e, IntegerType, IntegerLit(9))
	VarDecl(d, IntegerType, IntegerLit(10))
	FuncDecl(main, VoidType, [], None, BlockStmt([ContinueStmt(), BreakStmt(), ReturnStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), WhileStmt(BooleanLit(True), BlockStmt([])), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), BlockStmt([])))), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), WhileStmt(BooleanLit(True), BlockStmt([])), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), BlockStmt([]))), DoWhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), AssignStmt(Id(x), IntegerLit(3))])), WhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([VarDecl(x, IntegerType)])), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), WhileStmt(BooleanLit(True), BlockStmt([])), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), BlockStmt([]))), WhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([VarDecl(x, IntegerType)]))]))
	VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test70(self):
        input = """ gram : function integer(out a : integer) inherit func{} """
        expect = """Program([
	FuncDecl(gram, IntegerType, [OutParam(a, IntegerType)], func, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test71(self):
        input = """ main : function void(){
                continue;
                break;
                return;
                for(i = 1, i < 4, i + 1) 
                if(i==4) 
                    while(true){}
                else
                    if(i==4){}
                if(i==4) 
                    while(true){}
                else
                    if(i==4){}
                do{
                        x,y:integer;
                        x=3;
                    }
                    while(x<10);
                while(x<10){x:integer;}
                if(i==4) 
                    while(true){}
                else
                    if(i==4){}
                while(x<10){x:integer;}
                } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ContinueStmt(), BreakStmt(), ReturnStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), WhileStmt(BooleanLit(True), BlockStmt([])), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), BlockStmt([])))), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), WhileStmt(BooleanLit(True), BlockStmt([])), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), BlockStmt([]))), DoWhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), AssignStmt(Id(x), IntegerLit(3))])), WhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([VarDecl(x, IntegerType)])), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), WhileStmt(BooleanLit(True), BlockStmt([])), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), BlockStmt([]))), WhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([VarDecl(x, IntegerType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test72(self):
        input = """ main : function void(){
                if(a == 1){
                    foo(x);}
                    {}
                    foo(y);
                    {{foo(z);}}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([CallStmt(foo, Id(x))])), BlockStmt([]), CallStmt(foo, Id(y)), BlockStmt([BlockStmt([CallStmt(foo, Id(z))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        input = """ main:function void(){
            for(i = 1, i < 4, i + 1) 
                if(i==4) 
                    while(true){}
                else
                    if(i==4){}
        } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), WhileStmt(BooleanLit(True), BlockStmt([])), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), BlockStmt([]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test74(self):
        input = """ main : function void(){ 
                        a = _id *6 /4.0/_id[1,2,3]*{1,2,3,4}/true;} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(/, BinExpr(*, BinExpr(/, BinExpr(/, BinExpr(*, Id(_id), IntegerLit(6)), FloatLit(4.0)), ArrayCell(_id, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test75(self):
        input = """ main : function void(){ 
                        return foo(foo({},{},{foo({a::b>(_d>-e)})})) + 1;} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(foo, [FuncCall(foo, [ArrayLit([]), ArrayLit([]), ArrayLit([FuncCall(foo, [ArrayLit([BinExpr(::, Id(a), BinExpr(>, Id(b), BinExpr(>, Id(_d), UnExpr(-, Id(e)))))])])])])]), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    #     def test76(self):
    #         input = """ main : function void(){
    #             for(a=3,a<10,a::"aa"){
    #                 a:integer = 1;
    #             }
    #             } """
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(3)]), IntegerLit(3)), BinExpr(<, ArrayCell(a, [IntegerLit(3), IntegerLit(4)]), IntegerLit(10)), BinExpr(::, ArrayCell(a, [IntegerLit(3), IntegerLit(4), IntegerLit(5)]), StringLit(aa)), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1))]))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = """a: string = "234"; """
        expect = """Program([
	VarDecl(a, StringType, StringLit(234))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test78(self):
        input = """main:function void(){if(a == 1){}}  """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test79(self):
        input = """ a :float= {};
                    b,c : integer=1,2;
                    a:auto;
                    a,b,c,d:float=1.2,{1.2,1.2,a[1,2]},_a,_b;"""
        expect = """Program([
	VarDecl(a, FloatType, ArrayLit([]))
	VarDecl(b, IntegerType, IntegerLit(1))
	VarDecl(c, IntegerType, IntegerLit(2))
	VarDecl(a, AutoType)
	VarDecl(a, FloatType, FloatLit(1.2))
	VarDecl(b, FloatType, ArrayLit([FloatLit(1.2), FloatLit(1.2), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])]))
	VarDecl(c, FloatType, Id(_a))
	VarDecl(d, FloatType, Id(_b))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test80(self):
        input = """ _a_ : function void () {
                arr = {};
                a=a[1,2]+(b[2,1]*c[3,2])/d[2,3];
            } """
        expect = """Program([
	FuncDecl(_a_, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([])), AssignStmt(Id(a), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), BinExpr(/, BinExpr(*, ArrayCell(b, [IntegerLit(2), IntegerLit(1)]), ArrayCell(c, [IntegerLit(3), IntegerLit(2)])), ArrayCell(d, [IntegerLit(2), IntegerLit(3)]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test81(self):
        input = """ main : function void () {
                a : array [5] of integer;
                a = a::b<d&&e&&f+g*!_abcd;
            }  """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType)), AssignStmt(Id(a), BinExpr(::, Id(a), BinExpr(<, Id(b), BinExpr(&&, BinExpr(&&, Id(d), Id(e)), BinExpr(+, Id(f), BinExpr(*, Id(g), UnExpr(!, Id(_abcd))))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test82(self):
        input = """ main : function void () {
                        if(false){
                            print(6);
                            if(true){
                                print(5);
                                do{
                                    print(4);
                                }
                                while(true);
                                while(false) break;
                            }
                        }
                }   """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(False), BlockStmt([CallStmt(print, IntegerLit(6)), IfStmt(BooleanLit(True), BlockStmt([CallStmt(print, IntegerLit(5)), DoWhileStmt(BooleanLit(True), BlockStmt([CallStmt(print, IntegerLit(4))])), WhileStmt(BooleanLit(False), BreakStmt())]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        input = """  main : function void () {
                    if(a==3) if(b==4) if(c==5) if(d==6) {}
                }    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(3)), IfStmt(BinExpr(==, Id(b), IntegerLit(4)), IfStmt(BinExpr(==, Id(c), IntegerLit(5)), IfStmt(BinExpr(==, Id(d), IntegerLit(6)), BlockStmt([])))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test84(self):
        input = """ main : function void () {
                    a=3;
                    b[1]=3;
                    a[3]=a[3];
                } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(3)), AssignStmt(ArrayCell(b, [IntegerLit(1)]), IntegerLit(3)), AssignStmt(ArrayCell(a, [IntegerLit(3)]), ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test85(self):
        input = """ main : function void () {
                    a : auto = {{1,2,3}};
                    b = a[1];
                    b : string;
                } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])), AssignStmt(Id(b), ArrayCell(a, [IntegerLit(1)])), VarDecl(b, StringType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test86(self):
        input = """ main : function void () {
                    a = {{1,2,3},a,foo(a,b),a[1,2,foo(a,b)]};
                } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), Id(a), FuncCall(foo, [Id(a), Id(b)]), ArrayCell(a, [IntegerLit(1), IntegerLit(2), FuncCall(foo, [Id(a), Id(b)])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test87(self):
        input = """  main : function void () {
                } 
                main : function array [3] of boolean () {
                }
                main : function integer () {
                }
                main : function float () {
                }
                main : function string () {
                }
                main : function boolean () {
                }
                main : function auto () {
                }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(main, ArrayType([3], BooleanType), [], None, BlockStmt([]))
	FuncDecl(main, IntegerType, [], None, BlockStmt([]))
	FuncDecl(main, FloatType, [], None, BlockStmt([]))
	FuncDecl(main, StringType, [], None, BlockStmt([]))
	FuncDecl(main, BooleanType, [], None, BlockStmt([]))
	FuncDecl(main, AutoType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test88(self):
        input = """ x,y:boolean=true,false;
                    x:array [3] of integer = {1,2,3};
                    main : function void () {
                    foo(a*b/c);
                }"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(x, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(/, BinExpr(*, Id(a), Id(b)), Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test89(self):
        input = """ main : function void () {
                    foo(_a,_b,-c);
                } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, Id(_a), Id(_b), UnExpr(-, Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test90(self):
        input = """ main : function void () {
                    a = {{{}}, {{}}, {{},{}}};
                }  """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([ArrayLit([ArrayLit([])]), ArrayLit([ArrayLit([])]), ArrayLit([ArrayLit([]), ArrayLit([])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test91(self):
        input = """ 
                func1 : function array [5] of integer(){
                    do{
                        x,y:integer;
                        x=3;
                    }
                    while(x<10);
                    while(x<10){x:integer;}
                    x:float;
                }
                """
        expect = """Program([
	FuncDecl(func1, ArrayType([5], IntegerType), [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), AssignStmt(Id(x), IntegerLit(3))])), WhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([VarDecl(x, IntegerType)])), VarDecl(x, FloatType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = """
                func1 : function array [5] of integer(a : integer,b:float,c:string,d:boolean){
                    return true;
                    return ;
                    return 1_123;
                    return 1_123.4;
                    return foo(abc);
                    return _a;
                    return _a[1,2];
                }
                """
        expect = """Program([
	FuncDecl(func1, ArrayType([5], IntegerType), [Param(a, IntegerType), Param(b, FloatType), Param(c, StringType), Param(d, BooleanType)], None, BlockStmt([ReturnStmt(BooleanLit(True)), ReturnStmt(), ReturnStmt(IntegerLit(1123)), ReturnStmt(FloatLit(1123.4)), ReturnStmt(FuncCall(foo, [Id(abc)])), ReturnStmt(Id(_a)), ReturnStmt(ArrayCell(_a, [IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        input = """
                func1 : function integer(a : array [5] of integer){
                    return 1;
                }
                """
        expect = """Program([
	FuncDecl(func1, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test94(self):
        input = """
                func1 : function integer(a : array [5] of integer){
                    return 1;
                }
                """
        expect = """Program([
	FuncDecl(func1, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test95(self):
        input = """a,b : integer = {1,2,3},1_2;"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, IntegerType, IntegerLit(12))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test96(self):
        input = """a12 : array [1] of integer = {1,2};"""
        expect = """Program([
	VarDecl(a12, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = """
        x : integer = 1;
        foo: function array [5] of integer(){}
        _foo: function void(a : integer){}
        x ,z:float =1.e-5,4.9;
        __foo: function void(a : integer){}
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	FuncDecl(foo, ArrayType([5], IntegerType), [], None, BlockStmt([]))
	FuncDecl(_foo, VoidType, [Param(a, IntegerType)], None, BlockStmt([]))
	VarDecl(x, FloatType, FloatLit(1e-05))
	VarDecl(z, FloatType, FloatLit(4.9))
	FuncDecl(__foo, VoidType, [Param(a, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test98(self):
        input = """
            x : integer;
            main : function void () {
                count(1+1,foo(1--2,{1,2,foo(a,b)}));} 
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(count, BinExpr(+, IntegerLit(1), IntegerLit(1)), FuncCall(foo, [BinExpr(-, IntegerLit(1), UnExpr(-, IntegerLit(2))), ArrayLit([IntegerLit(1), IntegerLit(2), FuncCall(foo, [Id(a), Id(b)])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test99(self):
        input = """
            main : function void (inherit out x : array[3] of string) {}
        """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(x, ArrayType([3], StringType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test100(self):
        input = """
            _The_end__ : integer = 1_0.0;
        """
        expect = """Program([
	VarDecl(_The_end__, IntegerType, FloatLit(10.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
