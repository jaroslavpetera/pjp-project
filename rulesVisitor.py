# Generated from rules.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .rulesParser import rulesParser
else:
    from rulesParser import rulesParser

# This class defines a complete generic visitor for a parse tree produced by rulesParser.

class rulesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by rulesParser#prog.
    def visitProg(self, ctx:rulesParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#declaration.
    def visitDeclaration(self, ctx:rulesParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#exprStat.
    def visitExprStat(self, ctx:rulesParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#readStat.
    def visitReadStat(self, ctx:rulesParser.ReadStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#writeStat.
    def visitWriteStat(self, ctx:rulesParser.WriteStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#blockStat.
    def visitBlockStat(self, ctx:rulesParser.BlockStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#ifStat.
    def visitIfStat(self, ctx:rulesParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#whileStat.
    def visitWhileStat(self, ctx:rulesParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#fopenStat.
    def visitFopenStat(self, ctx:rulesParser.FopenStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#fopenStat2.
    def visitFopenStat2(self, ctx:rulesParser.FopenStat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#writeFileStat.
    def visitWriteFileStat(self, ctx:rulesParser.WriteFileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#fappendStat.
    def visitFappendStat(self, ctx:rulesParser.FappendStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#forStat.
    def visitForStat(self, ctx:rulesParser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#doWhileStat.
    def visitDoWhileStat(self, ctx:rulesParser.DoWhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#increment.
    def visitIncrement(self, ctx:rulesParser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#decrement.
    def visitDecrement(self, ctx:rulesParser.DecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#breakStat.
    def visitBreakStat(self, ctx:rulesParser.BreakStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#continueStat.
    def visitContinueStat(self, ctx:rulesParser.ContinueStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#emptyStat.
    def visitEmptyStat(self, ctx:rulesParser.EmptyStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#type_spec.
    def visitType_spec(self, ctx:rulesParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#stringIndex.
    def visitStringIndex(self, ctx:rulesParser.StringIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#mulDivMod.
    def visitMulDivMod(self, ctx:rulesParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#oct.
    def visitOct(self, ctx:rulesParser.OctContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#logicalNot.
    def visitLogicalNot(self, ctx:rulesParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#bool.
    def visitBool(self, ctx:rulesParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#string.
    def visitString(self, ctx:rulesParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#addSubConcat.
    def visitAddSubConcat(self, ctx:rulesParser.AddSubConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#logicalAnd.
    def visitLogicalAnd(self, ctx:rulesParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#float.
    def visitFloat(self, ctx:rulesParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#parenthesis.
    def visitParenthesis(self, ctx:rulesParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#int.
    def visitInt(self, ctx:rulesParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#hexa.
    def visitHexa(self, ctx:rulesParser.HexaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#unaryMinus.
    def visitUnaryMinus(self, ctx:rulesParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#relational.
    def visitRelational(self, ctx:rulesParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#id.
    def visitId(self, ctx:rulesParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#logicalOr.
    def visitLogicalOr(self, ctx:rulesParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#equality.
    def visitEquality(self, ctx:rulesParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#ternaryOp.
    def visitTernaryOp(self, ctx:rulesParser.TernaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#assign.
    def visitAssign(self, ctx:rulesParser.AssignContext):
        return self.visitChildren(ctx)



del rulesParser