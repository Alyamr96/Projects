// milestone_1.g4 file
grammar milestone_1;

NEWLINE : [\r\n]+;
WHITESPACE : ' '+;

VARIABLE : 'var';
AND : 'and';

YIELD : 'yield';
LETTER : 'a'..'z' | 'A'..'Z';
DIGIT : '0'..'9';
IDENTIFIER : LETTER ('_'? (LETTER | DIGIT))* | LETTER;

HEXDIGIT : DIGIT | 'A'..'F' | 'a'..'f';
OCTDIGIT : '0'..'7';
BINDIGIT : '0' | '1';
HEX_LIT : '0' ('x' | 'X') HEXDIGIT ('_'? HEXDIGIT)*;
DEC_LIT : DIGIT ('_'? DIGIT)*;
OCT_LIT : '0' 'o' OCTDIGIT ('_'? OCTDIGIT)*;
BIN_LIT : '0' ('b' | 'B') BINDIGIT ('_'? BINDIGIT)*;
INT_LIT : HEX_LIT | DEC_LIT | OCT_LIT | BIN_LIT;

INT8_LIT : INT_LIT '\'' ('i' | 'I') '8';
INT16_LIT : INT_LIT '\'' ('i' | 'I') '16';
INT32_LIT : INT_LIT '\'' ('i' | 'I') '32';
INT64_LIT : INT_LIT '\'' ('i' | 'I') '64';
UINT_LIT : INT_LIT '\'' ('u' | 'U');
UINT8_LIT : INT_LIT '\'' ('u' | 'U') '8';
UINT16_LIT : INT_LIT '\'' ('u' | 'U') '16';
UINT32_LIT : INT_LIT '\'' ('u' | 'U') '32';
UINT64_LIT : INT_LIT '\'' ('u' | 'U') '64';

EXP : ('e' | 'E') ('+' | '-')? DIGIT ('_'? DIGIT)*;
FLOAT_LIT : DIGIT ('_'? DIGIT)* (('.' DIGIT ('_'? DIGIT)* EXP?) | EXP);
FLOAT32_SUFFIX : ('f' | 'F') '32'?;
FLOAT32_LIT : HEX_LIT '\'' FLOAT32_SUFFIX | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\''? FLOAT32_SUFFIX;
FLOAT64_SUFFIX : (('f' | 'F') '64') | 'd' | 'D';
FLOAT64_LIT : HEX_LIT '\'' FLOAT64_SUFFIX | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\''? FLOAT64_SUFFIX;

EQUALS_OPERATOR : '==' | '=';
ADD_OPERATOR : '+';
MUL_OPERATOR : '*';
MINUS_OPERATOR : '-';
DIV_OPERATOR : '/';
BITWISE_NOT_OPERATOR : '~';
AND_OPERATOR : '&';
OR_OPERATOR : '|';
LESS_THAN : '<';
GREATER_THAN : '>';
AT : 'at';
MODULUS : '%';
NOT_OPERATOR : '!';
XOR_OPERATOR : '^';
DOT : '.';
COLON : ':';
OPEN_PAREN : '(';
CLOSE_PAREN : ')';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';
OPEN_BRACK : '[';
CLOSE_BRACK : ']';
COMMA : ',';
SEMI_COLON : ';';  

expr : NEWLINE | WHITESPACE | VARIABLE | AND | YIELD | LETTER | DIGIT | IDENTIFIER | HEXDIGIT | OCTDIGIT | BINDIGIT | HEX_LIT | DEC_LIT | OCT_LIT | BIN_LIT | INT_LIT | INT8_LIT | INT16_LIT | INT32_LIT | INT64_LIT | UINT_LIT | UINT8_LIT | UINT16_LIT | UINT32_LIT | UINT64_LIT | EXP | FLOAT_LIT | FLOAT32_SUFFIX | FLOAT32_LIT | FLOAT64_SUFFIX | FLOAT64_LIT | EQUALS_OPERATOR | ADD_OPERATOR | MUL_OPERATOR | MINUS_OPERATOR | DIV_OPERATOR | BITWISE_NOT_OPERATOR | AND_OPERATOR | OR_OPERATOR | LESS_THAN | GREATER_THAN | AT | MODULUS | NOT_OPERATOR | XOR_OPERATOR | DOT | COLON | OPEN_PAREN | CLOSE_PAREN | OPEN_BRACE | CLOSE_BRACE | OPEN_BRACK | CLOSE_BRACK | COMMA | SEMI_COLON;






















