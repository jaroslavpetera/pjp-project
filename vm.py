import sys

class VirtualMachine:
    def __init__(self):
        self.stack = []   # Náš zásobník
        self.memory = {}  # Paměť pro proměnné (a, b, c...)
        self.labels = {}  # pamatuju si na kterem radku je jaky label
        self.instructions = []

    def load_instructions(self, lines):
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            self.instructions.append(parts)

            if parts[0] == "label":
                label_id = parts[1]
                self.labels[label_id] = len(self.instructions) - 1

    def run(self):
        ip = 0  # Instruction Pointer (ukazatel na aktuální řádek kódu)
        
        # 2. PRŮCHOD: Fyzické vykonávání instrukcí
        while ip < len(self.instructions):
            parts = self.instructions[ip]
            cmd = parts[0]

            if cmd == "label":
                pass # Labely jen označují místo, nic se při nich neděje

            # --- VKLÁDÁNÍ A VYBÍRÁNÍ ZE ZÁSOBNÍKU ---
            elif cmd == "push":
                val_type = parts[1]
                if val_type == 'S':
                    # Řetězce mohou mít mezery, musíme je spojit zpět
                    val = " ".join(parts[2:])
                    if val.startswith('"') and val.endswith('"'):
                        val = val[1:-1] # Odstranění uvozovek
                    self.stack.append(val)
                elif val_type == 'I' or val_type == 'B':
                    val = parts[2]
                    if val == 'true': self.stack.append(True)
                    elif val == 'false': self.stack.append(False)
                    else: self.stack.append(int(val))
                elif val_type == 'F':
                    self.stack.append(float(parts[2]))

            elif cmd == "pop":
                self.stack.pop()

            # --- PROMĚNNÉ ---
            elif cmd == "load":
                var_name = parts[1]
                self.stack.append(self.memory.get(var_name, 0))

            elif cmd == "save":
                var_name = parts[1] # Ignorujeme případný typ I/F/S/B
                if len(parts) == 3: # Kompatibilita, kdyby tam byl typ (SAVE I a)
                    var_name = parts[2]
                self.memory[var_name] = self.stack.pop()

            # --- MATEMATIKA A LOGIKA ---
            elif cmd in ["add", "sub", "mul", "div", "mod", "lt", "gt", "eq", "and", "or", "concat"]:
                b = self.stack.pop()
                a = self.stack.pop()
                
                if cmd == "add": self.stack.append(a + b)
                elif cmd == "sub": self.stack.append(a - b)
                elif cmd == "mul": self.stack.append(a * b)
                elif cmd == "div": self.stack.append(a / b)
                elif cmd == "mod": self.stack.append(a % b)
                elif cmd == "lt": self.stack.append(a < b)
                elif cmd == "gt": self.stack.append(a > b)
                elif cmd == "eq": self.stack.append(a == b)
                elif cmd == "and": self.stack.append(a and b)
                elif cmd == "or": self.stack.append(a or b)
                elif cmd == "concat": self.stack.append(str(a) + str(b))

            # --- UNÁRNÍ OPERACE A PŘETYPOVÁNÍ ---
            elif cmd in ["uminus", "not"]:
                a = self.stack.pop()
                if cmd == "uminus": self.stack.append(-a)
                elif cmd == "not": self.stack.append(not a)

            elif cmd == "itof":
                a = self.stack.pop()
                self.stack.append(float(a))

            # --- SKOKY (ŘÍZENÍ TOKU PROGRAMU) ---
            elif cmd == "jmp":
                label_id = parts[1]
                ip = self.labels[label_id] # Přesuneme ukazatel na cílový label

            elif cmd == "fjmp":
                label_id = parts[1]
                condition = self.stack.pop()
                if not condition: # Pokud je na zásobníku False, skočíme
                    ip = self.labels[label_id]

            # --- VSTUP A VÝSTUP ---
            elif cmd == "print":
                count = int(parts[1])
                values = []
                for _ in range(count):
                    values.insert(0, self.stack.pop())
                
                # Upravíme hodnoty pro výpis (bool na malé písmena, zbytek na str)
                output_parts = []
                for v in values:
                    if isinstance(v, bool):
                        output_parts.append(str(v).lower())
                    else:
                        output_parts.append(str(v))
                
                # Vypíšeme všechno najednou spojené mezerou
                print(" ".join(output_parts))

            elif cmd == "read":
                val_type = parts[1]
                user_input = input(f">> (Zadej hodnotu): ")
                if val_type == 'I': self.stack.append(int(user_input))
                elif val_type == 'F': self.stack.append(float(user_input))
                elif val_type == 'B': self.stack.append(user_input.lower() == 'true')
                elif val_type == 'S': self.stack.append(user_input)

            elif cmd == "fopen":
                var_name = parts[1] # f
                filename = " ".join(parts[2:]).strip('"')

                self.memory[var_name] = open(filename, "w")

            elif cmd == "fopen2":
                var_name = parts[1] # f
                filename = " ".join(parts[2:]).strip('"')

                self.memory[var_name] = open(filename, "a")

            elif cmd == "f_write":
                var_name = parts[1] # f
                value_to_write = self.stack.pop()

                if var_name in self.memory:
                    file = self.memory[var_name]

                    file.write(str(value_to_write) + "\n")
                    file.flush()
                else:
                    print(f"soubor {file} neni otevreny!")

            elif cmd == 'fappend':
                var_name = parts[1] #f
                count = int(parts[2])

                values = []
                for _ in range(count):
                    values.insert(0, self.stack.pop())
                
                if var_name in self.memory:
                    file = self.memory[var_name]
                    line = " ".join(map(str, values))
                    file.write(line + "\n")
                    file.flush()

            elif cmd == "charAt":
                index = self.stack.pop()  # 1. Popne index (např. 1)
                string = self.stack.pop() # 2. Popne string (např. "AHOJ")
                
                # V Pythonu je indexování stringu hračka:
                result = string[index] 
                self.stack.append(result) # 3. Hodí výsledek ("H") zpět na zásobník


            else:
                print(f"Neznama instrukce: {cmd}")

            ip += 1 # Posuneme se na další instrukci

if __name__ == "__main__":
    filename = "output.txt"
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            
        vm = VirtualMachine()
        vm.load_instructions(lines)
        vm.run()
    except FileNotFoundError:
        print(f"Chyba: Soubor '{filename}' nebyl nalezen.")