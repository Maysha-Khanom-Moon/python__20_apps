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
    <br>

- cursor always try to read the right side contents. For 1st read it started from the beginnig and stop in the end. For 2nd time cursor already at the end, so nothing left to read!
    <br>

- readlines() --> Reads the entire file line by line and returns a list of strings, where each element in the list represents a line from the file
    <br>

- write() --> write entire content as a single string
- writelines() --> write a list
    <br>

- by default: open function mode = 'r'
    - help(open)
        <br>


##### why row string?
- r'file/path/name...'
- becuase /n or /t have special meaning, to remove the clash we use row string
- python console always gives row string


#### uses of python
1. web development
2. data science, ML, AI
3. automations
4. general programming
5. web scraping
6. others (data analysis, visualization, api building, etc)


#### List comprehension
List comprehendions can create a new list by modifiying an existing list

- [expression for item in iterable if condition] --> always return a list
    - new_todos = [item.strip('\n') for item in todos]


#### with-context manager
- recommended
- The file wile be closed implicitly once all the indented lines have been executed
    <br>
```
with open('file/path', 'mode') as file_variable:
    ... ...
```

#### creating and maintain a program
1. MVP --> minimum viable product
2. features add
3. bug fixing
4. code optimization
5. back to step 2


#### single line if-else
- checkLen = True if len(password) >= 8 else False
- checkLower = any(i in lower for i in password)

- The in operator is also known as a "containment test"

- match is more faster than if-elif-else. however, there is limitation to check conditions. Because match just check the value is equal or not, Others are not applicale


#### dictionary --> dict
- {(key, value), ...}
```
value: data
key: metadata

dir(dict)

dict.values() --> returns the list of values
dict.keys() --> returns the list of keys

dict["key"] = value ; if key is a string
or,
dict[number] = value ; if key is a number
or,
dict.key = value ; if key is a variable
```


#### Try-except
Used when you want to anticipate a specific kind of error. You can use it to display a friendly error message to the user instead of letting the program end abruptly showing the user an error message that they can hardly understand

```
try:
    ... ... ...
    firstly try this indented under "try"
    ... ... ...

except SpecificError:
    ... ... ...
```

#### Custom function
- Parameters: they are local variables that get a value dynamically when the function is called

- Arguments: assigned to arguments when the function is called.
