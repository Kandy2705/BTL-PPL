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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u01f4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3")
        buf.write("#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\78\u0165\n8\f8\168\u0168\138\39\39\3")
        buf.write("9\79\u016d\n9\f9\169\u0170\139\39\39\59\u0174\n9\39\5")
        buf.write("9\u0177\n9\3:\3:\3:\6:\u017c\n:\r:\16:\u017d\3:\5:\u0181")
        buf.write("\n:\3;\3;\3;\6;\u0186\n;\r;\16;\u0187\3;\3;\3<\3<\3<\6")
        buf.write("<\u018f\n<\r<\16<\u0190\3<\3<\3=\3=\3=\6=\u0198\n=\r=")
        buf.write("\16=\u0199\3=\3=\3>\3>\7>\u01a0\n>\f>\16>\u01a3\13>\3")
        buf.write(">\3>\3>\3?\3?\5?\u01aa\n?\3@\3@\3@\3A\3A\3A\3B\3B\5B\u01b4")
        buf.write("\nB\3C\3C\3C\3C\3C\7C\u01bb\nC\fC\16C\u01be\13C\3C\3C")
        buf.write("\3C\3C\3C\3D\3D\3D\3D\7D\u01c9\nD\fD\16D\u01cc\13D\3D")
        buf.write("\3D\3E\6E\u01d1\nE\rE\16E\u01d2\3F\6F\u01d6\nF\rF\16F")
        buf.write("\u01d7\3F\3F\3G\3G\3G\3H\3H\7H\u01e1\nH\fH\16H\u01e4\13")
        buf.write("H\3H\5H\u01e7\nH\3H\3H\3I\3I\7I\u01ed\nI\fI\16I\u01f0")
        buf.write("\13I\3I\3I\3I\3\u01bc\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}\2\177\2\u0081\2\u0083")
        buf.write("@\u0085A\u0087B\u0089C\u008bD\u008dE\u008fF\u0091G\3\2")
        buf.write("\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//")
        buf.write("\3\2\63;\3\2\62\62\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4")
        buf.write("\2ZZzz\5\2\62;CHch\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\4\2")
        buf.write("\f\f\17\17\5\2\13\13\16\17\"\"\4\3\f\f\17\17\2\u0203\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2")
        buf.write("\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2")
        buf.write("\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u0097")
        buf.write("\3\2\2\2\7\u00a1\3\2\2\2\t\u00a3\3\2\2\2\13\u00a6\3\2")
        buf.write("\2\2\r\u00ab\3\2\2\2\17\u00af\3\2\2\2\21\u00b6\3\2\2\2")
        buf.write("\23\u00bb\3\2\2\2\25\u00c0\3\2\2\2\27\u00c7\3\2\2\2\31")
        buf.write("\u00d1\3\2\2\2\33\u00d8\3\2\2\2\35\u00dc\3\2\2\2\37\u00e2")
        buf.write("\3\2\2\2!\u00ea\3\2\2\2#\u00f0\3\2\2\2%\u00f4\3\2\2\2")
        buf.write("\'\u00fd\3\2\2\2)\u0103\3\2\2\2+\u0109\3\2\2\2-\u010d")
        buf.write("\3\2\2\2/\u0112\3\2\2\2\61\u0118\3\2\2\2\63\u011a\3\2")
        buf.write("\2\2\65\u011d\3\2\2\2\67\u011f\3\2\2\29\u0121\3\2\2\2")
        buf.write(";\u0124\3\2\2\2=\u0126\3\2\2\2?\u0129\3\2\2\2A\u012c\3")
        buf.write("\2\2\2C\u012f\3\2\2\2E\u0131\3\2\2\2G\u0134\3\2\2\2I\u0137")
        buf.write("\3\2\2\2K\u013a\3\2\2\2M\u013d\3\2\2\2O\u0140\3\2\2\2")
        buf.write("Q\u0143\3\2\2\2S\u0146\3\2\2\2U\u0148\3\2\2\2W\u014a\3")
        buf.write("\2\2\2Y\u014c\3\2\2\2[\u014e\3\2\2\2]\u0150\3\2\2\2_\u0152")
        buf.write("\3\2\2\2a\u0154\3\2\2\2c\u0156\3\2\2\2e\u0158\3\2\2\2")
        buf.write("g\u015a\3\2\2\2i\u015c\3\2\2\2k\u015e\3\2\2\2m\u0160\3")
        buf.write("\2\2\2o\u0162\3\2\2\2q\u0169\3\2\2\2s\u0180\3\2\2\2u\u0182")
        buf.write("\3\2\2\2w\u018b\3\2\2\2y\u0194\3\2\2\2{\u019d\3\2\2\2")
        buf.write("}\u01a9\3\2\2\2\177\u01ab\3\2\2\2\u0081\u01ae\3\2\2\2")
        buf.write("\u0083\u01b3\3\2\2\2\u0085\u01b5\3\2\2\2\u0087\u01c4\3")
        buf.write("\2\2\2\u0089\u01d0\3\2\2\2\u008b\u01d5\3\2\2\2\u008d\u01db")
        buf.write("\3\2\2\2\u008f\u01de\3\2\2\2\u0091\u01ea\3\2\2\2\u0093")
        buf.write("\u0094\7c\2\2\u0094\u0095\7t\2\2\u0095\u0096\7t\2\2\u0096")
        buf.write("\4\3\2\2\2\u0097\u0098\7o\2\2\u0098\u0099\7w\2\2\u0099")
        buf.write("\u009a\7n\2\2\u009a\u009b\7v\2\2\u009b\u009c\7k\2\2\u009c")
        buf.write("\u009d\7\"\2\2\u009d\u009e\7c\2\2\u009e\u009f\7t\2\2\u009f")
        buf.write("\u00a0\7t\2\2\u00a0\6\3\2\2\2\u00a1\u00a2\7a\2\2\u00a2")
        buf.write("\b\3\2\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7h\2\2\u00a5")
        buf.write("\n\3\2\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7n\2\2\u00a8")
        buf.write("\u00a9\7u\2\2\u00a9\u00aa\7g\2\2\u00aa\f\3\2\2\2\u00ab")
        buf.write("\u00ac\7h\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7t\2\2\u00ae")
        buf.write("\16\3\2\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7g\2\2\u00b1")
        buf.write("\u00b2\7v\2\2\u00b2\u00b3\7w\2\2\u00b3\u00b4\7t\2\2\u00b4")
        buf.write("\u00b5\7p\2\2\u00b5\20\3\2\2\2\u00b6\u00b7\7h\2\2\u00b7")
        buf.write("\u00b8\7w\2\2\u00b8\u00b9\7p\2\2\u00b9\u00ba\7e\2\2\u00ba")
        buf.write("\22\3\2\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7{\2\2\u00bd")
        buf.write("\u00be\7r\2\2\u00be\u00bf\7g\2\2\u00bf\24\3\2\2\2\u00c0")
        buf.write("\u00c1\7u\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7t\2\2\u00c3")
        buf.write("\u00c4\7w\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6\7v\2\2\u00c6")
        buf.write("\26\3\2\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7p\2\2\u00c9")
        buf.write("\u00ca\7v\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7t\2\2\u00cc")
        buf.write("\u00cd\7h\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7e\2\2\u00cf")
        buf.write("\u00d0\7g\2\2\u00d0\30\3\2\2\2\u00d1\u00d2\7u\2\2\u00d2")
        buf.write("\u00d3\7v\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5\7k\2\2\u00d5")
        buf.write("\u00d6\7p\2\2\u00d6\u00d7\7i\2\2\u00d7\32\3\2\2\2\u00d8")
        buf.write("\u00d9\7k\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7v\2\2\u00db")
        buf.write("\34\3\2\2\2\u00dc\u00dd\7h\2\2\u00dd\u00de\7n\2\2\u00de")
        buf.write("\u00df\7q\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7v\2\2\u00e1")
        buf.write("\36\3\2\2\2\u00e2\u00e3\7d\2\2\u00e3\u00e4\7q\2\2\u00e4")
        buf.write("\u00e5\7q\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7\7g\2\2\u00e7")
        buf.write("\u00e8\7c\2\2\u00e8\u00e9\7p\2\2\u00e9 \3\2\2\2\u00ea")
        buf.write("\u00eb\7e\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write("\u00ee\7u\2\2\u00ee\u00ef\7v\2\2\u00ef\"\3\2\2\2\u00f0")
        buf.write("\u00f1\7x\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7t\2\2\u00f3")
        buf.write("$\3\2\2\2\u00f4\u00f5\7e\2\2\u00f5\u00f6\7q\2\2\u00f6")
        buf.write("\u00f7\7p\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7k\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc\7g\2\2\u00fc")
        buf.write("&\3\2\2\2\u00fd\u00fe\7d\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write("\u0100\7g\2\2\u0100\u0101\7c\2\2\u0101\u0102\7m\2\2\u0102")
        buf.write("(\3\2\2\2\u0103\u0104\7t\2\2\u0104\u0105\7c\2\2\u0105")
        buf.write("\u0106\7p\2\2\u0106\u0107\7i\2\2\u0107\u0108\7g\2\2\u0108")
        buf.write("*\3\2\2\2\u0109\u010a\7p\2\2\u010a\u010b\7k\2\2\u010b")
        buf.write("\u010c\7n\2\2\u010c,\3\2\2\2\u010d\u010e\7v\2\2\u010e")
        buf.write("\u010f\7t\2\2\u010f\u0110\7w\2\2\u0110\u0111\7g\2\2\u0111")
        buf.write(".\3\2\2\2\u0112\u0113\7h\2\2\u0113\u0114\7c\2\2\u0114")
        buf.write("\u0115\7n\2\2\u0115\u0116\7u\2\2\u0116\u0117\7g\2\2\u0117")
        buf.write("\60\3\2\2\2\u0118\u0119\7\60\2\2\u0119\62\3\2\2\2\u011a")
        buf.write("\u011b\7<\2\2\u011b\u011c\7?\2\2\u011c\64\3\2\2\2\u011d")
        buf.write("\u011e\7<\2\2\u011e\66\3\2\2\2\u011f\u0120\7>\2\2\u0120")
        buf.write("8\3\2\2\2\u0121\u0122\7>\2\2\u0122\u0123\7?\2\2\u0123")
        buf.write(":\3\2\2\2\u0124\u0125\7@\2\2\u0125<\3\2\2\2\u0126\u0127")
        buf.write("\7@\2\2\u0127\u0128\7?\2\2\u0128>\3\2\2\2\u0129\u012a")
        buf.write("\7?\2\2\u012a\u012b\7?\2\2\u012b@\3\2\2\2\u012c\u012d")
        buf.write("\7#\2\2\u012d\u012e\7?\2\2\u012eB\3\2\2\2\u012f\u0130")
        buf.write("\7?\2\2\u0130D\3\2\2\2\u0131\u0132\7-\2\2\u0132\u0133")
        buf.write("\7?\2\2\u0133F\3\2\2\2\u0134\u0135\7/\2\2\u0135\u0136")
        buf.write("\7?\2\2\u0136H\3\2\2\2\u0137\u0138\7,\2\2\u0138\u0139")
        buf.write("\7?\2\2\u0139J\3\2\2\2\u013a\u013b\7\61\2\2\u013b\u013c")
        buf.write("\7?\2\2\u013cL\3\2\2\2\u013d\u013e\7\'\2\2\u013e\u013f")
        buf.write("\7?\2\2\u013fN\3\2\2\2\u0140\u0141\7(\2\2\u0141\u0142")
        buf.write("\7(\2\2\u0142P\3\2\2\2\u0143\u0144\7~\2\2\u0144\u0145")
        buf.write("\7~\2\2\u0145R\3\2\2\2\u0146\u0147\7#\2\2\u0147T\3\2\2")
        buf.write("\2\u0148\u0149\7-\2\2\u0149V\3\2\2\2\u014a\u014b\7/\2")
        buf.write("\2\u014bX\3\2\2\2\u014c\u014d\7,\2\2\u014dZ\3\2\2\2\u014e")
        buf.write("\u014f\7\61\2\2\u014f\\\3\2\2\2\u0150\u0151\7\'\2\2\u0151")
        buf.write("^\3\2\2\2\u0152\u0153\7*\2\2\u0153`\3\2\2\2\u0154\u0155")
        buf.write("\7+\2\2\u0155b\3\2\2\2\u0156\u0157\7}\2\2\u0157d\3\2\2")
        buf.write("\2\u0158\u0159\7\177\2\2\u0159f\3\2\2\2\u015a\u015b\7")
        buf.write("]\2\2\u015bh\3\2\2\2\u015c\u015d\7_\2\2\u015dj\3\2\2\2")
        buf.write("\u015e\u015f\7=\2\2\u015fl\3\2\2\2\u0160\u0161\7.\2\2")
        buf.write("\u0161n\3\2\2\2\u0162\u0166\t\2\2\2\u0163\u0165\t\3\2")
        buf.write("\2\u0164\u0163\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167p\3\2\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0169\u016a\5s:\2\u016a\u016e\5\61\31\2\u016b")
        buf.write("\u016d\t\4\2\2\u016c\u016b\3\2\2\2\u016d\u0170\3\2\2\2")
        buf.write("\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0176\3")
        buf.write("\2\2\2\u0170\u016e\3\2\2\2\u0171\u0173\t\5\2\2\u0172\u0174")
        buf.write("\t\6\2\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0177\5s:\2\u0176\u0171\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177r\3\2\2\2\u0178\u0181\t\4\2\2\u0179")
        buf.write("\u017b\t\7\2\2\u017a\u017c\t\4\2\2\u017b\u017a\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3")
        buf.write("\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\b:\2\2\u0180\u0178")
        buf.write("\3\2\2\2\u0180\u0179\3\2\2\2\u0181t\3\2\2\2\u0182\u0183")
        buf.write("\t\b\2\2\u0183\u0185\t\t\2\2\u0184\u0186\t\n\2\2\u0185")
        buf.write("\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\b")
        buf.write(";\3\2\u018av\3\2\2\2\u018b\u018c\t\b\2\2\u018c\u018e\t")
        buf.write("\13\2\2\u018d\u018f\t\f\2\2\u018e\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u0192\3\2\2\2\u0192\u0193\b<\4\2\u0193x\3\2\2\2")
        buf.write("\u0194\u0195\t\b\2\2\u0195\u0197\t\r\2\2\u0196\u0198\t")
        buf.write("\16\2\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\3\2\2\2")
        buf.write("\u019b\u019c\b=\5\2\u019cz\3\2\2\2\u019d\u01a1\7$\2\2")
        buf.write("\u019e\u01a0\5}?\2\u019f\u019e\3\2\2\2\u01a0\u01a3\3\2")
        buf.write("\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\7$\2\2\u01a5")
        buf.write("\u01a6\b>\6\2\u01a6|\3\2\2\2\u01a7\u01aa\5\177@\2\u01a8")
        buf.write("\u01aa\n\17\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3\2\2")
        buf.write("\2\u01aa~\3\2\2\2\u01ab\u01ac\7^\2\2\u01ac\u01ad\t\20")
        buf.write("\2\2\u01ad\u0080\3\2\2\2\u01ae\u01af\7^\2\2\u01af\u01b0")
        buf.write("\n\20\2\2\u01b0\u0082\3\2\2\2\u01b1\u01b4\5-\27\2\u01b2")
        buf.write("\u01b4\5/\30\2\u01b3\u01b1\3\2\2\2\u01b3\u01b2\3\2\2\2")
        buf.write("\u01b4\u0084\3\2\2\2\u01b5\u01b6\7\61\2\2\u01b6\u01b7")
        buf.write("\7,\2\2\u01b7\u01bc\3\2\2\2\u01b8\u01bb\5\u0085C\2\u01b9")
        buf.write("\u01bb\13\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2")
        buf.write("\2\u01bb\u01be\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bc\u01ba")
        buf.write("\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf")
        buf.write("\u01c0\7,\2\2\u01c0\u01c1\7\61\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01c3\bC\7\2\u01c3\u0086\3\2\2\2\u01c4\u01c5\7")
        buf.write("\61\2\2\u01c5\u01c6\7\61\2\2\u01c6\u01ca\3\2\2\2\u01c7")
        buf.write("\u01c9\n\21\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc\3\2\2")
        buf.write("\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cd")
        buf.write("\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01ce\bD\7\2\u01ce")
        buf.write("\u0088\3\2\2\2\u01cf\u01d1\t\21\2\2\u01d0\u01cf\3\2\2")
        buf.write("\2\u01d1\u01d2\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u008a\3\2\2\2\u01d4\u01d6\t\22\2\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\b")
        buf.write("F\7\2\u01da\u008c\3\2\2\2\u01db\u01dc\13\2\2\2\u01dc\u01dd")
        buf.write("\bG\b\2\u01dd\u008e\3\2\2\2\u01de\u01e2\7$\2\2\u01df\u01e1")
        buf.write("\5}?\2\u01e0\u01df\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0")
        buf.write("\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4")
        buf.write("\u01e2\3\2\2\2\u01e5\u01e7\t\23\2\2\u01e6\u01e5\3\2\2")
        buf.write("\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\bH\t\2\u01e9\u0090")
        buf.write("\3\2\2\2\u01ea\u01ee\7$\2\2\u01eb\u01ed\5}?\2\u01ec\u01eb")
        buf.write("\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01ee\3\2\2\2")
        buf.write("\u01f1\u01f2\5\u0081A\2\u01f2\u01f3\bI\n\2\u01f3\u0092")
        buf.write("\3\2\2\2\27\2\u0166\u016e\u0173\u0176\u017d\u0180\u0187")
        buf.write("\u0190\u0199\u01a1\u01a9\u01b3\u01ba\u01bc\u01ca\u01d2")
        buf.write("\u01d7\u01e2\u01e6\u01ee\13\3:\2\3;\3\3<\4\3=\5\3>\6\b")
        buf.write("\2\2\3G\7\3H\b\3I\t")
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
    INT_DEC = 57
    INT_BIN = 58
    INT_OCT = 59
    INT_HEX = 60
    STRING_LIT = 61
    BOOLEAN_LIT = 62
    COMMENTS = 63
    COMMENTS_LINE = 64
    NEWLINE = 65
    WS = 66
    ERROR_CHAR = 67
    UNCLOSE_STRING = 68
    ILLEGAL_ESCAPE = 69

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
            "ID", "FLOAT_LIT", "INT_DEC", "INT_BIN", "INT_OCT", "INT_HEX", 
            "STRING_LIT", "BOOLEAN_LIT", "COMMENTS", "COMMENTS_LINE", "NEWLINE", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                  "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "NIL", "TRUE", "FALSE", "DOT", "COLONASSIGN", 
                  "COLON", "LT", "LE", "GT", "GE", "EQ", "NE", "ASSIGN", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "AND", "OR", "NOT", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", "ID", "FLOAT_LIT", 
                  "INT_DEC", "INT_BIN", "INT_OCT", "INT_HEX", "STRING_LIT", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "BOOLEAN_LIT", "COMMENTS", 
                  "COMMENTS_LINE", "NEWLINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[56] = self.INT_DEC_action 
            actions[57] = self.INT_BIN_action 
            actions[58] = self.INT_OCT_action 
            actions[59] = self.INT_HEX_action 
            actions[60] = self.STRING_LIT_action 
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
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

     


