from rulesVisitor import rulesVisitor
from rulesParser import rulesParser

class CompilerVisitor(rulesVisitor):
    def __init__(self, memory):
        self.memory = memory  # Převezmeme tabulku proměnných z TypeCheckeru (a: 'int', b: 'float' atd.)
        self.label_counter = 0 # Počítadlo pro unikátní skoky (label 0, label 1...)
        self.break_stack = []    # Zásobník labelů pro konce cyklů
        self.continue_stack = [] # Zásobník labelů pro začátky cyklů

    def get_new_label(self):
        # Funkce, která nám pro každý IF a WHILE vygeneruje nové, unikátní číslo
        self.label_counter += 1
        return self.label_counter

    def type_to_char(self, type_str):
        # Pomocná funkce pro převod našeho typu na znak pro instrukce (I, F, B, S)
        if type_str == 'int': return 'I'
        if type_str == 'float': return 'F'
        if type_str == 'bool': return 'B'
        if type_str == 'string': return 'S'
        return 'I'

    def visitProg(self, ctx:rulesParser.ProgContext):
        instructions = []
        for stat in ctx.stat():
            res = self.visit(stat)
            if res:
                if isinstance(res, tuple): # Pokud je to Assign, vezmi jen instrukce
                    instructions.extend(res[0])
                else:
                    instructions.extend(res)
        return instructions

    # ==========================================
    # PŘÍKAZY (STATEMENTS) - vrací list[string]
    # ==========================================

    def visitDeclaration(self, ctx:rulesParser.DeclarationContext):
        return [] # Při deklaraci nemusíme generovat žádné instrukce

    def visitAssign(self, ctx:rulesParser.AssignContext):
        var_name = ctx.ID().getText()
        var_type = self.memory[var_name]
        
        # Vyhodnotíme pravou stranu
        expr_inst, expr_type = self.visit(ctx.expr())
        
        instructions = expr_inst
        # Pokud ukládáme INT do FLOAT proměnné, musíme ho cestou přetypovat
        if expr_type == 'int' and var_type == 'float':
            instructions.append("itof")
            
        instructions.append(f"save {var_name}")

        instructions.append(f"load {var_name}")
        return instructions, var_type

    def visitExprStat(self, ctx:rulesParser.ExprStatContext):
        inst, _ = self.visit(ctx.expr())
        inst.append("pop") # Pokud někdo napíše jen "1+2;", musíme výsledek uklidit ze zásobníku
        return inst

    def visitReadStat(self, ctx:rulesParser.ReadStatContext):
        instructions = []
        for id_node in ctx.ID():
            var_name = id_node.getText()
            t_char = self.type_to_char(self.memory[var_name])
            instructions.append(f"read {t_char}")
            instructions.append(f"save {var_name}")
        return instructions

    def visitWriteStat(self, ctx:rulesParser.WriteStatContext):
        instructions = []
        expr_count = 0
        for expr_node in ctx.expr():
            inst, _ = self.visit(expr_node)
            instructions.extend(inst)
            expr_count += 1
        instructions.append(f"print {expr_count}")
        return instructions

    def visitBlockStat(self, ctx:rulesParser.BlockStatContext):
        instructions = []
        for stat in ctx.stat():
            inst = self.visit(stat)
            if inst: instructions.extend(inst)
        return instructions

    def visitIfStat(self, ctx:rulesParser.IfStatContext):
        cond_inst, _ = self.visit(ctx.expr())
        
        label_else = self.get_new_label()
        label_end = self.get_new_label()
        
        inst = cond_inst
        inst.append(f"fjmp {label_else}") # Pokud je podmínka False, skoč na Else
        
        # Vnitřek IF
        true_block = self.visit(ctx.stat(0))
        if true_block: inst.extend(true_block)
        inst.append(f"jmp {label_end}") # Po dokončení přeskoč zbytek
        
        # Vnitřek ELSE
        inst.append(f"label {label_else}")
        if ctx.stat(1): # Pokud ELSE existuje
            false_block = self.visit(ctx.stat(1))
            if false_block: inst.extend(false_block)
            
        inst.append(f"label {label_end}")
        return inst

    def visitWhileStat(self, ctx:rulesParser.WhileStatContext):
        label_start = self.get_new_label()
        label_end = self.get_new_label()

        # self.continue_stack.append(label_start) # pro break a continue
        # self.break_stack.append(label_end)
        
        inst = [f"label {label_start}"] # Návratový bod cyklu
        
        cond_inst, _ = self.visit(ctx.expr())
        inst.extend(cond_inst)
        inst.append(f"fjmp {label_end}") # Pokud už podmínka neplatí, ukonči cyklus
        
        # Vnitřek cyklu
        body_inst = self.visit(ctx.stat())
        if body_inst: inst.extend(body_inst)
        
        inst.append(f"jmp {label_start}") # Skoč zpět nahoru zkontrolovat podmínku
        inst.append(f"label {label_end}")

        # self.continue_stack.pop() # pro break a continue
        # self.break_stack.pop()

        return inst

    def visitEmptyStat(self, ctx:rulesParser.EmptyStatContext):
        return []
    
    def visitTernaryOp(self, ctx:rulesParser.TernaryOpContext):
        label_false = self.get_new_label()
        label_end = self.get_new_label()
        instructions = []

        # 1. Vyhodnotíme podmínku (ta před '?')
        cond_inst, _ = self.visit(ctx.expr(0))
        instructions.extend(cond_inst)
        instructions.append(f"fjmp {label_false}")

        # 2. TRUE větev (mezi '?' a ':')
        true_inst, true_type = self.visit(ctx.expr(1))
        instructions.extend(true_inst)
        instructions.append(f"jmp {label_end}")

        # 3. FALSE větev (za ':')
        instructions.append(f"label {label_false}")
        false_inst, false_type = self.visit(ctx.expr(2))
        instructions.extend(false_inst)

        # 4. Konec
        instructions.append(f"label {label_end}")

        # Typ výsledku bude ten, který mají větve (ideálně stejný)
        return instructions, true_type
    

    # ==========================================
    # VÝRAZY (EXPRESSIONS) - vrací (list[string], string)
    # ==========================================

    def _unify_numeric(self, left_inst, left_type, right_inst, right_type):
        # Tato pomocná funkce vyřeší automatické vkládání 'itof' instrukcí
        inst = left_inst[:]
        if left_type == 'int' and right_type == 'float':
            inst.append("itof") # Přetypuje int ležící na zásobníku
            
        inst.extend(right_inst)
        if left_type == 'float' and right_type == 'int':
            inst.append("itof") # Přetypuje zrovna vložený int
            
        res_type = 'float' if 'float' in (left_type, right_type) else 'int'
        return inst, res_type

    def visitMulDivMod(self, ctx:rulesParser.MulDivModContext):
        left_inst, left_type = self.visit(ctx.expr(0))
        right_inst, right_type = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if op == '%':
            return left_inst + right_inst + ["mod"], 'int'

        inst, res_type = self._unify_numeric(left_inst, left_type, right_inst, right_type)
        t_char = self.type_to_char(res_type)
        
        if op == '*': inst.append(f"mul {t_char}")
        else: inst.append(f"div {t_char}")
        return inst, res_type

    def visitAddSubConcat(self, ctx:rulesParser.AddSubConcatContext):
        left_inst, left_type = self.visit(ctx.expr(0))
        right_inst, right_type = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if op == '.':
            return left_inst + right_inst + ["concat"], 'string'

        inst, res_type = self._unify_numeric(left_inst, left_type, right_inst, right_type)
        t_char = self.type_to_char(res_type)
        
        if op == '+': inst.append(f"add {t_char}")
        else: inst.append(f"sub {t_char}")
        return inst, res_type

    def visitRelational(self, ctx:rulesParser.RelationalContext):
        left_inst, left_type = self.visit(ctx.expr(0))
        right_inst, right_type = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        inst, res_type = self._unify_numeric(left_inst, left_type, right_inst, right_type)
        t_char = self.type_to_char(res_type)
        
        if op == '<': inst.append(f"lt {t_char}")
        else: inst.append(f"gt {t_char}")
        return inst, 'bool'

    def visitEquality(self, ctx:rulesParser.EqualityContext):
        left_inst, left_type = self.visit(ctx.expr(0))
        right_inst, right_type = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        if left_type in ['int', 'float'] and right_type in ['int', 'float']:
            inst, res_type = self._unify_numeric(left_inst, left_type, right_inst, right_type)
            t_char = self.type_to_char(res_type)
        else:
            inst = left_inst + right_inst
            t_char = self.type_to_char(left_type)

        inst.append(f"eq {t_char}")
        if op == '!=':
            inst.append("not")
        return inst, 'bool'

    def visitLogicalAnd(self, ctx:rulesParser.LogicalAndContext):
        left_inst, _ = self.visit(ctx.expr(0))
        right_inst, _ = self.visit(ctx.expr(1))
        return left_inst + right_inst + ["and"], 'bool'
    


    def visitLogicalOr(self, ctx:rulesParser.LogicalOrContext):
        left_inst, _ = self.visit(ctx.expr(0))
        right_inst, _ = self.visit(ctx.expr(1))
        return left_inst + right_inst + ["or"], 'bool'

    def visitLogicalNot(self, ctx:rulesParser.LogicalNotContext):
        inst, _ = self.visit(ctx.expr())
        inst.append("not")
        return inst, 'bool'

    def visitUnaryMinus(self, ctx:rulesParser.UnaryMinusContext):
        inst, t = self.visit(ctx.expr())
        t_char = self.type_to_char(t)
        inst.append(f"uminus {t_char}")
        return inst, t

    def visitParenthesis(self, ctx:rulesParser.ParenthesisContext):
        return self.visit(ctx.expr())

    def visitId(self, ctx:rulesParser.IdContext):
        var_name = ctx.ID().getText()
        var_type = self.memory[var_name]
        return [f"load {var_name}"], var_type

    def visitInt(self, ctx:rulesParser.IntContext):
        return [f"push I {ctx.INT().getText()}"], 'int'

    def visitFloat(self, ctx:rulesParser.FloatContext):
        return [f"push F {ctx.FLOAT().getText()}"], 'float'

    def visitBool(self, ctx:rulesParser.BoolContext):
        return [f"push B {ctx.BOOL().getText()}"], 'bool'

    def visitString(self, ctx:rulesParser.StringContext):
        return [f"push S {ctx.STRING().getText()}"], 'string'
        
    def visitOct(self, ctx:rulesParser.OctContext):
        val = int(ctx.OCT().getText(), 8)
        return [f"push I {val}"], 'int'

    def visitHexa(self, ctx:rulesParser.HexaContext):
        val = int(ctx.HEXA().getText(), 16)
        return [f"push I {val}"], 'int'
    