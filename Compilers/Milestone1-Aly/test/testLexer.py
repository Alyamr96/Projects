# Generated from test.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("\25\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\13\n\2\r\2\16")
        buf.write("\2\f\3\3\6\3\20\n\3\r\3\16\3\21\3\4\3\4\2\2\5\3\3\5\4")
        buf.write("\7\5\3\2\5\4\2\f\f\17\17\3\2\62;\5\2,-//\61\61\2\26\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\3\n\3\2\2\2\5\17\3")
        buf.write("\2\2\2\7\23\3\2\2\2\t\13\t\2\2\2\n\t\3\2\2\2\13\f\3\2")
        buf.write("\2\2\f\n\3\2\2\2\f\r\3\2\2\2\r\4\3\2\2\2\16\20\t\3\2\2")
        buf.write("\17\16\3\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2")
        buf.write("\2\22\6\3\2\2\2\23\24\t\4\2\2\24\b\3\2\2\2\5\2\f\21\2")
        return buf.getvalue()


class testLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NEWLINE = 1
    INT = 2
    OPERATOR = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "INT", "OPERATOR" ]

    ruleNames = [ "NEWLINE", "INT", "OPERATOR" ]

    grammarFileName = "test.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


