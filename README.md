# starter-python-file
Folks starting out with Python might benefit from a file with some more advanced features in it. 
The file (called example_script.py):
1. gives some explanation of `#!/usr/bin/env python3`
2. notes source and license and some implications of that
3. imports [logging libary](https://docs.python.org/3.11/library/logging.html) while configuring it to be silent - then explains how to set it to other levels
4. provides a hello world function that runs
5. notes that string formatting method is used in making log messages
6. explains that line continuation character is used to have long line become two lines on screen while still functioning as one line of code
7. includes in the hello world function a nested for loop that will show logging messages if logging level reads `level=logging.DEBUG`
8. has example `logging.warning()` and `logging.error()` calls and messages with explanations
9. indicates space for use to add more code
10. uses `if __name__ == "__main__":` to provide a section for code that will run only if the script is executed from the commandline rather than import into the interpreter or another file
11. provides a pass statement so one can comment out the call to hello world and see the result of doing that when run from commandline as script
12. calls the hello world function
13. includes an example TODO: point to demonstrate an IDE feature - which can make those into lists
    


