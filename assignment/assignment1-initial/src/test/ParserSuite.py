import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """ 
        a,b, c: integer;
        a integer; 
        """
        expect = "Error on line 3 col 10: integer"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2(self):
        input = """ 
        a, b, c: integer = 3, 4, 5
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_3(self):
        input = """
        a, b, c: integer = 3, 4, 5, 6;
        """
        expect = "Error on line 2 col 34: ,"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_4(self):
        input = """
        a, b, c, d: integer = 3, 4, 5;
        """
        expect = "Error on line 2 col 37: ;"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_5(self):
        input = """
        a, b: integer = 3+4, 9%2;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_6(self):
        input = """
        a, b, c: int = 3, 4, 5;
        """
        expect = "Error on line 2 col 17: int"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_7(self):
        input = """: integer;"""
        expect = "Error on line 1 col 0: :"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_8(self):
        input = """a: integer = ;"""
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_9(self):
        input = """a: array [2,3] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_10(self):
        input = """a: array [2,3] of integer"""
        expect = "Error on line 1 col 25: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_11(self):
        input = """func1: function integer () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_12(self):
        input = """func1: function integer (p1: integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_13(self):
        input = """func1: function integer (out inherit p1: integer) {}"""
        expect = "Error on line 1 col 29: inherit"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_14(self):
        input = """func1: function integer (p1: integer) inherit func2 {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_15(self):
        input = """func1: function integer (p1: integer) func2 {}"""
        expect = "Error on line 1 col 38: func2"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_16(self):
        input = """main: function void () {};"""
        expect = "Error on line 1 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_17(self):
        input = """
        fact: function integer (n: integer) {
            x: integer = 65;
            if (n == 0) {return 1;}
            else {return n * fact(n - 1);}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_18(self):
        input = """
        fact: function integer (n: integer) {
            x: integer = 65;
            if (n == 0) {return 1;}
            else {return n * fact(n - 1);};
        }
        """
        expect = "Error on line 5 col 42: ;"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_19(self):
        input = """
        fact: function integer (n: integer) {
            x: integer == 65;
            if (n == 0) {return 1;}
            else {return n * fact(n - 1);}
        }
        """
        expect = "Error on line 3 col 23: =="
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_20(self):
        input = """
        fact: function integer (n: integer) {
            x: integer = 65;
            if (n = 0) {return 1;}
            else {return n * fact(n - 1);}
        }
        """
        expect = "Error on line 4 col 18: ="
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_21(self):
        input = """
        main: function void() {
            do
                a = a + 1;
            while (a > b);
        }
        """
        expect = "Error on line 4 col 16: a"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_22(self):
        input = """
        main: function void() {
            do {
                a = a + 1;
            }
            while (a > b)  
        }
        """
        expect = "Error on line 7 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_23(self):
        input = """
        main: function void() {
            while a == b {
                a = a + 1;
            }
        }
        
        """
        expect = "Error on line 3 col 18: a"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_24(self):
        input = """
        main: function void() {
            while (a == b) {
                a += 1;
            }
        }
        
        """
        expect = "Error on line 4 col 18: +"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_25(self):
        input = """
        main: function void() {
            while (a == b) {
                a++;
            }
        }
        """
        expect = "Error on line 4 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_26(self):
        input = """
        main: function void () {
            for (i = 0, i < 100, i + 1) {
                writeInt(i);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_27(self):
        input = """main: function void () {
                foo(2 + x, 4.0 / y);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_28(self):
        input = """main: function void () {
                 a = goo() + 5;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_29(self):
        input = """main: function void () {
                return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_30(self):
        input = """main: function void () {
                if (a > b) 
                    a = a + 1;
                    b = b + 2;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_31(self):
        input = """
        a: array [3] of integer = {1, 2, 3};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_32(self):
        input = """ a: array [2 + 2,3] of integer ;"""
        expect = "Error on line 1 col 13: +"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_33(self):
        input = """
        main: function void () {
            a[2,3] = 4;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_34(self):
        input = """
        main: function void () {
            a[0,2+2] = 4;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_35(self):
        input = """
        main: function void () {
            a[0][1] = 4;
        }
        """
        expect = "Error on line 3 col 16: ["
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_36(self):
        input = """
        main: function void () {
            a[0;1] = 4;
        }
        """
        expect = "Error on line 3 col 15: ;"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_37(self):
        input = """
        main: function void () {
            a = b = 4;
        }
        """
        expect = "Error on line 3 col 18: ="
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_38(self):
        input = """
        main: function void () {
            a = 4 = b;
        }
        """
        expect = "Error on line 3 col 18: ="
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_39(self):
        input = """
        main: function void () {
            a * b = c;
        }
        """
        expect = "Error on line 3 col 14: *"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_40(self):
        input = """
        main: function void () {
            a == b + 4;
        }
        """
        expect = "Error on line 3 col 14: =="
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_41(self):
        input = """def int main()
        {
            int a;
            a = 4 + 5;
            return a;
        }"""
        expect = "Error on line 1 col 4: int"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_42(self):
        input = """printf("%d", 12345)"""
        expect = "Error on line 1 col 6: ("
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_43(self):
        input = """a, b : integer <- 2023, 2024"""
        expect = "Error on line 1 col 15: <"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_44(self):
        input = """float a, b, c; boolean x, y; z;"""
        expect = "Error on line 1 col 0: float"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_45(self):
        input = """fact: function integer (n: integer ) inherit"""
        expect = "Error on line 1 col 44: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_46(self):
        input = """a, b: bool = true, false"""
        expect = "Error on line 1 col 6: bool"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_47(self):
        input = """
        main: function void () {
            if (a == b) then {
            a = a + 1;
        } else
            b = b+1;
        }"""

        expect = "Error on line 3 col 29: {"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_48(self):
        input = """
        main: function void () {
            if (a == b) {
            a = a + 1;
        } else
            b = b+1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_49(self):
        input = """a: int = 6;"""
        expect = "Error on line 1 col 3: int"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_50(self):
        input = """a = fact(); b = fact(1,2,3);"""
        expect = "Error on line 1 col 2: ="
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_51(self):
        input = """
        main: function void (){
            fact(2!);
        }
        """
        expect = "Error on line 3 col 18: !"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_52(self):
        input = """main: function void ()
        {
            a: integer = sqr(2);}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_53(self):
        input = """a, b, c: integer = 2023, 2023., true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_54(self):
        input = """a: array [2] of integer = {1, 2};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_55(self):
        input = """
        main: function void () {
             a: integer = fact(2) + 2023;
        }
       """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_56(self):
        input = """
        a: integer == 2023;"""
        expect = "Error on line 2 col 19: =="
        self.assertTrue(TestParser.test(input, expect, 256))

    # Bug
    def test_57(self):
        input = """a: boolean = true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_58(self):
        input = """
        main: function void () {
            while a < 100 { a = a + 1;}
        } 
        """
        expect = "Error on line 3 col 18: a"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_59(self):
        input = """
        main: function void () {
            do a = a + 1 while a < 100;
        } """
        expect = "Error on line 3 col 15: a"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_60(self):
        input = """
        main: function void () {
            for (,,) {}
        } """
        expect = "Error on line 3 col 17: ,"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_61(self):
        input = """
         main: function void () {
            for (i=0,i<100,i+1) {
                break;
                break
            }
        } """

        expect = "Error on line 6 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_62(self):
        input = """main: function void () {
            return
            }"""
        expect = "Error on line 3 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_63(self):
        input = """main: function void () {
            id: INTEGER = 2023;
            }"""
        expect = "Error on line 2 col 16: INTEGER"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_64(self):
        input = """id: char = "a";"""
        expect = "Error on line 1 col 4: char"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_65(self):
        input = """a: array[] of integer;"""
        expect = "Error on line 1 col 9: ]"
        self.assertTrue(TestParser.test(input, expect, 265))

    # Bug
    def test_66(self):
        input = """flag: boolean = true && false;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_67(self):
        input = """a: array[1] of integer = {1; 2; 3};"""
        expect = "Error on line 1 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_68(self):
        input = """s: string = "string1" + "string2";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    # Bug
    def test_69(self):
        input = """main: function void () {
            for (i = 0, i < 100 && i > 5, i + 1) i = i * 2;}"""
        expect = "Error on line 2 col 37: >"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_70(self):
        input = """a: integer = (int)(8.7)"""
        expect = "Error on line 1 col 18: ("
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_71(self):
        input = """
        main: function void () {
             a: auto = 2;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_72(self):
        input = """main: function void () {
            if (a === b) {}
            }"""
        expect = "Error on line 2 col 20: ="
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_73(self):
        input = """main: function void () {
            if (m % 2 == 0) {}
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_74(self):
        input = """main: function void () {
            a: void;
            }"""
        expect = "Error on line 2 col 15: void"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_75(self):
        input = """main: function void () {
            a: array [2] of void;
            }"""
        expect = "Error on line 2 col 28: void"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_76(self):
        input = """main: function void () {
            a: array [2] of auto;
            }"""
        expect = "Error on line 2 col 28: auto"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_77(self):
        input = """
        main: function void () {
            if (!!a) {}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_78(self):
        input = """main: function void () {if (a !== b + c)}
         """
        expect = "Error on line 1 col 32: ="
        self.assertTrue(TestParser.test(input, expect, 278))

    # Bug
    def test_79(self):
        input = """main: function void () {if (a == b) && (c == d) a = a + 1;}"""
        expect = "Error on line 1 col 36: &&"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_80(self):
        input = """
        main: function void () {for (i == 0, i < 100, i++) {}}
        """
        expect = "Error on line 2 col 39: =="
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_81(self):
        input = """
        x: integer = 65;
        for (i = x; i < 100; i + 1) {
            i = i + 1;
        }
        main: function void() {
        }
        """
        expect = "Error on line 3 col 8: for"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_82(self):
        input = """
        x: integer = 65;
        if (x <= 100) {
            i = i + 1;
        }
        main: function void() {
        }        
        """
        expect = "Error on line 3 col 8: if"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_83(self):
        input = """
        main: function void() {
            if () {}
        } 
        """
        expect = "Error on line 3 col 16: )"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_84(self):
        input = """
        main: function void() {
            do {} while ();
        } """
        expect = "Error on line 3 col 25: )"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_85(self):
        input = """
        main: function void() {
            if (a == b) && (c == d) {
                
            } 
        } 
        """
        expect = "Error on line 3 col 24: &&"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_86(self):
        input = """
        main: function void() {
            if (a == b) {
                
            } else;
        } 
        """
        expect = "Error on line 5 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_87(self):
        input = """
        main: function void() {
            if (a == b) {
                if (c == d) {
                    
                }
            } else {
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_88(self):
        input = """
        main: function void() {
            for (i = 0, i < 100, i+1) {
                a: integer = 2023;
                for (j=0,j<i,j+1) {
                    
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89(self):
        input = """
        main: function void() {
            for (i = 0, i < 100, i+1) 
                for (j=0,j<i,j+1)
                    writeInt(i+j);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_90(self):
        input = """
        main: function void() {
            if ((a == b) && (c == d)) {
                writeInt(a + b + c + d);
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_91(self):
        input = """
        main: function void() {
            do {} while (a < b) && (c < d);
        }
        """
        expect = "Error on line 3 col 32: &&"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_92(self):
        input = """
        main: function void() {
            do {} while ((a < b) && (c < d));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_93(self):
        input = """
        main: function void() {
            a[2+3] = 2024 - 2023;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_94(self):
        input = """
        main: function void() {
            a[2+3] = 2024 - 2023;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_95(self):
        input = """
        main: function void () {
            while (i < 100) {
                if (i == 50) break;
                i = i - 1;
            }
        }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_96(self):
        input = """ 
        main: function void () 
        {
            r, s: integer;
            r = 2.0;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_97(self):
        input = """
        x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return (n * fact(n - 1));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_98(self):
        input = """
        x: integer = 5;
        fact: function integer (n: integer) {
        }
        fact(x);
        """
        expect = "Error on line 5 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_99(self):
        input = """
        x: integer = 65;
        inc: function void(inherit out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            inc(x, fact(3));
            printInteger(x);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_100(self):
        input = """
        inc: function void(out n: integer, delta: integer)
            n = n + delta;
        """
        expect = "Error on line 3 col 12: n"
        self.assertTrue(TestParser.test(input, expect, 300))

    # def test_301(self):
    #     input = """a : array [1] of array [2] integer = {a[3], true, 1, 1., .e3};"""
    #     expect = "Error on line 1 col 17: array"
    #     self.assertTrue(TestParser.test(input, expect, 301))

    # def test_302(self):
    #     input = """a : integer = {{1},foo({1})};"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 302))

    # def test_303(self):
    #     """Test For Statement"""
    #     input = """ main: function integer(){
    #                     for(i = 0, i < 3, i = i+1)
    #                         if (a==b)
    #                             c=d;
    #                     else d;
    #                 }"""
    #     expect = """successful"""
    #     self.assertTrue(TestParser.test(input, expect, 303))

    def test_304(self):
        input = """a : function array [1] of string () inherit c { do return 1; while ({} == 1);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 304))
