import subprocess
import sys

def run_program_with_input(py_file, input_file):
    try:
        with open(input_file, 'r') as input_data:
            input_text = input_data.read()
        
        process = subprocess.Popen(
            [sys.executable, py_file],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        output, error = process.communicate(input_text)
        
        if process.returncode == 0:
            print("Program executed successfully.")
        
            output = output.split("\n",1)[1]
            with open("output.txt", 'w') as output_data:
                output_data.write(output) 
                
            print("Output written to output.txt")           
        else:
            print("Error occurred while running the program:")
            print("Output:\n", output)
            print("Error:\n", error)
    
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run_script.py <python_file.py> <input_file.txt>")
        sys.exit(1)
    
    python_file = sys.argv[1]
    input_file = sys.argv[2]
    
    run_program_with_input(python_file, input_file)
