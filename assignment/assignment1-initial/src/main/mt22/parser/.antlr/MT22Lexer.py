# Generated from c:\Users\HP\OneDrive\Desktop\222\ppl\assignment\assignment1-initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01cb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\2\7\2\u008c\n\2\f\2\16\2\u008f\13\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009a\n\3\f\3\16")
        buf.write("\3\u009d\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\63\7\63\u015a\n\63\f\63\16\63\u015d\13\63\3\63")
        buf.write("\3\63\6\63\u0161\n\63\r\63\16\63\u0162\7\63\u0165\n\63")
        buf.write("\f\63\16\63\u0168\13\63\3\63\3\63\5\63\u016c\n\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u0173\n\64\3\64\3\64\5\64\u0177")
        buf.write("\n\64\3\64\3\64\3\65\3\65\7\65\u017d\n\65\f\65\16\65\u0180")
        buf.write("\13\65\3\66\3\66\5\66\u0184\n\66\3\66\6\66\u0187\n\66")
        buf.write("\r\66\16\66\u0188\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\5\67\u0194\n\67\38\38\38\78\u0199\n8\f8\168\u019c")
        buf.write("\138\38\38\39\39\39\39\3:\3:\3:\3:\3;\3;\3;\3<\3<\3<\3")
        buf.write("=\3=\5=\u01b0\n=\3=\3=\3=\7=\u01b5\n=\f=\16=\u01b8\13")
        buf.write("=\3>\3>\3?\3?\3@\3@\3A\3A\3B\6B\u01c3\nB\rB\16B\u01c4")
        buf.write("\3B\3B\3C\3C\3C\3\u008d\2D\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\2k\2m\66o\67q8s9u\2w\2y:{\2}\2\177\2\u0081\2")
        buf.write("\u0083;\u0085<\3\2\13\4\2\f\f\17\17\4\2GGgg\4\2--//\4")
        buf.write("\2$$^^\n\2$$))^^ddhhppttvv\4\2C\\c|\3\2\62;\3\2\63;\5")
        buf.write("\2\n\f\16\17\"\"\2\u01d5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2")
        buf.write("q\3\2\2\2\2s\3\2\2\2\2y\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\3\u0087\3\2\2\2\5\u0095\3\2\2\2\7\u00a0\3\2\2")
        buf.write("\2\t\u00a5\3\2\2\2\13\u00ab\3\2\2\2\r\u00b3\3\2\2\2\17")
        buf.write("\u00b6\3\2\2\2\21\u00bb\3\2\2\2\23\u00c1\3\2\2\2\25\u00c7")
        buf.write("\3\2\2\2\27\u00cb\3\2\2\2\31\u00d4\3\2\2\2\33\u00d7\3")
        buf.write("\2\2\2\35\u00df\3\2\2\2\37\u00e6\3\2\2\2!\u00ed\3\2\2")
        buf.write("\2#\u00f2\3\2\2\2%\u00f8\3\2\2\2\'\u00fd\3\2\2\2)\u0101")
        buf.write("\3\2\2\2+\u010a\3\2\2\2-\u010d\3\2\2\2/\u0115\3\2\2\2")
        buf.write("\61\u011b\3\2\2\2\63\u011d\3\2\2\2\65\u011f\3\2\2\2\67")
        buf.write("\u0121\3\2\2\29\u0123\3\2\2\2;\u0125\3\2\2\2=\u0127\3")
        buf.write("\2\2\2?\u012a\3\2\2\2A\u012d\3\2\2\2C\u0130\3\2\2\2E\u0133")
        buf.write("\3\2\2\2G\u0135\3\2\2\2I\u0138\3\2\2\2K\u013a\3\2\2\2")
        buf.write("M\u013d\3\2\2\2O\u0140\3\2\2\2Q\u0142\3\2\2\2S\u0144\3")
        buf.write("\2\2\2U\u0146\3\2\2\2W\u0148\3\2\2\2Y\u014a\3\2\2\2[\u014c")
        buf.write("\3\2\2\2]\u014e\3\2\2\2_\u0150\3\2\2\2a\u0152\3\2\2\2")
        buf.write("c\u0154\3\2\2\2e\u016b\3\2\2\2g\u0176\3\2\2\2i\u017a\3")
        buf.write("\2\2\2k\u0181\3\2\2\2m\u0193\3\2\2\2o\u0195\3\2\2\2q\u019f")
        buf.write("\3\2\2\2s\u01a3\3\2\2\2u\u01a7\3\2\2\2w\u01aa\3\2\2\2")
        buf.write("y\u01af\3\2\2\2{\u01b9\3\2\2\2}\u01bb\3\2\2\2\177\u01bd")
        buf.write("\3\2\2\2\u0081\u01bf\3\2\2\2\u0083\u01c2\3\2\2\2\u0085")
        buf.write("\u01c8\3\2\2\2\u0087\u0088\7\61\2\2\u0088\u0089\7,\2\2")
        buf.write("\u0089\u008d\3\2\2\2\u008a\u008c\13\2\2\2\u008b\u008a")
        buf.write("\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008e\3\2\2\2\u008d")
        buf.write("\u008b\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u0090\u0091\7,\2\2\u0091\u0092\7\61\2\2\u0092\u0093\3")
        buf.write("\2\2\2\u0093\u0094\b\2\2\2\u0094\4\3\2\2\2\u0095\u0096")
        buf.write("\7\61\2\2\u0096\u0097\7\61\2\2\u0097\u009b\3\2\2\2\u0098")
        buf.write("\u009a\n\2\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\3")
        buf.write("\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\b\3\2\2\u009f\6")
        buf.write("\3\2\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3")
        buf.write("\7v\2\2\u00a3\u00a4\7q\2\2\u00a4\b\3\2\2\2\u00a5\u00a6")
        buf.write("\7d\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7m\2\2\u00aa\n\3\2\2\2\u00ab\u00ac")
        buf.write("\7d\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af")
        buf.write("\7n\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\f\3\2\2\2\u00b3\u00b4\7f\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\16\3\2\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8")
        buf.write("\7n\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba\7g\2\2\u00ba\20")
        buf.write("\3\2\2\2\u00bb\u00bc\7h\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be")
        buf.write("\7n\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0\7g\2\2\u00c0\22")
        buf.write("\3\2\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7v\2\2\u00c6\24")
        buf.write("\3\2\2\2\u00c7\u00c8\7h\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\26\3\2\2\2\u00cb\u00cc\7h\2\2\u00cc\u00cd")
        buf.write("\7w\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\30\3\2\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6")
        buf.write("\7h\2\2\u00d6\32\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7i\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de\7t\2\2\u00de\34")
        buf.write("\3\2\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5")
        buf.write("\7p\2\2\u00e5\36\3\2\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\u00ec\7i\2\2\u00ec \3\2\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0\7w\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\"\3\2\2\2\u00f2\u00f3\7y\2\2\u00f3\u00f4")
        buf.write("\7j\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7$\3\2\2\2\u00f8\u00f9\7x\2\2\u00f9\u00fa")
        buf.write("\7q\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7f\2\2\u00fc&\3")
        buf.write("\2\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100")
        buf.write("\7v\2\2\u0100(\3\2\2\2\u0101\u0102\7e\2\2\u0102\u0103")
        buf.write("\7q\2\2\u0103\u0104\7p\2\2\u0104\u0105\7v\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7p\2\2\u0107\u0108\7w\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109*\3\2\2\2\u010a\u010b\7q\2\2\u010b\u010c")
        buf.write("\7h\2\2\u010c,\3\2\2\2\u010d\u010e\7k\2\2\u010e\u010f")
        buf.write("\7p\2\2\u010f\u0110\7j\2\2\u0110\u0111\7g\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112\u0113\7k\2\2\u0113\u0114\7v\2\2\u0114.\3")
        buf.write("\2\2\2\u0115\u0116\7c\2\2\u0116\u0117\7t\2\2\u0117\u0118")
        buf.write("\7t\2\2\u0118\u0119\7c\2\2\u0119\u011a\7{\2\2\u011a\60")
        buf.write("\3\2\2\2\u011b\u011c\7-\2\2\u011c\62\3\2\2\2\u011d\u011e")
        buf.write("\7/\2\2\u011e\64\3\2\2\2\u011f\u0120\7,\2\2\u0120\66\3")
        buf.write("\2\2\2\u0121\u0122\7\61\2\2\u01228\3\2\2\2\u0123\u0124")
        buf.write("\7\'\2\2\u0124:\3\2\2\2\u0125\u0126\7#\2\2\u0126<\3\2")
        buf.write("\2\2\u0127\u0128\7(\2\2\u0128\u0129\7(\2\2\u0129>\3\2")
        buf.write("\2\2\u012a\u012b\7~\2\2\u012b\u012c\7~\2\2\u012c@\3\2")
        buf.write("\2\2\u012d\u012e\7?\2\2\u012e\u012f\7?\2\2\u012fB\3\2")
        buf.write("\2\2\u0130\u0131\7#\2\2\u0131\u0132\7?\2\2\u0132D\3\2")
        buf.write("\2\2\u0133\u0134\7>\2\2\u0134F\3\2\2\2\u0135\u0136\7>")
        buf.write("\2\2\u0136\u0137\7?\2\2\u0137H\3\2\2\2\u0138\u0139\7@")
        buf.write("\2\2\u0139J\3\2\2\2\u013a\u013b\7@\2\2\u013b\u013c\7?")
        buf.write("\2\2\u013cL\3\2\2\2\u013d\u013e\7<\2\2\u013e\u013f\7<")
        buf.write("\2\2\u013fN\3\2\2\2\u0140\u0141\7*\2\2\u0141P\3\2\2\2")
        buf.write("\u0142\u0143\7+\2\2\u0143R\3\2\2\2\u0144\u0145\7}\2\2")
        buf.write("\u0145T\3\2\2\2\u0146\u0147\7\177\2\2\u0147V\3\2\2\2\u0148")
        buf.write("\u0149\7]\2\2\u0149X\3\2\2\2\u014a\u014b\7_\2\2\u014b")
        buf.write("Z\3\2\2\2\u014c\u014d\7\60\2\2\u014d\\\3\2\2\2\u014e\u014f")
        buf.write("\7.\2\2\u014f^\3\2\2\2\u0150\u0151\7=\2\2\u0151`\3\2\2")
        buf.write("\2\u0152\u0153\7<\2\2\u0153b\3\2\2\2\u0154\u0155\7?\2")
        buf.write("\2\u0155d\3\2\2\2\u0156\u016c\7\62\2\2\u0157\u015b\5\u0081")
        buf.write("A\2\u0158\u015a\5\177@\2\u0159\u0158\3\2\2\2\u015a\u015d")
        buf.write("\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c")
        buf.write("\u0166\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u0160\5}?\2\u015f")
        buf.write("\u0161\5\177@\2\u0160\u015f\3\2\2\2\u0161\u0162\3\2\2")
        buf.write("\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165")
        buf.write("\3\2\2\2\u0164\u015e\3\2\2\2\u0165\u0168\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0169\3\2\2\2")
        buf.write("\u0168\u0166\3\2\2\2\u0169\u016a\b\63\3\2\u016a\u016c")
        buf.write("\3\2\2\2\u016b\u0156\3\2\2\2\u016b\u0157\3\2\2\2\u016c")
        buf.write("f\3\2\2\2\u016d\u016e\5e\63\2\u016e\u016f\5i\65\2\u016f")
        buf.write("\u0177\3\2\2\2\u0170\u0172\5e\63\2\u0171\u0173\5i\65\2")
        buf.write("\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\3")
        buf.write("\2\2\2\u0174\u0175\5k\66\2\u0175\u0177\3\2\2\2\u0176\u016d")
        buf.write("\3\2\2\2\u0176\u0170\3\2\2\2\u0177\u0178\3\2\2\2\u0178")
        buf.write("\u0179\b\64\4\2\u0179h\3\2\2\2\u017a\u017e\7\60\2\2\u017b")
        buf.write("\u017d\5\177@\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2")
        buf.write("\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fj\3\2")
        buf.write("\2\2\u0180\u017e\3\2\2\2\u0181\u0183\t\3\2\2\u0182\u0184")
        buf.write("\t\4\2\2\u0183\u0182\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0186\3\2\2\2\u0185\u0187\5\177@\2\u0186\u0185\3\2\2")
        buf.write("\2\u0187\u0188\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189l\3\2\2\2\u018a\u018b\7v\2\2\u018b\u018c")
        buf.write("\7t\2\2\u018c\u018d\7w\2\2\u018d\u0194\7g\2\2\u018e\u018f")
        buf.write("\7h\2\2\u018f\u0190\7c\2\2\u0190\u0191\7n\2\2\u0191\u0192")
        buf.write("\7u\2\2\u0192\u0194\7g\2\2\u0193\u018a\3\2\2\2\u0193\u018e")
        buf.write("\3\2\2\2\u0194n\3\2\2\2\u0195\u019a\7$\2\2\u0196\u0199")
        buf.write("\5u;\2\u0197\u0199\n\5\2\2\u0198\u0196\3\2\2\2\u0198\u0197")
        buf.write("\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019d\u019e\b8\5\2\u019ep\3\2\2\2\u019f\u01a0\5o8\2\u01a0")
        buf.write("\u01a1\5w<\2\u01a1\u01a2\b9\6\2\u01a2r\3\2\2\2\u01a3\u01a4")
        buf.write("\5o8\2\u01a4\u01a5\7$\2\2\u01a5\u01a6\b:\7\2\u01a6t\3")
        buf.write("\2\2\2\u01a7\u01a8\7^\2\2\u01a8\u01a9\t\6\2\2\u01a9v\3")
        buf.write("\2\2\2\u01aa\u01ab\7^\2\2\u01ab\u01ac\n\6\2\2\u01acx\3")
        buf.write("\2\2\2\u01ad\u01b0\5{>\2\u01ae\u01b0\5}?\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b6\3\2\2\2\u01b1")
        buf.write("\u01b5\5{>\2\u01b2\u01b5\5\177@\2\u01b3\u01b5\5}?\2\u01b4")
        buf.write("\u01b1\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3")
        buf.write("\2\2\2\u01b7z\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba")
        buf.write("\t\7\2\2\u01ba|\3\2\2\2\u01bb\u01bc\7a\2\2\u01bc~\3\2")
        buf.write("\2\2\u01bd\u01be\t\b\2\2\u01be\u0080\3\2\2\2\u01bf\u01c0")
        buf.write("\t\t\2\2\u01c0\u0082\3\2\2\2\u01c1\u01c3\t\n\2\2\u01c2")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c2\3\2\2\2")
        buf.write("\u01c4\u01c5\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\b")
        buf.write("B\2\2\u01c7\u0084\3\2\2\2\u01c8\u01c9\13\2\2\2\u01c9\u01ca")
        buf.write("\bC\b\2\u01ca\u0086\3\2\2\2\25\2\u008d\u009b\u015b\u0162")
        buf.write("\u0166\u016b\u0172\u0176\u017e\u0183\u0188\u0193\u0198")
        buf.write("\u019a\u01af\u01b4\u01b6\u01c4\t\b\2\2\3\63\2\3\64\3\3")
        buf.write("8\4\39\5\3:\6\3C\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCK_COMMENT = 1
    LINE_COMMENT = 2
    AUTO = 3
    BREAK = 4
    BOOLEAN = 5
    DO = 6
    ELSE = 7
    FALSE = 8
    FLOAT = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    TRUE = 16
    WHILE = 17
    VOID = 18
    OUT = 19
    CONTINUE = 20
    OF = 21
    INHERIT = 22
    ARRAY = 23
    ADD = 24
    SUB = 25
    MUL = 26
    DIV = 27
    MOD = 28
    NOT = 29
    AND = 30
    OR = 31
    EQUAL = 32
    NOT_EQUAL = 33
    LT = 34
    LE = 35
    GT = 36
    GE = 37
    CONCAT = 38
    LB = 39
    RB = 40
    LP = 41
    RP = 42
    LSB = 43
    RSB = 44
    DOT = 45
    COMMA = 46
    SEMI = 47
    COLON = 48
    EQ = 49
    INTLIT = 50
    FLOATLIT = 51
    BOOLLIT = 52
    UNCLOSE_STRING = 53
    ILLEGAL_ESCAPE = 54
    STRINGLIT = 55
    IDENTIFIER = 56
    WS = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "'.'", "','", "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LINE_COMMENT", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", "LE", "GT", 
            "GE", "CONCAT", "LB", "RB", "LP", "RP", "LSB", "RSB", "DOT", 
            "COMMA", "SEMI", "COLON", "EQ", "INTLIT", "FLOATLIT", "BOOLLIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRINGLIT", "IDENTIFIER", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "BLOCK_COMMENT", "LINE_COMMENT", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", 
                  "LT", "LE", "GT", "GE", "CONCAT", "LB", "RB", "LP", "RP", 
                  "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "EQ", "INTLIT", 
                  "FLOATLIT", "DECPART", "EXPPART", "BOOLLIT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STRINGLIT", "ESC", "ILLEGAL_ESC", "IDENTIFIER", 
                  "LETTER", "UNDERSCORE", "DIGIT", "NONZERO_DIGIT", "WS", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.INTLIT_action 
            actions[50] = self.FLOATLIT_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            actions[56] = self.STRINGLIT_action 
            actions[65] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise UncloseString(self.text[1:]) 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise IllegalEscape(self.text[1:]) 
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
             self.text = self.text[1:-1] 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


