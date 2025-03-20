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
        content = line.strip("output()").strip()
        print(content)

    def chk(self, line):
        condition = line.strip("chk()").strip()
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
def main():
    print("Welcome to HexaCode Interpreter")
    interpreter = HexaCodeInterpreter()
    while True:
        print("\nOptions:")
        print("1. Run HexaCode file (.Hxc)")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            filename = input("Enter the HexaCode file to run (with .Hxc extension): ")
            interpreter.run_file(filename)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
