# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u01ef\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0084")
        buf.write("\n\3\3\4\3\4\5\4\u0088\n\4\3\5\3\5\5\5\u008c\n\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0097\n\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00a8\n\t\3\n\3\n\3\n\5\n\u00ad\n\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00bb\n")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\5\r\u00c2\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\5\17\u00cc\n\17\3\20\3\20\5\20")
        buf.write("\u00d0\n\20\3\21\3\21\3\21\5\21\u00d5\n\21\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00db\n\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00ea\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\5\26\u00f7\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\30\3\30\3\30\5\30\u0103\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\5\36\u0128\n")
        buf.write("\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \5 \u013c\n \3!\3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\5")
        buf.write("+\u0177\n+\3,\3,\3,\3,\3,\5,\u017e\n,\3-\3-\3-\3-\3-\5")
        buf.write("-\u0185\n-\3.\3.\3.\3.\3.\5.\u018c\n.\3/\3/\3/\3/\3/\3")
        buf.write("/\7/\u0194\n/\f/\16/\u0197\13/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\7\60\u019f\n\60\f\60\16\60\u01a2\13\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u01aa\n\61\f\61\16\61\u01ad")
        buf.write("\13\61\3\62\3\62\3\62\5\62\u01b2\n\62\3\63\3\63\3\63\5")
        buf.write("\63\u01b7\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\5\64\u01c2\n\64\3\65\3\65\3\65\3\65\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38\58")
        buf.write("\u01d6\n8\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\5;\u01e5")
        buf.write("\n;\3<\3<\3<\3<\3=\3=\3>\3>\3>\2\5\\^`?\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz\2\7\3\2-\62\3\2+,\3\2%&\3")
        buf.write("\2\')\6\2\22\22\26\26\32\32\34\34\2\u01eb\2|\3\2\2\2\4")
        buf.write("\u0083\3\2\2\2\6\u0087\3\2\2\2\b\u008b\3\2\2\2\n\u008d")
        buf.write("\3\2\2\2\f\u0096\3\2\2\2\16\u0098\3\2\2\2\20\u00a7\3\2")
        buf.write("\2\2\22\u00ac\3\2\2\2\24\u00ae\3\2\2\2\26\u00ba\3\2\2")
        buf.write("\2\30\u00c1\3\2\2\2\32\u00c3\3\2\2\2\34\u00cb\3\2\2\2")
        buf.write("\36\u00cf\3\2\2\2 \u00d4\3\2\2\2\"\u00da\3\2\2\2$\u00e9")
        buf.write("\3\2\2\2&\u00eb\3\2\2\2(\u00ef\3\2\2\2*\u00f6\3\2\2\2")
        buf.write(",\u00f8\3\2\2\2.\u0102\3\2\2\2\60\u0104\3\2\2\2\62\u0110")
        buf.write("\3\2\2\2\64\u0116\3\2\2\2\66\u011e\3\2\2\28\u0121\3\2")
        buf.write("\2\2:\u0124\3\2\2\2<\u012b\3\2\2\2>\u013b\3\2\2\2@\u013d")
        buf.write("\3\2\2\2B\u0142\3\2\2\2D\u0148\3\2\2\2F\u014d\3\2\2\2")
        buf.write("H\u0153\3\2\2\2J\u0158\3\2\2\2L\u015e\3\2\2\2N\u0163\3")
        buf.write("\2\2\2P\u0169\3\2\2\2R\u016f\3\2\2\2T\u0176\3\2\2\2V\u017d")
        buf.write("\3\2\2\2X\u0184\3\2\2\2Z\u018b\3\2\2\2\\\u018d\3\2\2\2")
        buf.write("^\u0198\3\2\2\2`\u01a3\3\2\2\2b\u01b1\3\2\2\2d\u01b6\3")
        buf.write("\2\2\2f\u01c1\3\2\2\2h\u01c3\3\2\2\2j\u01c7\3\2\2\2l\u01cc")
        buf.write("\3\2\2\2n\u01d5\3\2\2\2p\u01d7\3\2\2\2r\u01d9\3\2\2\2")
        buf.write("t\u01e4\3\2\2\2v\u01e6\3\2\2\2x\u01ea\3\2\2\2z\u01ec\3")
        buf.write("\2\2\2|}\5\4\3\2}~\7\2\2\3~\3\3\2\2\2\177\u0080\5\6\4")
        buf.write("\2\u0080\u0081\5\4\3\2\u0081\u0084\3\2\2\2\u0082\u0084")
        buf.write("\5\6\4\2\u0083\177\3\2\2\2\u0083\u0082\3\2\2\2\u0084\5")
        buf.write("\3\2\2\2\u0085\u0088\5\b\5\2\u0086\u0088\5\24\13\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088\7\3\2\2\2\u0089")
        buf.write("\u008c\5\n\6\2\u008a\u008c\5\16\b\2\u008b\u0089\3\2\2")
        buf.write("\2\u008b\u008a\3\2\2\2\u008c\t\3\2\2\2\u008d\u008e\5\f")
        buf.write("\7\2\u008e\u008f\7=\2\2\u008f\u0090\5\22\n\2\u0090\u0091")
        buf.write("\7<\2\2\u0091\13\3\2\2\2\u0092\u0093\7D\2\2\u0093\u0094")
        buf.write("\7;\2\2\u0094\u0097\5\f\7\2\u0095\u0097\7D\2\2\u0096\u0092")
        buf.write("\3\2\2\2\u0096\u0095\3\2\2\2\u0097\r\3\2\2\2\u0098\u0099")
        buf.write("\5\20\t\2\u0099\u009a\7<\2\2\u009a\17\3\2\2\2\u009b\u009c")
        buf.write("\7D\2\2\u009c\u009d\7;\2\2\u009d\u009e\5\20\t\2\u009e")
        buf.write("\u009f\7;\2\2\u009f\u00a0\5X-\2\u00a0\u00a8\3\2\2\2\u00a1")
        buf.write("\u00a2\7D\2\2\u00a2\u00a3\7=\2\2\u00a3\u00a4\5\22\n\2")
        buf.write("\u00a4\u00a5\7>\2\2\u00a5\u00a6\5X-\2\u00a6\u00a8\3\2")
        buf.write("\2\2\u00a7\u009b\3\2\2\2\u00a7\u00a1\3\2\2\2\u00a8\21")
        buf.write("\3\2\2\2\u00a9\u00ad\5p9\2\u00aa\u00ad\5r:\2\u00ab\u00ad")
        buf.write("\5z>\2\u00ac\u00a9\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab")
        buf.write("\3\2\2\2\u00ad\23\3\2\2\2\u00ae\u00af\7D\2\2\u00af\u00b0")
        buf.write("\7=\2\2\u00b0\u00b1\7\30\2\2\u00b1\u00b2\5n8\2\u00b2\u00b3")
        buf.write("\7\64\2\2\u00b3\u00b4\5\26\f\2\u00b4\u00b5\7\65\2\2\u00b5")
        buf.write("\u00b6\5 \21\2\u00b6\u00b7\5&\24\2\u00b7\25\3\2\2\2\u00b8")
        buf.write("\u00bb\5\30\r\2\u00b9\u00bb\3\2\2\2\u00ba\u00b8\3\2\2")
        buf.write("\2\u00ba\u00b9\3\2\2\2\u00bb\27\3\2\2\2\u00bc\u00bd\5")
        buf.write("\32\16\2\u00bd\u00be\7;\2\2\u00be\u00bf\5\30\r\2\u00bf")
        buf.write("\u00c2\3\2\2\2\u00c0\u00c2\5\32\16\2\u00c1\u00bc\3\2\2")
        buf.write("\2\u00c1\u00c0\3\2\2\2\u00c2\31\3\2\2\2\u00c3\u00c4\5")
        buf.write("\34\17\2\u00c4\u00c5\5\36\20\2\u00c5\u00c6\7D\2\2\u00c6")
        buf.write("\u00c7\7=\2\2\u00c7\u00c8\5\22\n\2\u00c8\33\3\2\2\2\u00c9")
        buf.write("\u00cc\7#\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00ca\3\2\2\2\u00cc\35\3\2\2\2\u00cd\u00d0\7 \2")
        buf.write("\2\u00ce\u00d0\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce")
        buf.write("\3\2\2\2\u00d0\37\3\2\2\2\u00d1\u00d2\7#\2\2\u00d2\u00d5")
        buf.write("\7D\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d1\3\2\2\2\u00d4")
        buf.write("\u00d3\3\2\2\2\u00d5!\3\2\2\2\u00d6\u00d7\5$\23\2\u00d7")
        buf.write("\u00d8\5\"\22\2\u00d8\u00db\3\2\2\2\u00d9\u00db\3\2\2")
        buf.write("\2\u00da\u00d6\3\2\2\2\u00da\u00d9\3\2\2\2\u00db#\3\2")
        buf.write("\2\2\u00dc\u00ea\5&\24\2\u00dd\u00ea\5\b\5\2\u00de\u00ea")
        buf.write("\5(\25\2\u00df\u00ea\5,\27\2\u00e0\u00ea\5\60\31\2\u00e1")
        buf.write("\u00ea\5\62\32\2\u00e2\u00ea\5\64\33\2\u00e3\u00ea\5\66")
        buf.write("\34\2\u00e4\u00ea\58\35\2\u00e5\u00ea\5:\36\2\u00e6\u00ea")
        buf.write("\5<\37\2\u00e7\u00ea\5> \2\u00e8\u00ea\5&\24\2\u00e9\u00dc")
        buf.write("\3\2\2\2\u00e9\u00dd\3\2\2\2\u00e9\u00de\3\2\2\2\u00e9")
        buf.write("\u00df\3\2\2\2\u00e9\u00e0\3\2\2\2\u00e9\u00e1\3\2\2\2")
        buf.write("\u00e9\u00e2\3\2\2\2\u00e9\u00e3\3\2\2\2\u00e9\u00e4\3")
        buf.write("\2\2\2\u00e9\u00e5\3\2\2\2\u00e9\u00e6\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea%\3\2\2\2\u00eb\u00ec")
        buf.write("\7\66\2\2\u00ec\u00ed\5\"\22\2\u00ed\u00ee\7\67\2\2\u00ee")
        buf.write("\'\3\2\2\2\u00ef\u00f0\5*\26\2\u00f0\u00f1\7>\2\2\u00f1")
        buf.write("\u00f2\5X-\2\u00f2\u00f3\7<\2\2\u00f3)\3\2\2\2\u00f4\u00f7")
        buf.write("\7D\2\2\u00f5\u00f7\5j\66\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f7+\3\2\2\2\u00f8\u00f9\7\31\2\2\u00f9")
        buf.write("\u00fa\7\64\2\2\u00fa\u00fb\5X-\2\u00fb\u00fc\7\65\2\2")
        buf.write("\u00fc\u00fd\5$\23\2\u00fd\u00fe\5.\30\2\u00fe-\3\2\2")
        buf.write("\2\u00ff\u0100\7\24\2\2\u0100\u0103\5$\23\2\u0101\u0103")
        buf.write("\3\2\2\2\u0102\u00ff\3\2\2\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("/\3\2\2\2\u0104\u0105\7\27\2\2\u0105\u0106\7\64\2\2\u0106")
        buf.write("\u0107\7D\2\2\u0107\u0108\7>\2\2\u0108\u0109\5X-\2\u0109")
        buf.write("\u010a\7;\2\2\u010a\u010b\5X-\2\u010b\u010c\7;\2\2\u010c")
        buf.write("\u010d\5X-\2\u010d\u010e\7\65\2\2\u010e\u010f\5$\23\2")
        buf.write("\u010f\61\3\2\2\2\u0110\u0111\7\36\2\2\u0111\u0112\7\64")
        buf.write("\2\2\u0112\u0113\5X-\2\u0113\u0114\7\65\2\2\u0114\u0115")
        buf.write("\5$\23\2\u0115\63\3\2\2\2\u0116\u0117\7\23\2\2\u0117\u0118")
        buf.write("\5&\24\2\u0118\u0119\7\36\2\2\u0119\u011a\7\64\2\2\u011a")
        buf.write("\u011b\5X-\2\u011b\u011c\7\65\2\2\u011c\u011d\7<\2\2\u011d")
        buf.write("\65\3\2\2\2\u011e\u011f\7\21\2\2\u011f\u0120\7<\2\2\u0120")
        buf.write("\67\3\2\2\2\u0121\u0122\7!\2\2\u0122\u0123\7<\2\2\u0123")
        buf.write("9\3\2\2\2\u0124\u0127\7\33\2\2\u0125\u0128\5X-\2\u0126")
        buf.write("\u0128\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0126\3\2\2\2")
        buf.write("\u0128\u0129\3\2\2\2\u0129\u012a\7<\2\2\u012a;\3\2\2\2")
        buf.write("\u012b\u012c\7D\2\2\u012c\u012d\7\64\2\2\u012d\u012e\5")
        buf.write("T+\2\u012e\u012f\7\65\2\2\u012f\u0130\7<\2\2\u0130=\3")
        buf.write("\2\2\2\u0131\u013c\5@!\2\u0132\u013c\5B\"\2\u0133\u013c")
        buf.write("\5D#\2\u0134\u013c\5F$\2\u0135\u013c\5H%\2\u0136\u013c")
        buf.write("\5J&\2\u0137\u013c\5L\'\2\u0138\u013c\5N(\2\u0139\u013c")
        buf.write("\5P)\2\u013a\u013c\5R*\2\u013b\u0131\3\2\2\2\u013b\u0132")
        buf.write("\3\2\2\2\u013b\u0133\3\2\2\2\u013b\u0134\3\2\2\2\u013b")
        buf.write("\u0135\3\2\2\2\u013b\u0136\3\2\2\2\u013b\u0137\3\2\2\2")
        buf.write("\u013b\u0138\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013a\3")
        buf.write("\2\2\2\u013c?\3\2\2\2\u013d\u013e\7\3\2\2\u013e\u013f")
        buf.write("\7\64\2\2\u013f\u0140\7\65\2\2\u0140\u0141\7<\2\2\u0141")
        buf.write("A\3\2\2\2\u0142\u0143\7\4\2\2\u0143\u0144\7\64\2\2\u0144")
        buf.write("\u0145\5X-\2\u0145\u0146\7\65\2\2\u0146\u0147\7<\2\2\u0147")
        buf.write("C\3\2\2\2\u0148\u0149\7\5\2\2\u0149\u014a\7\64\2\2\u014a")
        buf.write("\u014b\7\65\2\2\u014b\u014c\7<\2\2\u014cE\3\2\2\2\u014d")
        buf.write("\u014e\7\6\2\2\u014e\u014f\7\64\2\2\u014f\u0150\5X-\2")
        buf.write("\u0150\u0151\7\65\2\2\u0151\u0152\7<\2\2\u0152G\3\2\2")
        buf.write("\2\u0153\u0154\7\7\2\2\u0154\u0155\7\64\2\2\u0155\u0156")
        buf.write("\7\65\2\2\u0156\u0157\7<\2\2\u0157I\3\2\2\2\u0158\u0159")
        buf.write("\7\b\2\2\u0159\u015a\7\64\2\2\u015a\u015b\5X-\2\u015b")
        buf.write("\u015c\7\65\2\2\u015c\u015d\7<\2\2\u015dK\3\2\2\2\u015e")
        buf.write("\u015f\7\t\2\2\u015f\u0160\7\64\2\2\u0160\u0161\7\65\2")
        buf.write("\2\u0161\u0162\7<\2\2\u0162M\3\2\2\2\u0163\u0164\7\n\2")
        buf.write("\2\u0164\u0165\7\64\2\2\u0165\u0166\5X-\2\u0166\u0167")
        buf.write("\7\65\2\2\u0167\u0168\7<\2\2\u0168O\3\2\2\2\u0169\u016a")
        buf.write("\7\13\2\2\u016a\u016b\7\64\2\2\u016b\u016c\5T+\2\u016c")
        buf.write("\u016d\7\65\2\2\u016d\u016e\7<\2\2\u016eQ\3\2\2\2\u016f")
        buf.write("\u0170\7\f\2\2\u0170\u0171\7\64\2\2\u0171\u0172\7\65\2")
        buf.write("\2\u0172\u0173\7<\2\2\u0173S\3\2\2\2\u0174\u0177\5V,\2")
        buf.write("\u0175\u0177\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0175\3")
        buf.write("\2\2\2\u0177U\3\2\2\2\u0178\u0179\5X-\2\u0179\u017a\7")
        buf.write(";\2\2\u017a\u017b\5V,\2\u017b\u017e\3\2\2\2\u017c\u017e")
        buf.write("\5X-\2\u017d\u0178\3\2\2\2\u017d\u017c\3\2\2\2\u017eW")
        buf.write("\3\2\2\2\u017f\u0180\5Z.\2\u0180\u0181\7\63\2\2\u0181")
        buf.write("\u0182\5Z.\2\u0182\u0185\3\2\2\2\u0183\u0185\5Z.\2\u0184")
        buf.write("\u017f\3\2\2\2\u0184\u0183\3\2\2\2\u0185Y\3\2\2\2\u0186")
        buf.write("\u0187\5\\/\2\u0187\u0188\t\2\2\2\u0188\u0189\5\\/\2\u0189")
        buf.write("\u018c\3\2\2\2\u018a\u018c\5\\/\2\u018b\u0186\3\2\2\2")
        buf.write("\u018b\u018a\3\2\2\2\u018c[\3\2\2\2\u018d\u018e\b/\1\2")
        buf.write("\u018e\u018f\5^\60\2\u018f\u0195\3\2\2\2\u0190\u0191\f")
        buf.write("\4\2\2\u0191\u0192\t\3\2\2\u0192\u0194\5^\60\2\u0193\u0190")
        buf.write("\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196]\3\2\2\2\u0197\u0195\3\2\2\2\u0198")
        buf.write("\u0199\b\60\1\2\u0199\u019a\5`\61\2\u019a\u01a0\3\2\2")
        buf.write("\2\u019b\u019c\f\4\2\2\u019c\u019d\t\4\2\2\u019d\u019f")
        buf.write("\5`\61\2\u019e\u019b\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1_\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a3\u01a4\b\61\1\2\u01a4\u01a5\5b\62")
        buf.write("\2\u01a5\u01ab\3\2\2\2\u01a6\u01a7\f\4\2\2\u01a7\u01a8")
        buf.write("\t\5\2\2\u01a8\u01aa\5b\62\2\u01a9\u01a6\3\2\2\2\u01aa")
        buf.write("\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01aca\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01af\7*\2\2")
        buf.write("\u01af\u01b2\5b\62\2\u01b0\u01b2\5d\63\2\u01b1\u01ae\3")
        buf.write("\2\2\2\u01b1\u01b0\3\2\2\2\u01b2c\3\2\2\2\u01b3\u01b4")
        buf.write("\7&\2\2\u01b4\u01b7\5d\63\2\u01b5\u01b7\5f\64\2\u01b6")
        buf.write("\u01b3\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7e\3\2\2\2\u01b8")
        buf.write("\u01c2\5h\65\2\u01b9\u01c2\5j\66\2\u01ba\u01c2\5l\67\2")
        buf.write("\u01bb\u01c2\7D\2\2\u01bc\u01c2\7?\2\2\u01bd\u01c2\7@")
        buf.write("\2\2\u01be\u01c2\7\17\2\2\u01bf\u01c2\7C\2\2\u01c0\u01c2")
        buf.write("\5v<\2\u01c1\u01b8\3\2\2\2\u01c1\u01b9\3\2\2\2\u01c1\u01ba")
        buf.write("\3\2\2\2\u01c1\u01bb\3\2\2\2\u01c1\u01bc\3\2\2\2\u01c1")
        buf.write("\u01bd\3\2\2\2\u01c1\u01be\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c0\3\2\2\2\u01c2g\3\2\2\2\u01c3\u01c4\7\64\2")
        buf.write("\2\u01c4\u01c5\5X-\2\u01c5\u01c6\7\65\2\2\u01c6i\3\2\2")
        buf.write("\2\u01c7\u01c8\7D\2\2\u01c8\u01c9\78\2\2\u01c9\u01ca\5")
        buf.write("T+\2\u01ca\u01cb\79\2\2\u01cbk\3\2\2\2\u01cc\u01cd\7D")
        buf.write("\2\2\u01cd\u01ce\7\64\2\2\u01ce\u01cf\5T+\2\u01cf\u01d0")
        buf.write("\7\65\2\2\u01d0m\3\2\2\2\u01d1\u01d6\5p9\2\u01d2\u01d6")
        buf.write("\5r:\2\u01d3\u01d6\5x=\2\u01d4\u01d6\5z>\2\u01d5\u01d1")
        buf.write("\3\2\2\2\u01d5\u01d2\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6o\3\2\2\2\u01d7\u01d8\t\6\2\2\u01d8")
        buf.write("q\3\2\2\2\u01d9\u01da\7$\2\2\u01da\u01db\78\2\2\u01db")
        buf.write("\u01dc\5t;\2\u01dc\u01dd\79\2\2\u01dd\u01de\7\"\2\2\u01de")
        buf.write("\u01df\5p9\2\u01dfs\3\2\2\2\u01e0\u01e1\7?\2\2\u01e1\u01e2")
        buf.write("\7;\2\2\u01e2\u01e5\5t;\2\u01e3\u01e5\7?\2\2\u01e4\u01e0")
        buf.write("\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5u\3\2\2\2\u01e6\u01e7")
        buf.write("\7\66\2\2\u01e7\u01e8\5T+\2\u01e8\u01e9\7\67\2\2\u01e9")
        buf.write("w\3\2\2\2\u01ea\u01eb\7\37\2\2\u01eby\3\2\2\2\u01ec\u01ed")
        buf.write("\7\20\2\2\u01ed{\3\2\2\2\37\u0083\u0087\u008b\u0096\u00a7")
        buf.write("\u00ac\u00ba\u00c1\u00cb\u00cf\u00d4\u00da\u00e9\u00f6")
        buf.write("\u0102\u0127\u013b\u0176\u017d\u0184\u018b\u0195\u01a0")
        buf.write("\u01ab\u01b1\u01b6\u01c1\u01d5\u01e4")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readInteger'", "'printInteger'", "'readFloat'", 
                     "'printFloat'", "'readBoolean'", "'printBoolean'", 
                     "'readString'", "'printString'", "'super'", "'preventDefault'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'boolean'", "'do'", "'else'", "'false'", "'float'", 
                     "'for'", "'function'", "'if'", "'integer'", "'return'", 
                     "'string'", "'true'", "'while'", "'void'", "'out'", 
                     "'continue'", "'of'", "'inherit'", "'array'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "'.'", "','", 
                     "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "BOOLLIT", "AUTO", "BREAK", "BOOLEAN", 
                      "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
                      "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", 
                      "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                      "EQUAL", "NOT_EQUAL", "LT", "LE", "GT", "GE", "CONCAT", 
                      "LB", "RB", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", 
                      "SEMI", "COLON", "EQ", "INTLIT", "FLOATLIT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "STRINGLIT", "IDENTIFIER", "WS", 
                      "ERROR_CHAR" ]

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
    RULE_specialcall = 30
    RULE_readIntegerfun = 31
    RULE_printIntegerfun = 32
    RULE_readFloatfun = 33
    RULE_printFloatfun = 34
    RULE_readBooleanfun = 35
    RULE_printBooleanfun = 36
    RULE_readStringfun = 37
    RULE_printStringfun = 38
    RULE_superfun = 39
    RULE_preventDefaultfun = 40
    RULE_exprlist = 41
    RULE_exprprime = 42
    RULE_expr = 43
    RULE_expr1 = 44
    RULE_expr2 = 45
    RULE_expr3 = 46
    RULE_expr4 = 47
    RULE_expr5 = 48
    RULE_expr6 = 49
    RULE_expr7 = 50
    RULE_subexpr = 51
    RULE_arrayele = 52
    RULE_funccall = 53
    RULE_types = 54
    RULE_atomtype = 55
    RULE_arraytype = 56
    RULE_dimenslist = 57
    RULE_arraylit = 58
    RULE_voidtype = 59
    RULE_autotype = 60

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "shortvardecl", 
                   "idlist", "fullvardecl", "varinit", "vartyp", "funcdecl", 
                   "paramlist", "paramrime", "param", "paraminher", "paramout", 
                   "funcinher", "stmtlist", "stmt", "blockstmt", "assignstmt", 
                   "lhs", "ifstmt", "elsestmt", "forstmt", "whilestmt", 
                   "dowhilestmt", "breakstmt", "continuestmt", "returnstmt", 
                   "callstmt", "specialcall", "readIntegerfun", "printIntegerfun", 
                   "readFloatfun", "printFloatfun", "readBooleanfun", "printBooleanfun", 
                   "readStringfun", "printStringfun", "superfun", "preventDefaultfun", 
                   "exprlist", "exprprime", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "subexpr", "arrayele", 
                   "funccall", "types", "atomtype", "arraytype", "dimenslist", 
                   "arraylit", "voidtype", "autotype" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    BLOCK_COMMENT=11
    LINE_COMMENT=12
    BOOLLIT=13
    AUTO=14
    BREAK=15
    BOOLEAN=16
    DO=17
    ELSE=18
    FALSE=19
    FLOAT=20
    FOR=21
    FUNCTION=22
    IF=23
    INTEGER=24
    RETURN=25
    STRING=26
    TRUE=27
    WHILE=28
    VOID=29
    OUT=30
    CONTINUE=31
    OF=32
    INHERIT=33
    ARRAY=34
    ADD=35
    SUB=36
    MUL=37
    DIV=38
    MOD=39
    NOT=40
    AND=41
    OR=42
    EQUAL=43
    NOT_EQUAL=44
    LT=45
    LE=46
    GT=47
    GE=48
    CONCAT=49
    LB=50
    RB=51
    LP=52
    RP=53
    LSB=54
    RSB=55
    DOT=56
    COMMA=57
    SEMI=58
    COLON=59
    EQ=60
    INTLIT=61
    FLOATLIT=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    STRINGLIT=65
    IDENTIFIER=66
    WS=67
    ERROR_CHAR=68

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.decllist()
            self.state = 123
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = MT22Parser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.decl()
                self.state = 126
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.shortvardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortvardecl" ):
                return visitor.visitShortvardecl(self)
            else:
                return visitor.visitChildren(self)




    def shortvardecl(self):

        localctx = MT22Parser.ShortvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_shortvardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.idlist()
            self.state = 140
            self.match(MT22Parser.COLON)
            self.state = 141
            self.vartyp()
            self.state = 142
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idlist)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(MT22Parser.IDENTIFIER)
                self.state = 145
                self.match(MT22Parser.COMMA)
                self.state = 146
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFullvardecl" ):
                return visitor.visitFullvardecl(self)
            else:
                return visitor.visitChildren(self)




    def fullvardecl(self):

        localctx = MT22Parser.FullvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_fullvardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.varinit()
            self.state = 151
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarinit" ):
                return visitor.visitVarinit(self)
            else:
                return visitor.visitChildren(self)




    def varinit(self):

        localctx = MT22Parser.VarinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varinit)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(MT22Parser.IDENTIFIER)
                self.state = 154
                self.match(MT22Parser.COMMA)
                self.state = 155
                self.varinit()
                self.state = 156
                self.match(MT22Parser.COMMA)
                self.state = 157
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(MT22Parser.IDENTIFIER)
                self.state = 160
                self.match(MT22Parser.COLON)
                self.state = 161
                self.vartyp()
                self.state = 162
                self.match(MT22Parser.EQ)
                self.state = 163
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartyp" ):
                return visitor.visitVartyp(self)
            else:
                return visitor.visitChildren(self)




    def vartyp(self):

        localctx = MT22Parser.VartypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vartyp)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.atomtype()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.arraytype()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MT22Parser.IDENTIFIER)
            self.state = 173
            self.match(MT22Parser.COLON)
            self.state = 174
            self.match(MT22Parser.FUNCTION)
            self.state = 175
            self.types()
            self.state = 176
            self.match(MT22Parser.LB)
            self.state = 177
            self.paramlist()
            self.state = 178
            self.match(MT22Parser.RB)
            self.state = 179
            self.funcinher()
            self.state = 180
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MT22Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramlist)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamrime" ):
                return visitor.visitParamrime(self)
            else:
                return visitor.visitChildren(self)




    def paramrime(self):

        localctx = MT22Parser.ParamrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramrime)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.param()
                self.state = 187
                self.match(MT22Parser.COMMA)
                self.state = 188
                self.paramrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.paraminher()
            self.state = 194
            self.paramout()
            self.state = 195
            self.match(MT22Parser.IDENTIFIER)
            self.state = 196
            self.match(MT22Parser.COLON)
            self.state = 197
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaminher" ):
                return visitor.visitParaminher(self)
            else:
                return visitor.visitChildren(self)




    def paraminher(self):

        localctx = MT22Parser.ParaminherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paraminher)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamout" ):
                return visitor.visitParamout(self)
            else:
                return visitor.visitChildren(self)




    def paramout(self):

        localctx = MT22Parser.ParamoutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramout)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncinher" ):
                return visitor.visitFuncinher(self)
            else:
                return visitor.visitChildren(self)




    def funcinher(self):

        localctx = MT22Parser.FuncinherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funcinher)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(MT22Parser.INHERIT)
                self.state = 208
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = MT22Parser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmtlist)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0, MT22Parser.T__1, MT22Parser.T__2, MT22Parser.T__3, MT22Parser.T__4, MT22Parser.T__5, MT22Parser.T__6, MT22Parser.T__7, MT22Parser.T__8, MT22Parser.T__9, MT22Parser.BREAK, MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.CONTINUE, MT22Parser.LP, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.stmt()
                self.state = 213
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


        def specialcall(self):
            return self.getTypedRuleContext(MT22Parser.SpecialcallContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.assignstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 221
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 223
                self.whilestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 224
                self.dowhilestmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 225
                self.breakstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 226
                self.continuestmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 227
                self.returnstmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 228
                self.callstmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 229
                self.specialcall()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 230
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = MT22Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MT22Parser.LP)
            self.state = 234
            self.stmtlist()
            self.state = 235
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.lhs()
            self.state = 238
            self.match(MT22Parser.EQ)
            self.state = 239
            self.expr()
            self.state = 240
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lhs)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MT22Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(MT22Parser.IF)
            self.state = 247
            self.match(MT22Parser.LB)
            self.state = 248
            self.expr()
            self.state = 249
            self.match(MT22Parser.RB)
            self.state = 250
            self.stmt()
            self.state = 251
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = MT22Parser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elsestmt)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(MT22Parser.ELSE)
                self.state = 254
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MT22Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(MT22Parser.FOR)
            self.state = 259
            self.match(MT22Parser.LB)
            self.state = 260
            self.match(MT22Parser.IDENTIFIER)
            self.state = 261
            self.match(MT22Parser.EQ)
            self.state = 262
            self.expr()
            self.state = 263
            self.match(MT22Parser.COMMA)
            self.state = 264
            self.expr()
            self.state = 265
            self.match(MT22Parser.COMMA)
            self.state = 266
            self.expr()
            self.state = 267
            self.match(MT22Parser.RB)
            self.state = 268
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = MT22Parser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(MT22Parser.WHILE)
            self.state = 271
            self.match(MT22Parser.LB)
            self.state = 272
            self.expr()
            self.state = 273
            self.match(MT22Parser.RB)
            self.state = 274
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhilestmt" ):
                return visitor.visitDowhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhilestmt(self):

        localctx = MT22Parser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(MT22Parser.DO)
            self.state = 277
            self.blockstmt()
            self.state = 278
            self.match(MT22Parser.WHILE)
            self.state = 279
            self.match(MT22Parser.LB)
            self.state = 280
            self.expr()
            self.state = 281
            self.match(MT22Parser.RB)
            self.state = 282
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MT22Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(MT22Parser.BREAK)
            self.state = 285
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MT22Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(MT22Parser.CONTINUE)
            self.state = 288
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MT22Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(MT22Parser.RETURN)
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLLIT, MT22Parser.SUB, MT22Parser.NOT, MT22Parser.LB, MT22Parser.LP, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.state = 291
                self.expr()
                pass
            elif token in [MT22Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 295
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MT22Parser.IDENTIFIER)
            self.state = 298
            self.match(MT22Parser.LB)
            self.state = 299
            self.exprlist()
            self.state = 300
            self.match(MT22Parser.RB)
            self.state = 301
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readIntegerfun(self):
            return self.getTypedRuleContext(MT22Parser.ReadIntegerfunContext,0)


        def printIntegerfun(self):
            return self.getTypedRuleContext(MT22Parser.PrintIntegerfunContext,0)


        def readFloatfun(self):
            return self.getTypedRuleContext(MT22Parser.ReadFloatfunContext,0)


        def printFloatfun(self):
            return self.getTypedRuleContext(MT22Parser.PrintFloatfunContext,0)


        def readBooleanfun(self):
            return self.getTypedRuleContext(MT22Parser.ReadBooleanfunContext,0)


        def printBooleanfun(self):
            return self.getTypedRuleContext(MT22Parser.PrintBooleanfunContext,0)


        def readStringfun(self):
            return self.getTypedRuleContext(MT22Parser.ReadStringfunContext,0)


        def printStringfun(self):
            return self.getTypedRuleContext(MT22Parser.PrintStringfunContext,0)


        def superfun(self):
            return self.getTypedRuleContext(MT22Parser.SuperfunContext,0)


        def preventDefaultfun(self):
            return self.getTypedRuleContext(MT22Parser.PreventDefaultfunContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_specialcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecialcall" ):
                return visitor.visitSpecialcall(self)
            else:
                return visitor.visitChildren(self)




    def specialcall(self):

        localctx = MT22Parser.SpecialcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_specialcall)
        try:
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.readIntegerfun()
                pass
            elif token in [MT22Parser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.printIntegerfun()
                pass
            elif token in [MT22Parser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 305
                self.readFloatfun()
                pass
            elif token in [MT22Parser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 306
                self.printFloatfun()
                pass
            elif token in [MT22Parser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 307
                self.readBooleanfun()
                pass
            elif token in [MT22Parser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 308
                self.printBooleanfun()
                pass
            elif token in [MT22Parser.T__6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 309
                self.readStringfun()
                pass
            elif token in [MT22Parser.T__7]:
                self.enterOuterAlt(localctx, 8)
                self.state = 310
                self.printStringfun()
                pass
            elif token in [MT22Parser.T__8]:
                self.enterOuterAlt(localctx, 9)
                self.state = 311
                self.superfun()
                pass
            elif token in [MT22Parser.T__9]:
                self.enterOuterAlt(localctx, 10)
                self.state = 312
                self.preventDefaultfun()
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


    class ReadIntegerfunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readIntegerfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadIntegerfun" ):
                return visitor.visitReadIntegerfun(self)
            else:
                return visitor.visitChildren(self)




    def readIntegerfun(self):

        localctx = MT22Parser.ReadIntegerfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_readIntegerfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(MT22Parser.T__0)
            self.state = 316
            self.match(MT22Parser.LB)
            self.state = 317
            self.match(MT22Parser.RB)
            self.state = 318
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintIntegerfunContext(ParserRuleContext):
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printIntegerfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintIntegerfun" ):
                return visitor.visitPrintIntegerfun(self)
            else:
                return visitor.visitChildren(self)




    def printIntegerfun(self):

        localctx = MT22Parser.PrintIntegerfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_printIntegerfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(MT22Parser.T__1)
            self.state = 321
            self.match(MT22Parser.LB)
            self.state = 322
            self.expr()
            self.state = 323
            self.match(MT22Parser.RB)
            self.state = 324
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadFloatfunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readFloatfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadFloatfun" ):
                return visitor.visitReadFloatfun(self)
            else:
                return visitor.visitChildren(self)




    def readFloatfun(self):

        localctx = MT22Parser.ReadFloatfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_readFloatfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(MT22Parser.T__2)
            self.state = 327
            self.match(MT22Parser.LB)
            self.state = 328
            self.match(MT22Parser.RB)
            self.state = 329
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintFloatfunContext(ParserRuleContext):
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printFloatfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintFloatfun" ):
                return visitor.visitPrintFloatfun(self)
            else:
                return visitor.visitChildren(self)




    def printFloatfun(self):

        localctx = MT22Parser.PrintFloatfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_printFloatfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MT22Parser.T__3)
            self.state = 332
            self.match(MT22Parser.LB)
            self.state = 333
            self.expr()
            self.state = 334
            self.match(MT22Parser.RB)
            self.state = 335
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadBooleanfunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readBooleanfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadBooleanfun" ):
                return visitor.visitReadBooleanfun(self)
            else:
                return visitor.visitChildren(self)




    def readBooleanfun(self):

        localctx = MT22Parser.ReadBooleanfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_readBooleanfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(MT22Parser.T__4)
            self.state = 338
            self.match(MT22Parser.LB)
            self.state = 339
            self.match(MT22Parser.RB)
            self.state = 340
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintBooleanfunContext(ParserRuleContext):
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printBooleanfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintBooleanfun" ):
                return visitor.visitPrintBooleanfun(self)
            else:
                return visitor.visitChildren(self)




    def printBooleanfun(self):

        localctx = MT22Parser.PrintBooleanfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_printBooleanfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(MT22Parser.T__5)
            self.state = 343
            self.match(MT22Parser.LB)
            self.state = 344
            self.expr()
            self.state = 345
            self.match(MT22Parser.RB)
            self.state = 346
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStringfunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readStringfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStringfun" ):
                return visitor.visitReadStringfun(self)
            else:
                return visitor.visitChildren(self)




    def readStringfun(self):

        localctx = MT22Parser.ReadStringfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_readStringfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(MT22Parser.T__6)
            self.state = 349
            self.match(MT22Parser.LB)
            self.state = 350
            self.match(MT22Parser.RB)
            self.state = 351
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStringfunContext(ParserRuleContext):
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

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printStringfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStringfun" ):
                return visitor.visitPrintStringfun(self)
            else:
                return visitor.visitChildren(self)




    def printStringfun(self):

        localctx = MT22Parser.PrintStringfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_printStringfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(MT22Parser.T__7)
            self.state = 354
            self.match(MT22Parser.LB)
            self.state = 355
            self.expr()
            self.state = 356
            self.match(MT22Parser.RB)
            self.state = 357
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperfunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_superfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperfun" ):
                return visitor.visitSuperfun(self)
            else:
                return visitor.visitChildren(self)




    def superfun(self):

        localctx = MT22Parser.SuperfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_superfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(MT22Parser.T__8)
            self.state = 360
            self.match(MT22Parser.LB)
            self.state = 361
            self.exprlist()
            self.state = 362
            self.match(MT22Parser.RB)
            self.state = 363
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreventDefaultfunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_preventDefaultfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreventDefaultfun" ):
                return visitor.visitPreventDefaultfun(self)
            else:
                return visitor.visitChildren(self)




    def preventDefaultfun(self):

        localctx = MT22Parser.PreventDefaultfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_preventDefaultfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MT22Parser.T__9)
            self.state = 366
            self.match(MT22Parser.LB)
            self.state = 367
            self.match(MT22Parser.RB)
            self.state = 368
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exprlist)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLLIT, MT22Parser.SUB, MT22Parser.NOT, MT22Parser.LB, MT22Parser.LP, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = MT22Parser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exprprime)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.expr()
                self.state = 375
                self.match(MT22Parser.COMMA)
                self.state = 376
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.expr1()
                self.state = 382
                self.match(MT22Parser.CONCAT)
                self.state = 383
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.expr2(0)
                self.state = 389
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOT_EQUAL) | (1 << MT22Parser.LT) | (1 << MT22Parser.LE) | (1 << MT22Parser.GT) | (1 << MT22Parser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 390
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 398
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 399
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 400
                    self.expr3(0) 
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 409
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 410
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 411
                    self.expr4(0) 
                self.state = 416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 420
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 421
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 422
                    self.expr5() 
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr5)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(MT22Parser.NOT)
                self.state = 429
                self.expr5()
                pass
            elif token in [MT22Parser.BOOLLIT, MT22Parser.SUB, MT22Parser.LB, MT22Parser.LP, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr6)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(MT22Parser.SUB)
                self.state = 434
                self.expr6()
                pass
            elif token in [MT22Parser.BOOLLIT, MT22Parser.LB, MT22Parser.LP, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr7)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.subexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.arrayele()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 440
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 441
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 442
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 443
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 444
                self.match(MT22Parser.BOOLLIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 445
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 446
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = MT22Parser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(MT22Parser.LB)
            self.state = 450
            self.expr()
            self.state = 451
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayele" ):
                return visitor.visitArrayele(self)
            else:
                return visitor.visitChildren(self)




    def arrayele(self):

        localctx = MT22Parser.ArrayeleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_arrayele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(MT22Parser.IDENTIFIER)
            self.state = 454
            self.match(MT22Parser.LSB)
            self.state = 455
            self.exprlist()
            self.state = 456
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MT22Parser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(MT22Parser.IDENTIFIER)
            self.state = 459
            self.match(MT22Parser.LB)
            self.state = 460
            self.exprlist()
            self.state = 461
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MT22Parser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_types)
        try:
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.atomtype()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.arraytype()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 465
                self.voidtype()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 466
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomtype" ):
                return visitor.visitAtomtype(self)
            else:
                return visitor.visitChildren(self)




    def atomtype(self):

        localctx = MT22Parser.AtomtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_atomtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = MT22Parser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(MT22Parser.ARRAY)
            self.state = 472
            self.match(MT22Parser.LSB)
            self.state = 473
            self.dimenslist()
            self.state = 474
            self.match(MT22Parser.RSB)
            self.state = 475
            self.match(MT22Parser.OF)
            self.state = 476
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimenslist" ):
                return visitor.visitDimenslist(self)
            else:
                return visitor.visitChildren(self)




    def dimenslist(self):

        localctx = MT22Parser.DimenslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_dimenslist)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(MT22Parser.INTLIT)
                self.state = 479
                self.match(MT22Parser.COMMA)
                self.state = 480
                self.dimenslist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = MT22Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(MT22Parser.LP)
            self.state = 485
            self.exprlist()
            self.state = 486
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidtype" ):
                return visitor.visitVoidtype(self)
            else:
                return visitor.visitChildren(self)




    def voidtype(self):

        localctx = MT22Parser.VoidtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_voidtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAutotype" ):
                return visitor.visitAutotype(self)
            else:
                return visitor.visitChildren(self)




    def autotype(self):

        localctx = MT22Parser.AutotypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_autotype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
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
        self._predicates[45] = self.expr2_sempred
        self._predicates[46] = self.expr3_sempred
        self._predicates[47] = self.expr4_sempred
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
         




