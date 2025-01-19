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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u01e2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\7\66\u0153\n\66\f\66\16\66\u0156\13\66\3\67\3\67\3\67")
        buf.write("\7\67\u015b\n\67\f\67\16\67\u015e\13\67\3\67\3\67\5\67")
        buf.write("\u0162\n\67\3\67\5\67\u0165\n\67\38\38\38\68\u016a\n8")
        buf.write("\r8\168\u016b\38\58\u016f\n8\39\39\39\69\u0174\n9\r9\16")
        buf.write("9\u0175\39\39\3:\3:\3:\6:\u017d\n:\r:\16:\u017e\3:\3:")
        buf.write("\3;\3;\3;\6;\u0186\n;\r;\16;\u0187\3;\3;\3<\3<\7<\u018e")
        buf.write("\n<\f<\16<\u0191\13<\3<\3<\3<\3=\3=\5=\u0198\n=\3>\3>")
        buf.write("\3>\3?\3?\3?\3@\3@\5@\u01a2\n@\3A\3A\3A\3A\3A\7A\u01a9")
        buf.write("\nA\fA\16A\u01ac\13A\3A\3A\3A\3A\3A\3B\3B\3B\3B\7B\u01b7")
        buf.write("\nB\fB\16B\u01ba\13B\3B\3B\3C\6C\u01bf\nC\rC\16C\u01c0")
        buf.write("\3D\6D\u01c4\nD\rD\16D\u01c5\3D\3D\3E\3E\3E\3F\3F\7F\u01cf")
        buf.write("\nF\fF\16F\u01d2\13F\3F\5F\u01d5\nF\3F\3F\3G\3G\7G\u01db")
        buf.write("\nG\fG\16G\u01de\13G\3G\3G\3G\3\u01aa\2H\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y\2{\2}\2\177")
        buf.write(">\u0081?\u0083@\u0085A\u0087B\u0089C\u008bD\u008dE\3\2")
        buf.write("\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//")
        buf.write("\3\2\63;\3\2\62\62\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4")
        buf.write("\2ZZzz\5\2\62;CHch\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\4\2")
        buf.write("\f\f\17\17\5\2\13\13\16\17\"\"\4\3\f\f\17\17\2\u01f1\2")
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
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\3\u008f\3\2\2\2\5\u0091\3\2\2\2\7\u0094\3\2\2\2\t\u0099")
        buf.write("\3\2\2\2\13\u009d\3\2\2\2\r\u00a4\3\2\2\2\17\u00a9\3\2")
        buf.write("\2\2\21\u00ae\3\2\2\2\23\u00b5\3\2\2\2\25\u00bf\3\2\2")
        buf.write("\2\27\u00c6\3\2\2\2\31\u00ca\3\2\2\2\33\u00d0\3\2\2\2")
        buf.write("\35\u00d8\3\2\2\2\37\u00de\3\2\2\2!\u00e2\3\2\2\2#\u00eb")
        buf.write("\3\2\2\2%\u00f1\3\2\2\2\'\u00f7\3\2\2\2)\u00fb\3\2\2\2")
        buf.write("+\u0100\3\2\2\2-\u0106\3\2\2\2/\u0108\3\2\2\2\61\u010b")
        buf.write("\3\2\2\2\63\u010d\3\2\2\2\65\u010f\3\2\2\2\67\u0112\3")
        buf.write("\2\2\29\u0114\3\2\2\2;\u0117\3\2\2\2=\u011a\3\2\2\2?\u011d")
        buf.write("\3\2\2\2A\u011f\3\2\2\2C\u0122\3\2\2\2E\u0125\3\2\2\2")
        buf.write("G\u0128\3\2\2\2I\u012b\3\2\2\2K\u012e\3\2\2\2M\u0131\3")
        buf.write("\2\2\2O\u0134\3\2\2\2Q\u0136\3\2\2\2S\u0138\3\2\2\2U\u013a")
        buf.write("\3\2\2\2W\u013c\3\2\2\2Y\u013e\3\2\2\2[\u0140\3\2\2\2")
        buf.write("]\u0142\3\2\2\2_\u0144\3\2\2\2a\u0146\3\2\2\2c\u0148\3")
        buf.write("\2\2\2e\u014a\3\2\2\2g\u014c\3\2\2\2i\u014e\3\2\2\2k\u0150")
        buf.write("\3\2\2\2m\u0157\3\2\2\2o\u016e\3\2\2\2q\u0170\3\2\2\2")
        buf.write("s\u0179\3\2\2\2u\u0182\3\2\2\2w\u018b\3\2\2\2y\u0197\3")
        buf.write("\2\2\2{\u0199\3\2\2\2}\u019c\3\2\2\2\177\u01a1\3\2\2\2")
        buf.write("\u0081\u01a3\3\2\2\2\u0083\u01b2\3\2\2\2\u0085\u01be\3")
        buf.write("\2\2\2\u0087\u01c3\3\2\2\2\u0089\u01c9\3\2\2\2\u008b\u01cc")
        buf.write("\3\2\2\2\u008d\u01d8\3\2\2\2\u008f\u0090\7a\2\2\u0090")
        buf.write("\4\3\2\2\2\u0091\u0092\7k\2\2\u0092\u0093\7h\2\2\u0093")
        buf.write("\6\3\2\2\2\u0094\u0095\7g\2\2\u0095\u0096\7n\2\2\u0096")
        buf.write("\u0097\7u\2\2\u0097\u0098\7g\2\2\u0098\b\3\2\2\2\u0099")
        buf.write("\u009a\7h\2\2\u009a\u009b\7q\2\2\u009b\u009c\7t\2\2\u009c")
        buf.write("\n\3\2\2\2\u009d\u009e\7t\2\2\u009e\u009f\7g\2\2\u009f")
        buf.write("\u00a0\7v\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2\7t\2\2\u00a2")
        buf.write("\u00a3\7p\2\2\u00a3\f\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5")
        buf.write("\u00a6\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7e\2\2\u00a8")
        buf.write("\16\3\2\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab\7{\2\2\u00ab")
        buf.write("\u00ac\7r\2\2\u00ac\u00ad\7g\2\2\u00ad\20\3\2\2\2\u00ae")
        buf.write("\u00af\7u\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7t\2\2\u00b1")
        buf.write("\u00b2\7w\2\2\u00b2\u00b3\7e\2\2\u00b3\u00b4\7v\2\2\u00b4")
        buf.write("\22\3\2\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7p\2\2\u00b7")
        buf.write("\u00b8\7v\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7t\2\2\u00ba")
        buf.write("\u00bb\7h\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7e\2\2\u00bd")
        buf.write("\u00be\7g\2\2\u00be\24\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0")
        buf.write("\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3")
        buf.write("\u00c4\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\26\3\2\2\2\u00c6")
        buf.write("\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7v\2\2\u00c9")
        buf.write("\30\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc\7n\2\2\u00cc")
        buf.write("\u00cd\7q\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7v\2\2\u00cf")
        buf.write("\32\3\2\2\2\u00d0\u00d1\7d\2\2\u00d1\u00d2\7q\2\2\u00d2")
        buf.write("\u00d3\7q\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7g\2\2\u00d5")
        buf.write("\u00d6\7c\2\2\u00d6\u00d7\7p\2\2\u00d7\34\3\2\2\2\u00d8")
        buf.write("\u00d9\7e\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7p\2\2\u00db")
        buf.write("\u00dc\7u\2\2\u00dc\u00dd\7v\2\2\u00dd\36\3\2\2\2\u00de")
        buf.write("\u00df\7x\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7t\2\2\u00e1")
        buf.write(" \3\2\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4\7q\2\2\u00e4")
        buf.write("\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7k\2\2\u00e7")
        buf.write("\u00e8\7p\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7g\2\2\u00ea")
        buf.write("\"\3\2\2\2\u00eb\u00ec\7d\2\2\u00ec\u00ed\7t\2\2\u00ed")
        buf.write("\u00ee\7g\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7m\2\2\u00f0")
        buf.write("$\3\2\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3\7c\2\2\u00f3")
        buf.write("\u00f4\7p\2\2\u00f4\u00f5\7i\2\2\u00f5\u00f6\7g\2\2\u00f6")
        buf.write("&\3\2\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7k\2\2\u00f9")
        buf.write("\u00fa\7n\2\2\u00fa(\3\2\2\2\u00fb\u00fc\7v\2\2\u00fc")
        buf.write("\u00fd\7t\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7g\2\2\u00ff")
        buf.write("*\3\2\2\2\u0100\u0101\7h\2\2\u0101\u0102\7c\2\2\u0102")
        buf.write("\u0103\7n\2\2\u0103\u0104\7u\2\2\u0104\u0105\7g\2\2\u0105")
        buf.write(",\3\2\2\2\u0106\u0107\7\60\2\2\u0107.\3\2\2\2\u0108\u0109")
        buf.write("\7<\2\2\u0109\u010a\7?\2\2\u010a\60\3\2\2\2\u010b\u010c")
        buf.write("\7<\2\2\u010c\62\3\2\2\2\u010d\u010e\7>\2\2\u010e\64\3")
        buf.write("\2\2\2\u010f\u0110\7>\2\2\u0110\u0111\7?\2\2\u0111\66")
        buf.write("\3\2\2\2\u0112\u0113\7@\2\2\u01138\3\2\2\2\u0114\u0115")
        buf.write("\7@\2\2\u0115\u0116\7?\2\2\u0116:\3\2\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118\u0119\7?\2\2\u0119<\3\2\2\2\u011a\u011b")
        buf.write("\7#\2\2\u011b\u011c\7?\2\2\u011c>\3\2\2\2\u011d\u011e")
        buf.write("\7?\2\2\u011e@\3\2\2\2\u011f\u0120\7-\2\2\u0120\u0121")
        buf.write("\7?\2\2\u0121B\3\2\2\2\u0122\u0123\7/\2\2\u0123\u0124")
        buf.write("\7?\2\2\u0124D\3\2\2\2\u0125\u0126\7,\2\2\u0126\u0127")
        buf.write("\7?\2\2\u0127F\3\2\2\2\u0128\u0129\7\61\2\2\u0129\u012a")
        buf.write("\7?\2\2\u012aH\3\2\2\2\u012b\u012c\7\'\2\2\u012c\u012d")
        buf.write("\7?\2\2\u012dJ\3\2\2\2\u012e\u012f\7(\2\2\u012f\u0130")
        buf.write("\7(\2\2\u0130L\3\2\2\2\u0131\u0132\7~\2\2\u0132\u0133")
        buf.write("\7~\2\2\u0133N\3\2\2\2\u0134\u0135\7#\2\2\u0135P\3\2\2")
        buf.write("\2\u0136\u0137\7-\2\2\u0137R\3\2\2\2\u0138\u0139\7/\2")
        buf.write("\2\u0139T\3\2\2\2\u013a\u013b\7,\2\2\u013bV\3\2\2\2\u013c")
        buf.write("\u013d\7\61\2\2\u013dX\3\2\2\2\u013e\u013f\7\'\2\2\u013f")
        buf.write("Z\3\2\2\2\u0140\u0141\7*\2\2\u0141\\\3\2\2\2\u0142\u0143")
        buf.write("\7+\2\2\u0143^\3\2\2\2\u0144\u0145\7}\2\2\u0145`\3\2\2")
        buf.write("\2\u0146\u0147\7\177\2\2\u0147b\3\2\2\2\u0148\u0149\7")
        buf.write("]\2\2\u0149d\3\2\2\2\u014a\u014b\7_\2\2\u014bf\3\2\2\2")
        buf.write("\u014c\u014d\7=\2\2\u014dh\3\2\2\2\u014e\u014f\7.\2\2")
        buf.write("\u014fj\3\2\2\2\u0150\u0154\t\2\2\2\u0151\u0153\t\3\2")
        buf.write("\2\u0152\u0151\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155l\3\2\2\2\u0156\u0154")
        buf.write("\3\2\2\2\u0157\u0158\5o8\2\u0158\u015c\5-\27\2\u0159\u015b")
        buf.write("\t\4\2\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u0164\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015f\u0161\t\5\2\2\u0160\u0162\t")
        buf.write("\6\2\2\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0165\5o8\2\u0164\u015f\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165n\3\2\2\2\u0166\u016f\t\4\2\2\u0167\u0169")
        buf.write("\t\7\2\2\u0168\u016a\t\4\2\2\u0169\u0168\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016d\u016f\b8\2\2\u016e\u0166\3")
        buf.write("\2\2\2\u016e\u0167\3\2\2\2\u016fp\3\2\2\2\u0170\u0171")
        buf.write("\t\b\2\2\u0171\u0173\t\t\2\2\u0172\u0174\t\n\2\2\u0173")
        buf.write("\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\b")
        buf.write("9\3\2\u0178r\3\2\2\2\u0179\u017a\t\b\2\2\u017a\u017c\t")
        buf.write("\13\2\2\u017b\u017d\t\f\2\2\u017c\u017b\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180\u0181\b:\4\2\u0181t\3\2\2\2")
        buf.write("\u0182\u0183\t\b\2\2\u0183\u0185\t\r\2\2\u0184\u0186\t")
        buf.write("\16\2\2\u0185\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189\u018a\b;\5\2\u018av\3\2\2\2\u018b\u018f\7$\2\2")
        buf.write("\u018c\u018e\5y=\2\u018d\u018c\3\2\2\2\u018e\u0191\3\2")
        buf.write("\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192")
        buf.write("\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0193\7$\2\2\u0193")
        buf.write("\u0194\b<\6\2\u0194x\3\2\2\2\u0195\u0198\5{>\2\u0196\u0198")
        buf.write("\n\17\2\2\u0197\u0195\3\2\2\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("z\3\2\2\2\u0199\u019a\7^\2\2\u019a\u019b\t\20\2\2\u019b")
        buf.write("|\3\2\2\2\u019c\u019d\7^\2\2\u019d\u019e\n\20\2\2\u019e")
        buf.write("~\3\2\2\2\u019f\u01a2\5)\25\2\u01a0\u01a2\5+\26\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2\u0080\3\2\2\2")
        buf.write("\u01a3\u01a4\7\61\2\2\u01a4\u01a5\7,\2\2\u01a5\u01aa\3")
        buf.write("\2\2\2\u01a6\u01a9\5\u0081A\2\u01a7\u01a9\13\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac\3\2\2\2")
        buf.write("\u01aa\u01ab\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ad\3")
        buf.write("\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae\7,\2\2\u01ae\u01af")
        buf.write("\7\61\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\bA\7\2\u01b1")
        buf.write("\u0082\3\2\2\2\u01b2\u01b3\7\61\2\2\u01b3\u01b4\7\61\2")
        buf.write("\2\u01b4\u01b8\3\2\2\2\u01b5\u01b7\n\21\2\2\u01b6\u01b5")
        buf.write("\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01bb\u01bc\bB\7\2\u01bc\u0084\3\2\2\2\u01bd\u01bf\t")
        buf.write("\21\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u0086\3\2\2\2")
        buf.write("\u01c2\u01c4\t\22\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c5")
        buf.write("\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c8\bD\7\2\u01c8\u0088\3\2\2\2")
        buf.write("\u01c9\u01ca\13\2\2\2\u01ca\u01cb\bE\b\2\u01cb\u008a\3")
        buf.write("\2\2\2\u01cc\u01d0\7$\2\2\u01cd\u01cf\5y=\2\u01ce\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2")
        buf.write("\u01d3\u01d5\t\23\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01d7\bF\t\2\u01d7\u008c\3\2\2\2\u01d8")
        buf.write("\u01dc\7$\2\2\u01d9\u01db\5y=\2\u01da\u01d9\3\2\2\2\u01db")
        buf.write("\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2")
        buf.write("\u01dd\u01df\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e0\5")
        buf.write("}?\2\u01e0\u01e1\bG\n\2\u01e1\u008e\3\2\2\2\27\2\u0154")
        buf.write("\u015c\u0161\u0164\u016b\u016e\u0175\u017e\u0187\u018f")
        buf.write("\u0197\u01a1\u01a8\u01aa\u01b8\u01c0\u01c5\u01d0\u01d4")
        buf.write("\u01dc\13\38\2\39\3\3:\4\3;\5\3<\6\b\2\2\3E\7\3F\b\3G")
        buf.write("\t")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    CONST = 14
    VAR = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    NIL = 19
    TRUE = 20
    FALSE = 21
    DOT = 22
    COLONASSIGN = 23
    COLON = 24
    LT = 25
    LE = 26
    GT = 27
    GE = 28
    EQ = 29
    NE = 30
    ASSIGN = 31
    ADD_ASSIGN = 32
    SUB_ASSIGN = 33
    MUL_ASSIGN = 34
    DIV_ASSIGN = 35
    MOD_ASSIGN = 36
    AND = 37
    OR = 38
    NOT = 39
    ADD = 40
    SUB = 41
    MUL = 42
    DIV = 43
    MOD = 44
    LPAREN = 45
    RPAREN = 46
    LBRACE = 47
    RBRACE = 48
    LBRACKET = 49
    RBRACKET = 50
    SEMICOLON = 51
    COMMA = 52
    ID = 53
    FLOAT_LIT = 54
    INT_DEC = 55
    INT_BIN = 56
    INT_OCT = 57
    INT_HEX = 58
    STRING_LIT = 59
    BOOLEAN_LIT = 60
    COMMENTS = 61
    COMMENTS_LINE = 62
    NEWLINE = 63
    WS = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'_'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'.'", "':='", "':'", "'<'", "'<='", "'>'", 
            "'>='", "'=='", "'!='", "'='", "'+='", "'-='", "'*='", "'/='", 
            "'%='", "'&&'", "'||'", "'!'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

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

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "DOT", "COLONASSIGN", "COLON", "LT", "LE", "GT", 
                  "GE", "EQ", "NE", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND", "OR", 
                  "NOT", "ADD", "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", 
                  "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", 
                  "COMMA", "ID", "FLOAT_LIT", "INT_DEC", "INT_BIN", "INT_OCT", 
                  "INT_HEX", "STRING_LIT", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "BOOLEAN_LIT", "COMMENTS", "COMMENTS_LINE", "NEWLINE", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[54] = self.INT_DEC_action 
            actions[55] = self.INT_BIN_action 
            actions[56] = self.INT_OCT_action 
            actions[57] = self.INT_HEX_action 
            actions[58] = self.STRING_LIT_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
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

     


