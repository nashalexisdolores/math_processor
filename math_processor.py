class MathProcessor:
    def __init__(self, input_f="integers.txt"):
        self.input_f = input_f

    def run_math(self):
        with open(self.input_f, 'r') as src, \
             open('double.txt', 'w') as d, \
             open('triple.txt', 'w') as t:
            for line in src:
                n = int(line.strip())
                if n % 2 == 0:
                    d.write(f"{n**2}\n")
                else:
                    t.write(f"{n**3}\n")