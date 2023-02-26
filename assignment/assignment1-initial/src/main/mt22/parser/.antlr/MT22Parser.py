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
        buf.write("\u0195\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3n\n\3\3\4\3\4\5\4r\n\4\3\5\3\5\5")
        buf.write("\5v\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0081")
        buf.write("\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u0092\n\t\3\n\3\n\3\n\5\n\u0097\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\5\f\u00a5\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00ac\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\5\17\u00b6\n\17\3")
        buf.write("\20\3\20\5\20\u00ba\n\20\3\21\3\21\3\21\5\21\u00bf\n\21")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00c5\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00d3")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\5\26\u00e0\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\5\30\u00ec\n\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\5\36\u0111")
        buf.write("\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \5")
        buf.write(" \u011d\n \3!\3!\3!\3!\3!\5!\u0124\n!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\5\"\u012b\n\"\3#\3#\3#\3#\3#\5#\u0132\n#\3$\3$\3")
        buf.write("$\3$\3$\3$\7$\u013a\n$\f$\16$\u013d\13$\3%\3%\3%\3%\3")
        buf.write("%\3%\7%\u0145\n%\f%\16%\u0148\13%\3&\3&\3&\3&\3&\3&\7")
        buf.write("&\u0150\n&\f&\16&\u0153\13&\3\'\3\'\3\'\5\'\u0158\n\'")
        buf.write("\3(\3(\3(\5(\u015d\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0168")
        buf.write("\n)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\5-\u017c\n-\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\5\60\u018b\n\60\3\61\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\63\3\63\3\63\2\5FHJ\64\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bd\2\7\3\2#(\3\2!\"\3\2\33\34\3\2\35\37\6\2\b\b\f\f")
        buf.write("\20\20\22\22\2\u0192\2f\3\2\2\2\4m\3\2\2\2\6q\3\2\2\2")
        buf.write("\bu\3\2\2\2\nw\3\2\2\2\f\u0080\3\2\2\2\16\u0082\3\2\2")
        buf.write("\2\20\u0091\3\2\2\2\22\u0096\3\2\2\2\24\u0098\3\2\2\2")
        buf.write("\26\u00a4\3\2\2\2\30\u00ab\3\2\2\2\32\u00ad\3\2\2\2\34")
        buf.write("\u00b5\3\2\2\2\36\u00b9\3\2\2\2 \u00be\3\2\2\2\"\u00c4")
        buf.write("\3\2\2\2$\u00d2\3\2\2\2&\u00d4\3\2\2\2(\u00d8\3\2\2\2")
        buf.write("*\u00df\3\2\2\2,\u00e1\3\2\2\2.\u00eb\3\2\2\2\60\u00ed")
        buf.write("\3\2\2\2\62\u00f9\3\2\2\2\64\u00ff\3\2\2\2\66\u0107\3")
        buf.write("\2\2\28\u010a\3\2\2\2:\u010d\3\2\2\2<\u0114\3\2\2\2>\u011c")
        buf.write("\3\2\2\2@\u0123\3\2\2\2B\u012a\3\2\2\2D\u0131\3\2\2\2")
        buf.write("F\u0133\3\2\2\2H\u013e\3\2\2\2J\u0149\3\2\2\2L\u0157\3")
        buf.write("\2\2\2N\u015c\3\2\2\2P\u0167\3\2\2\2R\u0169\3\2\2\2T\u016d")
        buf.write("\3\2\2\2V\u0172\3\2\2\2X\u017b\3\2\2\2Z\u017d\3\2\2\2")
        buf.write("\\\u017f\3\2\2\2^\u018a\3\2\2\2`\u018c\3\2\2\2b\u0190")
        buf.write("\3\2\2\2d\u0192\3\2\2\2fg\5\4\3\2gh\7\2\2\3h\3\3\2\2\2")
        buf.write("ij\5\6\4\2jk\5\4\3\2kn\3\2\2\2ln\5\6\4\2mi\3\2\2\2ml\3")
        buf.write("\2\2\2n\5\3\2\2\2or\5\b\5\2pr\5\24\13\2qo\3\2\2\2qp\3")
        buf.write("\2\2\2r\7\3\2\2\2sv\5\n\6\2tv\5\16\b\2us\3\2\2\2ut\3\2")
        buf.write("\2\2v\t\3\2\2\2wx\5\f\7\2xy\7\63\2\2yz\5\22\n\2z{\7\62")
        buf.write("\2\2{\13\3\2\2\2|}\7:\2\2}~\7\61\2\2~\u0081\5\f\7\2\177")
        buf.write("\u0081\7:\2\2\u0080|\3\2\2\2\u0080\177\3\2\2\2\u0081\r")
        buf.write("\3\2\2\2\u0082\u0083\5\20\t\2\u0083\u0084\7\62\2\2\u0084")
        buf.write("\17\3\2\2\2\u0085\u0086\7:\2\2\u0086\u0087\7\61\2\2\u0087")
        buf.write("\u0088\5\20\t\2\u0088\u0089\7\61\2\2\u0089\u008a\5B\"")
        buf.write("\2\u008a\u0092\3\2\2\2\u008b\u008c\7:\2\2\u008c\u008d")
        buf.write("\7\63\2\2\u008d\u008e\5\22\n\2\u008e\u008f\7\64\2\2\u008f")
        buf.write("\u0090\5B\"\2\u0090\u0092\3\2\2\2\u0091\u0085\3\2\2\2")
        buf.write("\u0091\u008b\3\2\2\2\u0092\21\3\2\2\2\u0093\u0097\5Z.")
        buf.write("\2\u0094\u0097\5\\/\2\u0095\u0097\5d\63\2\u0096\u0093")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\23\3\2\2\2\u0098\u0099\7:\2\2\u0099\u009a\7\63\2\2\u009a")
        buf.write("\u009b\7\16\2\2\u009b\u009c\5X-\2\u009c\u009d\7*\2\2\u009d")
        buf.write("\u009e\5\26\f\2\u009e\u009f\7+\2\2\u009f\u00a0\5 \21\2")
        buf.write("\u00a0\u00a1\5&\24\2\u00a1\25\3\2\2\2\u00a2\u00a5\5\30")
        buf.write("\r\2\u00a3\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3")
        buf.write("\3\2\2\2\u00a5\27\3\2\2\2\u00a6\u00a7\5\32\16\2\u00a7")
        buf.write("\u00a8\7\61\2\2\u00a8\u00a9\5\30\r\2\u00a9\u00ac\3\2\2")
        buf.write("\2\u00aa\u00ac\5\32\16\2\u00ab\u00a6\3\2\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\31\3\2\2\2\u00ad\u00ae\5\34\17\2\u00ae")
        buf.write("\u00af\5\36\20\2\u00af\u00b0\7:\2\2\u00b0\u00b1\7\63\2")
        buf.write("\2\u00b1\u00b2\5\22\n\2\u00b2\33\3\2\2\2\u00b3\u00b6\7")
        buf.write("\31\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b6\35\3\2\2\2\u00b7\u00ba\7\26\2\2\u00b8")
        buf.write("\u00ba\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2")
        buf.write("\u00ba\37\3\2\2\2\u00bb\u00bc\7\31\2\2\u00bc\u00bf\7:")
        buf.write("\2\2\u00bd\u00bf\3\2\2\2\u00be\u00bb\3\2\2\2\u00be\u00bd")
        buf.write("\3\2\2\2\u00bf!\3\2\2\2\u00c0\u00c1\5$\23\2\u00c1\u00c2")
        buf.write("\5\"\22\2\u00c2\u00c5\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4")
        buf.write("\u00c0\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5#\3\2\2\2\u00c6")
        buf.write("\u00d3\5&\24\2\u00c7\u00d3\5\b\5\2\u00c8\u00d3\5(\25\2")
        buf.write("\u00c9\u00d3\5,\27\2\u00ca\u00d3\5\60\31\2\u00cb\u00d3")
        buf.write("\5\62\32\2\u00cc\u00d3\5\64\33\2\u00cd\u00d3\5\66\34\2")
        buf.write("\u00ce\u00d3\58\35\2\u00cf\u00d3\5:\36\2\u00d0\u00d3\5")
        buf.write("<\37\2\u00d1\u00d3\5&\24\2\u00d2\u00c6\3\2\2\2\u00d2\u00c7")
        buf.write("\3\2\2\2\u00d2\u00c8\3\2\2\2\u00d2\u00c9\3\2\2\2\u00d2")
        buf.write("\u00ca\3\2\2\2\u00d2\u00cb\3\2\2\2\u00d2\u00cc\3\2\2\2")
        buf.write("\u00d2\u00cd\3\2\2\2\u00d2\u00ce\3\2\2\2\u00d2\u00cf\3")
        buf.write("\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3%")
        buf.write("\3\2\2\2\u00d4\u00d5\7,\2\2\u00d5\u00d6\5\"\22\2\u00d6")
        buf.write("\u00d7\7-\2\2\u00d7\'\3\2\2\2\u00d8\u00d9\5*\26\2\u00d9")
        buf.write("\u00da\7\64\2\2\u00da\u00db\5B\"\2\u00db\u00dc\7\62\2")
        buf.write("\2\u00dc)\3\2\2\2\u00dd\u00e0\7:\2\2\u00de\u00e0\5T+\2")
        buf.write("\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0+\3\2\2")
        buf.write("\2\u00e1\u00e2\7\17\2\2\u00e2\u00e3\7*\2\2\u00e3\u00e4")
        buf.write("\5B\"\2\u00e4\u00e5\7+\2\2\u00e5\u00e6\5$\23\2\u00e6\u00e7")
        buf.write("\5.\30\2\u00e7-\3\2\2\2\u00e8\u00e9\7\n\2\2\u00e9\u00ec")
        buf.write("\5$\23\2\u00ea\u00ec\3\2\2\2\u00eb\u00e8\3\2\2\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec/\3\2\2\2\u00ed\u00ee\7\r\2\2\u00ee")
        buf.write("\u00ef\7*\2\2\u00ef\u00f0\7:\2\2\u00f0\u00f1\7\64\2\2")
        buf.write("\u00f1\u00f2\5B\"\2\u00f2\u00f3\7\61\2\2\u00f3\u00f4\5")
        buf.write("B\"\2\u00f4\u00f5\7\61\2\2\u00f5\u00f6\5B\"\2\u00f6\u00f7")
        buf.write("\7+\2\2\u00f7\u00f8\5$\23\2\u00f8\61\3\2\2\2\u00f9\u00fa")
        buf.write("\7\24\2\2\u00fa\u00fb\7*\2\2\u00fb\u00fc\5B\"\2\u00fc")
        buf.write("\u00fd\7+\2\2\u00fd\u00fe\5$\23\2\u00fe\63\3\2\2\2\u00ff")
        buf.write("\u0100\7\t\2\2\u0100\u0101\5&\24\2\u0101\u0102\7\24\2")
        buf.write("\2\u0102\u0103\7*\2\2\u0103\u0104\5B\"\2\u0104\u0105\7")
        buf.write("+\2\2\u0105\u0106\7\62\2\2\u0106\65\3\2\2\2\u0107\u0108")
        buf.write("\7\7\2\2\u0108\u0109\7\62\2\2\u0109\67\3\2\2\2\u010a\u010b")
        buf.write("\7\27\2\2\u010b\u010c\7\62\2\2\u010c9\3\2\2\2\u010d\u0110")
        buf.write("\7\21\2\2\u010e\u0111\5B\"\2\u010f\u0111\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0112\u0113\7\62\2\2\u0113;\3\2\2\2\u0114\u0115\7:\2")
        buf.write("\2\u0115\u0116\7*\2\2\u0116\u0117\5> \2\u0117\u0118\7")
        buf.write("+\2\2\u0118\u0119\7\62\2\2\u0119=\3\2\2\2\u011a\u011d")
        buf.write("\5@!\2\u011b\u011d\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011b")
        buf.write("\3\2\2\2\u011d?\3\2\2\2\u011e\u011f\5B\"\2\u011f\u0120")
        buf.write("\7\61\2\2\u0120\u0121\5@!\2\u0121\u0124\3\2\2\2\u0122")
        buf.write("\u0124\5B\"\2\u0123\u011e\3\2\2\2\u0123\u0122\3\2\2\2")
        buf.write("\u0124A\3\2\2\2\u0125\u0126\5D#\2\u0126\u0127\7)\2\2\u0127")
        buf.write("\u0128\5D#\2\u0128\u012b\3\2\2\2\u0129\u012b\5D#\2\u012a")
        buf.write("\u0125\3\2\2\2\u012a\u0129\3\2\2\2\u012bC\3\2\2\2\u012c")
        buf.write("\u012d\5F$\2\u012d\u012e\t\2\2\2\u012e\u012f\5F$\2\u012f")
        buf.write("\u0132\3\2\2\2\u0130\u0132\5F$\2\u0131\u012c\3\2\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132E\3\2\2\2\u0133\u0134\b$\1\2\u0134")
        buf.write("\u0135\5H%\2\u0135\u013b\3\2\2\2\u0136\u0137\f\4\2\2\u0137")
        buf.write("\u0138\t\3\2\2\u0138\u013a\5H%\2\u0139\u0136\3\2\2\2\u013a")
        buf.write("\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013cG\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f\b%\1\2")
        buf.write("\u013f\u0140\5J&\2\u0140\u0146\3\2\2\2\u0141\u0142\f\4")
        buf.write("\2\2\u0142\u0143\t\4\2\2\u0143\u0145\5J&\2\u0144\u0141")
        buf.write("\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147I\3\2\2\2\u0148\u0146\3\2\2\2\u0149")
        buf.write("\u014a\b&\1\2\u014a\u014b\5L\'\2\u014b\u0151\3\2\2\2\u014c")
        buf.write("\u014d\f\4\2\2\u014d\u014e\t\5\2\2\u014e\u0150\5L\'\2")
        buf.write("\u014f\u014c\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3")
        buf.write("\2\2\2\u0151\u0152\3\2\2\2\u0152K\3\2\2\2\u0153\u0151")
        buf.write("\3\2\2\2\u0154\u0155\7 \2\2\u0155\u0158\5L\'\2\u0156\u0158")
        buf.write("\5N(\2\u0157\u0154\3\2\2\2\u0157\u0156\3\2\2\2\u0158M")
        buf.write("\3\2\2\2\u0159\u015a\7\34\2\2\u015a\u015d\5N(\2\u015b")
        buf.write("\u015d\5P)\2\u015c\u0159\3\2\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("O\3\2\2\2\u015e\u0168\5R*\2\u015f\u0168\5T+\2\u0160\u0168")
        buf.write("\5V,\2\u0161\u0168\7:\2\2\u0162\u0168\7\65\2\2\u0163\u0168")
        buf.write("\7\66\2\2\u0164\u0168\7\5\2\2\u0165\u0168\79\2\2\u0166")
        buf.write("\u0168\5`\61\2\u0167\u015e\3\2\2\2\u0167\u015f\3\2\2\2")
        buf.write("\u0167\u0160\3\2\2\2\u0167\u0161\3\2\2\2\u0167\u0162\3")
        buf.write("\2\2\2\u0167\u0163\3\2\2\2\u0167\u0164\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0166\3\2\2\2\u0168Q\3\2\2\2\u0169\u016a")
        buf.write("\7*\2\2\u016a\u016b\5B\"\2\u016b\u016c\7+\2\2\u016cS\3")
        buf.write("\2\2\2\u016d\u016e\7:\2\2\u016e\u016f\7.\2\2\u016f\u0170")
        buf.write("\5> \2\u0170\u0171\7/\2\2\u0171U\3\2\2\2\u0172\u0173\7")
        buf.write(":\2\2\u0173\u0174\7*\2\2\u0174\u0175\5> \2\u0175\u0176")
        buf.write("\7+\2\2\u0176W\3\2\2\2\u0177\u017c\5Z.\2\u0178\u017c\5")
        buf.write("\\/\2\u0179\u017c\5b\62\2\u017a\u017c\5d\63\2\u017b\u0177")
        buf.write("\3\2\2\2\u017b\u0178\3\2\2\2\u017b\u0179\3\2\2\2\u017b")
        buf.write("\u017a\3\2\2\2\u017cY\3\2\2\2\u017d\u017e\t\6\2\2\u017e")
        buf.write("[\3\2\2\2\u017f\u0180\7\32\2\2\u0180\u0181\7.\2\2\u0181")
        buf.write("\u0182\5^\60\2\u0182\u0183\7/\2\2\u0183\u0184\7\30\2\2")
        buf.write("\u0184\u0185\5Z.\2\u0185]\3\2\2\2\u0186\u0187\7\65\2\2")
        buf.write("\u0187\u0188\7\61\2\2\u0188\u018b\5^\60\2\u0189\u018b")
        buf.write("\7\65\2\2\u018a\u0186\3\2\2\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("_\3\2\2\2\u018c\u018d\7,\2\2\u018d\u018e\5> \2\u018e\u018f")
        buf.write("\7-\2\2\u018fa\3\2\2\2\u0190\u0191\7\25\2\2\u0191c\3\2")
        buf.write("\2\2\u0192\u0193\7\6\2\2\u0193e\3\2\2\2\36mqu\u0080\u0091")
        buf.write("\u0096\u00a4\u00ab\u00b5\u00b9\u00be\u00c4\u00d2\u00df")
        buf.write("\u00eb\u0110\u011c\u0123\u012a\u0131\u013b\u0146\u0151")
        buf.write("\u0157\u015c\u0167\u017b\u018a")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
                     "'false'", "'float'", "'for'", "'function'", "'if'", 
                     "'integer'", "'return'", "'string'", "'true'", "'while'", 
                     "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
                     "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'::'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "'.'", "','", "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>", "BLOCK_COMMENT", "LINE_COMMENT", "BOOLLIT", 
                      "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", 
                      "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
                      "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                      "OF", "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", 
                      "LE", "GT", "GE", "CONCAT", "LB", "RB", "LP", "RP", 
                      "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "EQ", 
                      "INTLIT", "FLOATLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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
    RULE_callstmt = 29
    RULE_exprlist = 30
    RULE_exprprime = 31
    RULE_expr = 32
    RULE_expr1 = 33
    RULE_expr2 = 34
    RULE_expr3 = 35
    RULE_expr4 = 36
    RULE_expr5 = 37
    RULE_expr6 = 38
    RULE_expr7 = 39
    RULE_subexpr = 40
    RULE_arrayele = 41
    RULE_funccall = 42
    RULE_types = 43
    RULE_atomtype = 44
    RULE_arraytype = 45
    RULE_dimenslist = 46
    RULE_arraylit = 47
    RULE_voidtype = 48
    RULE_autotype = 49

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "shortvardecl", 
                   "idlist", "fullvardecl", "varinit", "vartyp", "funcdecl", 
                   "paramlist", "paramrime", "param", "paraminher", "paramout", 
                   "funcinher", "stmtlist", "stmt", "blockstmt", "assignstmt", 
                   "lhs", "ifstmt", "elsestmt", "forstmt", "whilestmt", 
                   "dowhilestmt", "breakstmt", "continuestmt", "returnstmt", 
                   "callstmt", "exprlist", "exprprime", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "subexpr", "arrayele", "funccall", "types", "atomtype", 
                   "arraytype", "dimenslist", "arraylit", "voidtype", "autotype" ]

    EOF = Token.EOF
    BLOCK_COMMENT=1
    LINE_COMMENT=2
    BOOLLIT=3
    AUTO=4
    BREAK=5
    BOOLEAN=6
    DO=7
    ELSE=8
    FALSE=9
    FLOAT=10
    FOR=11
    FUNCTION=12
    IF=13
    INTEGER=14
    RETURN=15
    STRING=16
    TRUE=17
    WHILE=18
    VOID=19
    OUT=20
    CONTINUE=21
    OF=22
    INHERIT=23
    ARRAY=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    NOT=30
    AND=31
    OR=32
    EQUAL=33
    NOT_EQUAL=34
    LT=35
    LE=36
    GT=37
    GE=38
    CONCAT=39
    LB=40
    RB=41
    LP=42
    RP=43
    LSB=44
    RSB=45
    DOT=46
    COMMA=47
    SEMI=48
    COLON=49
    EQ=50
    INTLIT=51
    FLOATLIT=52
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
            self.state = 100
            self.decllist()
            self.state = 101
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
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.decl()
                self.state = 104
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
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
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.shortvardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
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
            self.state = 117
            self.idlist()
            self.state = 118
            self.match(MT22Parser.COLON)
            self.state = 119
            self.vartyp()
            self.state = 120
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
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(MT22Parser.IDENTIFIER)
                self.state = 123
                self.match(MT22Parser.COMMA)
                self.state = 124
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
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
            self.state = 128
            self.varinit()
            self.state = 129
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


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(MT22Parser.IDENTIFIER)
                self.state = 132
                self.match(MT22Parser.COMMA)
                self.state = 133
                self.varinit()
                self.state = 134
                self.match(MT22Parser.COMMA)
                self.state = 135
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(MT22Parser.IDENTIFIER)
                self.state = 138
                self.match(MT22Parser.COLON)
                self.state = 139
                self.vartyp()
                self.state = 140
                self.match(MT22Parser.EQ)
                self.state = 141
                self.expr()
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
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.atomtype()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.arraytype()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
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
            self.state = 150
            self.match(MT22Parser.IDENTIFIER)
            self.state = 151
            self.match(MT22Parser.COLON)
            self.state = 152
            self.match(MT22Parser.FUNCTION)
            self.state = 153
            self.types()
            self.state = 154
            self.match(MT22Parser.LB)
            self.state = 155
            self.paramlist()
            self.state = 156
            self.match(MT22Parser.RB)
            self.state = 157
            self.funcinher()
            self.state = 158
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
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.param()
                self.state = 165
                self.match(MT22Parser.COMMA)
                self.state = 166
                self.paramrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
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
            self.state = 171
            self.paraminher()
            self.state = 172
            self.paramout()
            self.state = 173
            self.match(MT22Parser.IDENTIFIER)
            self.state = 174
            self.match(MT22Parser.COLON)
            self.state = 175
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
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
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
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
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
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(MT22Parser.INHERIT)
                self.state = 186
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
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BREAK, MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.CONTINUE, MT22Parser.LP, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.stmt()
                self.state = 191
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
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.assignstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 199
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 200
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 201
                self.whilestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 202
                self.dowhilestmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 203
                self.breakstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 204
                self.continuestmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 205
                self.returnstmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 206
                self.callstmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 207
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
            self.state = 210
            self.match(MT22Parser.LP)
            self.state = 211
            self.stmtlist()
            self.state = 212
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
            self.state = 214
            self.lhs()
            self.state = 215
            self.match(MT22Parser.EQ)
            self.state = 216
            self.expr()
            self.state = 217
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
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
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
            self.state = 223
            self.match(MT22Parser.IF)
            self.state = 224
            self.match(MT22Parser.LB)
            self.state = 225
            self.expr()
            self.state = 226
            self.match(MT22Parser.RB)
            self.state = 227
            self.stmt()
            self.state = 228
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
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(MT22Parser.ELSE)
                self.state = 231
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
            self.state = 235
            self.match(MT22Parser.FOR)
            self.state = 236
            self.match(MT22Parser.LB)
            self.state = 237
            self.match(MT22Parser.IDENTIFIER)
            self.state = 238
            self.match(MT22Parser.EQ)
            self.state = 239
            self.expr()
            self.state = 240
            self.match(MT22Parser.COMMA)
            self.state = 241
            self.expr()
            self.state = 242
            self.match(MT22Parser.COMMA)
            self.state = 243
            self.expr()
            self.state = 244
            self.match(MT22Parser.RB)
            self.state = 245
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
            self.state = 247
            self.match(MT22Parser.WHILE)
            self.state = 248
            self.match(MT22Parser.LB)
            self.state = 249
            self.expr()
            self.state = 250
            self.match(MT22Parser.RB)
            self.state = 251
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
            self.state = 253
            self.match(MT22Parser.DO)
            self.state = 254
            self.blockstmt()
            self.state = 255
            self.match(MT22Parser.WHILE)
            self.state = 256
            self.match(MT22Parser.LB)
            self.state = 257
            self.expr()
            self.state = 258
            self.match(MT22Parser.RB)
            self.state = 259
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
            self.state = 261
            self.match(MT22Parser.BREAK)
            self.state = 262
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
            self.state = 264
            self.match(MT22Parser.CONTINUE)
            self.state = 265
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnstmt




    def returnstmt(self):

        localctx = MT22Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(MT22Parser.RETURN)
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLLIT, MT22Parser.SUB, MT22Parser.NOT, MT22Parser.LB, MT22Parser.LP, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.state = 268
                self.expr()
                pass
            elif token in [MT22Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 272
            self.match(MT22Parser.SEMI)
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
        self.enterRule(localctx, 58, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MT22Parser.IDENTIFIER)
            self.state = 275
            self.match(MT22Parser.LB)
            self.state = 276
            self.exprlist()
            self.state = 277
            self.match(MT22Parser.RB)
            self.state = 278
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

        def exprprime(self):
            return self.getTypedRuleContext(MT22Parser.ExprprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exprlist)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLLIT, MT22Parser.SUB, MT22Parser.NOT, MT22Parser.LB, MT22Parser.LP, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.exprprime()
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


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprprime(self):
            return self.getTypedRuleContext(MT22Parser.ExprprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprprime




    def exprprime(self):

        localctx = MT22Parser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exprprime)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.expr()
                self.state = 285
                self.match(MT22Parser.COMMA)
                self.state = 286
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
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
        self.enterRule(localctx, 64, self.RULE_expr)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.expr1()
                self.state = 292
                self.match(MT22Parser.CONCAT)
                self.state = 293
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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
        self.enterRule(localctx, 66, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.expr2(0)
                self.state = 299
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOT_EQUAL) | (1 << MT22Parser.LT) | (1 << MT22Parser.LE) | (1 << MT22Parser.GT) | (1 << MT22Parser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 300
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.expr3(0) 
                self.state = 315
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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 321
                    self.expr4(0) 
                self.state = 326
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 330
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 331
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 332
                    self.expr5() 
                self.state = 337
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
        self.enterRule(localctx, 74, self.RULE_expr5)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(MT22Parser.NOT)
                self.state = 339
                self.expr5()
                pass
            elif token in [MT22Parser.BOOLLIT, MT22Parser.SUB, MT22Parser.LB, MT22Parser.LP, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
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
        self.enterRule(localctx, 76, self.RULE_expr6)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(MT22Parser.SUB)
                self.state = 344
                self.expr6()
                pass
            elif token in [MT22Parser.BOOLLIT, MT22Parser.LB, MT22Parser.LP, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
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

        def arraylit(self):
            return self.getTypedRuleContext(MT22Parser.ArraylitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr7




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr7)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.subexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.arrayele()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 352
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 353
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 354
                self.match(MT22Parser.BOOLLIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 355
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 356
                self.arraylit()
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
        self.enterRule(localctx, 80, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(MT22Parser.LB)
            self.state = 360
            self.expr()
            self.state = 361
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
        self.enterRule(localctx, 82, self.RULE_arrayele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(MT22Parser.IDENTIFIER)
            self.state = 364
            self.match(MT22Parser.LSB)
            self.state = 365
            self.exprlist()
            self.state = 366
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
        self.enterRule(localctx, 84, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(MT22Parser.IDENTIFIER)
            self.state = 369
            self.match(MT22Parser.LB)
            self.state = 370
            self.exprlist()
            self.state = 371
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
        self.enterRule(localctx, 86, self.RULE_types)
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.atomtype()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.arraytype()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.voidtype()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 376
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
        self.enterRule(localctx, 88, self.RULE_atomtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
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
        self.enterRule(localctx, 90, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(MT22Parser.ARRAY)
            self.state = 382
            self.match(MT22Parser.LSB)
            self.state = 383
            self.dimenslist()
            self.state = 384
            self.match(MT22Parser.RSB)
            self.state = 385
            self.match(MT22Parser.OF)
            self.state = 386
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
        self.enterRule(localctx, 92, self.RULE_dimenslist)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.match(MT22Parser.INTLIT)
                self.state = 389
                self.match(MT22Parser.COMMA)
                self.state = 390
                self.dimenslist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
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
        self.enterRule(localctx, 94, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(MT22Parser.LP)
            self.state = 395
            self.exprlist()
            self.state = 396
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
        self.enterRule(localctx, 96, self.RULE_voidtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
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
        self.enterRule(localctx, 98, self.RULE_autotype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
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
        self._predicates[34] = self.expr2_sempred
        self._predicates[35] = self.expr3_sempred
        self._predicates[36] = self.expr4_sempred
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
         




