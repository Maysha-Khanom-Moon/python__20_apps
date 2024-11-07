# The Python Mega Course
There are 2 catergories of Program:
1. Non-Interactive Programs

2. Interactive Programs
    - CLI -- Command Line Interface
    - GUI -- Graphical User Interface (desktop)
    - Web Interface Programs (web apps)

#### day 03
- python (source code) --> CPython (interpreter) --> processor (machine code) --> execution (output)

- CPython --> python language is written by C

- .py also a text file

```
while loop -->  iterates as long as the while-condition is True

for loop --> iterates that many times as there are items in the list that is being iterated

Match-case --> to match a string out of a predefined number of strings

If-else --> check more complex conditions
```

#### day 05
- variables that are only referenced inside a function are implicitly global
- outside the function it's not possible to access the local variables


#### day 06
- read() --> Reads the entire content of the file as a single string
- 1st file.read() --> whole file data
- 2nd file.read() --> empty
- because no longer read anything else from the file since it has already reached EOF

- cursor always try to read the right side contents. For 1st read it started from the beginnig and stop in the end. For 2nd time cursor already at the end, so nothing left to read!

- readlines() --> Reads the entire file line by line and returns a list of strings, where each element in the list represents a line from the file

- write() --> write entire content as a single string
- writelines() --> write a list

##### why row string?
- r'file/path/name...'
- becuase /n or /t have special meaning, to remove the clash we use row string