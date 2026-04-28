from rulesVisitor import rulesVisitor
from rulesParser import rulesParser
import sys

class TypeCheckVisitor(rulesVisitor):
    def __init__(self):
        # Místo hodnot si budeme ukládat typy. Např: self.memory['a'] = 'int'
        self.memory = {}
        self.errors = [] # Sem budeme sbírat všechny chyby, ať je vypíšeme najednou

    def visitProg(self, ctx:rulesParser.ProgContext):
        for stat in ctx.stat():
            self.visit(stat)
            
        # Pokud jsme našli nějaké chyby, vypíšeme je a ukončíme program
        if len(self.errors) > 0:
            print("Nalezeny typove chyby:")
            for err in self.errors:
                print(f" - {err}")
            sys.exit(1) # Zastavíme překlad
            
        return "Typova kontrola uspesna!"

    # --- PŘÍKAZY ---

    def visitDeclaration(self, ctx:rulesParser.DeclarationContext): # ziskani deklarace promenne
        var_type = ctx.type_spec().getText()
        for id_node in ctx.ID():
            var_name = id_node.getText()
            if var_name in self.memory:
                self.errors.append(f"Promenna '{var_name}' uz byla deklarovana.")
            else:
                self.memory[var_name] = var_type
                # self.memory[var_name] = (var_type, is_const)

    def visitAssign(self, ctx:rulesParser.AssignContext):
        var_name = ctx.ID().getText()
        
        # PRAVIDLO 2: Existuje vůbec ta proměnná?
        if var_name not in self.memory:
            self.errors.append(f"Pouziti nedeklarovane promenne '{var_name}'.")
            return 'error_type'
            
        expected_type = self.memory[var_name]
        # expected_type, is_const = self.memory[var_name]
        # if is_const:
            # self.errors.append(f"chyba, {var_name} je constanta")
            # return 'error_type'
        # POKUD BYCH CHTEL KDEKOLIV DOSTAVAT self.memory[var_name], MUSEL BYCH PSAT self.memory[var_name][0] kvuli tomu tuple
        # a do .g4 k deklaraci 'constant'? samozrejme
        
        # Zjistíme, jaký typ nám vrátil výraz na pravé straně (např. 'float')
        actual_type = self.visit(ctx.expr())
        if actual_type == 'error_type':
            return 'error_type'
        
        # PRAVIDLO 3: Zabráníme uložení float do int
        if expected_type == 'int' and actual_type == 'float':
            self.errors.append(f"Nelze priradit 'float' do promenne '{var_name}' typu 'int'.")
        elif expected_type != actual_type and not (expected_type == 'float' and actual_type == 'int'): # dovolujeme ulozit int do floatu, jinak to musi sedet
            self.errors.append(f"Typova neshoda: Nelze ulozit {actual_type} do {expected_type}.")
            
        # Vracíme typ levé strany (pro případ a = b = 5)
        return expected_type
    
    def visitExprStat(self, ctx):
        self.visit(ctx.expr())

    def visitReadStat(self, ctx:rulesParser.ReadStatContext):
        # Kontrola, zda všechny čtené proměnné existují
        for id_node in ctx.ID():
            var_name = id_node.getText()
            if var_name not in self.memory:
                self.errors.append(f"Nelze cist do nedeklarovane promenne '{var_name}'.")

    def visitWriteStat(self, ctx:rulesParser.WriteStatContext):
        # Projdeme všechny výrazy k výpisu, jestli v nich není typová chyba
        for expr_node in ctx.expr():
            self.visit(expr_node)

    def visitBlockStat(self, ctx:rulesParser.BlockStatContext):
        for stat in ctx.stat():
            self.visit(stat)

    def visitIfStat(self, ctx:rulesParser.IfStatContext):
        cond_type = self.visit(ctx.expr())
        if cond_type != 'bool' and cond_type != 'error_type':
            self.errors.append(f"Podminka v 'if' musi byt typu 'bool', ale je '{cond_type}'.")
        self.visit(ctx.stat(0)) # Zkontrolujeme vnitřek IFu
        if ctx.stat(1):         # Pokud existuje ELSE větev, zkontrolujeme i tu
            self.visit(ctx.stat(1))

    def visitWhileStat(self, ctx:rulesParser.WhileStatContext):
        cond_type = self.visit(ctx.expr())
        if cond_type != 'bool' and cond_type != 'error_type':
            self.errors.append(f"Podminka ve 'while' musi byt typu 'bool', ale je '{cond_type}'.")
        self.visit(ctx.stat())

    def visitEmptyStat(self, ctx:rulesParser.EmptyStatContext):
        pass

    def visitFopenStat(self, ctx:rulesParser.FopenStatContext):
        f_name = ctx.ID().getText()

        if f_name not in self.memory:
            self.errors.append(f"soubor neexistuje {f_name}")
        if self.memory[f_name] != 'FILE':
            self.errors.append(f"{f_name} neni typu FILE")

    def visitFopenStat2(self, ctx:rulesParser.FopenStat2Context):
        f_name = ctx.ID().getText()

        if f_name not in self.memory:
            self.errors.append(f"soubor neexistuje {f_name}")
        if self.memory[f_name] != 'FILE':
            self.errors.append(f"{f_name} neni typu FILE")

    def visitWriteFileStat(self, ctx:rulesParser.WriteFileStatContext):
        f_name = ctx.ID().getText()
        if f_name not in self.memory:
            self.errors.append(f"soubor neexistuje {f_name}")
        if self.memory[f_name] != 'FILE':
            self.errors.append(f"{f_name} neni typu FILE")
        
        for expr in ctx.expr():
            self.visit(expr)

    def visitFappendStat(self, ctx:rulesParser.FappendStatContext):
        f_name = ctx.ID().getText()
        if f_name not in self.memory:
            self.errors.append(f"soubor neexistuje {f_name}")
        if self.memory[f_name] != 'FILE':
            self.errors.append(f"{f_name} neni typu FILE")
        
        for expr in ctx.expr():
            self.visit(expr)

    # def visitStringIndex(self, ctx:rulesParser.StringIndexContext):
    #     var_name = ctx.ID().getText()
    #     if var_name not in self.memory:
    #         self.errors.append(f"pouziti nedeklarovane promenne {var_name}")
    #         return 'error_type'
        
    #     if self.memory[var_name] != 'string':
    #         return 'error_type'
        
    #     index_type = self.visit(ctx.expr()) # kontrola vyrazu uvnitr jestli je int
    #     if index_type != 'int' and index_type != 'error_type':
    #         return 'error_type'

    #     return 'char'
    def visitStringIndex(self, ctx:rulesParser.StringIndexContext): # pro INT
        var_name = ctx.ID().getText()
        if var_name not in self.memory:
            self.errors.append(f"pouziti nedeklarovane promenne {var_name}")
            return 'error_type'
        
        var_type = self.memory[var_name]
        
        # if self.memory[var_name] != 'string':
            # return 'error_type'

        index_type = self.visit(ctx.expr()) # kontrola vyrazu uvnitr jestli je int
        if index_type != 'int':
            return 'error_type'
        if var_type == 'string':
            return 'char'
        else:
            return 'int'
    
    def visitForStat(self, ctx:rulesParser.ForStatContext):
        self.visit(ctx.init)

        cond_type = self.visit(ctx.cond)
        if cond_type != 'bool' and cond_type != 'error_type':
            self.errors.append(f"podminka ve FOR musi byt BOOL, ne {cond_type}")

        self.visit(ctx.step)
        self.visit(ctx.body)

    def visitDoWhileStat(self, ctx:rulesParser.DoWhileStatContext):
        self.visit(ctx.body)
        cond_type = self.visit(ctx.cond)
        if cond_type != 'bool' and cond_type != 'error_type':
            self.errors.append(f"Podminka v 'do-while' musi byt 'bool', ne '{cond_type}'.")

    def visitIncrement(self, ctx:rulesParser.IncrementContext):
        var_name = ctx.ID().getText()
        
        # 1. Existuje ta proměnná vůbec?
        if var_name not in self.memory:
            self.errors.append(f"Chyba: Pokus o inkrementaci nedeklarovane promenne '{var_name}'.")
            return 'error_type'
            
        var_type = self.memory[var_name]
        
        # 2. Je to cislo? (int nebo float)
        if var_type not in ['int', 'float']:
            self.errors.append(f"Typova chyba: Operaci '++' nelze pouzit na typ {var_type}. Ocekavan 'int' nebo 'float'.")
            return 'error_type'
            
        return var_type

    def visitDecrement(self, ctx:rulesParser.DecrementContext):
        var_name = ctx.ID().getText()
        
        if var_name not in self.memory:
            self.errors.append(f"Chyba: Pokus o dekrementaci nedeklarovane promenne '{var_name}'.")
            return 'error_type'
            
        var_type = self.memory[var_name]
        
        if var_type not in ['int', 'float']:
            self.errors.append(f"Typova chyba: Operaci '--' nelze pouzit na typ {var_type}. Ocekavan 'int' nebo 'float'.")
            return 'error_type'
            
        return var_type
    
    def visitTernaryOp(self, ctx:rulesParser.TernaryOpContext):
        cond_type = self.visit(ctx.expr(0))
        if cond_type != 'bool':
            self.errors.append("Podminka v ternarnim operatoru musi byt bool.")
        
        t_type = self.visit(ctx.expr(1))
        f_type = self.visit(ctx.expr(2))
        
        if t_type != f_type:
            self.errors.append("Vetve ternarniho operatoru musi mit stejny typ.")
            
        return t_type
    
    def visitBreakStat(self, ctx:rulesParser.BreakStatContext):
        # Můžeš si v TypeCheckeru taky vést stack nebo jen counter
        # pokud je counter == 0, vyhodíš chybu "Break mimo cyklus"
        return 'void' 

    def visitContinueStat(self, ctx:rulesParser.ContinueStatContext):
        return 'void'
    
    def visitArrayDeclaration(self, ctx:rulesParser.ArrayDeclarationContext):
        var_type = ctx.type_spec().getText() # int, float...
        var_name = ctx.ID().getText()
        self.memory[var_name] = 'array' # int arr kdyztak
        # self.memory[var_name] = f"{var_type}_array"

    def visitArrayAssign(self, ctx:rulesParser.ArrayAssignContext):
        var_name = ctx.ID().getText()
        if self.memory[var_name] != 'array':
            self.errors.append(f"{var_name} neni pole")

        # array_kind = self.memory[var_name] # 'float_array'
        # expected_element_type = array_kind.split('_')[0] # 'float'

        self.visit(ctx.expr(0))
        
        # actual_value_type = self.visit(ctx.expr(1))
        self.visit(ctx.expr(1))

        # if expected_element_type == 'float' and actual_value_type == 'int':
            # pass
        # elif expected_element_type != actual_value_type:
            # self.errors.append("chyba")
        # return 'void'

    # --- LITERÁLY (Základní stavební kameny) ---
    # Tyhle funkce teď místo hodnot (5, 3.14) vrací jen svůj TYP
    def visitMulDivMod(self, ctx:rulesParser.MulDivModContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if left == 'error_type' or right == 'error_type': return 'error_type'

        if op == '%': # Modulo pouze pro celá čísla
            if left != 'int' or right != 'int':
                self.errors.append(f"Operace '%' vyzaduje 'int', ale dostala '{left}' a '{right}'.")
                return 'error_type'
            return 'int'
        else: # Násobení a dělení
            if left not in ['int', 'float'] or right not in ['int', 'float']:
                self.errors.append(f"Operace '{op}' ocekava cisla (int/float), dostala '{left}' a '{right}'.")
                return 'error_type'
            return 'float' if left == 'float' or right == 'float' else 'int'

    def visitAddSubConcat(self, ctx:rulesParser.AddSubConcatContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if left == 'error_type' or right == 'error_type': return 'error_type'

        if op == '.': # Slučování textů
            if left != 'string' or right != 'string':
                self.errors.append(f"Operace '.' (concat) vyzaduje 'string', dostala '{left}' a '{right}'.")
                return 'error_type'
            return 'string'
        else: # Sčítání a odčítání
            if left not in ['int', 'float'] or right not in ['int', 'float']:
                self.errors.append(f"Operace '{op}' ocekava cisla, dostala '{left}' a '{right}'.")
                return 'error_type'
            return 'float' if left == 'float' or right == 'float' else 'int'

    def visitRelational(self, ctx:rulesParser.RelationalContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left not in ['int', 'float'] or right not in ['int', 'float']:
            self.errors.append(f"Porovnavani (<, >) ocekava cisla, dostalo '{left}' a '{right}'.")
            return 'error_type'
        return 'bool' # Výsledek porovnání je vždy pravda/nepravda

    def visitEquality(self, ctx:rulesParser.EqualityContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == 'error_type' or right == 'error_type': return 'error_type'
        # int a float jdou porovnat, jinak musí být typy stejné (nelze porovnat string a bool)
        if left != right and not ((left == 'int' and right == 'float') or (left == 'float' and right == 'int')):
            self.errors.append(f"Nelze porovnavat (==, !=) odlisne typy: '{left}' a '{right}'.")
            return 'error_type'
        return 'bool'

    def visitLogicalAnd(self, ctx:rulesParser.LogicalAndContext):
        return self._check_logical(ctx, '&&')

    def visitLogicalOr(self, ctx:rulesParser.LogicalOrContext):
        return self._check_logical(ctx, '||')
        
    def _check_logical(self, ctx, op):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left != 'bool' or right != 'bool':
            self.errors.append(f"Logicka operace '{op}' vyzaduje 'bool', dostala '{left}' a '{right}'.")
            return 'error_type'
        return 'bool'

    def visitUnaryMinus(self, ctx:rulesParser.UnaryMinusContext):
        expr_type = self.visit(ctx.expr())
        if expr_type not in ['int', 'float'] and expr_type != 'error_type':
            self.errors.append(f"Unarni minus '-' lze pouzit jen na cisla, ne na '{expr_type}'.")
            return 'error_type'
        return expr_type

    def visitLogicalNot(self, ctx:rulesParser.LogicalNotContext):
        expr_type = self.visit(ctx.expr())
        if expr_type != 'bool' and expr_type != 'error_type':
            self.errors.append(f"Logicky zapor '!' lze pouzit jen na 'bool', ne na '{expr_type}'.")
            return 'error_type'
        return 'bool'

    def visitParenthesis(self, ctx:rulesParser.ParenthesisContext):
        return self.visit(ctx.expr())

    def visitId(self, ctx:rulesParser.IdContext):
        var_name = ctx.ID().getText()
        if var_name not in self.memory:
            self.errors.append(f"Pouziti nedeklarovane promenne '{var_name}'.")
            return 'error_type'
        return self.memory[var_name]

    # ZÁKLADNÍ LITERÁLY
    def visitInt(self, ctx:rulesParser.IntContext): return 'int'
    def visitFloat(self, ctx:rulesParser.FloatContext): return 'float'
    def visitBool(self, ctx:rulesParser.BoolContext): return 'bool'
    def visitString(self, ctx:rulesParser.StringContext): return 'string'
    def visitOct(self, ctx:rulesParser.OctContext): return 'int'
    def visitHexa(self, ctx:rulesParser.HexaContext): return 'int'