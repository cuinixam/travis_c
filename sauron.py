# The all seeing eye


import subprocess
import sys
import os

def main():
    print("[1] Running the Tools Test Suite ...")
    test_tools_proc = subprocess.Popen(["python3",'./test/run_all_tests.py'])
    status = test_tools_proc.wait()
    
    if status:
        print("Tools Test Suite [FAILED]")
        sys.exit(status)
    print("Tools Test Suite [PASSED]")
    
    print("[2] Run make to build the project ...")
    my_make = subprocess.Popen("make")
    status = my_make.wait()
    
    if status:
        print("Build process [FAILED]")
    else:
        print("Build process [PASSED]")
    
    sys.exit(status)

if __name__ == "__main__":
    main()
