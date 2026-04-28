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
int soucet;
int cislo;
string vysledek;
FILE f;

// 1. Deklarace pole (podle tvého nového pravidla)
int mojePole[6];

// 2. Naplnění pole pomocí for cyklu
for (i = 0; i < 5; i = i + 1) {
    mojePole[i] = i * 10;
}

// 3. Otevření souboru
fopen f "vysledky.txt";
fappend f, "Vypocet hodnot z pole:";

soucet = 0;

// 4. Analýza pole, ternární operátor a zápis
for (i = 0; i < 5; i = i + 1) {
    cislo = mojePole[i];
    soucet = soucet + cislo;
    
    // Ternární operátor pro určení typu
    vysledek = (cislo % 20 == 0) ? "nasobek 20" : "ostatni";
    
    // Výpis do konzole i do souboru
    write "Index:", i, "Hodnota:", cislo, "Typ:", vysledek;
    fappend f, "Hodnota:", cislo, "Typ:", vysledek;
}

fappend f, "Celkovy soucet:", soucet;
write "Hotovo, soucet je:", soucet;
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