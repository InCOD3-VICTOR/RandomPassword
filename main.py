"""

Title: Random Password
Author: InsideExploit
Version: 1.0.0

"""

# Some usefull imports
import random, string, signal, sys

max_lenght = 8192

# Handler Quit

def handler_quit(sig, frame):
    sys.exit(0) # Function on keybind

signal.signal(signal.SIGINT, handler_quit) # Start thread and handle the signal (Check when pressed)

# Generate Function
def get_random_string(length):

    print("\n")

    if(length > max_lenght):
        print("[ERROR] The lenght is too much, please retry with less one. (You can change max lenght from the source)")
        exit(-1)

    letters = string.ascii_letters # You can use ascii_lowercase for generate lowercase characters only, ascii_uppercase for generate uppercase characters only and ascii_letters for both
    array_passwrod = ''.join(random.choice(letters) for i in range(length))
    print("[SUCCESS] Your password has been generated: ", array_passwrod)

# Main Function
def start():

    print("""
██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ███╗    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗████╗ ████║    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██╔████╔██║    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║██║╚██╔╝██║    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚═╝ ██║    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
""") # Print an ASCII Text

    print("Welcome to Random Password Generator, this program is coded in python and its an open source project.") # Just an additional welcome line
    print("Please select an option about password generator types:") # Additional line for asking selection of types
    print("\n")
    lenght_request = input("1) How much characters?: ")  # Ask for special characters
    
    get_random_string(int(lenght_request)) # Enable function with parameters and execute it


# Start Function
if __name__ == "__main__":
    start()
