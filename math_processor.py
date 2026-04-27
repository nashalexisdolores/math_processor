import os

class MathProcessor:
    def __init__(self, input_f="integers.txt"):
        # This line finds the folder where THIS script is saved
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.input_path = os.path.join(base_dir, input_f)
        self.double_path = os.path.join(base_dir, "double.txt")
        self.triple_path = os.path.join(base_dir, "triple.txt")

    def run_math(self):
        if not os.path.exists(self.input_path):
            print(f"Error: Could not find {self.input_path}")
            print("Make sure 'integers.txt' is in the same folder as this script!")
            return

        try:
            with open(self.input_path, 'r') as src, \
                 open(self.double_path, 'w') as d_file, \
                 open(self.triple_path, 'w') as t_file:
                
                for line in src:
                    val = line.strip()
                    if not val: continue # Skip empty lines
                    
                    num = int(val)
                    if num % 2 == 0:
                        d_file.write(f"{num**2}\n")
                    else:
                        t_file.write(f"{num**3}\n")
            
            print("Processing successful! Check double.txt and triple.txt.")
            
        except ValueError:
            print("Error: The file contains non-integer data.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")