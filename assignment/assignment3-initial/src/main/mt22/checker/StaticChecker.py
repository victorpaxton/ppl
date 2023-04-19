from Visitor import Visitor
from AST import *
from StaticError import *


class FuncType(Type):
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class NoType(Type):
    pass


class Utils:
    def isNaN(e):
        return type(e) not in [IntegerType, FloatType]


class Symbol:
    def __init__(self, name, type, value=None):
        self.name = name
        self.type = type
        self.value = value


class GetEnv(Visitor):
    def __init__(self):
        pass

    # decls: List[Decl]
    def visitProgram(self, ctx: Program, o):
        o = []
        for decl in ctx.decls:
            if type(decl) is FuncDecl:
                o = self.visit(decl, o)

        return o

    # Declarations

    def visitVarDecl(self, ctx: VarDecl, o):
        pass

    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ctx: FuncDecl, o):
        for decl in o:
            if decl.name == ctx.name:
                return o

        return o + [ctx]


class StaticChecker(Visitor):
    # Program

    global_env = [
        FuncDecl("readInteger", IntegerType(), [], None, BlockStmt([])),
        FuncDecl("printInteger", VoidType(), [ParamDecl("", IntegerType())], None, BlockStmt([])),
        FuncDecl("readFloat", FloatType(), [], None, BlockStmt([])),
        FuncDecl("printFloat", VoidType(), [ParamDecl("", FloatType())], None, BlockStmt([])),
        FuncDecl("readBoolean", BooleanType(), [], None, BlockStmt([])),
        FuncDecl("printBoolean", VoidType(), [ParamDecl("", BooleanType())], None, BlockStmt([])),
        FuncDecl("readString", StringType(), [], None, BlockStmt([])),
        FuncDecl("printString", VoidType(), [ParamDecl("", StringType())], None, BlockStmt([])),
        FuncDecl("preventDefault", VoidType(), [], None, BlockStmt([])),
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, [])

    # decls: List[Decl]
    def visitProgram(self, ctx: Program, o):

        func_env = GetEnv().visit(ctx, []) + StaticChecker.global_env

        # Check for main function existence
        haveMain = False
        for decl in func_env:
            if decl.name == "main" and not decl.params and type(decl.return_type) is VoidType:
                haveMain = True
                break

        o = [[]] + [func_env]

        for decl in ctx.decls:
            o = self.visit(decl, o)

        if not haveMain:
            raise NoEntryPoint()

    # Declarations

    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ctx: VarDecl, o):
        print("at vardecl: ", o)
        for decl in o[0]:
            if decl.name == ctx.name:
                raise Redeclared(Variable(), ctx.name)

        if type(ctx.typ) is AutoType and ctx.init is None:
            raise Invalid(Variable(), ctx.name)

        if ctx.init is not None:
            expType = self.visit(ctx.init, o)

            if type(ctx.typ) is AutoType:
                ctx.typ = expType

            if type(expType) is IntegerType:
                if type(ctx.typ) not in [IntegerType, FloatType]:
                    raise TypeMismatchInVarDecl(ctx)

            elif type(expType) is not type(ctx.typ):
                raise TypeMismatchInVarDecl(ctx)

        o[0] += [ctx]

        return o

    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ctx: FuncDecl, o):
        for decl in o[0]:
            if decl.name == ctx.name:
                raise Redeclared(Function(), ctx.name)

        o[0] += [ctx]

        env = [[]] + o

        if ctx.inherit is not None:
            nullInherit = True
            for func_decl in o[-1]:
                if func_decl.name == ctx.inherit:
                    nullInherit = False
                    env[0] += [func_decl]

                    temp = []
                    for param_decl in func_decl.params:
                        for elem in temp:
                            if param_decl.name == elem:
                                raise Redeclared(Parameter(), param_decl.name)
                        temp += [param_decl.name]

                        if param_decl.inherit:
                            env[0] += [param_decl]

                    break

            if nullInherit:
                raise Undeclared(Function(), ctx.inherit)

        # params
        for param_decl in ctx.params:
            for inheritParam in env[0]:
                if param_decl.name == inheritParam.name:
                    raise Invalid(Parameter(), param_decl.name)
            env[0] += [param_decl]

        # check first statement
        print(ctx.name, ": ", env)

        flag = 0

        if ctx.inherit is not None:
            parent = env[0][0]

            # non-empty params list
            if parent.params:
                # empty body
                if not ctx.body.body:
                    raise InvalidStatementInFunction(ctx.name)

                # non-empty body
                firstStatement = ctx.body.body[0]

                if type(firstStatement) is not CallStmt:
                    raise InvalidStatementInFunction(ctx.name)

                if firstStatement.name == "super":

                    if len(firstStatement.args) >= len(parent.params):
                        for i in range(len(parent.params)):
                            argType = self.visit(firstStatement.args[i], env)
                            paramType = parent.params[i].typ
                            print(argType, paramType)
                            if type(paramType) is AutoType:
                                env[0][0].params[i].typ = argType
                            if type(argType) is IntegerType:
                                if type(paramType) not in [IntegerType, FloatType]:
                                    raise TypeMismatchInExpression(firstStatement.args[i])
                            elif type(argType) is not type(paramType):
                                raise TypeMismatchInExpression(firstStatement.args[i])

                        if len(firstStatement.args) > len(parent.params):
                            raise TypeMismatchInExpression(firstStatement.args[len(parent.params)])
                    else:
                        raise TypeMismatchInExpression()

                elif firstStatement.name == "preventDefault" and firstStatement.args:
                    raise InvalidStatementInFunction(ctx.name)

                else:
                    raise InvalidStatementInFunction(ctx.name)

                # continue from line 2
                flag = 1

            # empty params list
            else:
                # empty params list and non-empty body
                if ctx.body.body:
                    firstStatement = ctx.body.body[0]
                    if type(firstStatement) is CallStmt:
                        if firstStatement.name in ["super", "preventDefault"]:
                            if firstStatement.args:
                                raise InvalidStatementInFunction(ctx.name)
                            flag = 1

        # rest statements
        for stmt in ctx.body.body[flag:]:
            print(stmt)
            if type(stmt) is VarDecl:
                env = self.visit(stmt, env)
            else:
                # inLoop is False
                self.visit(stmt, (False, env))

        return o

    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ctx: ParamDecl, param):
        pass

    # Statements
    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast, param):
        print(ast.rhs, ast.lhs)
        print("param: ", param)
        ltype = self.visit(ast.lhs, param)
        rtype = self.visit(ast.rhs, param)

        print(rtype, ltype)

        if type(ltype) is VoidType:
            raise TypeMismatchInStatement(ast)

        if type(rtype) is IntegerType:
            if type(ltype) not in [IntegerType, FloatType]:
                raise TypeMismatchInStatement(ast)

        elif type(rtype) is not type(ltype):
            raise TypeMismatchInStatement(ast)

    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast, o):
        inLoop = o[0]
        env = [[]] + o[1]
        for stmt in ast.body:
            if type(stmt) is VarDecl:
                env = self.visit(stmt, env)
            else:
                self.visit(stmt, (inLoop, env))

        return o

    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast, o):
        inLoop, env = o

        condType = self.visit(ast.cond, env)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.tstmt, (inLoop, env))

        if ast.fstmt:
            self.visit(ast.fstmt, (inLoop, env))

    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast, o):
        inLoop, env = o

        print(ast.init)
        if type(self.visit(ast.init.lhs, env)) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        # type mismatch expression i error
        self.visit(ast.init, env)

        condType = self.visit(ast.cond, env)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        updType = self.visit(ast.upd, env)
        if type(updType) is not IntegerType:
            raise TypeMismatchInStatement(ast)

        # inLoop is True
        self.visit(ast.stmt, (True, env))

    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast, o):
        inLoop, env = o

        condType = self.visit(ast.cond, env)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, (True, env))

    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast, o):
        inLoop, env = o

        self.visit(ast.stmt, (True, env))

        condType = self.visit(ast.cond, env)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)

    def visitBreakStmt(self, ast, o):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast, o):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ast)

    # expr: Expr or None = None
    def visitReturnStmt(self, ast, o):
        if ast.expr:
            typeReturn = self.visit(ast.expr, o)
            return typeReturn
        return VoidType()

    # name: str, args: List[Expr]
    def visitCallStmt(self, ast, o):
        inLoop, env = o
        print("at callstmt: ", o)
        for decl in env[-1]:
            if decl.name == ast.name:

                # param type check
                # ..............
                print("decl: ", decl)
                print("ast: ", ast)
                if len(decl.params) != len(ast.args):
                    raise TypeMismatchInStatement(ast)

                for i in range(len(decl.params)):
                    argType = self.visit(ast.args[i], env)
                    paramType = decl.params[i].typ

                    if type(argType) is IntegerType:
                        if type(paramType) not in [IntegerType, FloatType]:
                            raise TypeMismatchInStatement(ast)
                    elif type(argType) is not type(paramType):
                        raise TypeMismatchInStatement(ast)

                return

        raise Undeclared(Function(), ast.name)

    # Expressions

    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ast, param):
        ltype = self.visit(ast.left, param)
        rtype = self.visit(ast.right, param)

        if ast.op in ["+", "-", "*"]:
            if Utils.isNaN(ltype) or Utils.isNaN(rtype):
                raise TypeMismatchInExpression(ast)
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType()
            if type(ltype) is FloatType or type(rtype) is FloatType:
                return FloatType()

        if ast.op in ["/"]:
            if Utils.isNaN(ltype) or Utils.isNaN(rtype):
                raise TypeMismatchInExpression(ast)
            return FloatType()

        if ast.op in ["%"]:
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ["&&", "||"]:
            if type(ltype) is BooleanType and type(rtype) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ["::"]:
            if type(ltype) is StringType and type(rtype) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ["==", "!="]:
            if (type(ltype) is IntegerType or type(ltype) is BooleanType) and (
                type(rtype) is IntegerType or type(rtype) is BooleanType
            ):
                return BooleanType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ["<", ">", "<=", ">="]:
            if Utils.isNaN(ltype) or Utils.isNaN(rtype):
                raise TypeMismatchInExpression(ast)
            return BooleanType()

    # op: str, val: Expr
    def visitUnExpr(self, ast, param):
        et = self.visit(ast.val, param)

        if ast.op in ["-"]:
            if type(et) is IntegerType:
                return IntegerType()
            if type(et) is FloatType:
                return FloatType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ["!"]:
            if type(et) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)

    def visitId(self, ast, o):
        print("o at id: ", o)
        if type(o) is tuple:
            env = o[1]
        else:
            env = o

        for env2 in env[:-1]:
            for decl in env2:
                if type(decl) is VarDecl and decl.name == ast.name:
                    return decl.typ

        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, param):
        pass

    def visitIntegerLit(self, ast, param):
        return IntegerType()

    def visitFloatLit(self, ast, param):
        return FloatType()

    def visitStringLit(self, ast, param):
        return StringType()

    def visitBooleanLit(self, ast, param):
        return BooleanType()

    # explist: List[Expr]
    def visitArrayLit(self, ast, param):
        explist = ast.explist

        if len(explist) == 0:
            return NoType()

        flag = self.visit(explist[0], param)

        for elem in explist[1:]:
            elemType = self.visit(elem, param)
            if type(elemType) is not type(flag):
                raise IllegalArrayLiteral(explist)

        return flag

    # name: str, args: List[Expr]
    def visitFuncCall(self, ast, o):
        print("at funccall: ", o)

        if type(o) is tuple:
            inLoop, env = o
        else:
            env = o

        for decl in env[-1]:
            if decl.name == ast.name:
                if decl.return_type is VoidType:
                    raise TypeMismatchInExpression(ast)

                # param type check
                # ..............
                print("decl: ", decl)
                print("ast: ", ast)
                if len(decl.params) != len(ast.args):
                    raise TypeMismatchInExpression(ast)

                for i in range(len(decl.params)):
                    argType = self.visit(ast.args[i], env)
                    paramType = decl.params[i].typ

                    if type(argType) is IntegerType:
                        if type(paramType) not in [IntegerType, FloatType]:
                            raise TypeMismatchInStatement(ast)
                    elif type(argType) is not type(paramType):
                        raise TypeMismatchInStatement(ast)

                return decl.return_type

        raise Undeclared(Function(), ast.name)

    # Types

    def visitIntegerType(self, ast, param):
        return IntegerType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBooleanType(self, ast, param):
        return BooleanType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        pass

    def visitAutoType(self, ast, param):
        return AutoType()

    def visitVoidType(self, ast, param):
        return VoidType()
