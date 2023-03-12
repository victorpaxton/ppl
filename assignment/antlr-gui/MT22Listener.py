# Generated from MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete listener for a parse tree produced by MT22Parser.
class MT22Listener(ParseTreeListener):

    # Enter a parse tree produced by MT22Parser#program.
    def enterProgram(self, ctx:MT22Parser.ProgramContext):
        pass

    # Exit a parse tree produced by MT22Parser#program.
    def exitProgram(self, ctx:MT22Parser.ProgramContext):
        pass


    # Enter a parse tree produced by MT22Parser#decllist.
    def enterDecllist(self, ctx:MT22Parser.DecllistContext):
        pass

    # Exit a parse tree produced by MT22Parser#decllist.
    def exitDecllist(self, ctx:MT22Parser.DecllistContext):
        pass


    # Enter a parse tree produced by MT22Parser#decl.
    def enterDecl(self, ctx:MT22Parser.DeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#decl.
    def exitDecl(self, ctx:MT22Parser.DeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#vardecl.
    def enterVardecl(self, ctx:MT22Parser.VardeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#vardecl.
    def exitVardecl(self, ctx:MT22Parser.VardeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#shortvardecl.
    def enterShortvardecl(self, ctx:MT22Parser.ShortvardeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#shortvardecl.
    def exitShortvardecl(self, ctx:MT22Parser.ShortvardeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#idlist.
    def enterIdlist(self, ctx:MT22Parser.IdlistContext):
        pass

    # Exit a parse tree produced by MT22Parser#idlist.
    def exitIdlist(self, ctx:MT22Parser.IdlistContext):
        pass


    # Enter a parse tree produced by MT22Parser#fullvardecl.
    def enterFullvardecl(self, ctx:MT22Parser.FullvardeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#fullvardecl.
    def exitFullvardecl(self, ctx:MT22Parser.FullvardeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#varinit.
    def enterVarinit(self, ctx:MT22Parser.VarinitContext):
        pass

    # Exit a parse tree produced by MT22Parser#varinit.
    def exitVarinit(self, ctx:MT22Parser.VarinitContext):
        pass


    # Enter a parse tree produced by MT22Parser#vartyp.
    def enterVartyp(self, ctx:MT22Parser.VartypContext):
        pass

    # Exit a parse tree produced by MT22Parser#vartyp.
    def exitVartyp(self, ctx:MT22Parser.VartypContext):
        pass


    # Enter a parse tree produced by MT22Parser#funcdecl.
    def enterFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#funcdecl.
    def exitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#paramlist.
    def enterParamlist(self, ctx:MT22Parser.ParamlistContext):
        pass

    # Exit a parse tree produced by MT22Parser#paramlist.
    def exitParamlist(self, ctx:MT22Parser.ParamlistContext):
        pass


    # Enter a parse tree produced by MT22Parser#paramrime.
    def enterParamrime(self, ctx:MT22Parser.ParamrimeContext):
        pass

    # Exit a parse tree produced by MT22Parser#paramrime.
    def exitParamrime(self, ctx:MT22Parser.ParamrimeContext):
        pass


    # Enter a parse tree produced by MT22Parser#param.
    def enterParam(self, ctx:MT22Parser.ParamContext):
        pass

    # Exit a parse tree produced by MT22Parser#param.
    def exitParam(self, ctx:MT22Parser.ParamContext):
        pass


    # Enter a parse tree produced by MT22Parser#paraminher.
    def enterParaminher(self, ctx:MT22Parser.ParaminherContext):
        pass

    # Exit a parse tree produced by MT22Parser#paraminher.
    def exitParaminher(self, ctx:MT22Parser.ParaminherContext):
        pass


    # Enter a parse tree produced by MT22Parser#paramout.
    def enterParamout(self, ctx:MT22Parser.ParamoutContext):
        pass

    # Exit a parse tree produced by MT22Parser#paramout.
    def exitParamout(self, ctx:MT22Parser.ParamoutContext):
        pass


    # Enter a parse tree produced by MT22Parser#funcinher.
    def enterFuncinher(self, ctx:MT22Parser.FuncinherContext):
        pass

    # Exit a parse tree produced by MT22Parser#funcinher.
    def exitFuncinher(self, ctx:MT22Parser.FuncinherContext):
        pass


    # Enter a parse tree produced by MT22Parser#stmtlist.
    def enterStmtlist(self, ctx:MT22Parser.StmtlistContext):
        pass

    # Exit a parse tree produced by MT22Parser#stmtlist.
    def exitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        pass


    # Enter a parse tree produced by MT22Parser#stmt.
    def enterStmt(self, ctx:MT22Parser.StmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#stmt.
    def exitStmt(self, ctx:MT22Parser.StmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#blockstmt.
    def enterBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#blockstmt.
    def exitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#assignstmt.
    def enterAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#assignstmt.
    def exitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#lhs.
    def enterLhs(self, ctx:MT22Parser.LhsContext):
        pass

    # Exit a parse tree produced by MT22Parser#lhs.
    def exitLhs(self, ctx:MT22Parser.LhsContext):
        pass


    # Enter a parse tree produced by MT22Parser#ifstmt.
    def enterIfstmt(self, ctx:MT22Parser.IfstmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#ifstmt.
    def exitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#elsestmt.
    def enterElsestmt(self, ctx:MT22Parser.ElsestmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#elsestmt.
    def exitElsestmt(self, ctx:MT22Parser.ElsestmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#forstmt.
    def enterForstmt(self, ctx:MT22Parser.ForstmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#forstmt.
    def exitForstmt(self, ctx:MT22Parser.ForstmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#whilestmt.
    def enterWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#whilestmt.
    def exitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#dowhilestmt.
    def enterDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#dowhilestmt.
    def exitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#breakstmt.
    def enterBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#breakstmt.
    def exitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#continuestmt.
    def enterContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#continuestmt.
    def exitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#returnstmt.
    def enterReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#returnstmt.
    def exitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#callstmt.
    def enterCallstmt(self, ctx:MT22Parser.CallstmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#callstmt.
    def exitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#specialcall.
    def enterSpecialcall(self, ctx:MT22Parser.SpecialcallContext):
        pass

    # Exit a parse tree produced by MT22Parser#specialcall.
    def exitSpecialcall(self, ctx:MT22Parser.SpecialcallContext):
        pass


    # Enter a parse tree produced by MT22Parser#readIntegerfun.
    def enterReadIntegerfun(self, ctx:MT22Parser.ReadIntegerfunContext):
        pass

    # Exit a parse tree produced by MT22Parser#readIntegerfun.
    def exitReadIntegerfun(self, ctx:MT22Parser.ReadIntegerfunContext):
        pass


    # Enter a parse tree produced by MT22Parser#printIntegerfun.
    def enterPrintIntegerfun(self, ctx:MT22Parser.PrintIntegerfunContext):
        pass

    # Exit a parse tree produced by MT22Parser#printIntegerfun.
    def exitPrintIntegerfun(self, ctx:MT22Parser.PrintIntegerfunContext):
        pass


    # Enter a parse tree produced by MT22Parser#readFloatfun.
    def enterReadFloatfun(self, ctx:MT22Parser.ReadFloatfunContext):
        pass

    # Exit a parse tree produced by MT22Parser#readFloatfun.
    def exitReadFloatfun(self, ctx:MT22Parser.ReadFloatfunContext):
        pass


    # Enter a parse tree produced by MT22Parser#printFloatfun.
    def enterPrintFloatfun(self, ctx:MT22Parser.PrintFloatfunContext):
        pass

    # Exit a parse tree produced by MT22Parser#printFloatfun.
    def exitPrintFloatfun(self, ctx:MT22Parser.PrintFloatfunContext):
        pass


    # Enter a parse tree produced by MT22Parser#readBooleanfun.
    def enterReadBooleanfun(self, ctx:MT22Parser.ReadBooleanfunContext):
        pass

    # Exit a parse tree produced by MT22Parser#readBooleanfun.
    def exitReadBooleanfun(self, ctx:MT22Parser.ReadBooleanfunContext):
        pass


    # Enter a parse tree produced by MT22Parser#printBooleanfun.
    def enterPrintBooleanfun(self, ctx:MT22Parser.PrintBooleanfunContext):
        pass

    # Exit a parse tree produced by MT22Parser#printBooleanfun.
    def exitPrintBooleanfun(self, ctx:MT22Parser.PrintBooleanfunContext):
        pass


    # Enter a parse tree produced by MT22Parser#readStringfun.
    def enterReadStringfun(self, ctx:MT22Parser.ReadStringfunContext):
        pass

    # Exit a parse tree produced by MT22Parser#readStringfun.
    def exitReadStringfun(self, ctx:MT22Parser.ReadStringfunContext):
        pass


    # Enter a parse tree produced by MT22Parser#printStringfun.
    def enterPrintStringfun(self, ctx:MT22Parser.PrintStringfunContext):
        pass

    # Exit a parse tree produced by MT22Parser#printStringfun.
    def exitPrintStringfun(self, ctx:MT22Parser.PrintStringfunContext):
        pass


    # Enter a parse tree produced by MT22Parser#superfun.
    def enterSuperfun(self, ctx:MT22Parser.SuperfunContext):
        pass

    # Exit a parse tree produced by MT22Parser#superfun.
    def exitSuperfun(self, ctx:MT22Parser.SuperfunContext):
        pass


    # Enter a parse tree produced by MT22Parser#preventDefaultfun.
    def enterPreventDefaultfun(self, ctx:MT22Parser.PreventDefaultfunContext):
        pass

    # Exit a parse tree produced by MT22Parser#preventDefaultfun.
    def exitPreventDefaultfun(self, ctx:MT22Parser.PreventDefaultfunContext):
        pass


    # Enter a parse tree produced by MT22Parser#exprlist.
    def enterExprlist(self, ctx:MT22Parser.ExprlistContext):
        pass

    # Exit a parse tree produced by MT22Parser#exprlist.
    def exitExprlist(self, ctx:MT22Parser.ExprlistContext):
        pass


    # Enter a parse tree produced by MT22Parser#exprprime.
    def enterExprprime(self, ctx:MT22Parser.ExprprimeContext):
        pass

    # Exit a parse tree produced by MT22Parser#exprprime.
    def exitExprprime(self, ctx:MT22Parser.ExprprimeContext):
        pass


    # Enter a parse tree produced by MT22Parser#expr.
    def enterExpr(self, ctx:MT22Parser.ExprContext):
        pass

    # Exit a parse tree produced by MT22Parser#expr.
    def exitExpr(self, ctx:MT22Parser.ExprContext):
        pass


    # Enter a parse tree produced by MT22Parser#expr1.
    def enterExpr1(self, ctx:MT22Parser.Expr1Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr1.
    def exitExpr1(self, ctx:MT22Parser.Expr1Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr2.
    def enterExpr2(self, ctx:MT22Parser.Expr2Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr2.
    def exitExpr2(self, ctx:MT22Parser.Expr2Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr3.
    def enterExpr3(self, ctx:MT22Parser.Expr3Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr3.
    def exitExpr3(self, ctx:MT22Parser.Expr3Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr4.
    def enterExpr4(self, ctx:MT22Parser.Expr4Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr4.
    def exitExpr4(self, ctx:MT22Parser.Expr4Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr5.
    def enterExpr5(self, ctx:MT22Parser.Expr5Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr5.
    def exitExpr5(self, ctx:MT22Parser.Expr5Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr6.
    def enterExpr6(self, ctx:MT22Parser.Expr6Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr6.
    def exitExpr6(self, ctx:MT22Parser.Expr6Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr7.
    def enterExpr7(self, ctx:MT22Parser.Expr7Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr7.
    def exitExpr7(self, ctx:MT22Parser.Expr7Context):
        pass


    # Enter a parse tree produced by MT22Parser#subexpr.
    def enterSubexpr(self, ctx:MT22Parser.SubexprContext):
        pass

    # Exit a parse tree produced by MT22Parser#subexpr.
    def exitSubexpr(self, ctx:MT22Parser.SubexprContext):
        pass


    # Enter a parse tree produced by MT22Parser#arrayele.
    def enterArrayele(self, ctx:MT22Parser.ArrayeleContext):
        pass

    # Exit a parse tree produced by MT22Parser#arrayele.
    def exitArrayele(self, ctx:MT22Parser.ArrayeleContext):
        pass


    # Enter a parse tree produced by MT22Parser#funccall.
    def enterFunccall(self, ctx:MT22Parser.FunccallContext):
        pass

    # Exit a parse tree produced by MT22Parser#funccall.
    def exitFunccall(self, ctx:MT22Parser.FunccallContext):
        pass


    # Enter a parse tree produced by MT22Parser#types.
    def enterTypes(self, ctx:MT22Parser.TypesContext):
        pass

    # Exit a parse tree produced by MT22Parser#types.
    def exitTypes(self, ctx:MT22Parser.TypesContext):
        pass


    # Enter a parse tree produced by MT22Parser#atomtype.
    def enterAtomtype(self, ctx:MT22Parser.AtomtypeContext):
        pass

    # Exit a parse tree produced by MT22Parser#atomtype.
    def exitAtomtype(self, ctx:MT22Parser.AtomtypeContext):
        pass


    # Enter a parse tree produced by MT22Parser#arraytype.
    def enterArraytype(self, ctx:MT22Parser.ArraytypeContext):
        pass

    # Exit a parse tree produced by MT22Parser#arraytype.
    def exitArraytype(self, ctx:MT22Parser.ArraytypeContext):
        pass


    # Enter a parse tree produced by MT22Parser#dimenslist.
    def enterDimenslist(self, ctx:MT22Parser.DimenslistContext):
        pass

    # Exit a parse tree produced by MT22Parser#dimenslist.
    def exitDimenslist(self, ctx:MT22Parser.DimenslistContext):
        pass


    # Enter a parse tree produced by MT22Parser#arraylit.
    def enterArraylit(self, ctx:MT22Parser.ArraylitContext):
        pass

    # Exit a parse tree produced by MT22Parser#arraylit.
    def exitArraylit(self, ctx:MT22Parser.ArraylitContext):
        pass


    # Enter a parse tree produced by MT22Parser#voidtype.
    def enterVoidtype(self, ctx:MT22Parser.VoidtypeContext):
        pass

    # Exit a parse tree produced by MT22Parser#voidtype.
    def exitVoidtype(self, ctx:MT22Parser.VoidtypeContext):
        pass


    # Enter a parse tree produced by MT22Parser#autotype.
    def enterAutotype(self, ctx:MT22Parser.AutotypeContext):
        pass

    # Exit a parse tree produced by MT22Parser#autotype.
    def exitAutotype(self, ctx:MT22Parser.AutotypeContext):
        pass



del MT22Parser