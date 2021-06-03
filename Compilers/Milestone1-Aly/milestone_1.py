import argparse
from antlr4 import *
from milestone_1Lexer import milestone_1Lexer
from milestone_1Listener import milestone_1Listener
from milestone_1Parser import milestone_1Parser
from antlr4.tree.Trees import Trees

def get_token_type(token):
    if token.type == milestone_1Lexer.NEWLINE:
        return "NEWLINE"
    elif token.type == milestone_1Lexer.WHITESPACE:
        return "WHITESPACE"
    elif token.type == milestone_1Lexer.VARIABLE:
        return "VARIABLE"    
    elif token.type == milestone_1Lexer.AND:
        return "AND"
    elif token.type == milestone_1Lexer.YIELD:
        return "YIELD"
    elif token.type == milestone_1Lexer.LETTER:
        return "LETTER"
    elif token.type == milestone_1Lexer.DIGIT:
        return "DIGIT"
    elif token.type == milestone_1Lexer.IDENTIFIER:
        return "IDENTIFIER"
    elif token.type == milestone_1Lexer.HEXDIGIT:
        return "HEXDIGIT"
    elif token.type == milestone_1Lexer.OCTDIGIT:
        return "OCTDIGIT"
    elif token.type == milestone_1Lexer.BINDIGIT:
        return "BINDIGIT"
    elif token.type == milestone_1Lexer.HEX_LIT:
        return "HEX_LIT"
    elif token.type == milestone_1Lexer.DEC_LIT:
        return "DEC_LIT"
    elif token.type == milestone_1Lexer.OCT_LIT:
        return "OCT_LIT"
    elif token.type == milestone_1Lexer.BIN_LIT:
        return "BIN_LIT"
    elif token.type == milestone_1Lexer.INT_LIT:
        return "INT_LIT"
    elif token.type == milestone_1Lexer.INT8_LIT:
        return "INT8_LIT"
    elif token.type == milestone_1Lexer.INT16_LIT:
        return "INT16_LIT"
    elif token.type == milestone_1Lexer.INT32_LIT:
        return "INT32_LIT"
    elif token.type == milestone_1Lexer.INT64_LIT:
        return "INT64_LIT"
    elif token.type == milestone_1Lexer.UINT_LIT:
        return "UINT_LIT"
    elif token.type == milestone_1Lexer.UINT8_LIT:
        return "UINT8_LIT"
    elif token.type == milestone_1Lexer.UINT16_LIT:
        return "UINT16_LIT"
    elif token.type == milestone_1Lexer.UINT32_LIT:
        return "UINT32_LIT"
    elif token.type == milestone_1Lexer.UINT64_LIT:
        return "UINT64_LIT"
    elif token.type == milestone_1Lexer.EXP:
        return "EXP"
    elif token.type == milestone_1Lexer.FLOAT_LIT:
        return "FLOAT_LIT"
    elif token.type == milestone_1Lexer.FLOAT32_SUFFIX:
        return "FLOAT32_SUFFIX"
    elif token.type == milestone_1Lexer.FLOAT32_LIT:
        return "FLOAT32_LIT"
    elif token.type == milestone_1Lexer.FLOAT64_SUFFIX:
        return "FLOAT64_SUFFIX"
    elif token.type == milestone_1Lexer.FLOAT64_LIT:
        return "FLOAT64_LIT"
    elif token.type == milestone_1Lexer.EQUALS_OPERATOR:
        return "EQUALS_OPERATOR"
    elif token.type == milestone_1Lexer.ADD_OPERATOR:
        return "ADD_OPERATOR"
    elif token.type == milestone_1Lexer.MUL_OPERATOR:
        return "MUL_OPERATOR"
    elif token.type == milestone_1Lexer.MINUS_OPERATOR:
        return "MINUS_OPERATOR"
    elif token.type == milestone_1Lexer.DIV_OPERATOR:
        return "DIV_OPERATOR"
    elif token.type == milestone_1Lexer.BITWISE_NOT_OPERATOR:
        return "BITWISE_NOT_OPERATOR"
    elif token.type == milestone_1Lexer.AND_OPERATOR:
        return "AND_OPERATOR"
    elif token.type == milestone_1Lexer.OR_OPERATOR:
        return "OR_OPERATOR"
    elif token.type == milestone_1Lexer.LESS_THAN:
        return "LESS_THAN"
    elif token.type == milestone_1Lexer.GREATER_THAN:
        return "GREATER_THAN"
    elif token.type == milestone_1Lexer.AT:
        return "AT"
    elif token.type == milestone_1Lexer.MODULUS:
        return "MODULUS"
    elif token.type == milestone_1Lexer.NOT_OPERATOR:
        return "NOT_OPERATOR"
    elif token.type == milestone_1Lexer.XOR_OPERATOR:
        return "XOR_OPERATOR"
    elif token.type == milestone_1Lexer.DOT:
        return "DOT"
    elif token.type == milestone_1Lexer.COLON:
        return "COLON"
    elif token.type == milestone_1Lexer.OPEN_PAREN:
        return "OPEN_PAREN"
    elif token.type == milestone_1Lexer.CLOSE_PAREN:
        return "CLOSE_PAREN"
    elif token.type == milestone_1Lexer.OPEN_BRACE:
        return "OPEN_BRACE"
    elif token.type == milestone_1Lexer.CLOSE_BRACE:
        return "CLOSE_BRACE"
    elif token.type == milestone_1Lexer.OPEN_BRACK:
        return "OPEN_BRACK"
    elif token.type == milestone_1Lexer.CLOSE_BRACK:
        return "CLOSE_BRACK"
    elif token.type == milestone_1Lexer.COMMA:
        return "COMMA"
    elif token.type == milestone_1Lexer.SEMI_COLON:
        return "SEMI_COLON"
    else:
        return "ERROR UNKNOWN TOKEN"

def main():

    with open(args.file, "r") as file:
        lines = file.read()
    input_stream = InputStream(lines)
    lexer = milestone_1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = milestone_1Parser(token_stream)

 #   tree = parser.start()
 #   print(Trees.toStringTree(tree,None, parser))

    output_file = open("milestone_1_result.txt","w+")
    token = lexer.nextToken()

    while not token.type == Token.EOF:
        print(get_token_type(token), token.text)
        if "NEWLINE" not in get_token_type(token):
            if "WHITESPACE" not in get_token_type(token):
                 output_file.write(get_token_type(token)+" "+token.text+"\n")
        token = lexer.nextToken()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?", metavar="file")

    args = parser.parse_args()

    print(args.file)
	
    main()	
