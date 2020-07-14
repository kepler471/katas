class Smallfuck:
    def __init__(self, code_, tape_):
        self.instructions = {
            ">": self.move,
            "<": self.move,
            "*": self.flip,
            "[": self.goto,
            "]": self.goto,
        }
        self.power = True
        self.code = [x for x in code_ if x in self.instructions.keys()]
        self.tape = list(tape_)
        self.pointer = 0
        self.cmd = 0

    def evaluate(self):
        if self.power:
            self.instructions[self.code[self.cmd]]()
            if self.cmd > len(self.code) - 1:
                self.power = False
            elif self.pointer < 0 or self.pointer > len(self.tape) - 1:
                self.power = False

    def move(self):
        if self.code[self.cmd] == ">":
            self.cmd += 1
            self.pointer += 1
        elif self.code[self.cmd] == "<":
            self.cmd += 1
            self.pointer -= 1

    def flip(self):
        self.tape[self.pointer] = str(1 - int(self.tape[self.pointer]))
        self.cmd += 1

    def goto(self):
        def search(code, cmd, bit):
            count = 1
            bra = code[cmd]
            ket, sign = (']', 1) if bra == '[' else ('[', -1)
            scope = code[cmd + 1:] if bra == '[' else reversed(code[: cmd - 1])
            if (bra == '[' and not int(bit)) or (bra == ']' and int(bit)):
                for n, i in enumerate(scope):
                    if i == bra:
                        count += 1
                    elif i == ket:
                        count -= 1
                        if count == 0:
                            return sign * (n + 2)
            return 1

        self.cmd += search(self.code, self.cmd, self.tape[self.pointer])


def interpreter(code, tape):
    program = Smallfuck(code, tape)
    while program.power:
        program.evaluate()
    return "".join(program.tape)
