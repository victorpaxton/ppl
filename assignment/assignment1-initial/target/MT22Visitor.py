# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#shortvardecl.
    def visitShortvardecl(self, ctx:MT22Parser.ShortvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fullvardecl.
    def visitFullvardecl(self, ctx:MT22Parser.FullvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varinit.
    def visitVarinit(self, ctx:MT22Parser.VarinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vartyp.
    def visitVartyp(self, ctx:MT22Parser.VartypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramrime.
    def visitParamrime(self, ctx:MT22Parser.ParamrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paraminher.
    def visitParaminher(self, ctx:MT22Parser.ParaminherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramout.
    def visitParamout(self, ctx:MT22Parser.ParamoutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcinher.
    def visitFuncinher(self, ctx:MT22Parser.FuncinherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elsestmt.
    def visitElsestmt(self, ctx:MT22Parser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhilestmt.
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#retexpr.
    def visitRetexpr(self, ctx:MT22Parser.RetexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprpime.
    def visitExprpime(self, ctx:MT22Parser.ExprpimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayele.
    def visitArrayele(self, ctx:MT22Parser.ArrayeleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funccall.
    def visitFunccall(self, ctx:MT22Parser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#types.
    def visitTypes(self, ctx:MT22Parser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomtype.
    def visitAtomtype(self, ctx:MT22Parser.AtomtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraytype.
    def visitArraytype(self, ctx:MT22Parser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimenslist.
    def visitDimenslist(self, ctx:MT22Parser.DimenslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#voidtype.
    def visitVoidtype(self, ctx:MT22Parser.VoidtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#autotype.
    def visitAutotype(self, ctx:MT22Parser.AutotypeContext):
        return self.visitChildren(ctx)



del MT22Parser