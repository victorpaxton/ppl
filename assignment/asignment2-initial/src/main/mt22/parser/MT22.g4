// ID: 2014533

grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decllist  EOF ;

decllist: decl decllist | decl ;
decl: vardecl | funcdecl ;

/*********** Variables declaration *******************/
// vardecl: idlist COLON vartyp varinit SEMI ;

// vartyp: atomtype | arraytype | autotype ;
// idlist: IDENTIFIER COMMA idlist | IDENTIFIER ;
// varinit: EQ exprpime | ;

vardecl: shortvardecl | fullvardecl ;

shortvardecl: idlist COLON vartyp SEMI;
idlist: IDENTIFIER COMMA idlist | IDENTIFIER ;

fullvardecl: varinit SEMI ;
varinit: IDENTIFIER COMMA varinit COMMA expr | IDENTIFIER COLON vartyp EQ expr ;
vartyp: atomtype | arraytype | autotype ;


/*********** Functions declaration *******************/
funcdecl: IDENTIFIER COLON FUNCTION types LB paramlist RB funcinher blockstmt;

paramlist: paramrime | ;
paramrime: param COMMA paramrime | param ;
param: (INHERIT | ) (OUT | ) IDENTIFIER COLON vartyp;
// paraminher: INHERIT | ;
// paramout: OUT | ;

funcinher: INHERIT IDENTIFIER | ;


/*********** Statements *******************/
stmtlist: stmt stmtlist | ;
stmt: blockstmt | vardecl | assignstmt | ifstmt | forstmt | whilestmt | dowhilestmt | breakstmt | continuestmt | returnstmt | callstmt ;
blockstmt: LP stmtlist RP;

assignstmt: lhs EQ expr SEMI;
lhs: IDENTIFIER | arrayele;
ifstmt: IF LB expr RB stmt (ELSE stmt | );
// elsestmt: ELSE stmt | ;
forstmt: FOR LB IDENTIFIER EQ expr COMMA expr COMMA expr RB stmt;
// forstmt: FOR LB assignstmt COMMA expr COMMA expr RB stmt;
whilestmt: WHILE LB expr RB stmt;
dowhilestmt: DO blockstmt WHILE LB expr RB SEMI;
breakstmt: BREAK SEMI ;
continuestmt: CONTINUE SEMI ;
returnstmt: RETURN (expr | ) SEMI;
callstmt: IDENTIFIER LB exprlist RB SEMI;

/*********** Expressions list *******************/
exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr ;

expr: expr1 CONCAT expr1 | expr1 ;
expr1: expr2 (EQUAL | NOT_EQUAL | LT | GT | LE | GE) expr2 | expr2 ;
expr2: expr2 (AND | OR) expr3 | expr3 ;
expr3: expr3 (ADD | SUB) expr4 | expr4 ;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5 ;
expr5: NOT expr5 | expr6 ;
expr6: SUB expr6 | expr7 ;
// expr7: IDENTIFIER LSB expr8 RSB | expr8 ;
expr7: subexpr | arrayele | funccall | IDENTIFIER | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arraylit;

subexpr: LB expr RB;
arrayele: IDENTIFIER LSB exprlist RSB ;
funccall: IDENTIFIER LB exprlist RB;


/*********** Types system *******************/
types: atomtype | arraytype | voidtype | autotype;

atomtype: BOOLEAN | INTEGER | FLOAT | STRING ;

arraytype: ARRAY LSB dimenslist RSB OF atomtype;
dimenslist: INTLIT COMMA dimenslist | INTLIT;

arraylit: LP exprlist RP ;

voidtype: VOID;

autotype: AUTO;


/*********** Comment *******************/
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

/*********** Keywords *******************/
BOOLLIT: TRUE | FALSE ;

AUTO: 'auto' ;
BREAK: 'break' ;
BOOLEAN: 'boolean' ;
DO: 'do' ;
ELSE: 'else' ;
FALSE: 'false' ;
FLOAT: 'float' ;
FOR: 'for' ;
FUNCTION: 'function' ;
IF: 'if' ;
INTEGER: 'integer' ;
RETURN: 'return' ;
STRING: 'string' ;
TRUE: 'true';
WHILE: 'while' ;
VOID: 'void' ;
OUT: 'out' ;
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

/*********** Operator *******************/
ADD: '+'; 	SUB: '-'; 	MUL: '*'; 	DIV: '/'; 	MOD: '%';
NOT: '!'; 	AND: '&&';	OR: '||';	
EQUAL: '==';	NOT_EQUAL: '!='; 
LT: '<';	LE: '<=';	GT: '>';	GE: '>=';
CONCAT: '::'; 

/*********** Seperators *******************/
LB: '('; 	RB: ')';
LP: '{'; 	RP: '}';
LSB: '['; 	RSB: ']';
DOT: '.';	COMMA: ',';
SEMI: ';';	COLON: ':';
EQ: '=';


/*********** Literals *******************/

// INTLIT: '0' | [1-9] [0-9]* ([_] [0-9]+)* {self.text = self.text.replace("_", "")};
INTLIT: '0' | NONZERO_DIGIT DIGIT* (UNDERSCORE DIGIT+)*  {self.text = self.text.replace("_", "")} ;

FLOATLIT: (INTLIT DECPART | INTLIT DECPART? EXPPART | DECPART EXPPART)  {self.text = self.text.replace("_", "")} ;

fragment DECPART: '.' DIGIT*;
fragment EXPPART: [eE] [-+]? DIGIT+;



// String literal
UNCLOSE_STRING: '"' (ESC | ~[\\"])*  { raise UncloseString(self.text[1:]) } ;

ILLEGAL_ESCAPE: UNCLOSE_STRING ILLEGAL_ESC  { raise IllegalEscape(self.text[1:]) } ;

STRINGLIT: UNCLOSE_STRING '"'  { self.text = self.text[1:-1] } ;

fragment ESC: '\\' [bfrnt'\\"] ; 
fragment ILLEGAL_ESC: '\\' ~[bfrnt'\\"] ;

// IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]* ;
IDENTIFIER: (LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)* ;

fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: '_';
fragment DIGIT: [0-9];
fragment NONZERO_DIGIT: [1-9];

WS : [ \t\b\f\r\n]+ -> skip ; // skip


ERROR_CHAR: . {raise ErrorToken(self.text)};