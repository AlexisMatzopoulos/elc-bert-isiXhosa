# imports the subprocess module to run external commands
import subprocess

# function to run a given python script
def run_script(script_name):
    print(f"Running {script_name}...")  # logs the script being run
    # runs the script and captures output
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    # checks if the script ran successfully
    if result.returncode == 0:
        print(f"{script_name} completed successfully.")  # success message
    else:
        print(f"{script_name} failed with error:")  # failure message
        print(result.stderr)  # prints the error output

# main function to run a list of scripts
def main():
    scripts = ['preprocess_xhosa.py', 'preprocess_xhosa_all.py']  # list of scripts to run

    for script in scripts:
        run_script(script)  # runs each script in the list

# ensures the main function is only run if the script is executed directly
if __name__ == "__main__":
    main()