class HexaCodeInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        lines = code.split("\n")
        for line in lines:
            self.execute(line.strip())

    def execute(self, line):
        tokens = line.split(" ")

        if tokens[0] == "output":
            self.output(line)
        elif tokens[0] == "chk":
            self.chk(line)
        elif tokens[0] == "function":
            self.create_function(line)
        elif "=" in line:  # Variable assignment
            self.assign_variable(line)

    def output(self, line):
        if "output(" in line and line.endswith(")"):
            content = line[len("output("):-1]  # Remove "output(" and ")"
            content = content.strip('"')  # Remove surrounding quotes
            print(content)
        else:
            print("Error: Invalid output syntax.")

    def chk(self, line):
        condition = line.replace("chk", "").strip("()").strip()
        if condition == "true":
            print("Condition is true!")
        else:
            print("Condition is false!")

    def create_function(self, line):
        print("Function created.")

    def assign_variable(self, line):
        var_name, var_value = line.split("=")
        self.variables[var_name.strip()] = var_value.strip()
        print(f"Variable {var_name.strip()} assigned to {var_value.strip()}")

    # Method to run HexaCode files
    def run_file(self, file_path):
        if not file_path.endswith(".Hxc"):
            print("Error: The file must end with '.Hxc'.")
            return
        
        try:
            with open(file_path, "r") as file:
                code = file.read()
            self.interpret(code)
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")

# Command-line interaction
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        interpreter = HexaCodeInterpreter()
        interpreter.run_file(filename)
    else:
        print("Usage: python HexaCodeInterpreter.py <file.Hxc>")
