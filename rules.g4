grammar rules;

/** The start rule; begin parsing here. */
prog: stat+ ; // sekvence 1 nebo vice prikazu


stat: type_spec ID (',' ID)* ';'                # declaration
    | expr ';'                                  # exprStat
    | 'read' ID (',' ID)* ';'                   # readStat
    | 'write' expr (',' expr)* ';'              # writeStat
    | '{' stat* '}'                             # blockStat
    | 'if' '(' expr ')' stat ('else' stat)?     # ifStat
    | 'while' '(' expr ')' stat                 # whileStat
    | ';'                                       # emptyStat
    ;


type_spec: 'int' | 'float' | 'bool' | 'string' ;

expr: '-' expr                      # unaryMinus
    | '!' expr                      # logicalNot
    | expr op=('*'|'/'|'%') expr    # mulDivMod
    | expr op=('+'|'-'|'.') expr    # addSubConcat
    | expr op=('<'|'>') expr        # relational
    | expr op=('=='|'!=') expr      # equality
    | expr '&&' expr                # logicalAnd
    | expr '||' expr                # logicalOr
    | expr '?' expr ':' expr        # ternaryOp
    | <assoc=right> ID '=' expr     # assign
    | ID '[' expr ']'               # stringIndex
    | INT                           # int
    | FLOAT                         # float
    | OCT                           # oct
    | HEXA                          # hexa
    | BOOL                          # bool
    | STRING                        # string
    | ID                            # id
    | '(' expr ')'                  # parenthesis
    ;

// LEXER - SLOVNIK
BOOL : 'true' | 'false' ;
ID : [a-zA-Z][a-zA-Z0-9]* ;         // musi zacinat pismenem, pak i cisla
FLOAT : [0-9]+ '.' [0-9]+ ;         // desetinna cisla
INT : [1-9][0-9]* | '0' ;           // DEC match integers
OCT : '0'[0-7]+ ;                   // OCT 
HEXA : '0x'[0-9a-fA-F]+ ;           // HEXA
STRING : '"' .*? '"' ;              // textove retezce "text"

COMMENT : '//' ~[\r\n]* -> skip ;   // ignorovani komentaru do konce radku
WS : [ \t\r\n]+ -> skip ;           // ignorovani whitespace a novych radku