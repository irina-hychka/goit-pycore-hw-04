import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_directory_tree(directory, indent=""):
    '''
    Prints the directory tree structure. Directories are displayed in blue,
    files - in green, error - in red.

    Param:
    directory (str or Path): The path to the directory that should be displayed.
    indent (str, optional): A string used for indentation to visually represent directory levels. 
    Defaults to an empty string.

    Returns:
    None: The function prints the directory structure but does not return any value. 
    ''' 
    try:
        path = Path(directory)
        
        # Checks if the given path exists
        if not path.exists():
            print(Fore.RED + "Error: The specified path does not exist." + Style.RESET_ALL)
            return
        
        # Checks if the given path is a directory
        if not path.is_dir():
            print(Fore.RED + "Error: The specified path is not a directory." + Style.RESET_ALL)
            return
        
        # Prints the root directory name in cyan
        print(Fore.CYAN + path.name + Style.RESET_ALL)
        
        # Prints recursively subdirectories and files
        def _print_tree(current_path, level_indent):
            for item in sorted(current_path.iterdir()):
                if item.is_dir():
                    # Prints directory name in blue
                    print(level_indent + Fore.BLUE + item.name + Style.RESET_ALL)
                    # Recursive call with increased indentation
                    _print_tree(item, level_indent + "    ")
                else:
                    # Prints file name in green
                    print(level_indent + Fore.GREEN + item.name + Style.RESET_ALL)
        # Starts recursion from the first level
        _print_tree(path, "    ")
    
    except Exception as e:
        # Prints error message if an exception
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)

# Initializes colorama
init()

# Checks if a directory path was provided as a command-line argument
if len(sys.argv) < 2:
    print(Fore.RED + "Usage: python script.py <directory_path>" + Style.RESET_ALL)
else:
    # Get the path from the command-line argument
    directory_path = sys.argv[1]  
    print_directory_tree(directory_path)