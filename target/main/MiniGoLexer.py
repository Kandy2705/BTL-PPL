# Generated from main/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u0204\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\78\u0167\n8\f8\168\u016a\13")
        buf.write("8\39\69\u016d\n9\r9\169\u016e\39\39\79\u0173\n9\f9\16")
        buf.write("9\u0176\139\39\39\59\u017a\n9\39\69\u017d\n9\r9\169\u017e")
        buf.write("\59\u0181\n9\3:\3:\3:\3:\5:\u0187\n:\3;\3;\3;\6;\u018c")
        buf.write("\n;\r;\16;\u018d\3;\5;\u0191\n;\3<\3<\3<\6<\u0196\n<\r")
        buf.write("<\16<\u0197\3<\3<\3=\3=\3=\6=\u019f\n=\r=\16=\u01a0\3")
        buf.write("=\3=\3>\3>\3>\6>\u01a8\n>\r>\16>\u01a9\3>\3>\3?\3?\7?")
        buf.write("\u01b0\n?\f?\16?\u01b3\13?\3?\3?\3?\3@\3@\5@\u01ba\n@")
        buf.write("\3A\3A\3A\3B\3B\3B\3C\3C\5C\u01c4\nC\3D\3D\3D\3D\3D\7")
        buf.write("D\u01cb\nD\fD\16D\u01ce\13D\3D\3D\3D\3D\3D\3E\3E\3E\3")
        buf.write("E\7E\u01d9\nE\fE\16E\u01dc\13E\3E\3E\3F\6F\u01e1\nF\r")
        buf.write("F\16F\u01e2\3G\6G\u01e6\nG\rG\16G\u01e7\3G\3G\3H\3H\3")
        buf.write("H\3I\3I\7I\u01f1\nI\fI\16I\u01f4\13I\3I\5I\u01f7\nI\3")
        buf.write("I\3I\3J\3J\7J\u01fd\nJ\fJ\16J\u0200\13J\3J\3J\3J\3\u01cc")
        buf.write("\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177\2\u0081\2\u0083\2\u0085A\u0087B\u0089")
        buf.write("C\u008bD\u008dE\u008fF\u0091G\u0093H\3\2\24\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\3\2\63;\3\2\62")
        buf.write("\62\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;")
        buf.write("CHch\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\4\2\f\f\17\17\5\2")
        buf.write("\13\13\16\16\"\"\4\3\f\f\17\17\2\u0218\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u0099\3\2\2")
        buf.write("\2\7\u00a3\3\2\2\2\t\u00a5\3\2\2\2\13\u00a8\3\2\2\2\r")
        buf.write("\u00ad\3\2\2\2\17\u00b1\3\2\2\2\21\u00b8\3\2\2\2\23\u00bd")
        buf.write("\3\2\2\2\25\u00c2\3\2\2\2\27\u00c9\3\2\2\2\31\u00d3\3")
        buf.write("\2\2\2\33\u00da\3\2\2\2\35\u00de\3\2\2\2\37\u00e4\3\2")
        buf.write("\2\2!\u00ec\3\2\2\2#\u00f2\3\2\2\2%\u00f6\3\2\2\2\'\u00ff")
        buf.write("\3\2\2\2)\u0105\3\2\2\2+\u010b\3\2\2\2-\u010f\3\2\2\2")
        buf.write("/\u0114\3\2\2\2\61\u011a\3\2\2\2\63\u011c\3\2\2\2\65\u011f")
        buf.write("\3\2\2\2\67\u0121\3\2\2\29\u0123\3\2\2\2;\u0126\3\2\2")
        buf.write("\2=\u0128\3\2\2\2?\u012b\3\2\2\2A\u012e\3\2\2\2C\u0131")
        buf.write("\3\2\2\2E\u0133\3\2\2\2G\u0136\3\2\2\2I\u0139\3\2\2\2")
        buf.write("K\u013c\3\2\2\2M\u013f\3\2\2\2O\u0142\3\2\2\2Q\u0145\3")
        buf.write("\2\2\2S\u0148\3\2\2\2U\u014a\3\2\2\2W\u014c\3\2\2\2Y\u014e")
        buf.write("\3\2\2\2[\u0150\3\2\2\2]\u0152\3\2\2\2_\u0154\3\2\2\2")
        buf.write("a\u0156\3\2\2\2c\u0158\3\2\2\2e\u015a\3\2\2\2g\u015c\3")
        buf.write("\2\2\2i\u015e\3\2\2\2k\u0160\3\2\2\2m\u0162\3\2\2\2o\u0164")
        buf.write("\3\2\2\2q\u016c\3\2\2\2s\u0186\3\2\2\2u\u0190\3\2\2\2")
        buf.write("w\u0192\3\2\2\2y\u019b\3\2\2\2{\u01a4\3\2\2\2}\u01ad\3")
        buf.write("\2\2\2\177\u01b9\3\2\2\2\u0081\u01bb\3\2\2\2\u0083\u01be")
        buf.write("\3\2\2\2\u0085\u01c3\3\2\2\2\u0087\u01c5\3\2\2\2\u0089")
        buf.write("\u01d4\3\2\2\2\u008b\u01e0\3\2\2\2\u008d\u01e5\3\2\2\2")
        buf.write("\u008f\u01eb\3\2\2\2\u0091\u01ee\3\2\2\2\u0093\u01fa\3")
        buf.write("\2\2\2\u0095\u0096\7c\2\2\u0096\u0097\7t\2\2\u0097\u0098")
        buf.write("\7t\2\2\u0098\4\3\2\2\2\u0099\u009a\7o\2\2\u009a\u009b")
        buf.write("\7w\2\2\u009b\u009c\7n\2\2\u009c\u009d\7v\2\2\u009d\u009e")
        buf.write("\7k\2\2\u009e\u009f\7\"\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\u00a2\7t\2\2\u00a2\6\3\2\2\2\u00a3\u00a4")
        buf.write("\7a\2\2\u00a4\b\3\2\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7h\2\2\u00a7\n\3\2\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa")
        buf.write("\7n\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac\7g\2\2\u00ac\f")
        buf.write("\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7t\2\2\u00b0\16\3\2\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7w\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\u00b7\7p\2\2\u00b7\20\3\2\2\2\u00b8\u00b9")
        buf.write("\7h\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc")
        buf.write("\7e\2\2\u00bc\22\3\2\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7{\2\2\u00bf\u00c0\7r\2\2\u00c0\u00c1\7g\2\2\u00c1\24")
        buf.write("\3\2\2\2\u00c2\u00c3\7u\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5")
        buf.write("\7t\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\26\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce")
        buf.write("\7t\2\2\u00ce\u00cf\7h\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1")
        buf.write("\7e\2\2\u00d1\u00d2\7g\2\2\u00d2\30\3\2\2\2\u00d3\u00d4")
        buf.write("\7u\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7")
        buf.write("\7k\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7i\2\2\u00d9\32")
        buf.write("\3\2\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\34\3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0")
        buf.write("\7n\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\36\3\2\2\2\u00e4\u00e5\7d\2\2\u00e5\u00e6")
        buf.write("\7q\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9")
        buf.write("\7g\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7p\2\2\u00eb \3")
        buf.write("\2\2\2\u00ec\u00ed\7e\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef")
        buf.write("\7p\2\2\u00ef\u00f0\7u\2\2\u00f0\u00f1\7v\2\2\u00f1\"")
        buf.write("\3\2\2\2\u00f2\u00f3\7x\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5")
        buf.write("\7t\2\2\u00f5$\3\2\2\2\u00f6\u00f7\7e\2\2\u00f7\u00f8")
        buf.write("\7q\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7k\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe")
        buf.write("\7g\2\2\u00fe&\3\2\2\2\u00ff\u0100\7d\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7g\2\2\u0102\u0103\7c\2\2\u0103\u0104")
        buf.write("\7m\2\2\u0104(\3\2\2\2\u0105\u0106\7t\2\2\u0106\u0107")
        buf.write("\7c\2\2\u0107\u0108\7p\2\2\u0108\u0109\7i\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a*\3\2\2\2\u010b\u010c\7p\2\2\u010c\u010d")
        buf.write("\7k\2\2\u010d\u010e\7n\2\2\u010e,\3\2\2\2\u010f\u0110")
        buf.write("\7v\2\2\u0110\u0111\7t\2\2\u0111\u0112\7w\2\2\u0112\u0113")
        buf.write("\7g\2\2\u0113.\3\2\2\2\u0114\u0115\7h\2\2\u0115\u0116")
        buf.write("\7c\2\2\u0116\u0117\7n\2\2\u0117\u0118\7u\2\2\u0118\u0119")
        buf.write("\7g\2\2\u0119\60\3\2\2\2\u011a\u011b\7\60\2\2\u011b\62")
        buf.write("\3\2\2\2\u011c\u011d\7<\2\2\u011d\u011e\7?\2\2\u011e\64")
        buf.write("\3\2\2\2\u011f\u0120\7<\2\2\u0120\66\3\2\2\2\u0121\u0122")
        buf.write("\7>\2\2\u01228\3\2\2\2\u0123\u0124\7>\2\2\u0124\u0125")
        buf.write("\7?\2\2\u0125:\3\2\2\2\u0126\u0127\7@\2\2\u0127<\3\2\2")
        buf.write("\2\u0128\u0129\7@\2\2\u0129\u012a\7?\2\2\u012a>\3\2\2")
        buf.write("\2\u012b\u012c\7?\2\2\u012c\u012d\7?\2\2\u012d@\3\2\2")
        buf.write("\2\u012e\u012f\7#\2\2\u012f\u0130\7?\2\2\u0130B\3\2\2")
        buf.write("\2\u0131\u0132\7?\2\2\u0132D\3\2\2\2\u0133\u0134\7-\2")
        buf.write("\2\u0134\u0135\7?\2\2\u0135F\3\2\2\2\u0136\u0137\7/\2")
        buf.write("\2\u0137\u0138\7?\2\2\u0138H\3\2\2\2\u0139\u013a\7,\2")
        buf.write("\2\u013a\u013b\7?\2\2\u013bJ\3\2\2\2\u013c\u013d\7\61")
        buf.write("\2\2\u013d\u013e\7?\2\2\u013eL\3\2\2\2\u013f\u0140\7\'")
        buf.write("\2\2\u0140\u0141\7?\2\2\u0141N\3\2\2\2\u0142\u0143\7(")
        buf.write("\2\2\u0143\u0144\7(\2\2\u0144P\3\2\2\2\u0145\u0146\7~")
        buf.write("\2\2\u0146\u0147\7~\2\2\u0147R\3\2\2\2\u0148\u0149\7#")
        buf.write("\2\2\u0149T\3\2\2\2\u014a\u014b\7-\2\2\u014bV\3\2\2\2")
        buf.write("\u014c\u014d\7/\2\2\u014dX\3\2\2\2\u014e\u014f\7,\2\2")
        buf.write("\u014fZ\3\2\2\2\u0150\u0151\7\61\2\2\u0151\\\3\2\2\2\u0152")
        buf.write("\u0153\7\'\2\2\u0153^\3\2\2\2\u0154\u0155\7*\2\2\u0155")
        buf.write("`\3\2\2\2\u0156\u0157\7+\2\2\u0157b\3\2\2\2\u0158\u0159")
        buf.write("\7}\2\2\u0159d\3\2\2\2\u015a\u015b\7\177\2\2\u015bf\3")
        buf.write("\2\2\2\u015c\u015d\7]\2\2\u015dh\3\2\2\2\u015e\u015f\7")
        buf.write("_\2\2\u015fj\3\2\2\2\u0160\u0161\7=\2\2\u0161l\3\2\2\2")
        buf.write("\u0162\u0163\7.\2\2\u0163n\3\2\2\2\u0164\u0168\t\2\2\2")
        buf.write("\u0165\u0167\t\3\2\2\u0166\u0165\3\2\2\2\u0167\u016a\3")
        buf.write("\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169p")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016d\t\4\2\2\u016c")
        buf.write("\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016c\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0174\5")
        buf.write("\61\31\2\u0171\u0173\t\4\2\2\u0172\u0171\3\2\2\2\u0173")
        buf.write("\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0180\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0179\t")
        buf.write("\5\2\2\u0178\u017a\t\6\2\2\u0179\u0178\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a\u017c\3\2\2\2\u017b\u017d\t\4\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f\u0181\3\2\2\2\u0180\u0177\3")
        buf.write("\2\2\2\u0180\u0181\3\2\2\2\u0181r\3\2\2\2\u0182\u0187")
        buf.write("\5u;\2\u0183\u0187\5w<\2\u0184\u0187\5y=\2\u0185\u0187")
        buf.write("\5{>\2\u0186\u0182\3\2\2\2\u0186\u0183\3\2\2\2\u0186\u0184")
        buf.write("\3\2\2\2\u0186\u0185\3\2\2\2\u0187t\3\2\2\2\u0188\u0191")
        buf.write("\t\4\2\2\u0189\u018b\t\7\2\2\u018a\u018c\t\4\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b\3\2\2\2")
        buf.write("\u018d\u018e\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0191\b")
        buf.write(";\2\2\u0190\u0188\3\2\2\2\u0190\u0189\3\2\2\2\u0191v\3")
        buf.write("\2\2\2\u0192\u0193\t\b\2\2\u0193\u0195\t\t\2\2\u0194\u0196")
        buf.write("\t\n\2\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019a\b<\3\2\u019ax\3\2\2\2\u019b\u019c\t\b\2\2")
        buf.write("\u019c\u019e\t\13\2\2\u019d\u019f\t\f\2\2\u019e\u019d")
        buf.write("\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\b=\4\2")
        buf.write("\u01a3z\3\2\2\2\u01a4\u01a5\t\b\2\2\u01a5\u01a7\t\r\2")
        buf.write("\2\u01a6\u01a8\t\16\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01a9")
        buf.write("\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01ac\b>\5\2\u01ac|\3\2\2\2\u01ad")
        buf.write("\u01b1\7$\2\2\u01ae\u01b0\5\177@\2\u01af\u01ae\3\2\2\2")
        buf.write("\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3")
        buf.write("\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5")
        buf.write("\7$\2\2\u01b5\u01b6\b?\6\2\u01b6~\3\2\2\2\u01b7\u01ba")
        buf.write("\5\u0081A\2\u01b8\u01ba\n\17\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01b8\3\2\2\2\u01ba\u0080\3\2\2\2\u01bb\u01bc\7^\2\2")
        buf.write("\u01bc\u01bd\t\20\2\2\u01bd\u0082\3\2\2\2\u01be\u01bf")
        buf.write("\7^\2\2\u01bf\u01c0\n\20\2\2\u01c0\u0084\3\2\2\2\u01c1")
        buf.write("\u01c4\5-\27\2\u01c2\u01c4\5/\30\2\u01c3\u01c1\3\2\2\2")
        buf.write("\u01c3\u01c2\3\2\2\2\u01c4\u0086\3\2\2\2\u01c5\u01c6\7")
        buf.write("\61\2\2\u01c6\u01c7\7,\2\2\u01c7\u01cc\3\2\2\2\u01c8\u01cb")
        buf.write("\5\u0087D\2\u01c9\u01cb\13\2\2\2\u01ca\u01c8\3\2\2\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01cd\3\2\2\2")
        buf.write("\u01cc\u01ca\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc\3")
        buf.write("\2\2\2\u01cf\u01d0\7,\2\2\u01d0\u01d1\7\61\2\2\u01d1\u01d2")
        buf.write("\3\2\2\2\u01d2\u01d3\bD\7\2\u01d3\u0088\3\2\2\2\u01d4")
        buf.write("\u01d5\7\61\2\2\u01d5\u01d6\7\61\2\2\u01d6\u01da\3\2\2")
        buf.write("\2\u01d7\u01d9\n\21\2\2\u01d8\u01d7\3\2\2\2\u01d9\u01dc")
        buf.write("\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db")
        buf.write("\u01dd\3\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01de\bE\7\2")
        buf.write("\u01de\u008a\3\2\2\2\u01df\u01e1\t\21\2\2\u01e0\u01df")
        buf.write("\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e3\3\2\2\2\u01e3\u008c\3\2\2\2\u01e4\u01e6\t\22\2")
        buf.write("\2\u01e5\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e5")
        buf.write("\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9")
        buf.write("\u01ea\bG\7\2\u01ea\u008e\3\2\2\2\u01eb\u01ec\13\2\2\2")
        buf.write("\u01ec\u01ed\bH\b\2\u01ed\u0090\3\2\2\2\u01ee\u01f2\7")
        buf.write("$\2\2\u01ef\u01f1\5\177@\2\u01f0\u01ef\3\2\2\2\u01f1\u01f4")
        buf.write("\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write("\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f7\t\23\2")
        buf.write("\2\u01f6\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9")
        buf.write("\bI\t\2\u01f9\u0092\3\2\2\2\u01fa\u01fe\7$\2\2\u01fb\u01fd")
        buf.write("\5\177@\2\u01fc\u01fb\3\2\2\2\u01fd\u0200\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0201\3\2\2\2")
        buf.write("\u0200\u01fe\3\2\2\2\u0201\u0202\5\u0083B\2\u0202\u0203")
        buf.write("\bJ\n\2\u0203\u0094\3\2\2\2\32\2\u0168\u016e\u0174\u0179")
        buf.write("\u017e\u0180\u0186\u018d\u0190\u0197\u01a0\u01a9\u01b1")
        buf.write("\u01b9\u01c3\u01ca\u01cc\u01da\u01e2\u01e7\u01f2\u01f6")
        buf.write("\u01fe\13\3;\2\3<\3\3=\4\3>\5\3?\6\b\2\2\3H\7\3I\b\3J")
        buf.write("\t")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    IF = 4
    ELSE = 5
    FOR = 6
    RETURN = 7
    FUNC = 8
    TYPE = 9
    STRUCT = 10
    INTERFACE = 11
    STRING = 12
    INT = 13
    FLOAT = 14
    BOOLEAN = 15
    CONST = 16
    VAR = 17
    CONTINUE = 18
    BREAK = 19
    RANGE = 20
    NIL = 21
    TRUE = 22
    FALSE = 23
    DOT = 24
    COLONASSIGN = 25
    COLON = 26
    LT = 27
    LE = 28
    GT = 29
    GE = 30
    EQ = 31
    NE = 32
    ASSIGN = 33
    ADD_ASSIGN = 34
    SUB_ASSIGN = 35
    MUL_ASSIGN = 36
    DIV_ASSIGN = 37
    MOD_ASSIGN = 38
    AND = 39
    OR = 40
    NOT = 41
    ADD = 42
    SUB = 43
    MUL = 44
    DIV = 45
    MOD = 46
    LPAREN = 47
    RPAREN = 48
    LBRACE = 49
    RBRACE = 50
    LBRACKET = 51
    RBRACKET = 52
    SEMICOLON = 53
    COMMA = 54
    ID = 55
    FLOAT_LIT = 56
    INTEGER_LIT = 57
    INT_DEC = 58
    INT_BIN = 59
    INT_OCT = 60
    INT_HEX = 61
    STRING_LIT = 62
    BOOLEAN_LIT = 63
    COMMENTS = 64
    COMMENTS_LINE = 65
    NEWLINE = 66
    WS = 67
    ERROR_CHAR = 68
    UNCLOSE_STRING = 69
    ILLEGAL_ESCAPE = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'arr'", "'multi arr'", "'_'", "'if'", "'else'", "'for'", "'return'", 
            "'func'", "'type'", "'struct'", "'interface'", "'string'", "'int'", 
            "'float'", "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
            "'range'", "'nil'", "'true'", "'false'", "'.'", "':='", "':'", 
            "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", "'='", "'+='", 
            "'-='", "'*='", "'/='", "'%='", "'&&'", "'||'", "'!'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "DOT", "COLONASSIGN", 
            "COLON", "LT", "LE", "GT", "GE", "EQ", "NE", "ASSIGN", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND", 
            "OR", "NOT", "ADD", "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", 
            "ID", "FLOAT_LIT", "INTEGER_LIT", "INT_DEC", "INT_BIN", "INT_OCT", 
            "INT_HEX", "STRING_LIT", "BOOLEAN_LIT", "COMMENTS", "COMMENTS_LINE", 
            "NEWLINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "TRUE", "FALSE", "DOT", "COLONASSIGN", 
                  "COLON", "LT", "LE", "GT", "GE", "EQ", "NE", "ASSIGN", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "AND", "OR", "NOT", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", "ID", "FLOAT_LIT", 
                  "INTEGER_LIT", "INT_DEC", "INT_BIN", "INT_OCT", "INT_HEX", 
                  "STRING_LIT", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "BOOLEAN_LIT", 
                  "COMMENTS", "COMMENTS_LINE", "NEWLINE", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[57] = self.INT_DEC_action 
            actions[58] = self.INT_BIN_action 
            actions[59] = self.INT_OCT_action 
            actions[60] = self.INT_HEX_action 
            actions[61] = self.STRING_LIT_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_DEC_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = str(int(self.text, 10))

     

    def INT_BIN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = str(int(self.text, 2))

     

    def INT_OCT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = str(int(self.text, 8))

     

    def INT_HEX_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                self.text = str(int(self.text, 16))

     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[1:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

                raise IllegalEscape(self.text[1:])

     


