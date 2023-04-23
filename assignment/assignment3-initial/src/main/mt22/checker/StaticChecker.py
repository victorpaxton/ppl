from Visitor import Visitor
from AST import *
from StaticError import *


class FuncType(Type):
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class NoType(Type):
    pass


# NumberType is IntegerType or FloatType
class NumberType(Type):
    pass


class Utils:
    def isNaN(e):
        return type(e) not in [IntegerType, FloatType]

    def inferType(o, name, typ):
        for env in o[:-1]:
            for decl in env:
                if decl.name == name:
                    if type(decl) in [VarDecl, ParamDecl]:
                        decl.typ = typ
                        return typ
                    elif type(decl) is FuncDecl:
                        decl.return_type = typ
                        for decl2 in o[-1]:
                            if decl2.name == name:
                                decl2.return_type = typ
                        return typ

    def isSameArrayType(left, right):
        return left.dimensions == right.dimensions and type(left.typ) is type(right.typ)


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
        # print("at vardecl: ", o)
        for decl in o[0]:
            if decl.name == ctx.name:
                raise Redeclared(Variable(), ctx.name)

        if type(ctx.typ) is AutoType and ctx.init is None:
            raise Invalid(Variable(), ctx.name)

        if ctx.init is not None:
            expType = self.visit(ctx.init, o)

            # print("*** :", ctx.name)
            # print("expType: ", expType)
            # print("ctx.typ: ", ctx.typ)

            if type(ctx.typ) is AutoType:
                ctx.typ = expType
            elif type(ctx.typ) is ArrayType:
                if type(expType) is not ArrayType or not Utils.isSameArrayType(ctx.typ, expType):
                    raise TypeMismatchInVarDecl(ctx)

            if type(expType) is AutoType:
                expType = Utils.inferType(o, ctx.init.name, ctx.typ)
            elif type(expType) is IntegerType:
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

                    # check for redeclared parameters in the inherit function
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
        # check for redeclared parameters
        temp = []
        for param_decl in ctx.params:
            for elem in temp:
                if param_decl.name == elem:
                    raise Redeclared(Parameter(), param_decl.name)
            temp += [param_decl.name]

        # check for invalid
        for param_decl in ctx.params:
            for inheritParam in env[0]:
                if param_decl.name == inheritParam.name:
                    raise Invalid(Parameter(), param_decl.name)
            env[0] += [param_decl]

        # check first statement
        # print(ctx.name, ": ********** ", env)

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
                            # print(argType, paramType)
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
        returned = False
        # Return at another statements: for, while, assign, if, .... (not yet)

        for stmt in ctx.body.body[flag:]:
            # print(stmt)
            if type(stmt) is VarDecl:
                env = self.visit(stmt, env)
            elif type(stmt) is ReturnStmt:
                # directly return statement, only the first
                if not returned:
                    returned = True
                    retExpType = self.visit(stmt, env)

                    if type(ctx.return_type) is AutoType:
                        if type(retExpType) is not AutoType:
                            ctx.return_type = Utils.inferType(env, ctx.name, retExpType)

                    if type(retExpType) is IntegerType:
                        if type(ctx.return_type) not in [IntegerType, FloatType]:
                            raise TypeMismatchInStatement(stmt)
                    elif type(ctx.return_type) is not type(retExpType):
                        raise TypeMismatchInStatement(stmt)
                else:
                    continue
            else:
                # inLoop is False
                self.visit(stmt, (ctx, False, env))

        return o

    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ctx: ParamDecl, param):
        pass

    # Statements
    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast, param):
        # print(ast.rhs, ast.lhs)
        # print("param: ", param)
        ltype = self.visit(ast.lhs, param)
        rtype = self.visit(ast.rhs, param)

        # print(rtype, ltype)
        if type(ltype) is AutoType:
            ltype = Utils.inferType(param[2], ast.lhs.name, rtype)
        elif type(ltype) is VoidType:
            raise TypeMismatchInStatement(ast)

        if type(rtype) is AutoType:
            rtype = Utils.inferType(param[2], ast.rhs.name, ltype)
        elif type(rtype) is IntegerType:
            if type(ltype) not in [IntegerType, FloatType]:
                raise TypeMismatchInStatement(ast)

        elif type(rtype) is not type(ltype):
            raise TypeMismatchInStatement(ast)

    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast, o):
        inFunction = o[0]
        inLoop = o[1]
        env = [[]] + o[2]
        returned = False
        for stmt in ast.body:
            if type(stmt) is VarDecl:
                env = self.visit(stmt, env)
            elif type(stmt) is ReturnStmt:
                # directly return statement, only the first
                if not returned:
                    returned = True
                    retExpType = self.visit(stmt, env)

                    if type(inFunction.return_type) is AutoType:
                        inFunction.return_type = Utils.inferType(env, inFunction.name, retExpType)
                    if type(retExpType) is IntegerType:
                        if type(inFunction.return_type) not in [IntegerType, FloatType]:
                            raise TypeMismatchInStatement(stmt)
                    elif type(inFunction.return_type) is not type(retExpType):
                        raise TypeMismatchInStatement(stmt)
                else:
                    continue
            else:
                self.visit(stmt, (inFunction, inLoop, env))

        return o

    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast, o):
        inFunction, inLoop, env = o

        condType = self.visit(ast.cond, env)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        if type(ast.tstmt) is ReturnStmt:
            retExpType = self.visit(ast.tstmt, (inFunction, inLoop, env))

            if type(inFunction.return_type) is AutoType:
                inFunction.return_type = Utils.inferType(env, inFunction.name, retExpType)
            if type(retExpType) is IntegerType:
                if type(inFunction.return_type) not in [IntegerType, FloatType]:
                    raise TypeMismatchInStatement(ast.tstmt)
            elif type(inFunction.return_type) is not type(retExpType):
                raise TypeMismatchInStatement(ast.tstmt)

        else:
            self.visit(ast.tstmt, (inFunction, inLoop, env))

        # have false stmt
        if ast.fstmt:

            if type(ast.fstmt) is ReturnStmt:
                retExpType = self.visit(ast.fstmt, (inFunction, inLoop, env))

                if type(inFunction.return_type) is AutoType:
                    inFunction.return_type = Utils.inferType(env, inFunction.name, retExpType)
                if type(retExpType) is IntegerType:
                    if type(inFunction.return_type) not in [IntegerType, FloatType]:
                        raise TypeMismatchInStatement(ast.fstmt)
                elif type(inFunction.return_type) is not type(retExpType):
                    raise TypeMismatchInStatement(ast.fstmt)

            else:
                self.visit(ast.fstmt, (inFunction, inLoop, env))

    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast, o):
        inFunction, inLoop, env = o

        # print(ast.init)
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
        if type(ast.stmt) is ReturnStmt:
            retExpType = self.visit(ast.stmt, (inFunction, inLoop, env))

            if type(inFunction.return_type) is AutoType:
                inFunction.return_type = Utils.inferType(env, inFunction.name, retExpType)
            if type(retExpType) is IntegerType:
                if type(inFunction.return_type) not in [IntegerType, FloatType]:
                    raise TypeMismatchInStatement(ast.stmt)
            elif type(inFunction.return_type) is not type(retExpType):
                raise TypeMismatchInStatement(ast.stmt)
        else:
            self.visit(ast.stmt, (inFunction, True, env))

    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast, o):
        inFunction, inLoop, env = o

        condType = self.visit(ast.cond, env)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        if type(ast.stmt) is ReturnStmt:
            retExpType = self.visit(ast.stmt, (inFunction, inLoop, env))

            if type(inFunction.return_type) is AutoType:
                inFunction.return_type = Utils.inferType(env, inFunction.name, retExpType)
            if type(retExpType) is IntegerType:
                if type(inFunction.return_type) not in [IntegerType, FloatType]:
                    raise TypeMismatchInStatement(ast.stmt)
            elif type(inFunction.return_type) is not type(retExpType):
                raise TypeMismatchInStatement(ast.stmt)
        else:
            self.visit(ast.stmt, (inFunction, True, env))

    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast, o):
        inFunction, inLoop, env = o

        if type(ast.stmt) is ReturnStmt:
            retExpType = self.visit(ast.stmt, (inFunction, inLoop, env))

            if type(inFunction.return_type) is AutoType:
                inFunction.return_type = Utils.inferType(env, inFunction.name, retExpType)
            if type(retExpType) is IntegerType:
                if type(inFunction.return_type) not in [IntegerType, FloatType]:
                    raise TypeMismatchInStatement(ast.stmt)
            elif type(inFunction.return_type) is not type(retExpType):
                raise TypeMismatchInStatement(ast.stmt)
        else:
            self.visit(ast.stmt, (inFunction, True, env))

        condType = self.visit(ast.cond, env)
        if type(condType) is not BooleanType:
            raise TypeMismatchInStatement(ast)

    def visitBreakStmt(self, ast, o):
        inFunction, inLoop, env = o
        if not inLoop:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast, o):
        inFunction, inLoop, env = o
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
        inFunction, inLoop, env = o
        # print("at callstmt: ", o)

        # check if name of function is redeclared for an identifier in local
        for decl in env[0]:
            if decl.name == ast.name:
                raise Undeclared(Function(), ast.name)

        for decl in env[-1]:
            if decl.name == ast.name:

                # param type check
                # ..............
                # print("decl: ", decl)
                # print("ast: ", ast)
                if len(decl.params) != len(ast.args):
                    raise TypeMismatchInStatement(ast)

                for i in range(len(decl.params)):
                    argType = self.visit(ast.args[i], env)
                    paramType = decl.params[i].typ

                    if type(paramType) is AutoType:
                        decl.params[i].typ = argType
                        paramType = Utils.inferType(env, decl.name, argType)

                    if type(argType) is IntegerType:
                        if type(paramType) not in [IntegerType, FloatType]:
                            raise TypeMismatchInStatement(ast)
                    elif type(argType) is ArrayType:
                        if type(paramType) is not ArrayType or not Utils.isSameArrayType(argType, paramType):
                            raise TypeMismatchInStatement(ast)
                    elif type(argType) is not type(paramType):
                        raise TypeMismatchInStatement(ast)

                if decl.return_type is AutoType:
                    decl.return_type = VoidType()
                    Utils.infer(env, decl.name, VoidType())

                return

        raise Undeclared(Function(), ast.name)

    # Expressions

    # op: str, left: Expr, right: Expr

    def visitBinExpr(self, ast, param):
        if type(param) is tuple:
            inFunction, inLoop, env = param
        else:
            env = param

        ltype = self.visit(ast.left, param)
        rtype = self.visit(ast.right, param)

        if ast.op in ["+", "-", "*"]:
            if type(ltype) in [IntegerType, FloatType, AutoType] and type(rtype) in [IntegerType, FloatType, AutoType]:
                if type(ltype) is AutoType or type(rtype) is AutoType:
                    return AutoType()
                if type(ltype) is IntegerType and type(rtype) is IntegerType:
                    return IntegerType()
                return FloatType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ["/"]:
            if type(ltype) in [IntegerType, FloatType, AutoType] and type(ltype) in [IntegerType, FloatType, AutoType]:
                return FloatType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ["%"]:
            if type(ltype) is AutoType:
                ltype = Utils.inferType(env, ast.left.name, IntegerType())
            if type(rtype) is AutoType:
                rtype = Utils.inferType(env, ast.right.name, IntegerType())

            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ["&&", "||"]:
            if type(ltype) is AutoType:
                ltype = Utils.inferType(env, ast.left.name, BooleanType())
            if type(rtype) is AutoType:
                rtype = Utils.inferType(env, ast.right.name, BooleanType())

            if type(ltype) is BooleanType and type(rtype) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ["::"]:
            if type(ltype) is AutoType:
                ltype = Utils.inferType(env, ast.left.name, StringType())
            if type(rtype) is AutoType:
                rtype = Utils.inferType(env, ast.right.name, StringType())

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
            if type(et) is AutoType:
                return AutoType()
            if type(et) is IntegerType:
                return IntegerType()
            if type(et) is FloatType:
                return FloatType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ["!"]:
            if type(et) is AutoType:
                et = Utils.inferType(param, ast.val.name, BooleanType())

            if type(et) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)

    def visitId(self, ast, o):
        # print("o at id: ", o)
        if type(o) is tuple:
            env = o[2]
        else:
            env = o

        for env2 in env[:-1]:
            for decl in env2:
                if type(decl) in [VarDecl, ParamDecl] and decl.name == ast.name:
                    return decl.typ

        raise Undeclared(Identifier(), ast.name)

    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast, o):
        if type(o) is tuple:
            inFunction, inLoop, env = o
        else:
            env = o

        for env2 in env[:-1]:
            for decl in env2:
                if decl.name == ast.name:
                    # print("array cell: ", ast)
                    # print("decl: ", decl)

                    if type(decl.typ) is not ArrayType:
                        raise TypeMismatchInExpression(ast)
                    else:
                        if len(ast.cell) > len(decl.typ.dimensions):
                            raise TypeMismatchInExpression(ast)

                        for exp in ast.cell:
                            expType = self.visit(exp, env)
                            if type(expType) is not IntegerType:
                                raise TypeMismatchInExpression(ast)

                        if len(ast.cell) == len(decl.typ.dimensions):
                            return decl.typ.typ
                        flag = len(ast.cell)
                        return ArrayType(decl.typ.dimensions[flag:], decl.typ.typ)

        raise Undeclared(Identifier(), ast.name)

    def visitIntegerLit(self, ast, param):
        return IntegerType()

    def visitFloatLit(self, ast, param):
        return FloatType()

    def visitStringLit(self, ast, param):
        return StringType()

    def visitBooleanLit(self, ast, param):
        return BooleanType()

    # arraylit: {{0, 1, 2}, {3, 4, 5}}
    # => ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])])
    # => typ: ArrayType([2, 3], IntegerType)

    # arraylit: {{{4, 8},{2, 4},{1, 6}}, {{3, 6},{5, 4},{9, 3}}}
    # => ArrayLit([ArrayLit([ArrayLit([IntegerLit(4), IntegerLit(8)]), ArrayLit([IntegerLit(2), IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(6)])]), ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(6)]), ArrayLit([IntegerLit(5), IntegerLit(4)]), ArrayLit([IntegerLit(9), IntegerLit(3)])])])
    # => typ: ArrayType([2, 3, 2], IntegerType)

    # explist: List[Expr]
    def visitArrayLit(self, ast, param):
        return self.visitArrayLitHelper(ast, (ast, param))

    def visitArrayLitHelper(self, ast, param):
        rootAst, env = param

        if type(ast.explist[0]) is ArrayLit:
            first = self.visitArrayLitHelper(ast.explist[0], (rootAst, env))
        else:
            first = self.visit(ast.explist[0], env)

        for elem in ast.explist[1:]:
            if type(elem) is ArrayLit:
                elemType = self.visitArrayLitHelper(elem, (rootAst, env))
            else:
                elemType = self.visit(elem, env)

            # print("first: ", first)
            # print("elem: ", elem)
            # print("elemType: ", elemType)
            # print("----")

            if type(first) is ArrayType and type(elemType) is ArrayType:
                if not Utils.isSameArrayType(first, elemType):
                    raise IllegalArrayLiteral(rootAst)

            elif type(first) is not type(elemType):
                raise IllegalArrayLiteral(rootAst)

        if type(first) is ArrayType:
            return ArrayType([len(ast.explist)] + first.dimensions, first.typ)
        return ArrayType([len(ast.explist)], first)

    # name: str, args: List[Expr]
    def visitFuncCall(self, ast, o):
        # print("at funccall: ", o)

        if type(o) is tuple:
            inFunction, inLoop, env = o
        else:
            env = o

        # check if name of function is redeclared for an identifier in local
        for decl in env[0]:
            if decl.name == ast.name and type(decl) in [VarDecl, ParamDecl]:
                raise Undeclared(Function(), ast.name)

        for decl in env[-1]:
            if decl.name == ast.name:
                if decl.return_type is VoidType:
                    raise TypeMismatchInExpression(ast)

                # param type check
                # ..............
                # print("decl: ", decl)
                # print("ast: ", ast)
                if len(decl.params) != len(ast.args):
                    raise TypeMismatchInExpression(ast)

                for i in range(len(decl.params)):
                    argType = self.visit(ast.args[i], env)
                    paramType = decl.params[i].typ

                    if type(paramType) is AutoType:
                        decl.params[i].typ = argType
                        paramType = Utils.inferType(env, decl.name, argType)

                    # print("****:", decl.name)
                    # print("******argType: ", argType)
                    # print("******paramType: ", paramType)

                    if type(argType) is IntegerType:
                        if type(paramType) not in [IntegerType, FloatType]:
                            raise TypeMismatchInExpression(ast)
                    elif type(argType) is ArrayType:
                        if type(paramType) is not ArrayType or not Utils.isSameArrayType(argType, paramType):
                            raise TypeMismatchInExpression(ast)
                    elif type(argType) is not type(paramType):
                        raise TypeMismatchInExpression(ast)

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

    # dimensions: List[int], typ: AtomicType
    def visitArrayType(self, ast, param):
        return ast

    def visitAutoType(self, ast, param):
        return AutoType()

    def visitVoidType(self, ast, param):
        return VoidType()
