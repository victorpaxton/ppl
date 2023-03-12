from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decllist  EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))

    # decllist: decl decllist | decl ;
    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decllist())

    # decl: vardecl | funcdecl ;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return self.visitChildren(ctx)

    #################### Variable Declaration #######################################

    # vardecl: shortvardecl | fullvardecl ;
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        return self.visitChildren(ctx)

    # fullvardecl: varinit SEMI ;
    def visitFullvardecl(self, ctx: MT22Parser.FullvardeclContext):
        return self.visit(ctx.varinit())

    # varinit: IDENTIFIER COMMA varinit COMMA expr | IDENTIFIER COLON vartyp EQ expr ;
    # x, y: integer = 2022, 2023;
    def visitVarinitHelper(self, ctx: MT22Parser.VarinitContext, idlist, exprlist, vartyp):
        if ctx.EQ():
            idlist = idlist + [ctx.IDENTIFIER().getText()]
            exprlist = [self.visit(ctx.expr())] + exprlist
            vartyp = self.visit(ctx.vartyp())
            return (idlist, exprlist, vartyp)
        else:
            idlist = idlist + [ctx.IDENTIFIER().getText()]
            exprlist = [self.visit(ctx.expr())] + exprlist
            return self.visitVarinitHelper(ctx.varinit(), idlist, exprlist, vartyp)

    def visitVarinit(self, ctx: MT22Parser.VarinitContext):
        # result = (idlist, exprlist, vartyp)
        result = self.visitVarinitHelper(ctx, [], [], Type())
        idlist = result[0]
        exprlist = result[1]
        vartyp = result[2]
        return list(map(lambda id, init: VarDecl(id, vartyp, init), idlist, exprlist))

    # shortvardecl: idlist COLON vartyp SEMI;
    def visitShortvardecl(self, ctx: MT22Parser.ShortvardeclContext):
        idlist = self.visit(ctx.idlist())
        vartyp = self.visit(ctx.vartyp())
        return list(map(lambda id: VarDecl(id, vartyp), idlist))

    #################### Function Declaration #######################################

    # funcdecl: IDENTIFIER COLON FUNCTION types LB paramlist RB funcinher blockstmt;
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        return [
            FuncDecl(
                ctx.IDENTIFIER().getText(),
                self.visit(ctx.types()),
                self.visit(ctx.paramlist()),
                self.visit(ctx.funcinher()),
                self.visit(ctx.blockstmt()),
            )
        ]

    # paramlist: paramrime | ;
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramrime())

    # paramrime: param COMMA paramrime | param ;
    def visitParamrime(self, ctx: MT22Parser.ParamrimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        return [self.visit(ctx.param())] + self.visit(ctx.paramrime())

    # param: (INHERIT | ) (OUT | ) IDENTIFIER COLON vartyp;
    def visitParam(self, ctx: MT22Parser.ParamContext):
        return ParamDecl(
            ctx.IDENTIFIER().getText(),
            self.visit(ctx.vartyp()),
            True if ctx.OUT() else False,
            True if ctx.INHERIT() else False,
        )

    # funcinher: INHERIT IDENTIFIER | ;
    def visitFuncinher(self, ctx: MT22Parser.FuncinherContext):
        if ctx.INHERIT():
            return ctx.IDENTIFIER().getText()
        return None

    #################### Types #######################################
    # types: atomtype | arraytype | voidtype | autotype;
    def visitTypes(self, ctx: MT22Parser.TypesContext):
        return self.visitChildren(ctx)

    # vartyp: atomtype | arraytype | autotype ;
    def visitVartyp(self, ctx: MT22Parser.VartypContext):
        return self.visitChildren(ctx)

    # atomtype: BOOLEAN | INTEGER | FLOAT | STRING ;
    def visitAtomtype(self, ctx: MT22Parser.AtomtypeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        return StringType()

    def visitVoidtype(self, ctx: MT22Parser.VoidtypeContext):
        return VoidType()

    # arraytype: ARRAY LSB dimenslist RSB OF atomtype;
    def visitArraytype(self, ctx: MT22Parser.ArraytypeContext):
        return ArrayType(self.visit(ctx.dimenslist()), self.visit(ctx.atomtype()))

    # dimenslist: INTLIT COMMA dimenslist | INTLIT;
    def visitDimenslist(self, ctx: MT22Parser.DimenslistContext):
        if ctx.getChildCount() == 1:
            return [IntegerLit(int(ctx.INTLIT().getText()))]
        return [IntegerLit(int(ctx.INTLIT().getText()))] + self.visit(ctx.dimenslist())

    # autotype: AUTO;
    def visitAutotype(self, ctx: MT22Parser.AutotypeContext):
        return AutoType()

    # idlist: IDENTIFIER COMMA idlist | IDENTIFIER ;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        return [ctx.IDENTIFIER().getText()] + self.visit(ctx.idlist())

    #################### Statements #######################################
    # stmtlist: stmt stmtlist | ;
    def visitStmtlist(self, ctx: MT22Parser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())

    # stmt: blockstmt | vardecl | assignstmt | ifstmt | forstmt | whilestmt | dowhilestmt | breakstmt | continuestmt | returnstmt | callstmt  ;
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visitChildren(ctx)

    # blockstmt: LP stmtlist RP;
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        return BlockStmt(self.visit(ctx.stmtlist()))

    # assignstmt: lhs EQ expr SEMI;
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    # lhs: IDENTIFIER | arrayele;
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        return Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitArrayele(ctx.arrayele())

    # ifstmt: IF LB expr RB stmt (ELSE stmt | );
    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()[0]), self.visit(ctx.stmt()[1]))
        return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()[0]))

    # forstmt: FOR LB assignstmt COMMA expr COMMA expr RB stmt;
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        return ForStmt(
            self.visit(ctx.assignstmt()), self.visit(ctx.expr()[0]), self.visit(ctx.expr()[1]), self.visit(ctx.stmt())
        )

    # whilestmt: WHILE LB expr RB stmt;
    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))

    # dowhilestmt: DO blockstmt WHILE LB expr RB SEMI;
    def visitDowhilestmt(self, ctx: MT22Parser.DowhilestmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockstmt()))

    # breakstmt: BREAK SEMI ;
    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()

    # continuestmt: CONTINUE SEMI ;
    def visitContinuestmt(self, ctx: MT22Parser.ContinuestmtContext):
        return ContinueStmt()

    # returnstmt: RETURN (expr | ) SEMI;
    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        return ReturnStmt() if ctx.getChildCount() == 2 else ReturnStmt(self.visit(ctx.expr()))

    # callstmt: IDENTIFIER LB exprlist RB SEMI;
    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        return CallStmt(ctx.IDENTIFIER().getText(), self.visit(ctx.exprlist()))

    #################### Expression #######################################
    # exprlist: exprprime | ;
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.exprprime())

    # exprprime: expr COMMA exprprime | expr ;
    def visitExprprime(self, ctx: MT22Parser.ExprprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())

    # expr: expr1 CONCAT expr1 | expr1 ;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.CONCAT().getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    # expr1: expr2 (EQUAL | NOT_EQUAL | LT | GT | LE | GE) expr2 | expr2 ;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        if ctx.EQUAL():
            return BinExpr(ctx.EQUAL().getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        if ctx.NOT_EQUAL():
            return BinExpr(ctx.NOT_EQUAL().getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        if ctx.LT():
            return BinExpr(ctx.LT().getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        if ctx.GT():
            return BinExpr(ctx.GT().getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        if ctx.LE():
            return BinExpr(ctx.LE().getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        if ctx.GE():
            return BinExpr(ctx.GE().getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    # expr2: expr2 (AND | OR) expr3 | expr3 ;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        if ctx.AND():
            return BinExpr(ctx.AND().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return BinExpr(ctx.OR().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))

    # expr3: expr3 (ADD | SUB) expr4 | expr4 ;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        if ctx.ADD():
            return BinExpr(ctx.ADD().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return BinExpr(ctx.SUB().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))

    # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5 ;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        if ctx.MUL():
            return BinExpr(ctx.MUL().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        if ctx.DIV():
            return BinExpr(ctx.DIV().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))

        return BinExpr(ctx.MOD().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))

    # expr5: NOT expr5 | expr6 ;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        return UnExpr(ctx.NOT().getText(), self.visit(ctx.expr5()))

    # expr6: SUB expr6 | expr7 ;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        return UnExpr(ctx.SUB().getText(), self.visit(ctx.expr6()))

    # expr7: subexpr | arrayele | funccall | IDENTIFIER | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arraylit;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        if ctx.BOOLLIT():
            return BooleanLit(True if ctx.BOOLLIT().getText() == "True" else False)
        if ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.subexpr():
            return self.visit(ctx.subexpr())
        if ctx.arrayele():
            return self.visit(ctx.arrayele())
        if ctx.funccall():
            return self.visit(ctx.funccall())
        return self.visit(ctx.arraylit())

    # subexpr: LB expr RB;
    def visitSubexpr(self, ctx: MT22Parser.SubexprContext):
        return self.visit(ctx.expr())

    # arrayele: IDENTIFIER LSB exprlist RSB ;
    def visitArrayele(self, ctx: MT22Parser.ArrayeleContext):
        return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.exprlist()))

    # funccall: IDENTIFIER LB exprlist RB;
    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        return FuncCall(ctx.IDENTIFIER().getText(), self.visit(ctx.exprlist()))
