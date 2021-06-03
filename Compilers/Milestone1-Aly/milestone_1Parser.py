# Generated from milestone_1.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\39")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\3\3\2\39\2\5\2\4\3\2")
        buf.write("\2\2\4\5\t\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class milestone_1Parser ( Parser ):

    grammarFileName = "milestone_1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'var'", "'and'", 
                     "'yield'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'*'", 
                     "'-'", "'/'", "'~'", "'&'", "'|'", "'<'", "'>'", "'at'", 
                     "'%'", "'!'", "'^'", "'.'", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "WHITESPACE", "VARIABLE", 
                      "AND", "YIELD", "LETTER", "DIGIT", "IDENTIFIER", "HEXDIGIT", 
                      "OCTDIGIT", "BINDIGIT", "HEX_LIT", "DEC_LIT", "OCT_LIT", 
                      "BIN_LIT", "INT_LIT", "INT8_LIT", "INT16_LIT", "INT32_LIT", 
                      "INT64_LIT", "UINT_LIT", "UINT8_LIT", "UINT16_LIT", 
                      "UINT32_LIT", "UINT64_LIT", "EXP", "FLOAT_LIT", "FLOAT32_SUFFIX", 
                      "FLOAT32_LIT", "FLOAT64_SUFFIX", "FLOAT64_LIT", "EQUALS_OPERATOR", 
                      "ADD_OPERATOR", "MUL_OPERATOR", "MINUS_OPERATOR", 
                      "DIV_OPERATOR", "BITWISE_NOT_OPERATOR", "AND_OPERATOR", 
                      "OR_OPERATOR", "LESS_THAN", "GREATER_THAN", "AT", 
                      "MODULUS", "NOT_OPERATOR", "XOR_OPERATOR", "DOT", 
                      "COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", 
                      "CLOSE_BRACE", "OPEN_BRACK", "CLOSE_BRACK", "COMMA", 
                      "SEMI_COLON" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    NEWLINE=1
    WHITESPACE=2
    VARIABLE=3
    AND=4
    YIELD=5
    LETTER=6
    DIGIT=7
    IDENTIFIER=8
    HEXDIGIT=9
    OCTDIGIT=10
    BINDIGIT=11
    HEX_LIT=12
    DEC_LIT=13
    OCT_LIT=14
    BIN_LIT=15
    INT_LIT=16
    INT8_LIT=17
    INT16_LIT=18
    INT32_LIT=19
    INT64_LIT=20
    UINT_LIT=21
    UINT8_LIT=22
    UINT16_LIT=23
    UINT32_LIT=24
    UINT64_LIT=25
    EXP=26
    FLOAT_LIT=27
    FLOAT32_SUFFIX=28
    FLOAT32_LIT=29
    FLOAT64_SUFFIX=30
    FLOAT64_LIT=31
    EQUALS_OPERATOR=32
    ADD_OPERATOR=33
    MUL_OPERATOR=34
    MINUS_OPERATOR=35
    DIV_OPERATOR=36
    BITWISE_NOT_OPERATOR=37
    AND_OPERATOR=38
    OR_OPERATOR=39
    LESS_THAN=40
    GREATER_THAN=41
    AT=42
    MODULUS=43
    NOT_OPERATOR=44
    XOR_OPERATOR=45
    DOT=46
    COLON=47
    OPEN_PAREN=48
    CLOSE_PAREN=49
    OPEN_BRACE=50
    CLOSE_BRACE=51
    OPEN_BRACK=52
    CLOSE_BRACK=53
    COMMA=54
    SEMI_COLON=55

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(milestone_1Parser.NEWLINE, 0)

        def WHITESPACE(self):
            return self.getToken(milestone_1Parser.WHITESPACE, 0)

        def VARIABLE(self):
            return self.getToken(milestone_1Parser.VARIABLE, 0)

        def AND(self):
            return self.getToken(milestone_1Parser.AND, 0)

        def YIELD(self):
            return self.getToken(milestone_1Parser.YIELD, 0)

        def LETTER(self):
            return self.getToken(milestone_1Parser.LETTER, 0)

        def DIGIT(self):
            return self.getToken(milestone_1Parser.DIGIT, 0)

        def IDENTIFIER(self):
            return self.getToken(milestone_1Parser.IDENTIFIER, 0)

        def HEXDIGIT(self):
            return self.getToken(milestone_1Parser.HEXDIGIT, 0)

        def OCTDIGIT(self):
            return self.getToken(milestone_1Parser.OCTDIGIT, 0)

        def BINDIGIT(self):
            return self.getToken(milestone_1Parser.BINDIGIT, 0)

        def HEX_LIT(self):
            return self.getToken(milestone_1Parser.HEX_LIT, 0)

        def DEC_LIT(self):
            return self.getToken(milestone_1Parser.DEC_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(milestone_1Parser.OCT_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(milestone_1Parser.BIN_LIT, 0)

        def INT_LIT(self):
            return self.getToken(milestone_1Parser.INT_LIT, 0)

        def INT8_LIT(self):
            return self.getToken(milestone_1Parser.INT8_LIT, 0)

        def INT16_LIT(self):
            return self.getToken(milestone_1Parser.INT16_LIT, 0)

        def INT32_LIT(self):
            return self.getToken(milestone_1Parser.INT32_LIT, 0)

        def INT64_LIT(self):
            return self.getToken(milestone_1Parser.INT64_LIT, 0)

        def UINT_LIT(self):
            return self.getToken(milestone_1Parser.UINT_LIT, 0)

        def UINT8_LIT(self):
            return self.getToken(milestone_1Parser.UINT8_LIT, 0)

        def UINT16_LIT(self):
            return self.getToken(milestone_1Parser.UINT16_LIT, 0)

        def UINT32_LIT(self):
            return self.getToken(milestone_1Parser.UINT32_LIT, 0)

        def UINT64_LIT(self):
            return self.getToken(milestone_1Parser.UINT64_LIT, 0)

        def EXP(self):
            return self.getToken(milestone_1Parser.EXP, 0)

        def FLOAT_LIT(self):
            return self.getToken(milestone_1Parser.FLOAT_LIT, 0)

        def FLOAT32_SUFFIX(self):
            return self.getToken(milestone_1Parser.FLOAT32_SUFFIX, 0)

        def FLOAT32_LIT(self):
            return self.getToken(milestone_1Parser.FLOAT32_LIT, 0)

        def FLOAT64_SUFFIX(self):
            return self.getToken(milestone_1Parser.FLOAT64_SUFFIX, 0)

        def FLOAT64_LIT(self):
            return self.getToken(milestone_1Parser.FLOAT64_LIT, 0)

        def EQUALS_OPERATOR(self):
            return self.getToken(milestone_1Parser.EQUALS_OPERATOR, 0)

        def ADD_OPERATOR(self):
            return self.getToken(milestone_1Parser.ADD_OPERATOR, 0)

        def MUL_OPERATOR(self):
            return self.getToken(milestone_1Parser.MUL_OPERATOR, 0)

        def MINUS_OPERATOR(self):
            return self.getToken(milestone_1Parser.MINUS_OPERATOR, 0)

        def DIV_OPERATOR(self):
            return self.getToken(milestone_1Parser.DIV_OPERATOR, 0)

        def BITWISE_NOT_OPERATOR(self):
            return self.getToken(milestone_1Parser.BITWISE_NOT_OPERATOR, 0)

        def AND_OPERATOR(self):
            return self.getToken(milestone_1Parser.AND_OPERATOR, 0)

        def OR_OPERATOR(self):
            return self.getToken(milestone_1Parser.OR_OPERATOR, 0)

        def LESS_THAN(self):
            return self.getToken(milestone_1Parser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(milestone_1Parser.GREATER_THAN, 0)

        def AT(self):
            return self.getToken(milestone_1Parser.AT, 0)

        def MODULUS(self):
            return self.getToken(milestone_1Parser.MODULUS, 0)

        def NOT_OPERATOR(self):
            return self.getToken(milestone_1Parser.NOT_OPERATOR, 0)

        def XOR_OPERATOR(self):
            return self.getToken(milestone_1Parser.XOR_OPERATOR, 0)

        def DOT(self):
            return self.getToken(milestone_1Parser.DOT, 0)

        def COLON(self):
            return self.getToken(milestone_1Parser.COLON, 0)

        def OPEN_PAREN(self):
            return self.getToken(milestone_1Parser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(milestone_1Parser.CLOSE_PAREN, 0)

        def OPEN_BRACE(self):
            return self.getToken(milestone_1Parser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(milestone_1Parser.CLOSE_BRACE, 0)

        def OPEN_BRACK(self):
            return self.getToken(milestone_1Parser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(milestone_1Parser.CLOSE_BRACK, 0)

        def COMMA(self):
            return self.getToken(milestone_1Parser.COMMA, 0)

        def SEMI_COLON(self):
            return self.getToken(milestone_1Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return milestone_1Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = milestone_1Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << milestone_1Parser.NEWLINE) | (1 << milestone_1Parser.WHITESPACE) | (1 << milestone_1Parser.VARIABLE) | (1 << milestone_1Parser.AND) | (1 << milestone_1Parser.YIELD) | (1 << milestone_1Parser.LETTER) | (1 << milestone_1Parser.DIGIT) | (1 << milestone_1Parser.IDENTIFIER) | (1 << milestone_1Parser.HEXDIGIT) | (1 << milestone_1Parser.OCTDIGIT) | (1 << milestone_1Parser.BINDIGIT) | (1 << milestone_1Parser.HEX_LIT) | (1 << milestone_1Parser.DEC_LIT) | (1 << milestone_1Parser.OCT_LIT) | (1 << milestone_1Parser.BIN_LIT) | (1 << milestone_1Parser.INT_LIT) | (1 << milestone_1Parser.INT8_LIT) | (1 << milestone_1Parser.INT16_LIT) | (1 << milestone_1Parser.INT32_LIT) | (1 << milestone_1Parser.INT64_LIT) | (1 << milestone_1Parser.UINT_LIT) | (1 << milestone_1Parser.UINT8_LIT) | (1 << milestone_1Parser.UINT16_LIT) | (1 << milestone_1Parser.UINT32_LIT) | (1 << milestone_1Parser.UINT64_LIT) | (1 << milestone_1Parser.EXP) | (1 << milestone_1Parser.FLOAT_LIT) | (1 << milestone_1Parser.FLOAT32_SUFFIX) | (1 << milestone_1Parser.FLOAT32_LIT) | (1 << milestone_1Parser.FLOAT64_SUFFIX) | (1 << milestone_1Parser.FLOAT64_LIT) | (1 << milestone_1Parser.EQUALS_OPERATOR) | (1 << milestone_1Parser.ADD_OPERATOR) | (1 << milestone_1Parser.MUL_OPERATOR) | (1 << milestone_1Parser.MINUS_OPERATOR) | (1 << milestone_1Parser.DIV_OPERATOR) | (1 << milestone_1Parser.BITWISE_NOT_OPERATOR) | (1 << milestone_1Parser.AND_OPERATOR) | (1 << milestone_1Parser.OR_OPERATOR) | (1 << milestone_1Parser.LESS_THAN) | (1 << milestone_1Parser.GREATER_THAN) | (1 << milestone_1Parser.AT) | (1 << milestone_1Parser.MODULUS) | (1 << milestone_1Parser.NOT_OPERATOR) | (1 << milestone_1Parser.XOR_OPERATOR) | (1 << milestone_1Parser.DOT) | (1 << milestone_1Parser.COLON) | (1 << milestone_1Parser.OPEN_PAREN) | (1 << milestone_1Parser.CLOSE_PAREN) | (1 << milestone_1Parser.OPEN_BRACE) | (1 << milestone_1Parser.CLOSE_BRACE) | (1 << milestone_1Parser.OPEN_BRACK) | (1 << milestone_1Parser.CLOSE_BRACK) | (1 << milestone_1Parser.COMMA) | (1 << milestone_1Parser.SEMI_COLON))) != 0)):
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





