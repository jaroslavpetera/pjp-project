# Generated from rules.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,54,194,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,1,1,1,1,1,1,1,
        1,1,5,1,42,8,1,10,1,12,1,45,9,1,1,1,1,1,1,1,1,1,5,1,51,8,1,10,1,
        12,1,54,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,64,8,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,5,1,86,8,1,10,1,12,1,89,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,5,1,99,8,1,10,1,12,1,102,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,135,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,163,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,189,
        8,3,10,3,12,3,192,9,3,1,3,0,1,6,4,0,2,4,6,0,5,1,0,22,27,1,0,30,32,
        2,0,28,28,33,34,1,0,35,36,1,0,37,38,232,0,9,1,0,0,0,2,134,1,0,0,
        0,4,136,1,0,0,0,6,162,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,
        0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,14,3,4,2,0,14,19,
        5,47,0,0,15,16,5,1,0,0,16,18,5,47,0,0,17,15,1,0,0,0,18,21,1,0,0,
        0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,
        5,2,0,0,23,135,1,0,0,0,24,25,3,6,3,0,25,26,5,2,0,0,26,135,1,0,0,
        0,27,28,5,3,0,0,28,33,5,47,0,0,29,30,5,1,0,0,30,32,5,47,0,0,31,29,
        1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,
        35,33,1,0,0,0,36,135,5,2,0,0,37,38,5,4,0,0,38,43,3,6,3,0,39,40,5,
        1,0,0,40,42,3,6,3,0,41,39,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,
        44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,2,0,0,47,135,1,0,
        0,0,48,52,5,5,0,0,49,51,3,2,1,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,
        1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,135,5,6,0,0,
        56,57,5,7,0,0,57,58,5,8,0,0,58,59,3,6,3,0,59,60,5,9,0,0,60,63,3,
        2,1,0,61,62,5,10,0,0,62,64,3,2,1,0,63,61,1,0,0,0,63,64,1,0,0,0,64,
        135,1,0,0,0,65,66,5,11,0,0,66,67,5,8,0,0,67,68,3,6,3,0,68,69,5,9,
        0,0,69,70,3,2,1,0,70,135,1,0,0,0,71,72,5,12,0,0,72,73,5,47,0,0,73,
        74,5,52,0,0,74,135,5,2,0,0,75,76,5,13,0,0,76,77,5,47,0,0,77,78,5,
        1,0,0,78,79,5,52,0,0,79,135,5,2,0,0,80,81,5,47,0,0,81,82,5,14,0,
        0,82,87,3,6,3,0,83,84,5,14,0,0,84,86,3,6,3,0,85,83,1,0,0,0,86,89,
        1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,0,0,0,
        90,91,5,2,0,0,91,135,1,0,0,0,92,93,5,15,0,0,93,94,5,47,0,0,94,95,
        5,1,0,0,95,100,3,6,3,0,96,97,5,1,0,0,97,99,3,6,3,0,98,96,1,0,0,0,
        99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,
        100,1,0,0,0,103,104,5,2,0,0,104,135,1,0,0,0,105,106,5,16,0,0,106,
        107,5,8,0,0,107,108,3,6,3,0,108,109,5,2,0,0,109,110,3,6,3,0,110,
        111,5,2,0,0,111,112,3,6,3,0,112,113,5,9,0,0,113,114,3,2,1,0,114,
        135,1,0,0,0,115,116,5,17,0,0,116,117,3,2,1,0,117,118,5,11,0,0,118,
        119,5,8,0,0,119,120,3,6,3,0,120,121,5,9,0,0,121,122,5,2,0,0,122,
        135,1,0,0,0,123,124,5,47,0,0,124,125,5,18,0,0,125,135,5,2,0,0,126,
        127,5,47,0,0,127,128,5,19,0,0,128,135,5,2,0,0,129,130,5,20,0,0,130,
        135,5,2,0,0,131,132,5,21,0,0,132,135,5,2,0,0,133,135,5,2,0,0,134,
        13,1,0,0,0,134,24,1,0,0,0,134,27,1,0,0,0,134,37,1,0,0,0,134,48,1,
        0,0,0,134,56,1,0,0,0,134,65,1,0,0,0,134,71,1,0,0,0,134,75,1,0,0,
        0,134,80,1,0,0,0,134,92,1,0,0,0,134,105,1,0,0,0,134,115,1,0,0,0,
        134,123,1,0,0,0,134,126,1,0,0,0,134,129,1,0,0,0,134,131,1,0,0,0,
        134,133,1,0,0,0,135,3,1,0,0,0,136,137,7,0,0,0,137,5,1,0,0,0,138,
        139,6,3,-1,0,139,140,5,28,0,0,140,163,3,6,3,19,141,142,5,29,0,0,
        142,163,3,6,3,18,143,144,5,47,0,0,144,145,5,43,0,0,145,163,3,6,3,
        10,146,147,5,47,0,0,147,148,5,44,0,0,148,149,3,6,3,0,149,150,5,45,
        0,0,150,163,1,0,0,0,151,163,5,49,0,0,152,163,5,48,0,0,153,163,5,
        50,0,0,154,163,5,51,0,0,155,163,5,46,0,0,156,163,5,52,0,0,157,163,
        5,47,0,0,158,159,5,8,0,0,159,160,3,6,3,0,160,161,5,9,0,0,161,163,
        1,0,0,0,162,138,1,0,0,0,162,141,1,0,0,0,162,143,1,0,0,0,162,146,
        1,0,0,0,162,151,1,0,0,0,162,152,1,0,0,0,162,153,1,0,0,0,162,154,
        1,0,0,0,162,155,1,0,0,0,162,156,1,0,0,0,162,157,1,0,0,0,162,158,
        1,0,0,0,163,190,1,0,0,0,164,165,10,17,0,0,165,166,7,1,0,0,166,189,
        3,6,3,18,167,168,10,16,0,0,168,169,7,2,0,0,169,189,3,6,3,17,170,
        171,10,15,0,0,171,172,7,3,0,0,172,189,3,6,3,16,173,174,10,14,0,0,
        174,175,7,4,0,0,175,189,3,6,3,15,176,177,10,13,0,0,177,178,5,39,
        0,0,178,189,3,6,3,14,179,180,10,12,0,0,180,181,5,40,0,0,181,189,
        3,6,3,13,182,183,10,11,0,0,183,184,5,41,0,0,184,185,3,6,3,0,185,
        186,5,42,0,0,186,187,3,6,3,12,187,189,1,0,0,0,188,164,1,0,0,0,188,
        167,1,0,0,0,188,170,1,0,0,0,188,173,1,0,0,0,188,176,1,0,0,0,188,
        179,1,0,0,0,188,182,1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,
        191,1,0,0,0,191,7,1,0,0,0,192,190,1,0,0,0,12,11,19,33,43,52,63,87,
        100,134,162,188,190
    ]

