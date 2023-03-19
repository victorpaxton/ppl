import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    """test variable declaration"""

    def test1(self):
        input = """ a,b,c : string; """
        expect = """Program([
	VarDecl(a, StringType)
	VarDecl(b, StringType)
	VarDecl(c, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test2(self):
        input = """ a,b,c : string = "a","b","c"; """
        expect = """Program([
	VarDecl(a, StringType, StringLit(a))
	VarDecl(b, StringType, StringLit(b))
	VarDecl(c, StringType, StringLit(c))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test3(self):
        input = """a,b,c : string = "a","b",1; """
        expect = """Program([
	VarDecl(a, StringType, StringLit(a))
	VarDecl(b, StringType, StringLit(b))
	VarDecl(c, StringType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4(self):
        input = """a : string = a; """
        expect = """Program([
	VarDecl(a, StringType, Id(a))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test5(self):
        input = """a: array [1] of integer = {}; """
        expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test6(self):
        input = """a: array [1] of integer = {1,2,3}; """
        expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test7(self):
        input = """a: array [1] of integer = {a,b,c}; """
        expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayLit([Id(a), Id(b), Id(c)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test8(self):
        input = """a: array [1] of integer = {true, 3, {}}; """
        expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayLit([BooleanLit(True), IntegerLit(3), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test9(self):
        input = """
            fact: function integer(){
                
            }
        """
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test10(self):
        input = """
            main: function void () {
                x = foo(-{1,2,3});
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), FuncCall(foo, [UnExpr(-, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test11(self):
        input = """
        main: function void (){
            if (i) return 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(i), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test12(self):
        input = """main: function void (){
                x: integer = 1;
                x= -foo(b,c,d,e);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), AssignStmt(Id(x), UnExpr(-, FuncCall(foo, [Id(b), Id(c), Id(d), Id(e)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test13(self):
        input = """
        main: function void (inherit out x: string){
            if(true){
                id = (------------id == 21) > 4;
            }
            else {
                if(false){}else{}
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(x, StringType)], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(id), BinExpr(>, BinExpr(==, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, Id(id))))))))))))), IntegerLit(21)), IntegerLit(4)))]), BlockStmt([IfStmt(BooleanLit(False), BlockStmt([]), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test14(self):
        input = """
            main:function void (){
                if (x) 
                    if(y) return 1; 
                    else return 2;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(x), IfStmt(Id(y), ReturnStmt(IntegerLit(1)), ReturnStmt(IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test15(self):
        input = """
        inc: function void(out n: integer, delta: integer) inherit abc {
            if(--a[foo(8,{1,3,4}),a[a[a[5]]]]) return;
            else 
                if (_1) return a==2+d; 
                else return true;
        }      
        """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], abc, BlockStmt([IfStmt(UnExpr(-, UnExpr(-, ArrayCell(a, [FuncCall(foo, [IntegerLit(8), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4)])]), ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(5)])])])]))), ReturnStmt(), IfStmt(Id(_1), ReturnStmt(BinExpr(==, Id(a), BinExpr(+, IntegerLit(2), Id(d)))), ReturnStmt(BooleanLit(True))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test16(self):
        input = """
            fibo: function integer (n: integer){
                if (n==1) return 1;
                if (n==0) return 0;
                return n + fibo(n-1);
            }  
        """
        expect = """Program([
	FuncDecl(fibo, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1))), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(0))), ReturnStmt(BinExpr(+, Id(n), FuncCall(fibo, [BinExpr(-, Id(n), IntegerLit(1))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        input = """
        main: function void (){
            while(true)
                do{
                    a[-"a"]=b>d;
                }while(1);
        } 
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), DoWhileStmt(IntegerLit(1), BlockStmt([AssignStmt(ArrayCell(a, [UnExpr(-, StringLit(a))]), BinExpr(>, Id(b), Id(d)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test18(self):
        input = """
            a:integer = a[1];
            b: string = {-foo(),123,"string"};
            sum: function integer(a:integer, b:integer){
                return (a+b);
            } 
        """
        expect = """Program([
	VarDecl(a, IntegerType, ArrayCell(a, [IntegerLit(1)]))
	VarDecl(b, StringType, ArrayLit([UnExpr(-, FuncCall(foo, [])), IntegerLit(123), StringLit(string)]))
	FuncDecl(sum, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        input = """
            max:function integer (x:integer, y:integer){
                if (x > y)
                    return x;
                else
                    return y;
            }  
            main:function void(){
                m:integer = max(9,!-1);
                print(m);
            }
        """
        expect = """Program([
	FuncDecl(max, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(x), Id(y)), ReturnStmt(Id(x)), ReturnStmt(Id(y)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(m, IntegerType, FuncCall(max, [IntegerLit(9), UnExpr(!, UnExpr(-, IntegerLit(1)))])), CallStmt(print, Id(m))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        input = """
            True:function boolean(x:integer){
                return !true;
            }  
        """
        expect = """Program([
	FuncDecl(True, BooleanType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(UnExpr(!, BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test21(self):
        input = """
            I_Luv_U: function string(life: integer){
                while(life != end){
                    print("I" + "Will" + "Keep" + "Loving" + "You");
                    life = life + 1;
                }
                return I_Luv_U(life-life);
            }  
        """
        expect = """Program([
	FuncDecl(I_Luv_U, StringType, [Param(life, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(!=, Id(life), Id(end)), BlockStmt([CallStmt(print, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, StringLit(I), StringLit(Will)), StringLit(Keep)), StringLit(Loving)), StringLit(You))), AssignStmt(Id(life), BinExpr(+, Id(life), IntegerLit(1)))])), ReturnStmt(FuncCall(I_Luv_U, [BinExpr(-, Id(life), Id(life))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test22(self):
        input = """
            Travelling_path: function string(start: string,end:string){
                while(start!=end){
                    path = path + start;
                    start = nextDest(start);
                }
                return path;
            }   
        """
        expect = """Program([
	FuncDecl(Travelling_path, StringType, [Param(start, StringType), Param(end, StringType)], None, BlockStmt([WhileStmt(BinExpr(!=, Id(start), Id(end)), BlockStmt([AssignStmt(Id(path), BinExpr(+, Id(path), Id(start))), AssignStmt(Id(start), FuncCall(nextDest, [Id(start)]))])), ReturnStmt(Id(path))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test23(self):
        input = """
                        x:integer = {1,2,3==foo()+(4>6)} ;    
        """
        expect = """Program([
	VarDecl(x, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), BinExpr(==, IntegerLit(3), BinExpr(+, FuncCall(foo, []), BinExpr(>, IntegerLit(4), IntegerLit(6))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test24(self):
        input = """a: array [2] of integer = {}; """
        expect = """Program([
	VarDecl(a, ArrayType([2], IntegerType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test25(self):
        input = """
            isEqual: function boolean (_1:string, _2:string){
                return _1==_2;
            }
        """
        expect = """Program([
	FuncDecl(isEqual, BooleanType, [Param(_1, StringType), Param(_2, StringType)], None, BlockStmt([ReturnStmt(BinExpr(==, Id(_1), Id(_2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test26(self):
        input = """_x_:string = {{\n}}; """
        expect = """Program([
	VarDecl(_x_, StringType, ArrayLit([ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test27(self):
        input = """
            /* This 
            is 
            a 
            comment */
            concat:function string(string1:string, string2:string){
                return string1::string2;
            }
        """
        expect = """Program([
	FuncDecl(concat, StringType, [Param(string1, StringType), Param(string2, StringType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(string1), Id(string2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test28(self):
        input = """
            concat:function string(string1:string,string2:string,string3:string){
                return {(string1::(string2::string3))};
            }
        """
        expect = """Program([
	FuncDecl(concat, StringType, [Param(string1, StringType), Param(string2, StringType), Param(string3, StringType)], None, BlockStmt([ReturnStmt(ArrayLit([BinExpr(::, Id(string1), BinExpr(::, Id(string2), Id(string3)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test29(self):
        input = """
            main:function void (){
                a = a+b::c+d;
            }  
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(+, Id(a), Id(b)), BinExpr(+, Id(c), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test30(self):
        input = """
            arr:function integer () {
                return {{},{},{}};
            } 
        """
        expect = """Program([
	FuncDecl(arr, IntegerType, [], None, BlockStmt([ReturnStmt(ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test31(self):
        input = """
                a:auto = true||false::"a";
        """
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(::, BinExpr(||, BooleanLit(True), BooleanLit(False)), StringLit(a)))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test32(self):
        input = """a:string = {"}"}; """
        expect = """Program([
	VarDecl(a, StringType, ArrayLit([StringLit(})]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        input = """
            program: function string(){
                for (i = foo(goo(hoo({1,2,3}))), (x+2)==(z>=a[4]), a[{1}] + 1)
                {
                
                }
            }  
        """
        expect = """Program([
	FuncDecl(program, StringType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), FuncCall(foo, [FuncCall(goo, [FuncCall(hoo, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])])])), BinExpr(==, BinExpr(+, Id(x), IntegerLit(2)), BinExpr(>=, Id(z), ArrayCell(a, [IntegerLit(4)]))), BinExpr(+, ArrayCell(a, [ArrayLit([IntegerLit(1)])]), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test34(self):
        input = """
            func:function void() {
                a[1::2] = 1;
                return;
            }  
        """
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(::, IntegerLit(1), IntegerLit(2))]), IntegerLit(1)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test35(self):
        input = """
            hpt: string = "dep trai\\n";
        """
        expect = """Program([
	VarDecl(hpt, StringType, StringLit(dep trai\\n))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test36(self):
        input = """
            a:float = .00001e5;
        """
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(1.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test37(self):
        input = """
            a:float = 12.34e-56;
        """
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(1.234e-55))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test38(self):
        input = """
            /* @#$%^^&************(())*/
            factorial: function float (n:float){
                if (n==1) return 1;
                return n * factorial(n-1);

            }
        """
        expect = """Program([
	FuncDecl(factorial, FloatType, [Param(n, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1))), ReturnStmt(BinExpr(*, Id(n), FuncCall(factorial, [BinExpr(-, Id(n), IntegerLit(1))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test39(self):
        input = """
            floaT: function float (){
                return 1.;
            }
        """
        expect = """Program([
	FuncDecl(floaT, FloatType, [], None, BlockStmt([ReturnStmt(FloatLit(1.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test40(self):
        input = """
            main:function float (){
                foo(1.E-10);
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([CallStmt(foo, FloatLit(1e-10))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test41(self):
        input = """
            _1:string = ("asd"::123)::foo(bc::{123,321});
        """
        expect = """Program([
	VarDecl(_1, StringType, BinExpr(::, BinExpr(::, StringLit(asd), IntegerLit(123)), FuncCall(foo, [BinExpr(::, Id(bc), ArrayLit([IntegerLit(123), IntegerLit(321)]))])))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test42(self):
        input = """
             _1:string = ("asd"::123)::(a[4]::foo(bc::{123,321}));
        """
        expect = """Program([
	VarDecl(_1, StringType, BinExpr(::, BinExpr(::, StringLit(asd), IntegerLit(123)), BinExpr(::, ArrayCell(a, [IntegerLit(4)]), FuncCall(foo, [BinExpr(::, Id(bc), ArrayLit([IntegerLit(123), IntegerLit(321)]))]))))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test43(self):
        input = """
            HpTIsmE: function integer (out x:string){
                a_b_c_=1_2_3_4_5.E-9;
            }
        """
        expect = """Program([
	FuncDecl(HpTIsmE, IntegerType, [OutParam(x, StringType)], None, BlockStmt([AssignStmt(Id(a_b_c_), FloatLit(1.2345e-05))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test44(self):
        input = """
            x: float = 1_2_3.e-10 + ---2_3_4.E20;
        """
        expect = """Program([
	VarDecl(x, FloatType, BinExpr(+, FloatLit(1.23e-08), UnExpr(-, UnExpr(-, UnExpr(-, FloatLit(2.34e+22))))))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test45(self):
        input = """
            quadratic_eqation_solver: function float(a:float,b:float,c:float){
                delta = b*b - 4*a*c;
                x1 = (-b - sqrt(delta))/(2*a) ;
                x2 = (-b + sqrt(delta))/(2*a) ;
                return {x1,x2};
            }
            main:function void (){
                print(quadratic_equation_solver(1,2,1));
            }
        """
        expect = """Program([
	FuncDecl(quadratic_eqation_solver, FloatType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([AssignStmt(Id(delta), BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), AssignStmt(Id(x1), BinExpr(/, BinExpr(-, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(x2), BinExpr(/, BinExpr(+, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), ReturnStmt(ArrayLit([Id(x1), Id(x2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(quadratic_equation_solver, [IntegerLit(1), IntegerLit(2), IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test46(self):
        input = """
            quadratic_eqation_solver: function float(a:float,b:float,c:float){
                delta = b*b - 4*a*c;
                x1 = (-b - sqrt(delta))/(2*a) ;
                x2 = (-b + sqrt(delta))/(2*a) ;
                return {x1,x2};
            }
            quartic_equation_solver: function float(a:float,b:float,c:float){
                res: array [2] of float = quadratic_equation_solver(a,b,c);
                x1,x2,x3,x4:float = -squrt(res[0]),sqrt(res[o]),-sqrt(res[1]),sqrt(res[1]);
                return {x1,x2,x3,x4};
            }
            main:function void (){
                print(quartic_equation_solver(1,2,1));
            }
        """
        expect = """Program([
	FuncDecl(quadratic_eqation_solver, FloatType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([AssignStmt(Id(delta), BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), AssignStmt(Id(x1), BinExpr(/, BinExpr(-, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(x2), BinExpr(/, BinExpr(+, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), ReturnStmt(ArrayLit([Id(x1), Id(x2)]))]))
	FuncDecl(quartic_equation_solver, FloatType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([VarDecl(res, ArrayType([2], FloatType), FuncCall(quadratic_equation_solver, [Id(a), Id(b), Id(c)])), VarDecl(x1, FloatType, UnExpr(-, FuncCall(squrt, [ArrayCell(res, [IntegerLit(0)])]))), VarDecl(x2, FloatType, FuncCall(sqrt, [ArrayCell(res, [Id(o)])])), VarDecl(x3, FloatType, UnExpr(-, FuncCall(sqrt, [ArrayCell(res, [IntegerLit(1)])]))), VarDecl(x4, FloatType, FuncCall(sqrt, [ArrayCell(res, [IntegerLit(1)])])), ReturnStmt(ArrayLit([Id(x1), Id(x2), Id(x3), Id(x4)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(quartic_equation_solver, [IntegerLit(1), IntegerLit(2), IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test47(self):
        input = """
            //Hello world in MT22 language
            main: function void(){
                printStr("Hello world");
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printStr, StringLit(Hello world))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test48(self):
        input = """
            eat: function void(animal: string){
                if (animal=="dog") food = meat;
                else if (animal == "cat") food = fish;
                else food = worm;
            }
        """
        expect = """Program([
	FuncDecl(eat, VoidType, [Param(animal, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(animal), StringLit(dog)), AssignStmt(Id(food), Id(meat)), IfStmt(BinExpr(==, Id(animal), StringLit(cat)), AssignStmt(Id(food), Id(fish)), AssignStmt(Id(food), Id(worm))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test49(self):
        input = """
            eat: function void(animal: string){
                if (animal=="dog") {food = meat;}
                else {if (animal == "cat") {food = fish;}
                else {food = worm;}}
            }
        """
        expect = """Program([
	FuncDecl(eat, VoidType, [Param(animal, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(animal), StringLit(dog)), BlockStmt([AssignStmt(Id(food), Id(meat))]), BlockStmt([IfStmt(BinExpr(==, Id(animal), StringLit(cat)), BlockStmt([AssignStmt(Id(food), Id(fish))]), BlockStmt([AssignStmt(Id(food), Id(worm))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test50(self):
        input = """
            bool1,bool2:boolean = a[true],b[false];
        """
        expect = """Program([
	VarDecl(bool1, BooleanType, ArrayCell(a, [BooleanLit(True)]))
	VarDecl(bool2, BooleanType, ArrayCell(b, [BooleanLit(False)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test51(self):
        input = """
            main: function boolean (x:boolean){
                {
                    if(1) do{
                    
                    }while(a);
                }
            }
        """
        expect = """Program([
	FuncDecl(main, BooleanType, [Param(x, BooleanType)], None, BlockStmt([BlockStmt([IfStmt(IntegerLit(1), DoWhileStmt(Id(a), BlockStmt([])))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test52(self):
        input = """
            main:function void(){
                foo(
                    3,
                    4,
                    -goo(),
                    a[t],
                    .E2
                )
                ;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(3), IntegerLit(4), UnExpr(-, FuncCall(goo, [])), ArrayCell(a, [Id(t)]), FloatLit(0.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test53(self):
        input = """
		x:float = -.e1;
		"""
        expect = """Program([
	VarDecl(x, FloatType, UnExpr(-, FloatLit(0.0)))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test54(self):
        input = """
		x:float = -1.e0000;
		y:boolean = a&&(true||false);
		"""
        expect = """Program([
	VarDecl(x, FloatType, UnExpr(-, FloatLit(1.0)))
	VarDecl(y, BooleanType, BinExpr(&&, Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False))))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test55(self):
        input = """
		main:function boolean(inherit out x: integer) inherit abc {
			
		}
		"""
        expect = """Program([
	FuncDecl(main, BooleanType, [InheritOutParam(x, IntegerType)], abc, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test56(self):
        input = """
		main:function boolean(inherit out x: integer) inherit abc {
			a,b,c,d:auto;
		}
		"""
        expect = """Program([
	FuncDecl(main, BooleanType, [InheritOutParam(x, IntegerType)], abc, BlockStmt([VarDecl(a, AutoType), VarDecl(b, AutoType), VarDecl(c, AutoType), VarDecl(d, AutoType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test57(self):
        input = """
		a:array [2,3] of string = {"1","2"}; 
		"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], StringType), ArrayLit([StringLit(1), StringLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test58(self):
        input = """
		goo:function void (t:auto) {
			t[1,2,goo(t)] = -3.;
		}
		"""
        expect = """Program([
	FuncDecl(goo, VoidType, [Param(t, AutoType)], None, BlockStmt([AssignStmt(ArrayCell(t, [IntegerLit(1), IntegerLit(2), FuncCall(goo, [Id(t)])]), UnExpr(-, FloatLit(3.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test59(self):
        input = """
		a:array [2,3] of string = {"1","2"}; 
		a:array [2,3] of boolean = {{},{}};
		a:array [2,3] of integer = {goo()};  
		"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], StringType), ArrayLit([StringLit(1), StringLit(2)]))
	VarDecl(a, ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([FuncCall(goo, [])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test60(self):
        input = """
		b:integer = 1.e0 - -2.E12 + -str;
		"""
        expect = """Program([
	VarDecl(b, IntegerType, BinExpr(+, BinExpr(-, FloatLit(1.0), UnExpr(-, FloatLit(2000000000000.0))), UnExpr(-, Id(str))))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test61(self):
        input = """
		a:function void(){}
		b:function void(){}
		c:float;
		"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([]))
	FuncDecl(b, VoidType, [], None, BlockStmt([]))
	VarDecl(c, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test62(self):
        input = """
		a:function void(){
			do {
				if(1) 
					for(a="x"::"y", a >= goo()||foo(), a&&true){}
			}while(false);
		} 
		"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([IfStmt(IntegerLit(1), ForStmt(AssignStmt(Id(a), BinExpr(::, StringLit(x), StringLit(y))), BinExpr(>=, Id(a), BinExpr(||, FuncCall(goo, []), FuncCall(foo, []))), BinExpr(&&, Id(a), BooleanLit(True)), BlockStmt([])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        input = """
			test:function auto () {
				a = a-b+c*d/e;
			}
		"""
        expect = """Program([
	FuncDecl(test, AutoType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(-, Id(a), Id(b)), BinExpr(/, BinExpr(*, Id(c), Id(d)), Id(e))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test64(self):
        input = """
		main:function array [1,2,3] of string () {
			return {1,2,3};
		}  
		"""
        expect = """Program([
	FuncDecl(main, ArrayType([1, 2, 3], StringType), [], None, BlockStmt([ReturnStmt(ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test65(self):
        input = """
		h,g: auto;
		main:function void (inherit h: integer, out g: string) {
			h = g;
		}
		"""
        expect = """Program([
	VarDecl(h, AutoType)
	VarDecl(g, AutoType)
	FuncDecl(main, VoidType, [InheritParam(h, IntegerType), OutParam(g, StringType)], None, BlockStmt([AssignStmt(Id(h), Id(g))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test66(self):
        input = """
		l:string = "{\\'}";
		"""
        expect = """Program([
	VarDecl(l, StringType, StringLit({\\'}))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test67(self):
        input = """
		sum:function integer(a:integer, b:integer) {
			return a + b + 1_22222222_3e2;
		}
		"""
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(a), Id(b)), FloatLit(122222222300.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test68(self):
        input = """
			b:function void () inherit a{
				{{{{{{{}}}}}}}
			}
		"""
        expect = """Program([
	FuncDecl(b, VoidType, [], a, BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test69(self):
        input = """
		main:function boolean () {
			while(1) if(2) {} else str = ((str::str)::str)::str;
		}
		"""
        expect = """Program([
	FuncDecl(main, BooleanType, [], None, BlockStmt([WhileStmt(IntegerLit(1), IfStmt(IntegerLit(2), BlockStmt([]), AssignStmt(Id(str), BinExpr(::, BinExpr(::, BinExpr(::, Id(str), Id(str)), Id(str)), Id(str)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test70(self):
        input = """
		 input: auto;
		 i:  function void () {
			input[1] = input;
			goo();
		 }
		"""
        expect = """Program([
	VarDecl(input, AutoType)
	FuncDecl(i, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(input, [IntegerLit(1)]), Id(input)), CallStmt(goo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test71(self):
        input = """
		 i:  function void () {
			foo();
			goo();
			hoo();
		 }
		"""
        expect = """Program([
	FuncDecl(i, VoidType, [], None, BlockStmt([CallStmt(foo, ), CallStmt(goo, ), CallStmt(hoo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test72(self):
        input = """
		main:function void (){
			____1 = 1_0;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(____1), IntegerLit(10))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        input = """
		func:function string () {
			goo(1||2);
		}
		"""
        expect = """Program([
	FuncDecl(func, StringType, [], None, BlockStmt([CallStmt(goo, BinExpr(||, IntegerLit(1), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test74(self):
        input = """
		def:function integer () {
			return def(_x && _y);
		}
		"""
        expect = """Program([
	FuncDecl(def, IntegerType, [], None, BlockStmt([ReturnStmt(FuncCall(def, [BinExpr(&&, Id(_x), Id(_y))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test75(self):
        input = """
			a: array [1] of boolean = {self(a[1],{})};
		"""
        expect = """Program([
	VarDecl(a, ArrayType([1], BooleanType), ArrayLit([FuncCall(self, [ArrayCell(a, [IntegerLit(1)]), ArrayLit([])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test76(self):
        input = """
		block: function void () {
			block = block == block;
		}
		"""
        expect = """Program([
	FuncDecl(block, VoidType, [], None, BlockStmt([AssignStmt(Id(block), BinExpr(==, Id(block), Id(block)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = """
		 i:  function void () {
			return (a==3) || (b==a);	
		}
		"""
        expect = """Program([
	FuncDecl(i, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(||, BinExpr(==, Id(a), IntegerLit(3)), BinExpr(==, Id(b), Id(a))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test78(self):
        input = """
		null:function void (null:auto){
			return;
		}
		"""
        expect = """Program([
	FuncDecl(null, VoidType, [Param(null, AutoType)], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test79(self):
        input = """
		str: string = "";
		"""
        expect = """Program([
	VarDecl(str, StringType, StringLit())
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test80(self):
        input = """
		_1,_2,_3,_4: auto = 1,2,3,4;
		"""
        expect = """Program([
	VarDecl(_1, AutoType, IntegerLit(1))
	VarDecl(_2, AutoType, IntegerLit(2))
	VarDecl(_3, AutoType, IntegerLit(3))
	VarDecl(_4, AutoType, IntegerLit(4))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test81(self):
        input = """
		 i:  function void () {
			t = foo(goo(hoo()));
		 }
		"""
        expect = """Program([
	FuncDecl(i, VoidType, [], None, BlockStmt([AssignStmt(Id(t), FuncCall(foo, [FuncCall(goo, [FuncCall(hoo, [])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test82(self):
        input = """
		main:function void (){
			return 1_0_1_2.e-00010;
		}
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(FloatLit(1.012e-07))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        input = """
		func:function string () {
			{goo(1&&2);}
		}
		"""
        expect = """Program([
	FuncDecl(func, StringType, [], None, BlockStmt([BlockStmt([CallStmt(goo, BinExpr(&&, IntegerLit(1), IntegerLit(2)))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test84(self):
        input = """
		BinExp:function array [2,2] of string () {
			BinExp = {BinExp[1]};
		}
		"""
        expect = """Program([
	FuncDecl(BinExp, ArrayType([2, 2], StringType), [], None, BlockStmt([AssignStmt(Id(BinExp), ArrayLit([ArrayCell(BinExp, [IntegerLit(1)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test85(self):
        input = """
			a: array [1] of boolean;
		"""
        expect = """Program([
	VarDecl(a, ArrayType([1], BooleanType))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test86(self):
        input = """
		block: function void () {
			block = (block || block == block || block);
		}
		"""
        expect = """Program([
	FuncDecl(block, VoidType, [], None, BlockStmt([AssignStmt(Id(block), BinExpr(==, BinExpr(||, Id(block), Id(block)), BinExpr(||, Id(block), Id(block))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test87(self):
        input = """
		 stage: function auto () {
			if(!isDead()){
				stage = stage + 1;
			}
			return false;
		 }
		"""
        expect = """Program([
	FuncDecl(stage, AutoType, [], None, BlockStmt([IfStmt(UnExpr(!, FuncCall(isDead, [])), BlockStmt([AssignStmt(Id(stage), BinExpr(+, Id(stage), IntegerLit(1)))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test88(self):
        input = """
		null:function void (inherit out null: integer) inherit null{
			return null + none;
		}
		"""
        expect = """Program([
	FuncDecl(null, VoidType, [InheritOutParam(null, IntegerType)], null, BlockStmt([ReturnStmt(BinExpr(+, Id(null), Id(none)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test89(self):
        input = """
		str: string = {""};
		"""
        expect = """Program([
	VarDecl(str, StringType, ArrayLit([StringLit()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test90(self):
        input = """
		func1:function void () {}
		func2:function void () inherit func1 {
			func1();
			return func1();
		}
		"""
        expect = """Program([
	FuncDecl(func1, VoidType, [], None, BlockStmt([]))
	FuncDecl(func2, VoidType, [], func1, BlockStmt([CallStmt(func1, ), ReturnStmt(FuncCall(func1, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test91(self):
        input = """
		a,b,c,d : string = a[1],b+d,{123,4},foo(goo(hoo()));
		"""
        expect = """Program([
	VarDecl(a, StringType, ArrayCell(a, [IntegerLit(1)]))
	VarDecl(b, StringType, BinExpr(+, Id(b), Id(d)))
	VarDecl(c, StringType, ArrayLit([IntegerLit(123), IntegerLit(4)]))
	VarDecl(d, StringType, FuncCall(foo, [FuncCall(goo, [FuncCall(hoo, [])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = """ 
		fact: function integer(){
                if(true) {a,b,c,d: integer;}
            }
		"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType), VarDecl(d, IntegerType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        input = """
		main: function void () {
                x = foo(-{1,2,3});
                while (true) {
                    do {}
                    while(false);
                }
            }
		"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), FuncCall(foo, [UnExpr(-, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))])), WhileStmt(BooleanLit(True), BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test94(self):
        input = """
        sub: function integer(){{{{
            do {x = x + 1;}
            while(true);
        }}}}  
        """
        expect = """Program([
	FuncDecl(sub, IntegerType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test95(self):
        input = """
            True:function boolean(x:integer){
                return true-false == a || b;
            }  
        """
        expect = """Program([
	FuncDecl(True, BooleanType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(==, BinExpr(-, BooleanLit(True), BooleanLit(False)), BinExpr(||, Id(a), Id(b))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test96(self):
        input = """
		x:integer = {1,2,(3==4)>6}  	;
		"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), BinExpr(>, BinExpr(==, IntegerLit(3), IntegerLit(4)), IntegerLit(6))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = """
		fact: function integer (){
              {
                  {  
                    return;
                  }
              }
	    }
		"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([BlockStmt([BlockStmt([ReturnStmt()])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test98(self):
        input = """
		a : integer = {{{{{{{{}}}}}}},s};
		"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([])])])])])])]), Id(s)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test99(self):
        input = """
            a,_ : auto = _,_;
            main:function void (){
                
            }
        """
        expect = """Program([
	VarDecl(a, AutoType, Id(_))
	VarDecl(_, AutoType, Id(_))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test100(self):
        input = """
		 func: function array [2,2] of integer (){
                return {{1},{2},{3}};
            }  
        """
        expect = """Program([
	FuncDecl(func, ArrayType([2, 2], IntegerType), [], None, BlockStmt([ReturnStmt(ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)]), ArrayLit([IntegerLit(3)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
