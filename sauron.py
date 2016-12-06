# The all seeing eye


import subprocess
import sys

def main():
    # Call make to build the project
    my_make = subprocess.Popen("make")

    sys.exit(my_make.wait())

if __name__ == "__main__":
    main()