class rulesParser ( Parser ):

    grammarFileName = "rules.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'fopen'", 
                     "'fopen2'", "'<<'", "'fappend'", "'for'", "'do'", "'++'", 
                     "'--'", "'break'", "'continue'", "'int'", "'float'", 
                     "'bool'", "'string'", "'FILE'", "'char'", "'-'", "'!'", 
                     "'*'", "'/'", "'%'", "'+'", "'.'", "'<'", "'>'", "'=='", 
                     "'!='", "'&&'", "'||'", "'?'", "':'", "'='", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOOL", "ID", "FLOAT", "INT", 
                      "OCT", "HEXA", "STRING", "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_type_spec = 2
    RULE_expr = 3

    ruleNames =  [ "prog", "stat", "type_spec", "expr" ]

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
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    BOOL=46
    ID=47
    FLOAT=48
    INT=49
    OCT=50
    HEXA=51
    STRING=52
    COMMENT=53
    WS=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.StatContext)
            else:
                return self.getTypedRuleContext(rulesParser.StatContext,i)


        def getRuleIndex(self):
            return rulesParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = rulesParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8936831583500732) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rulesParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReadStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(rulesParser.ID)
            else:
                return self.getToken(rulesParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStat" ):
                listener.enterReadStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStat" ):
                listener.exitReadStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStat" ):
                return visitor.visitReadStat(self)
            else:
                return visitor.visitChildren(self)


    class IfStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(rulesParser.ExprContext,0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.StatContext)
            else:
                return self.getTypedRuleContext(rulesParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)


    class DoWhileStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.body = None # StatContext
            self.cond = None # ExprContext
            self.copyFrom(ctx)

        def stat(self):
            return self.getTypedRuleContext(rulesParser.StatContext,0)

        def expr(self):
            return self.getTypedRuleContext(rulesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStat" ):
                listener.enterDoWhileStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStat" ):
                listener.exitDoWhileStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhileStat" ):
                return visitor.visitDoWhileStat(self)
            else:
                return visitor.visitChildren(self)


    class BlockStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.StatContext)
            else:
                return self.getTypedRuleContext(rulesParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStat" ):
                listener.enterBlockStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStat" ):
                listener.exitBlockStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStat" ):
                return visitor.visitBlockStat(self)
            else:
                return visitor.visitChildren(self)


    class ExprStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(rulesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStat" ):
                listener.enterExprStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStat" ):
                listener.exitExprStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStat" ):
                return visitor.visitExprStat(self)
            else:
                return visitor.visitChildren(self)


    class ContinueStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStat" ):
                listener.enterContinueStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStat" ):
                listener.exitContinueStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStat" ):
                return visitor.visitContinueStat(self)
            else:
                return visitor.visitChildren(self)


    class IncrementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(rulesParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncrement" ):
                listener.enterIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncrement" ):
                listener.exitIncrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncrement" ):
                return visitor.visitIncrement(self)
            else:
                return visitor.visitChildren(self)


    class FopenStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(rulesParser.ID, 0)
        def STRING(self):
            return self.getToken(rulesParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFopenStat" ):
                listener.enterFopenStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFopenStat" ):
                listener.exitFopenStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFopenStat" ):
                return visitor.visitFopenStat(self)
            else:
                return visitor.visitChildren(self)


    class FopenStat2Context(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(rulesParser.ID, 0)
        def STRING(self):
            return self.getToken(rulesParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFopenStat2" ):
                listener.enterFopenStat2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFopenStat2" ):
                listener.exitFopenStat2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFopenStat2" ):
                return visitor.visitFopenStat2(self)
            else:
                return visitor.visitChildren(self)


    class BreakStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStat" ):
                listener.enterBreakStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStat" ):
                listener.exitBreakStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStat" ):
                return visitor.visitBreakStat(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_spec(self):
            return self.getTypedRuleContext(rulesParser.Type_specContext,0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(rulesParser.ID)
            else:
                return self.getToken(rulesParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class FappendStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(rulesParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFappendStat" ):
                listener.enterFappendStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFappendStat" ):
                listener.exitFappendStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFappendStat" ):
                return visitor.visitFappendStat(self)
            else:
                return visitor.visitChildren(self)


    class ForStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.init = None # ExprContext
            self.cond = None # ExprContext
            self.step = None # ExprContext
            self.body = None # StatContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)

        def stat(self):
            return self.getTypedRuleContext(rulesParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStat" ):
                listener.enterForStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStat" ):
                listener.exitForStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStat" ):
                return visitor.visitForStat(self)
            else:
                return visitor.visitChildren(self)


    class WriteFileStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(rulesParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteFileStat" ):
                listener.enterWriteFileStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteFileStat" ):
                listener.exitWriteFileStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteFileStat" ):
                return visitor.visitWriteFileStat(self)
            else:
                return visitor.visitChildren(self)


    class DecrementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(rulesParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecrement" ):
                listener.enterDecrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecrement" ):
                listener.exitDecrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecrement" ):
                return visitor.visitDecrement(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStat" ):
                listener.enterEmptyStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStat" ):
                listener.exitEmptyStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStat" ):
                return visitor.visitEmptyStat(self)
            else:
                return visitor.visitChildren(self)


    class WriteStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStat" ):
                listener.enterWriteStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStat" ):
                listener.exitWriteStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStat" ):
                return visitor.visitWriteStat(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(rulesParser.ExprContext,0)

        def stat(self):
            return self.getTypedRuleContext(rulesParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStat" ):
                listener.enterWhileStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStat" ):
                listener.exitWhileStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStat" ):
                return visitor.visitWhileStat(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = rulesParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = rulesParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.type_spec()
                self.state = 14
                self.match(rulesParser.ID)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 15
                    self.match(rulesParser.T__0)
                    self.state = 16
                    self.match(rulesParser.ID)
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 22
                self.match(rulesParser.T__1)
                pass

            elif la_ == 2:
                localctx = rulesParser.ExprStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(rulesParser.T__1)
                pass

            elif la_ == 3:
                localctx = rulesParser.ReadStatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(rulesParser.T__2)
                self.state = 28
                self.match(rulesParser.ID)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 29
                    self.match(rulesParser.T__0)
                    self.state = 30
                    self.match(rulesParser.ID)
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 36
                self.match(rulesParser.T__1)
                pass

            elif la_ == 4:
                localctx = rulesParser.WriteStatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.match(rulesParser.T__3)
                self.state = 38
                self.expr(0)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 39
                    self.match(rulesParser.T__0)
                    self.state = 40
                    self.expr(0)
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 46
                self.match(rulesParser.T__1)
                pass

            elif la_ == 5:
                localctx = rulesParser.BlockStatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.match(rulesParser.T__4)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8936831583500732) != 0):
                    self.state = 49
                    self.stat()
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 55
                self.match(rulesParser.T__5)
                pass

            elif la_ == 6:
                localctx = rulesParser.IfStatContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.match(rulesParser.T__6)
                self.state = 57
                self.match(rulesParser.T__7)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.match(rulesParser.T__8)
                self.state = 60
                self.stat()
                self.state = 63
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 61
                    self.match(rulesParser.T__9)
                    self.state = 62
                    self.stat()


                pass

            elif la_ == 7:
                localctx = rulesParser.WhileStatContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 65
                self.match(rulesParser.T__10)
                self.state = 66
                self.match(rulesParser.T__7)
                self.state = 67
                self.expr(0)
                self.state = 68
                self.match(rulesParser.T__8)
                self.state = 69
                self.stat()
                pass

            elif la_ == 8:
                localctx = rulesParser.FopenStatContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.match(rulesParser.T__11)
                self.state = 72
                self.match(rulesParser.ID)
                self.state = 73
                self.match(rulesParser.STRING)
                self.state = 74
                self.match(rulesParser.T__1)
                pass

            elif la_ == 9:
                localctx = rulesParser.FopenStat2Context(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 75
                self.match(rulesParser.T__12)
                self.state = 76
                self.match(rulesParser.ID)
                self.state = 77
                self.match(rulesParser.T__0)
                self.state = 78
                self.match(rulesParser.STRING)
                self.state = 79
                self.match(rulesParser.T__1)
                pass

            elif la_ == 10:
                localctx = rulesParser.WriteFileStatContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 80
                self.match(rulesParser.ID)
                self.state = 81
                self.match(rulesParser.T__13)
                self.state = 82
                self.expr(0)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 83
                    self.match(rulesParser.T__13)
                    self.state = 84
                    self.expr(0)
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 90
                self.match(rulesParser.T__1)
                pass

            elif la_ == 11:
                localctx = rulesParser.FappendStatContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 92
                self.match(rulesParser.T__14)
                self.state = 93
                self.match(rulesParser.ID)
                self.state = 94
                self.match(rulesParser.T__0)
                self.state = 95
                self.expr(0)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 96
                    self.match(rulesParser.T__0)
                    self.state = 97
                    self.expr(0)
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.match(rulesParser.T__1)
                pass

            elif la_ == 12:
                localctx = rulesParser.ForStatContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 105
                self.match(rulesParser.T__15)
                self.state = 106
                self.match(rulesParser.T__7)
                self.state = 107
                localctx.init = self.expr(0)
                self.state = 108
                self.match(rulesParser.T__1)
                self.state = 109
                localctx.cond = self.expr(0)
                self.state = 110
                self.match(rulesParser.T__1)
                self.state = 111
                localctx.step = self.expr(0)
                self.state = 112
                self.match(rulesParser.T__8)
                self.state = 113
                localctx.body = self.stat()
                pass

            elif la_ == 13:
                localctx = rulesParser.DoWhileStatContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 115
                self.match(rulesParser.T__16)
                self.state = 116
                localctx.body = self.stat()
                self.state = 117
                self.match(rulesParser.T__10)
                self.state = 118
                self.match(rulesParser.T__7)
                self.state = 119
                localctx.cond = self.expr(0)
                self.state = 120
                self.match(rulesParser.T__8)
                self.state = 121
                self.match(rulesParser.T__1)
                pass

            elif la_ == 14:
                localctx = rulesParser.IncrementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 123
                self.match(rulesParser.ID)
                self.state = 124
                self.match(rulesParser.T__17)
                self.state = 125
                self.match(rulesParser.T__1)
                pass

            elif la_ == 15:
                localctx = rulesParser.DecrementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 126
                self.match(rulesParser.ID)
                self.state = 127
                self.match(rulesParser.T__18)
                self.state = 128
                self.match(rulesParser.T__1)
                pass

            elif la_ == 16:
                localctx = rulesParser.BreakStatContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 129
                self.match(rulesParser.T__19)
                self.state = 130
                self.match(rulesParser.T__1)
                pass

            elif la_ == 17:
                localctx = rulesParser.ContinueStatContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 131
                self.match(rulesParser.T__20)
                self.state = 132
                self.match(rulesParser.T__1)
                pass

            elif la_ == 18:
                localctx = rulesParser.EmptyStatContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 133
                self.match(rulesParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rulesParser.RULE_type_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_spec" ):
                listener.enterType_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_spec" ):
                listener.exitType_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_spec" ):
                return visitor.visitType_spec(self)
            else:
                return visitor.visitChildren(self)




    def type_spec(self):

        localctx = rulesParser.Type_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rulesParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringIndexContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(rulesParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(rulesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringIndex" ):
                listener.enterStringIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringIndex" ):
                listener.exitStringIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringIndex" ):
                return visitor.visitStringIndex(self)
            else:
                return visitor.visitChildren(self)


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class OctContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OCT(self):
            return self.getToken(rulesParser.OCT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOct" ):
                listener.enterOct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOct" ):
                listener.exitOct(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOct" ):
                return visitor.visitOct(self)
            else:
                return visitor.visitChildren(self)


    class LogicalNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(rulesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalNot" ):
                listener.enterLogicalNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalNot" ):
                listener.exitLogicalNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalNot" ):
                return visitor.visitLogicalNot(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(rulesParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(rulesParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class AddSubConcatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubConcat" ):
                listener.enterAddSubConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubConcat" ):
                listener.exitAddSubConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubConcat" ):
                return visitor.visitAddSubConcat(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(rulesParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(rulesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(rulesParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class HexaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEXA(self):
            return self.getToken(rulesParser.HEXA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHexa" ):
                listener.enterHexa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHexa" ):
                listener.exitHexa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHexa" ):
                return visitor.visitHexa(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(rulesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(rulesParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)


    class EqualityContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)


    class TernaryOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryOp" ):
                listener.enterTernaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryOp" ):
                listener.exitTernaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryOp" ):
                return visitor.visitTernaryOp(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rulesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(rulesParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(rulesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = rulesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = rulesParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 139
                self.match(rulesParser.T__27)
                self.state = 140
                self.expr(19)
                pass

            elif la_ == 2:
                localctx = rulesParser.LogicalNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 141
                self.match(rulesParser.T__28)
                self.state = 142
                self.expr(18)
                pass

            elif la_ == 3:
                localctx = rulesParser.AssignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 143
                self.match(rulesParser.ID)
                self.state = 144
                self.match(rulesParser.T__42)
                self.state = 145
                self.expr(10)
                pass

            elif la_ == 4:
                localctx = rulesParser.StringIndexContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(rulesParser.ID)
                self.state = 147
                self.match(rulesParser.T__43)
                self.state = 148
                self.expr(0)
                self.state = 149
                self.match(rulesParser.T__44)
                pass

            elif la_ == 5:
                localctx = rulesParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(rulesParser.INT)
                pass

            elif la_ == 6:
                localctx = rulesParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.match(rulesParser.FLOAT)
                pass

            elif la_ == 7:
                localctx = rulesParser.OctContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(rulesParser.OCT)
                pass

            elif la_ == 8:
                localctx = rulesParser.HexaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.match(rulesParser.HEXA)
                pass

            elif la_ == 9:
                localctx = rulesParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.match(rulesParser.BOOL)
                pass

            elif la_ == 10:
                localctx = rulesParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 156
                self.match(rulesParser.STRING)
                pass

            elif la_ == 11:
                localctx = rulesParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(rulesParser.ID)
                pass

            elif la_ == 12:
                localctx = rulesParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(rulesParser.T__7)
                self.state = 159
                self.expr(0)
                self.state = 160
                self.match(rulesParser.T__8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 188
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = rulesParser.MulDivModContext(self, rulesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 165
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 166
                        self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = rulesParser.AddSubConcatContext(self, rulesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 168
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 26038239232) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = rulesParser.RelationalContext(self, rulesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 171
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 172
                        self.expr(16)
                        pass

                    elif la_ == 4:
                        localctx = rulesParser.EqualityContext(self, rulesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 174
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==37 or _la==38):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 175
                        self.expr(15)
                        pass

                    elif la_ == 5:
                        localctx = rulesParser.LogicalAndContext(self, rulesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 177
                        self.match(rulesParser.T__38)
                        self.state = 178
                        self.expr(14)
                        pass

                    elif la_ == 6:
                        localctx = rulesParser.LogicalOrContext(self, rulesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 179
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 180
                        self.match(rulesParser.T__39)
                        self.state = 181
                        self.expr(13)
                        pass

                    elif la_ == 7:
                        localctx = rulesParser.TernaryOpContext(self, rulesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 182
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 183
                        self.match(rulesParser.T__40)
                        self.state = 184
                        self.expr(0)
                        self.state = 185
                        self.match(rulesParser.T__41)
                        self.state = 186
                        self.expr(12)
                        pass

             
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 11)
         




