import unittest
from TestUtils import TestChecker
from AST import *
from StaticError import *
from abc import ABC
from Visitor import Visitor


class CheckerSuite(unittest.TestCase):
    def test_1(self):
        input = """
            a:integer;
            a:integer;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test_1_1(self):
        input = """
            foo: function integer (inherit a: integer, inherit b: integer) {
                return a + b;	
            }
            foo: function float (inherit a: integer, inherit b: integer) {
                return a + b;	
            }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 400_1))
        
    def test_1_2(self):
        input = """
            foo: function integer (inherit a: integer, inherit b: integer) {
                c: integer;
                d: integer;
                c: float;
                return a + b;	
            }
            foo1: function float (inherit a: integer, inherit b: integer) {
                return a + b;	
            }
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 400_2))
        
    def test_1_3(self):
        input = """
            a: integer;
            main: function void () {
                
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400_3))
        
    def test_2(self):
        input = """
            a:integer = 1.4;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(1.4))"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_3(self):
        input = """
            a:float = 1;
            main: function void () {
                
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_4(self):
        input = """
            a:integer = 1.4 + 1;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, FloatLit(1.4), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_5(self):
        input = """
            a:integer = 1 + 2.2;
            a:integer;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, IntegerLit(1), FloatLit(2.2)))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_6(self):
        input = """
            a:auto = 10;
            b:auto = " hello";
            c:auto = a < 100.1;
        """
        expect = "Type mismatch in expression: BinExpr(<, Id(a), FloatLit(100.1))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_7(self):
        input = """
            a:auto = 10;
            b:auto = " hello";
            c:auto = a < 100;
            d:auto = b + a;
        """
        expect = "Type mismatch in expression: BinExpr(+, Id(b), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_8(self):
        input = """
            a: auto = 10;
            a: function auto ( a : integer , b : integer ) {}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_9(self):
        input = """
            a:auto = 10;
            b : function auto ( a : integer , b : integer ) {
                c: float = foo(1, 2);
                d: integer = foo(1, 2) + 1;
                foo(1, 2);
            }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_10(self):
        input = """
            a:auto = 10;
            foo : function auto ( a : integer , b : integer ) {
                c: float = foo(1, 2);
                d: integer = foo(1, 2) + 1;
                foo(1, 2);
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(d, IntegerType, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_11(self):
        input = """
            a:auto = 10;
            foo : function auto ( a : string , b : integer ) {
                c: float = foo(1, 2);
                d: integer = foo(1, 2) + a;
                foo(1, 2);
            }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_12(self):
        input = """
            a:auto = 10;
            foo : function auto ( a : integer , b : integer ) {
                c: integer = foo(1, 2);
                d: integer = foo(1, 2) + c;
                a(1, 2);
            }
        """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_13(self):
        input = """
            a:auto = 10;
            foo : function auto ( a : integer , b : integer ) {
                c: integer = foo(1, 2, 3);
                d: integer = foo(1, 2) + c;
                foo(1, 2);
            }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_14(self):
        input = """
            a:auto = 10;
            foo : function auto ( a : integer , b : integer ) {
                c: integer = foo(1, 2);
                d: integer = foo(1, 2) + c;
                foo(1, 2);
            }
        """
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_15(self):
        input = """
            a:auto = 10;
            foo : function auto ( a : integer , b : integer ) {
                c: integer = foo(1, 2);
                d: integer = foo(1, 2) + c;
                i: array [2, 3] of integer  = {"Kangxi", "Yongzheng", 1};
            }
        """
        expect = "Illegal array literal: ArrayLit([StringLit(Kangxi), StringLit(Yongzheng), IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_16(self):
        input = """
            a:auto = 10;
            foo : function auto ( a : integer , b : integer ) {
                c: integer = foo(1, 2);
                d: integer = foo(1, 2) + c;
                i: array [2, 3] of integer  = {"Kangxi", "Yongzheng", "Hello"};
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(i, ArrayType([2, 3], IntegerType), ArrayLit([StringLit(Kangxi), StringLit(Yongzheng), StringLit(Hello)]))"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_17(self):
        input = """
            a:auto = 10;
            foo : function auto ( a : integer , b : integer ) {
                i: array [2, 3] of integer  = {1, 2, 3};
                k: string = i;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(k, StringType, Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_18(self):
        input = """
            a:auto = 10;
            foo : function auto ( c : integer , b : integer ) {
                a: auto;
            }
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_19(self):
        input = """
            a:auto = 10;
            foop : function auto ( inherit c : integer , b : integer ){

            }
            foo : function auto ( c : integer) inherit foop {
                preventDefault();
            }
        """
        expect = "Invalid Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_20(self):
        input = """
            a:auto = 10;
            foop : function auto ( inherit c : integer , b : integer ){
                a: integer = 1+ 12 +14;
            }
            foo : function auto ( d : integer) inherit foop {
                super(1,2);
                a: string = 12;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, IntegerLit(12))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_21(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                preventDefault();
                a: string = 12;
            }
            foop : function auto ( inherit c : integer , b : integer ){
                a: integer = 1+ 12 + 14;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, IntegerLit(12))"
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_22(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer, d: integer) inherit foop {
                preventDefault();
                a: string = 12;
            }
            foop : function auto ( inherit c : integer , b : integer ){
                a: integer = 1+ 12 + 14;
            }
        """
        expect = "Redeclared Parameter: d"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_23(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) {
                a: string = "hello";
                i: array [2, 3] of string  = {"Kangxi", "Yongzheng", "hehe"};
                i = a;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(i), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_24(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer){
                a: string = "hello";
                i: array [2, 3] of string  = {"Kangxi", "Yongzheng", "hehe"};
                a = foo(1);
                d = foo(1);
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(d), FuncCall(foo, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_25(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer){
                a: string = "hello";
                i: array [2, 3] of string  = {"Kangxi", "Yongzheng", "hehe"};
                a = foo(1, 2);
                d = foo(1);
            }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_26(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : float){
                a: string = "hello";
                i: array [2, 3] of string  = {"Kangxi", "Yongzheng", "hehe"};
                a = foo(1.2);
                d = foo(1);
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_27(self):
        input = """
            a: auto = 10;
            foo : function auto ( d : float){
                return 1;
                return 3.3;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(3.3))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_28(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : float){
                i: integer;
                for (i = 1, i + 1, i + 1) {
                    a = a + 1;
                }
            }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_29(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : float){
                i: float;
                for (i = 1, i > 1.1, i + 1) {
                    a = a + 1;
                }
            }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(>, Id(i), FloatLit(1.1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_30(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : float){
                i: float;
                for (i = 1, i , i + 1) {
                    a = a + 1;
                }
            }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), Id(i), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_31(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : float){
                i: integer;
                for (i = 1, i < 1, i + 1) {
                    a = a + 1;
                }
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_32(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : float){
                i: float;
                if (b > 1) { b = b + 1;}
                    else { b = b + 1;}

            }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_33(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : float) {
                i: float;
                b: float;
                if (b + 1) { b = b + 1;}
                    else { b = b + 1;}
            }
        """
        expect = "Type mismatch in statement: IfStmt(BinExpr(+, Id(b), IntegerLit(1)), BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_34(self):
        input = """     
 
            foo2: function void (d: integer, e: string){}
            foo: function integer (a: array [1] of integer, c: auto) {
                d : integer;
                foo2(d, c);
                for (d = 1, d < 10, 1 + 2){
                }
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_35(self):
        input = """     
            foo2: function void (d: integer, e: string){}
            foo: function integer (a: array [1] of integer, c: auto) {
                d : integer;
                foo2(d, c);
                for (d = 1, d < 10, 1 + 2){
                    a["1"] = 1;
                }
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in expression: ArrayCell(a, [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_36(self):
        input = """     
            foo2: function void (d: integer, e: string){}
            foo: function integer (a: array [1] of integer, c: auto) {
                d : integer;
                foo2(d, c);
                for (d = 1, d < 10, 1 + 2){
                    a[1] = "a";
                }
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(1)]), StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_37(self):
        input = """     
            foo2: function void (d: integer, e: string){}
            foo: function integer (a: array [1] of integer, c: auto) {
                d : integer;
                foo2(d, c);
                for (d = 1, d < 10, 1 + 2){
                    a[1] = e;
                }
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_38(self):
        input = """     
            foo2: function void (d: integer, e: string){}
            foo: function integer (a: array [1] of integer, c: auto) {
                d : integer;
                foo2(d, c);
                for (d = 1, d < 10, 1 + 2){
                    break;
                    a[1] = e;
                }
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_39(self):
        input = """     
            foo2: function void (d: integer, e: string){}
            foo: function integer (a: array [1] of integer, c: auto) {
                d : integer;
                foo2(d, c);
                break;
                for (d = 1, d < 10, 1 + 2){
                    break;
                    a[1] = e;
                }
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_40(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,"1");
            }
            foop : function auto ( inherit c : integer , b : integer ){

            }
        """
        expect = "Type mismatch in statement: CallStmt(super, IntegerLit(1), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_41(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                readInteger();
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "Type mismatch in statement: CallStmt(readInteger, )"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_42(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                readFloat();
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "Type mismatch in statement: CallStmt(readFloat, )"

    def test_43(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                readBoolean();
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "Type mismatch in statement: CallStmt(readBoolean, )"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                a = readBoolean();
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), FuncCall(readBoolean, []))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_44(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                a = readInteger();
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_45(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                a = printString("hello");
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "Type mismatch in expression: FuncCall(printString, [StringLit(hello)])"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_46(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                printBoolean(true);
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_47(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                while(a + 1) a = 1;
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "Type mismatch in statement: WhileStmt(BinExpr(+, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_48(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                while(a > 1) {
                    printInteger(1);
                    foop(1, 2.3);
                }
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "Type mismatch in statement: CallStmt(foop, IntegerLit(1), FloatLit(2.3))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_49(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                while(a > 1) {
                    printInteger(1);
                }

                do 
                {
                    a = 1 + 1;
                }
                while (a > 1);

                break;
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_50(self):
        input = """
            a:auto = 10;
            foo : function auto ( d : integer) inherit foop {
                super(1,1);
                while(a > 1) {
                    printInteger(1);
                }
                do 
                {
                    a = 1 + 1;
                }
                while (a + 1);
                break;
            }
            foop : function auto ( inherit c : integer , b : integer ){
            }
        """
        expect = "Type mismatch in statement: DoWhileStmt(BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 449))
