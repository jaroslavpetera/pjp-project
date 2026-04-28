from antlr4 import *
from rulesLexer import rulesLexer
from rulesParser import rulesParser
# from EvalVisitor import EvalVisitor
from CompilerVisitor import CompilerVisitor
from TypeCheckVisitor import TypeCheckVisitor
# from EvalListener import EvalListener

def main():
#     input_text = """
# int a, b;
# a = 3;
# b = 4;
# a + b * 2;
# (1 + 2) * 3;
# c = 10;
# """
#     input_text = """
# int i;
# string status;

# for (i = 1; i <= 5; i++) {
#     status = (i % 2 == 0) ? "sude" : "liche";
#     write i, status;
# }
#     """
    input_text = """
int i;
string status;

for (i = 1; i < 6; i = i + 1) {
    status = (i % 2 == 0) ? "sude" : "liche";
    write i, status;
}
    """

    input_stream = InputStream(input_text)
    lexer = rulesLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = rulesParser(tokens)

    tree = parser.prog()

    print("typova kontrola\n")
    type_checker = TypeCheckVisitor()
    type_checker.visit(tree)
    print("typova kontrola hotova\n")

    # print("preklad do instrukci")
    # visitor = EvalVisitor()
    compiler = CompilerVisitor(type_checker.memory)
    instructions = compiler.visit(tree)

    with open("output.txt", "w") as f:
        for i in instructions:
            f.write(i + "\n")

    # listener = EvalListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, tree)

    # for key, value in listener.values.items():
        # print(f"{key}: {value}")

if __name__ == '__main__':
    main()