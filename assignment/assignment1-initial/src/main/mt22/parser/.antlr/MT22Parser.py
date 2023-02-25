# Generated from c:\Users\HP\OneDrive\Desktop\222\ppl\assignment\assignment1-initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u0197\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3p\n\3\3\4\3\4\5\4t\n\4")
        buf.write("\3\5\3\5\5\5x\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\5\7\u0083\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u0094\n\t\3\n\3\n\3\n\5\n\u0099")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\5\f\u00a7\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00ae\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\5\17\u00b8")
        buf.write("\n\17\3\20\3\20\5\20\u00bc\n\20\3\21\3\21\3\21\5\21\u00c1")
        buf.write("\n\21\3\22\3\22\3\22\3\22\5\22\u00c7\n\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00d5\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\26\3\26\5\26\u00e2\n\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\5\30\u00ee\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\5\37\u0116\n\37\3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\5!\u0120\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0127\n\"\3#\3#")
        buf.write("\3#\3#\3#\5#\u012e\n#\3$\3$\3$\3$\3$\5$\u0135\n$\3%\3")
        buf.write("%\3%\3%\3%\3%\7%\u013d\n%\f%\16%\u0140\13%\3&\3&\3&\3")
        buf.write("&\3&\3&\7&\u0148\n&\f&\16&\u014b\13&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\7\'\u0153\n\'\f\'\16\'\u0156\13\'\3(\3(\3(\5(\u015b")
        buf.write("\n(\3)\3)\3)\5)\u0160\n)\3*\3*\3*\3*\3*\3*\3*\3*\5*\u016a")
        buf.write("\n*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3")
        buf.write(".\3.\5.\u017e\n.\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\5\61\u018d\n\61\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\64\2\5HJL\65\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdf\2\7\3\2\"\'\3\2 !\3\2\32\33\3\2\34\36")
        buf.write("\6\2\7\7\13\13\17\17\21\21\2\u0192\2h\3\2\2\2\4o\3\2\2")
        buf.write("\2\6s\3\2\2\2\bw\3\2\2\2\ny\3\2\2\2\f\u0082\3\2\2\2\16")
        buf.write("\u0084\3\2\2\2\20\u0093\3\2\2\2\22\u0098\3\2\2\2\24\u009a")
        buf.write("\3\2\2\2\26\u00a6\3\2\2\2\30\u00ad\3\2\2\2\32\u00af\3")
        buf.write("\2\2\2\34\u00b7\3\2\2\2\36\u00bb\3\2\2\2 \u00c0\3\2\2")
        buf.write("\2\"\u00c6\3\2\2\2$\u00d4\3\2\2\2&\u00d6\3\2\2\2(\u00da")
        buf.write("\3\2\2\2*\u00e1\3\2\2\2,\u00e3\3\2\2\2.\u00ed\3\2\2\2")
        buf.write("\60\u00ef\3\2\2\2\62\u00fb\3\2\2\2\64\u0101\3\2\2\2\66")
        buf.write("\u0109\3\2\2\28\u010c\3\2\2\2:\u010f\3\2\2\2<\u0115\3")
        buf.write("\2\2\2>\u0117\3\2\2\2@\u011f\3\2\2\2B\u0126\3\2\2\2D\u012d")
        buf.write("\3\2\2\2F\u0134\3\2\2\2H\u0136\3\2\2\2J\u0141\3\2\2\2")
        buf.write("L\u014c\3\2\2\2N\u015a\3\2\2\2P\u015f\3\2\2\2R\u0169\3")
        buf.write("\2\2\2T\u016b\3\2\2\2V\u016f\3\2\2\2X\u0174\3\2\2\2Z\u017d")
        buf.write("\3\2\2\2\\\u017f\3\2\2\2^\u0181\3\2\2\2`\u018c\3\2\2\2")
        buf.write("b\u018e\3\2\2\2d\u0192\3\2\2\2f\u0194\3\2\2\2hi\5\4\3")
        buf.write("\2ij\7\2\2\3j\3\3\2\2\2kl\5\6\4\2lm\5\4\3\2mp\3\2\2\2")
        buf.write("np\5\6\4\2ok\3\2\2\2on\3\2\2\2p\5\3\2\2\2qt\5\b\5\2rt")
        buf.write("\5\24\13\2sq\3\2\2\2sr\3\2\2\2t\7\3\2\2\2ux\5\n\6\2vx")
        buf.write("\5\16\b\2wu\3\2\2\2wv\3\2\2\2x\t\3\2\2\2yz\5\f\7\2z{\7")
        buf.write("\62\2\2{|\5\22\n\2|}\7\61\2\2}\13\3\2\2\2~\177\7:\2\2")
        buf.write("\177\u0080\7\60\2\2\u0080\u0083\5\f\7\2\u0081\u0083\7")
        buf.write(":\2\2\u0082~\3\2\2\2\u0082\u0081\3\2\2\2\u0083\r\3\2\2")
        buf.write("\2\u0084\u0085\5\20\t\2\u0085\u0086\7\61\2\2\u0086\17")
        buf.write("\3\2\2\2\u0087\u0088\7:\2\2\u0088\u0089\7\60\2\2\u0089")
        buf.write("\u008a\5\20\t\2\u008a\u008b\7\60\2\2\u008b\u008c\5B\"")
        buf.write("\2\u008c\u0094\3\2\2\2\u008d\u008e\7:\2\2\u008e\u008f")
        buf.write("\7\62\2\2\u008f\u0090\5\22\n\2\u0090\u0091\7\63\2\2\u0091")
        buf.write("\u0092\5B\"\2\u0092\u0094\3\2\2\2\u0093\u0087\3\2\2\2")
        buf.write("\u0093\u008d\3\2\2\2\u0094\21\3\2\2\2\u0095\u0099\5\\")
        buf.write("/\2\u0096\u0099\5^\60\2\u0097\u0099\5f\64\2\u0098\u0095")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0097\3\2\2\2\u0099")
        buf.write("\23\3\2\2\2\u009a\u009b\7:\2\2\u009b\u009c\7\62\2\2\u009c")
        buf.write("\u009d\7\r\2\2\u009d\u009e\5Z.\2\u009e\u009f\7)\2\2\u009f")
        buf.write("\u00a0\5\26\f\2\u00a0\u00a1\7*\2\2\u00a1\u00a2\5 \21\2")
        buf.write("\u00a2\u00a3\5&\24\2\u00a3\25\3\2\2\2\u00a4\u00a7\5\30")
        buf.write("\r\2\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\27\3\2\2\2\u00a8\u00a9\5\32\16\2\u00a9")
        buf.write("\u00aa\7\60\2\2\u00aa\u00ab\5\30\r\2\u00ab\u00ae\3\2\2")
        buf.write("\2\u00ac\u00ae\5\32\16\2\u00ad\u00a8\3\2\2\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ae\31\3\2\2\2\u00af\u00b0\5\34\17\2\u00b0")
        buf.write("\u00b1\5\36\20\2\u00b1\u00b2\7:\2\2\u00b2\u00b3\7\62\2")
        buf.write("\2\u00b3\u00b4\5\22\n\2\u00b4\33\3\2\2\2\u00b5\u00b8\7")
        buf.write("\30\2\2\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\35\3\2\2\2\u00b9\u00bc\7\25\2\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2")
        buf.write("\u00bc\37\3\2\2\2\u00bd\u00be\7\30\2\2\u00be\u00c1\7:")
        buf.write("\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00bf")
        buf.write("\3\2\2\2\u00c1!\3\2\2\2\u00c2\u00c3\5$\23\2\u00c3\u00c4")
        buf.write("\5\"\22\2\u00c4\u00c7\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6")
        buf.write("\u00c2\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7#\3\2\2\2\u00c8")
        buf.write("\u00d5\5&\24\2\u00c9\u00d5\5\b\5\2\u00ca\u00d5\5(\25\2")
        buf.write("\u00cb\u00d5\5,\27\2\u00cc\u00d5\5\60\31\2\u00cd\u00d5")
        buf.write("\5\62\32\2\u00ce\u00d5\5\64\33\2\u00cf\u00d5\5\66\34\2")
        buf.write("\u00d0\u00d5\58\35\2\u00d1\u00d5\5:\36\2\u00d2\u00d5\5")
        buf.write("> \2\u00d3\u00d5\5&\24\2\u00d4\u00c8\3\2\2\2\u00d4\u00c9")
        buf.write("\3\2\2\2\u00d4\u00ca\3\2\2\2\u00d4\u00cb\3\2\2\2\u00d4")
        buf.write("\u00cc\3\2\2\2\u00d4\u00cd\3\2\2\2\u00d4\u00ce\3\2\2\2")
        buf.write("\u00d4\u00cf\3\2\2\2\u00d4\u00d0\3\2\2\2\u00d4\u00d1\3")
        buf.write("\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5%")
        buf.write("\3\2\2\2\u00d6\u00d7\7+\2\2\u00d7\u00d8\5\"\22\2\u00d8")
        buf.write("\u00d9\7,\2\2\u00d9\'\3\2\2\2\u00da\u00db\5*\26\2\u00db")
        buf.write("\u00dc\7\63\2\2\u00dc\u00dd\5D#\2\u00dd\u00de\7\61\2\2")
        buf.write("\u00de)\3\2\2\2\u00df\u00e2\7:\2\2\u00e0\u00e2\5V,\2\u00e1")
        buf.write("\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2+\3\2\2\2\u00e3")
        buf.write("\u00e4\7\16\2\2\u00e4\u00e5\7)\2\2\u00e5\u00e6\5D#\2\u00e6")
        buf.write("\u00e7\7*\2\2\u00e7\u00e8\5$\23\2\u00e8\u00e9\5.\30\2")
        buf.write("\u00e9-\3\2\2\2\u00ea\u00eb\7\t\2\2\u00eb\u00ee\5$\23")
        buf.write("\2\u00ec\u00ee\3\2\2\2\u00ed\u00ea\3\2\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee/\3\2\2\2\u00ef\u00f0\7\f\2\2\u00f0\u00f1")
        buf.write("\7)\2\2\u00f1\u00f2\7:\2\2\u00f2\u00f3\7\63\2\2\u00f3")
        buf.write("\u00f4\5D#\2\u00f4\u00f5\7\60\2\2\u00f5\u00f6\5D#\2\u00f6")
        buf.write("\u00f7\7\60\2\2\u00f7\u00f8\5D#\2\u00f8\u00f9\7*\2\2\u00f9")
        buf.write("\u00fa\5$\23\2\u00fa\61\3\2\2\2\u00fb\u00fc\7\23\2\2\u00fc")
        buf.write("\u00fd\7)\2\2\u00fd\u00fe\5D#\2\u00fe\u00ff\7*\2\2\u00ff")
        buf.write("\u0100\5$\23\2\u0100\63\3\2\2\2\u0101\u0102\7\b\2\2\u0102")
        buf.write("\u0103\5&\24\2\u0103\u0104\7\23\2\2\u0104\u0105\7)\2\2")
        buf.write("\u0105\u0106\5D#\2\u0106\u0107\7*\2\2\u0107\u0108\7\61")
        buf.write("\2\2\u0108\65\3\2\2\2\u0109\u010a\7\6\2\2\u010a\u010b")
        buf.write("\7\61\2\2\u010b\67\3\2\2\2\u010c\u010d\7\26\2\2\u010d")
        buf.write("\u010e\7\61\2\2\u010e9\3\2\2\2\u010f\u0110\7\20\2\2\u0110")
        buf.write("\u0111\5<\37\2\u0111\u0112\7\61\2\2\u0112;\3\2\2\2\u0113")
        buf.write("\u0116\5D#\2\u0114\u0116\3\2\2\2\u0115\u0113\3\2\2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0116=\3\2\2\2\u0117\u0118\7:\2\2\u0118")
        buf.write("\u0119\7)\2\2\u0119\u011a\5@!\2\u011a\u011b\7*\2\2\u011b")
        buf.write("\u011c\7\61\2\2\u011c?\3\2\2\2\u011d\u0120\5B\"\2\u011e")
        buf.write("\u0120\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2")
        buf.write("\u0120A\3\2\2\2\u0121\u0122\5D#\2\u0122\u0123\7\60\2\2")
        buf.write("\u0123\u0124\5B\"\2\u0124\u0127\3\2\2\2\u0125\u0127\5")
        buf.write("D#\2\u0126\u0121\3\2\2\2\u0126\u0125\3\2\2\2\u0127C\3")
        buf.write("\2\2\2\u0128\u0129\5F$\2\u0129\u012a\7(\2\2\u012a\u012b")
        buf.write("\5F$\2\u012b\u012e\3\2\2\2\u012c\u012e\5F$\2\u012d\u0128")
        buf.write("\3\2\2\2\u012d\u012c\3\2\2\2\u012eE\3\2\2\2\u012f\u0130")
        buf.write("\5H%\2\u0130\u0131\t\2\2\2\u0131\u0132\5H%\2\u0132\u0135")
        buf.write("\3\2\2\2\u0133\u0135\5H%\2\u0134\u012f\3\2\2\2\u0134\u0133")
        buf.write("\3\2\2\2\u0135G\3\2\2\2\u0136\u0137\b%\1\2\u0137\u0138")
        buf.write("\5J&\2\u0138\u013e\3\2\2\2\u0139\u013a\f\4\2\2\u013a\u013b")
        buf.write("\t\3\2\2\u013b\u013d\5J&\2\u013c\u0139\3\2\2\2\u013d\u0140")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("I\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0142\b&\1\2\u0142")
        buf.write("\u0143\5L\'\2\u0143\u0149\3\2\2\2\u0144\u0145\f\4\2\2")
        buf.write("\u0145\u0146\t\4\2\2\u0146\u0148\5L\'\2\u0147\u0144\3")
        buf.write("\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014aK\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014d")
        buf.write("\b\'\1\2\u014d\u014e\5N(\2\u014e\u0154\3\2\2\2\u014f\u0150")
        buf.write("\f\4\2\2\u0150\u0151\t\5\2\2\u0151\u0153\5N(\2\u0152\u014f")
        buf.write("\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155M\3\2\2\2\u0156\u0154\3\2\2\2\u0157")
        buf.write("\u0158\7\37\2\2\u0158\u015b\5N(\2\u0159\u015b\5P)\2\u015a")
        buf.write("\u0157\3\2\2\2\u015a\u0159\3\2\2\2\u015bO\3\2\2\2\u015c")
        buf.write("\u015d\7\33\2\2\u015d\u0160\5P)\2\u015e\u0160\5R*\2\u015f")
        buf.write("\u015c\3\2\2\2\u015f\u015e\3\2\2\2\u0160Q\3\2\2\2\u0161")
        buf.write("\u016a\5T+\2\u0162\u016a\5V,\2\u0163\u016a\5X-\2\u0164")
        buf.write("\u016a\7:\2\2\u0165\u016a\7\64\2\2\u0166\u016a\7\65\2")
        buf.write("\2\u0167\u016a\7\66\2\2\u0168\u016a\79\2\2\u0169\u0161")
        buf.write("\3\2\2\2\u0169\u0162\3\2\2\2\u0169\u0163\3\2\2\2\u0169")
        buf.write("\u0164\3\2\2\2\u0169\u0165\3\2\2\2\u0169\u0166\3\2\2\2")
        buf.write("\u0169\u0167\3\2\2\2\u0169\u0168\3\2\2\2\u016aS\3\2\2")
        buf.write("\2\u016b\u016c\7)\2\2\u016c\u016d\5D#\2\u016d\u016e\7")
        buf.write("*\2\2\u016eU\3\2\2\2\u016f\u0170\7:\2\2\u0170\u0171\7")
        buf.write("-\2\2\u0171\u0172\5@!\2\u0172\u0173\7.\2\2\u0173W\3\2")
        buf.write("\2\2\u0174\u0175\7:\2\2\u0175\u0176\7)\2\2\u0176\u0177")
        buf.write("\5@!\2\u0177\u0178\7*\2\2\u0178Y\3\2\2\2\u0179\u017e\5")
        buf.write("\\/\2\u017a\u017e\5^\60\2\u017b\u017e\5d\63\2\u017c\u017e")
        buf.write("\5f\64\2\u017d\u0179\3\2\2\2\u017d\u017a\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017c\3\2\2\2\u017e[\3\2\2\2\u017f")
        buf.write("\u0180\t\6\2\2\u0180]\3\2\2\2\u0181\u0182\7\31\2\2\u0182")
        buf.write("\u0183\7-\2\2\u0183\u0184\5`\61\2\u0184\u0185\7.\2\2\u0185")
        buf.write("\u0186\7\27\2\2\u0186\u0187\5\\/\2\u0187_\3\2\2\2\u0188")
        buf.write("\u0189\7\64\2\2\u0189\u018a\7\60\2\2\u018a\u018d\5`\61")
        buf.write("\2\u018b\u018d\7\64\2\2\u018c\u0188\3\2\2\2\u018c\u018b")
        buf.write("\3\2\2\2\u018da\3\2\2\2\u018e\u018f\7+\2\2\u018f\u0190")
        buf.write("\5@!\2\u0190\u0191\7,\2\2\u0191c\3\2\2\2\u0192\u0193\7")
        buf.write("\24\2\2\u0193e\3\2\2\2\u0194\u0195\7\5\2\2\u0195g\3\2")
        buf.write("\2\2\36osw\u0082\u0093\u0098\u00a6\u00ad\u00b7\u00bb\u00c0")
        buf.write("\u00c6\u00d4\u00e1\u00ed\u0115\u011f\u0126\u012d\u0134")
        buf.write("\u013e\u0149\u0154\u015a\u015f\u0169\u017d\u018c")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'boolean'", "'do'", "'else'", "'false'", "'float'", 
                     "'for'", "'function'", "'if'", "'integer'", "'return'", 
                     "'string'", "'true'", "'while'", "'void'", "'out'", 
                     "'continue'", "'of'", "'inherit'", "'array'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "'.'", "','", 
                     "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>", "BLOCK_COMMENT", "LINE_COMMENT", "AUTO", 
                      "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                      "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                      "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", 
                      "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", "LE", 
                      "GT", "GE", "CONCAT", "LB", "RB", "LP", "RP", "LSB", 
                      "RSB", "DOT", "COMMA", "SEMI", "COLON", "EQ", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "STRINGLIT", "IDENTIFIER", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_shortvardecl = 4
    RULE_idlist = 5
    RULE_fullvardecl = 6
    RULE_varinit = 7
    RULE_vartyp = 8
    RULE_funcdecl = 9
    RULE_paramlist = 10
    RULE_paramrime = 11
    RULE_param = 12
    RULE_paraminher = 13
    RULE_paramout = 14
    RULE_funcinher = 15
    RULE_stmtlist = 16
    RULE_stmt = 17
    RULE_blockstmt = 18
    RULE_assignstmt = 19
    RULE_lhs = 20
    RULE_ifstmt = 21
    RULE_elsestmt = 22
    RULE_forstmt = 23
    RULE_whilestmt = 24
    RULE_dowhilestmt = 25
    RULE_breakstmt = 26
    RULE_continuestmt = 27
    RULE_returnstmt = 28
    RULE_retexpr = 29
    RULE_callstmt = 30
    RULE_exprlist = 31
    RULE_exprpime = 32
    RULE_expr = 33
    RULE_expr1 = 34
    RULE_expr2 = 35
    RULE_expr3 = 36
    RULE_expr4 = 37
    RULE_expr5 = 38
    RULE_expr6 = 39
    RULE_expr7 = 40
    RULE_subexpr = 41
    RULE_arrayele = 42
    RULE_funccall = 43
    RULE_types = 44
    RULE_atomtype = 45
    RULE_arraytype = 46
    RULE_dimenslist = 47
    RULE_arraylit = 48
    RULE_voidtype = 49
    RULE_autotype = 50

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "shortvardecl", 
                   "idlist", "fullvardecl", "varinit", "vartyp", "funcdecl", 
                   "paramlist", "paramrime", "param", "paraminher", "paramout", 
                   "funcinher", "stmtlist", "stmt", "blockstmt", "assignstmt", 
                   "lhs", "ifstmt", "elsestmt", "forstmt", "whilestmt", 
                   "dowhilestmt", "breakstmt", "continuestmt", "returnstmt", 
                   "retexpr", "callstmt", "exprlist", "exprpime", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "subexpr", "arrayele", "funccall", "types", 
                   "atomtype", "arraytype", "dimenslist", "arraylit", "voidtype", 
                   "autotype" ]

    EOF = Token.EOF
    BLOCK_COMMENT=1
    LINE_COMMENT=2
    AUTO=3
    BREAK=4
    BOOLEAN=5
    DO=6
    ELSE=7
    FALSE=8
    FLOAT=9
    FOR=10
    FUNCTION=11
    IF=12
    INTEGER=13
    RETURN=14
    STRING=15
    TRUE=16
    WHILE=17
    VOID=18
    OUT=19
    CONTINUE=20
    OF=21
    INHERIT=22
    ARRAY=23
    ADD=24
    SUB=25
    MUL=26
    DIV=27
    MOD=28
    NOT=29
    AND=30
    OR=31
    EQUAL=32
    NOT_EQUAL=33
    LT=34
    LE=35
    GT=36
    GE=37
    CONCAT=38
    LB=39
    RB=40
    LP=41
    RP=42
    LSB=43
    RSB=44
    DOT=45
    COMMA=46
    SEMI=47
    COLON=48
    EQ=49
    INTLIT=50
    FLOATLIT=51
    BOOLLIT=52
    UNCLOSE_STRING=53
    ILLEGAL_ESCAPE=54
    STRINGLIT=55
    IDENTIFIER=56
    WS=57
    ERROR_CHAR=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.decllist()
            self.state = 103
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decllist




    def decllist(self):

        localctx = MT22Parser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.decl()
                self.state = 106
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shortvardecl(self):
            return self.getTypedRuleContext(MT22Parser.ShortvardeclContext,0)


        def fullvardecl(self):
            return self.getTypedRuleContext(MT22Parser.FullvardeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.shortvardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.fullvardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortvardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def vartyp(self):
            return self.getTypedRuleContext(MT22Parser.VartypContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_shortvardecl




    def shortvardecl(self):

        localctx = MT22Parser.ShortvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_shortvardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.idlist()
            self.state = 120
            self.match(MT22Parser.COLON)
            self.state = 121
            self.vartyp()
            self.state = 122
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idlist




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idlist)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(MT22Parser.IDENTIFIER)
                self.state = 125
                self.match(MT22Parser.COMMA)
                self.state = 126
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(MT22Parser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FullvardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varinit(self):
            return self.getTypedRuleContext(MT22Parser.VarinitContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_fullvardecl




    def fullvardecl(self):

        localctx = MT22Parser.FullvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_fullvardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.varinit()
            self.state = 131
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarinitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def varinit(self):
            return self.getTypedRuleContext(MT22Parser.VarinitContext,0)


        def exprpime(self):
            return self.getTypedRuleContext(MT22Parser.ExprpimeContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def vartyp(self):
            return self.getTypedRuleContext(MT22Parser.VartypContext,0)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_varinit




    def varinit(self):

        localctx = MT22Parser.VarinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varinit)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(MT22Parser.IDENTIFIER)
                self.state = 134
                self.match(MT22Parser.COMMA)
                self.state = 135
                self.varinit()
                self.state = 136
                self.match(MT22Parser.COMMA)
                self.state = 137
                self.exprpime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(MT22Parser.IDENTIFIER)
                self.state = 140
                self.match(MT22Parser.COLON)
                self.state = 141
                self.vartyp()
                self.state = 142
                self.match(MT22Parser.EQ)
                self.state = 143
                self.exprpime()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomtype(self):
            return self.getTypedRuleContext(MT22Parser.AtomtypeContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(MT22Parser.ArraytypeContext,0)


        def autotype(self):
            return self.getTypedRuleContext(MT22Parser.AutotypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vartyp




    def vartyp(self):

        localctx = MT22Parser.VartypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vartyp)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.atomtype()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.arraytype()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.autotype()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def types(self):
            return self.getTypedRuleContext(MT22Parser.TypesContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MT22Parser.ParamlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def funcinher(self):
            return self.getTypedRuleContext(MT22Parser.FuncinherContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(MT22Parser.IDENTIFIER)
            self.state = 153
            self.match(MT22Parser.COLON)
            self.state = 154
            self.match(MT22Parser.FUNCTION)
            self.state = 155
            self.types()
            self.state = 156
            self.match(MT22Parser.LB)
            self.state = 157
            self.paramlist()
            self.state = 158
            self.match(MT22Parser.RB)
            self.state = 159
            self.funcinher()
            self.state = 160
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramrime(self):
            return self.getTypedRuleContext(MT22Parser.ParamrimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramlist




    def paramlist(self):

        localctx = MT22Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramlist)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.paramrime()
                pass
            elif token in [MT22Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def paramrime(self):
            return self.getTypedRuleContext(MT22Parser.ParamrimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramrime




    def paramrime(self):

        localctx = MT22Parser.ParamrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramrime)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.param()
                self.state = 167
                self.match(MT22Parser.COMMA)
                self.state = 168
                self.paramrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paraminher(self):
            return self.getTypedRuleContext(MT22Parser.ParaminherContext,0)


        def paramout(self):
            return self.getTypedRuleContext(MT22Parser.ParamoutContext,0)


        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def vartyp(self):
            return self.getTypedRuleContext(MT22Parser.VartypContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_param




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.paraminher()
            self.state = 174
            self.paramout()
            self.state = 175
            self.match(MT22Parser.IDENTIFIER)
            self.state = 176
            self.match(MT22Parser.COLON)
            self.state = 177
            self.vartyp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaminherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paraminher




    def paraminher(self):

        localctx = MT22Parser.ParaminherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paraminher)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(MT22Parser.INHERIT)
                pass
            elif token in [MT22Parser.OUT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamoutContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paramout




    def paramout(self):

        localctx = MT22Parser.ParamoutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramout)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(MT22Parser.OUT)
                pass
            elif token in [MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncinherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcinher




    def funcinher(self):

        localctx = MT22Parser.FuncinherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funcinher)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(MT22Parser.INHERIT)
                self.state = 188
                self.match(MT22Parser.IDENTIFIER)
                pass
            elif token in [MT22Parser.LP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmtlist




    def stmtlist(self):

        localctx = MT22Parser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmtlist)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BREAK, MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.CONTINUE, MT22Parser.LP, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.stmt()
                self.state = 193
                self.stmtlist()
                pass
            elif token in [MT22Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MT22Parser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MT22Parser.ForstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(MT22Parser.WhilestmtContext,0)


        def dowhilestmt(self):
            return self.getTypedRuleContext(MT22Parser.DowhilestmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MT22Parser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
                self.assignstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 201
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 202
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 203
                self.whilestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 204
                self.dowhilestmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 205
                self.breakstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 206
                self.continuestmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 207
                self.returnstmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 208
                self.callstmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 209
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockstmt




    def blockstmt(self):

        localctx = MT22Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MT22Parser.LP)
            self.state = 213
            self.stmtlist()
            self.state = 214
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.lhs()
            self.state = 217
            self.match(MT22Parser.EQ)
            self.state = 218
            self.expr()
            self.state = 219
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def arrayele(self):
            return self.getTypedRuleContext(MT22Parser.ArrayeleContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_lhs




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lhs)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.arrayele()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def elsestmt(self):
            return self.getTypedRuleContext(MT22Parser.ElsestmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_ifstmt




    def ifstmt(self):

        localctx = MT22Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MT22Parser.IF)
            self.state = 226
            self.match(MT22Parser.LB)
            self.state = 227
            self.expr()
            self.state = 228
            self.match(MT22Parser.RB)
            self.state = 229
            self.stmt()
            self.state = 230
            self.elsestmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_elsestmt




    def elsestmt(self):

        localctx = MT22Parser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elsestmt)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(MT22Parser.ELSE)
                self.state = 233
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstmt




    def forstmt(self):

        localctx = MT22Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(MT22Parser.FOR)
            self.state = 238
            self.match(MT22Parser.LB)
            self.state = 239
            self.match(MT22Parser.IDENTIFIER)
            self.state = 240
            self.match(MT22Parser.EQ)
            self.state = 241
            self.expr()
            self.state = 242
            self.match(MT22Parser.COMMA)
            self.state = 243
            self.expr()
            self.state = 244
            self.match(MT22Parser.COMMA)
            self.state = 245
            self.expr()
            self.state = 246
            self.match(MT22Parser.RB)
            self.state = 247
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestmt




    def whilestmt(self):

        localctx = MT22Parser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(MT22Parser.WHILE)
            self.state = 250
            self.match(MT22Parser.LB)
            self.state = 251
            self.expr()
            self.state = 252
            self.match(MT22Parser.RB)
            self.state = 253
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestmt




    def dowhilestmt(self):

        localctx = MT22Parser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(MT22Parser.DO)
            self.state = 256
            self.blockstmt()
            self.state = 257
            self.match(MT22Parser.WHILE)
            self.state = 258
            self.match(MT22Parser.LB)
            self.state = 259
            self.expr()
            self.state = 260
            self.match(MT22Parser.RB)
            self.state = 261
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstmt




    def breakstmt(self):

        localctx = MT22Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MT22Parser.BREAK)
            self.state = 264
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestmt




    def continuestmt(self):

        localctx = MT22Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MT22Parser.CONTINUE)
            self.state = 267
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def retexpr(self):
            return self.getTypedRuleContext(MT22Parser.RetexprContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_returnstmt




    def returnstmt(self):

        localctx = MT22Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(MT22Parser.RETURN)
            self.state = 270
            self.retexpr()
            self.state = 271
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_retexpr




    def retexpr(self):

        localctx = MT22Parser.RetexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_retexpr)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB, MT22Parser.NOT, MT22Parser.LB, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.expr()
                pass
            elif token in [MT22Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MT22Parser.IDENTIFIER)
            self.state = 278
            self.match(MT22Parser.LB)
            self.state = 279
            self.exprlist()
            self.state = 280
            self.match(MT22Parser.RB)
            self.state = 281
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprpime(self):
            return self.getTypedRuleContext(MT22Parser.ExprpimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exprlist)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB, MT22Parser.NOT, MT22Parser.LB, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.exprpime()
                pass
            elif token in [MT22Parser.RB, MT22Parser.RP, MT22Parser.RSB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprpimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprpime(self):
            return self.getTypedRuleContext(MT22Parser.ExprpimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprpime




    def exprpime(self):

        localctx = MT22Parser.ExprpimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exprpime)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.expr()
                self.state = 288
                self.match(MT22Parser.COMMA)
                self.state = 289
                self.exprpime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(MT22Parser.CONCAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.expr1()
                self.state = 295
                self.match(MT22Parser.CONCAT)
                self.state = 296
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MT22Parser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(MT22Parser.LT, 0)

        def GT(self):
            return self.getToken(MT22Parser.GT, 0)

        def LE(self):
            return self.getToken(MT22Parser.LE, 0)

        def GE(self):
            return self.getToken(MT22Parser.GE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.expr2(0)
                self.state = 302
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOT_EQUAL) | (1 << MT22Parser.LT) | (1 << MT22Parser.LE) | (1 << MT22Parser.GT) | (1 << MT22Parser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 303
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 311
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 313
                    self.expr3(0) 
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 322
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 323
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 324
                    self.expr4(0) 
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 333
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 334
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 335
                    self.expr5() 
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr5)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(MT22Parser.NOT)
                self.state = 342
                self.expr5()
                pass
            elif token in [MT22Parser.SUB, MT22Parser.LB, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr6)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(MT22Parser.SUB)
                self.state = 347
                self.expr6()
                pass
            elif token in [MT22Parser.LB, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subexpr(self):
            return self.getTypedRuleContext(MT22Parser.SubexprContext,0)


        def arrayele(self):
            return self.getTypedRuleContext(MT22Parser.ArrayeleContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MT22Parser.FunccallContext,0)


        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MT22Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr7




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr7)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.subexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.arrayele()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 355
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 356
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 357
                self.match(MT22Parser.BOOLLIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 358
                self.match(MT22Parser.STRINGLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_subexpr




    def subexpr(self):

        localctx = MT22Parser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(MT22Parser.LB)
            self.state = 362
            self.expr()
            self.state = 363
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayeleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayele




    def arrayele(self):

        localctx = MT22Parser.ArrayeleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arrayele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MT22Parser.IDENTIFIER)
            self.state = 366
            self.match(MT22Parser.LSB)
            self.state = 367
            self.exprlist()
            self.state = 368
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funccall




    def funccall(self):

        localctx = MT22Parser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(MT22Parser.IDENTIFIER)
            self.state = 371
            self.match(MT22Parser.LB)
            self.state = 372
            self.exprlist()
            self.state = 373
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomtype(self):
            return self.getTypedRuleContext(MT22Parser.AtomtypeContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(MT22Parser.ArraytypeContext,0)


        def voidtype(self):
            return self.getTypedRuleContext(MT22Parser.VoidtypeContext,0)


        def autotype(self):
            return self.getTypedRuleContext(MT22Parser.AutotypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_types




    def types(self):

        localctx = MT22Parser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_types)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.atomtype()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.arraytype()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.voidtype()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
                self.autotype()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomtype




    def atomtype(self):

        localctx = MT22Parser.AtomtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_atomtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def dimenslist(self):
            return self.getTypedRuleContext(MT22Parser.DimenslistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomtype(self):
            return self.getTypedRuleContext(MT22Parser.AtomtypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraytype




    def arraytype(self):

        localctx = MT22Parser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(MT22Parser.ARRAY)
            self.state = 384
            self.match(MT22Parser.LSB)
            self.state = 385
            self.dimenslist()
            self.state = 386
            self.match(MT22Parser.RSB)
            self.state = 387
            self.match(MT22Parser.OF)
            self.state = 388
            self.atomtype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimenslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def dimenslist(self):
            return self.getTypedRuleContext(MT22Parser.DimenslistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimenslist




    def dimenslist(self):

        localctx = MT22Parser.DimenslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_dimenslist)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(MT22Parser.INTLIT)
                self.state = 391
                self.match(MT22Parser.COMMA)
                self.state = 392
                self.dimenslist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.match(MT22Parser.INTLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arraylit




    def arraylit(self):

        localctx = MT22Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(MT22Parser.LP)
            self.state = 397
            self.exprlist()
            self.state = 398
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_voidtype




    def voidtype(self):

        localctx = MT22Parser.VoidtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_voidtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(MT22Parser.VOID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AutotypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_autotype




    def autotype(self):

        localctx = MT22Parser.AutotypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_autotype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(MT22Parser.AUTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[35] = self.expr2_sempred
        self._predicates[36] = self.expr3_sempred
        self._predicates[37] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




