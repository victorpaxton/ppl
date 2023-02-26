import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # Test identifier
    def test_1(self):
        input = """A_0123, iDentifier_1"""
        expect = "A_0123,,,iDentifier_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))

    def test_2(self):
        input = """_@abcd"""
        expect = "_,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test_3(self):
        input = """a_1."""
        expect = "a_1,.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test_4(self):
        input = """1abc"""
        expect = "1,abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))

    # Comment
    def test_5(self):
        input = """ 
        abc id1 id2 _id id__1
        // inline comment
        /// inline /\ comment /
        for
        """
        expect = "abc,id1,id2,_id,id__1,for,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test_6(self):
        input = """
        id9 __id // This is a comment\n
        /// // This is a line// comment
        auto // auto id2022
        """
        expect = "id9,__id,auto,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 106))

    def test_7(self):
        input = """ 
        id9 __id /* This is a block comment\n id_2023 */
        auto /* auto id2022 
        for
        */
        """
        expect = "id9,__id,auto,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))

    def test_8(self):
        input = """
        id9 __id /**** This is a block comment\n */ id_2023 */
        if
        """
        expect = "id9,__id,id_2023,*,/,if,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 108))

    def test_9(self):
        input = """ 
        // id // /* Comment \n 
        */ 
        """
        expect = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 109))

    def test_10(self):
        input = """ 
        // /* Comment \n
        /*
        /*
        /* //
        */ id *//
        """
        expect = "id,*,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 110))

    # Test Literal
    def test_11(self):
        input = """123 1_2_3 1_234_567 1_2__34"""
        expect = "123,123,1234567,12,__34,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))

    #
    def test_12(self):
        input = """_123 1_2_34_ 0x123 0123 001"""
        expect = "_123,1234,_,0,x123,0,123,0,0,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))

    def test_13(self):
        input = """1.0234 1.2e3 7E-10 1_234_567.89 9.0 9. 2023e+03"""
        expect = "1.0234,1.2e3,7E-10,1234567.89,9.0,9.,2023e+03,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))

    def test_14(self):
        input = """ "He asked me:\\t \\"Where's John?\\"" """
        expect = """He asked me:\\t \\"Where's John?\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 114))

    def test_15(self):
        input = """ "He asked me:\\a \\"Where's John?\\"" """
        expect = "Illegal Escape In String: He asked me:\\a"
        self.assertTrue(TestLexer.test(input, expect, 115))

    def test_16(self):
        input = """ "He asked me: "Where's John?\\"" """
        expect = "He asked me: ,Where,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 116))

    def test_17(self):
        input = """ 
        {1,2, 3, 4,5}
        {"Kangxi", "Yongzheng", "Qianlong"}
        """
        expect = "{,1,,,2,,,3,,,4,,,5,},{,Kangxi,,,Yongzheng,,,Qianlong,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 117))

    def test_18(self):
        input = """ "0x123 001" """
        expect = "0x123 001,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 118))

    def test_19(self):
        input = """ true
        false """
        expect = "true,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))

    def test_20(self):
        input = """   TRUE truE TrueTRue TRUe 
        falSe falSEFAlse FAlsE False FAlSE
       """
        expect = "TRUE,truE,TrueTRue,TRUe,falSe,falSEFAlse,FAlsE,False,FAlSE,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 120))

    def test_21(self):
        input = """000123. 0e-3 123.e4"""
        expect = "0,0,0,123.,0e-3,123.e4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 121))

    def test_22(self):
        input = """.e10 e10 .123e-3"""
        expect = ".,e10,e10,.,123e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 122))

    def test_23(self):
        input = """ 
        ""
        "?@#$"
        "\\n\\b\\f\\r\\t\\' \\\ \\" " 
        """
        expect = """,?@#$,\\n\\b\\f\\r\\t\\' \\\ \\" ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 123))

    def test_24(self):
        input = """ "\\m \\l" """
        expect = "Illegal Escape In String: \\m"
        self.assertTrue(TestLexer.test(input, expect, 124))

    def test_25(self):
        input = """ "Closed" "Unclosed """
        expect = "Closed,Unclosed String: Unclosed "
        self.assertTrue(TestLexer.test(input, expect, 125))

    def test_26(self):
        input = """
        auto break boolean do else
false float for function if
integer return string true while
void out continue of inherit
array
        """
        expect = "auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 126))

    def test_27(self):
        input = """
        + - * / %
! && || ==
!= < <= > >=
::
        """
        expect = "+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))

    def test_28(self):
        input = """ 
        ( ) [ ] . , ; : { } =
        """
        expect = "(,),[,],.,,,;,:,{,},=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 128))

    def test_29(self):
        input = """ 
        a,b, c: integer;
        a integer; 
        """
        expect = "a,,,b,,,c,:,integer,;,a,integer,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 129))

    def test_30(self):
        input = """ 
        a, b, c: integer = 3, 4, 5;
        """
        expect = "a,,,b,,,c,:,integer,=,3,,,4,,,5,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 130))

    def test_31(self):
        input = """a = ~ b"""
        expect = "a,=,Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 131))

    def test_32(self):
        input = """a++ ++a a-- --b"""
        expect = "a,+,+,+,+,a,a,-,-,-,-,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 132))

    def test_33(self):
        input = """(a == b) ? a = a + 1 : b = b + 1"""
        expect = "(,a,==,b,),Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 133))

    def test_34(self):
        input = """a | b"""
        expect = "a,Error Token |"
        self.assertTrue(TestLexer.test(input, expect, 134))

    def test_35(self):
        input = """ ""::"string2"::"string3" """
        expect = ",::,string2,::,string3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 135))

    def test_36(self):
        input = """ a: array [2 + 2,3] of integer """
        expect = "a,:,array,[,2,+,2,,,3,],of,integer,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))

    def test_37(self):
        input = """arr[1+3,4,5] arr[3%2] = 6"""
        expect = "arr,[,1,+,3,,,4,,,5,],arr,[,3,%,2,],=,6,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 137))

    def test_38(self):
        input = """
        inc: function void(inherit out n: integer, delta: integer) {
            n = n + delta;
            return;
        }"""
        expect = "inc,:,function,void,(,inherit,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,delta,;,return,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))

    def test_39(self):
        input = """: integer;"""
        expect = ":,integer,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 139))

    def test_40(self):
        input = """ !true  a<>b+2^3)"""
        expect = "!,true,a,<,>,b,+,2,Error Token ^"
        self.assertTrue(TestLexer.test(input, expect, 140))

    def test_41(self):
        input = """
        def int main()
        {
            int a;
            a = 4 + 5;
            return a;
        }"""
        expect = "def,int,main,(,),{,int,a,;,a,=,4,+,5,;,return,a,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test_42(self):
        input = """printf("%d", 12345)"""
        expect = "printf,(,%d,,,12345,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 142))

    def test_43(self):
        input = """a, b : integer <- 2023, 2024"""
        expect = "a,,,b,:,integer,<,-,2023,,,2024,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test_44(self):
        input = """ 
    float a, b, c;
    boolean x, y; z;
    """
        expect = "float,a,,,b,,,c,;,boolean,x,,,y,;,z,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test_45(self):
        input = """@a = a"""
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 145))

    def test_46(self):
        input = """salary = 1200$"""
        expect = "salary,=,1200,Error Token $"
        self.assertTrue(TestLexer.test(input, expect, 146))

    def test_47(self):
        input = """
        # Comment?
        """
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test_48(self):
        input = """ Price: {`price`} """
        expect = "Price,:,{,Error Token `"
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test_49(self):
        input = """
        fact: function integer (n: integer ) inherit
        """
        expect = "fact,:,function,integer,(,n,:,integer,),inherit,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test_50(self):
        input = """ 
        inc: function void (out n: integer; delta integer) {
            n += delta;
        }
        """
        expect = "inc,:,function,void,(,out,n,:,integer,;,delta,integer,),{,n,+,=,delta,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))

    def test_51(self):
        input = """a, b: bool = true, false"""
        expect = "a,,,b,:,bool,=,true,,,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test_52(self):
        input = """ 
        if (a == b) then {
            a = a + 1;
        } else
            b = b+1;
        """
        expect = "if,(,a,==,b,),then,{,a,=,a,+,1,;,},else,b,=,b,+,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))

    def test_53(self):
        input = """a: string = "An unclose string!"""
        expect = "a,:,string,=,Unclosed String: An unclose string!"
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test_54(self):
        input = """a: int = 6;"""
        expect = "a,:,int,=,6,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_55(self):
        input = """a = fact(); b = fact(1,2,3);"""
        expect = "a,=,fact,(,),;,b,=,fact,(,1,,,2,,,3,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))

    def test_56(self):
        input = """a = fact(2!)"""
        expect = "a,=,fact,(,2,!,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))

    def test_57(self):
        input = """a: integer = sqr(2);"""
        expect = "a,:,integer,=,sqr,(,2,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 157))

    def test_58(self):
        input = """a, b, c: integer = 2023, 2023., true;"""
        expect = "a,,,b,,,c,:,integer,=,2023,,,2023.,,,true,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 158))

    def test_59(self):
        input = """a: array [2] of integer = {1, 2};"""
        expect = "a,:,array,[,2,],of,integer,=,{,1,,,2,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))

    def test_60(self):
        input = """a: integer = fact(2) + 2023;"""
        expect = "a,:,integer,=,fact,(,2,),+,2023,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))

    def test_61(self):
        input = """while a < 100 { a = a + 1;}"""
        expect = "while,a,<,100,{,a,=,a,+,1,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))

    def test_62(self):
        input = """do a = a + 1 while a < 100;"""
        expect = "do,a,=,a,+,1,while,a,<,100,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))

    def test_63(self):
        input = """ break; continue; break continue"""
        expect = "break,;,continue,;,break,continue,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 163))

    def test_64(self):
        input = """return; return result; return"""
        expect = "return,;,return,result,;,return,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))

    def test_65(self):
        input = """a: integer = 2023 mod 2;"""
        expect = "a,:,integer,=,2023,mod,2,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 165))

    def test_66(self):
        input = """id: INTEGER = 2023;"""
        expect = "id,:,INTEGER,=,2023,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 166))

    def test_67(self):
        input = """id: CHAR = 'a';"""
        expect = "id,:,CHAR,=,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 167))

    def test_68(self):
        input = """a: array[] of integer = {1, 2, 3};"""
        expect = "a,:,array,[,],of,integer,=,{,1,,,2,,,3,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 168))

    def test_69(self):
        input = """flag: boolean = true && false;"""
        expect = "flag,:,boolean,=,true,&&,false,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))

    def test_70(self):
        input = """a: array[] of integer = {1; 2; 3};"""
        expect = "a,:,array,[,],of,integer,=,{,1,;,2,;,3,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))

    def test_71(self):
        input = """readInteger(); printInteger(2023);"""
        expect = "readInteger,(,),;,printInteger,(,2023,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))

    def test_72(self):
        input = """readInteger(); printInteger(2023, 2024);"""
        expect = "readInteger,(,),;,printInteger,(,2023,,,2024,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))

    def test_73(self):
        input = """
        printString("Hello World!")
        """
        expect = "printString,(,Hello World!,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))

    def test_74(self):
        input = """s: stringConcat = "string1" + "string2"; """
        expect = "s,:,stringConcat,=,string1,+,string2,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))

    def test_75(self):
        input = """for (i = 0, i < 100 && i > 5, i + 1) i = i * 2;"""
        expect = "for,(,i,=,0,,,i,<,100,&&,i,>,5,,,i,+,1,),i,=,i,*,2,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))

    def test_76(self):
        input = """for (i = 0; i < 100 && i > 5; i + 1) i = i * 2;"""
        expect = "for,(,i,=,0,;,i,<,100,&&,i,>,5,;,i,+,1,),i,=,i,*,2,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))

    def test_77(self):
        input = """a: integer = (int)(8.7)"""
        expect = "a,:,integer,=,(,int,),(,8.7,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 177))

    def test_78(self):
        input = """ "abc \\n \\t"""
        expect = "Unclosed String: abc \\n \\t"
        self.assertTrue(TestLexer.test(input, expect, 178))

    def test_79(self):
        input = """ 
        if (a & b) a = a+ 1;
        """
        expect = "if,(,a,Error Token &"
        self.assertTrue(TestLexer.test(input, expect, 179))

    def test_80(self):
        input = """if (a === b) return;"""
        expect = "if,(,a,==,=,b,),return,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 180))

    def test_81(self):
        input = """if (m % 2 == 0) {}"""
        expect = "if,(,m,%,2,==,0,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))

    def test_82(self):
        input = """ "abc\\ldef"""
        expect = "Illegal Escape In String: abc\l"
        self.assertTrue(TestLexer.test(input, expect, 182))

    def test_83(self):
        input = """a: void;"""
        expect = "a,:,void,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))

    def test_84(self):
        input = """a: auto = 2;"""
        expect = "a,:,auto,=,2,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184))

    def test_85(self):
        input = """
        a, b, c: integer = ;
        """
        expect = "a,,,b,,,c,:,integer,=,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 185))

    def test_86(self):
        input = """// @@@^^^^````` """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 186))

    def test_87(self):
        input = """ 
        void
        /*
        """
        expect = "void,/,*,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test_88(self):
        input = """ "@@^^^$$$$" """
        expect = "@@^^^$$$$,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_89(self):
        input = """ \\t """
        expect = "Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test_90(self):
        input = """ __abcdef__ """
        expect = "__abcdef__,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_91(self):
        input = """complex = (4+5i)(7+8i);"""
        expect = "complex,=,(,4,+,5,i,),(,7,+,8,i,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_92(self):
        input = """ !!a """
        expect = "!,!,a,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_93(self):
        input = """ 1_234.5_678 """
        expect = "1234.5,_678,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_94(self):
        input = """ \( Something \) """
        expect = "Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test_95(self):
        input = """ << id >> """
        expect = "<,<,id,>,>,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_96(self):
        input = """ $c = $a + $b """
        expect = "Error Token $"
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test_97(self):
        input = """ \* abcd  """
        expect = "Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test_98(self):
        input = """ // /* 
        while
        """
        expect = "while,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 198))

    def test_99(self):
        input = """!(a == b)"""
        expect = "!,(,a,==,b,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))

    def test_100(self):
        input = """ (a >= c) && (b <= d)  """
        expect = "(,a,>=,c,),&&,(,b,<=,d,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 200))
