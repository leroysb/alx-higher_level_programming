# Exceptions

## Resources
1. [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
2. [Learn to Program 11 Static & Exceptipn Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4)

## Tasks
### 0. Safe list printing
A function that prints `x` elements of a list.
* Prototype: `def safe_print_list(my_list=[], x=0):`
* `my_list` can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* `x` represents the number of elements to print
* `x` can be bigger than the length of `my_list`
* Returns the real number of elements printed
* You have to use `try: / except:`
* You are not allowed to import any module
* You are not allowed to use `len()`

**File**: [0-safe_print_list.py](./0-safe_print_list.py)

### 1. Safe printing of an integer list
A function that prints an integer with `"{:d}".format()`.
* Prototype: `def safe_print_integer(value):`
* `value` can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
* Otherwise, returns `False`
* You have to use `try: / except:`
* You have to use `"{:d}".format()` to print as integer
* You are not allowed to import any module
* You are not allowed to use `type()`

**File**: [1-safe_print_integer.py](./1-safe_print_integer.py)

### 2. Print and count integers
A function that prints the first x elements of a list and only integers.
* Prototype: `def safe_print_list_integers(my_list=[], x=0):`
* `my_list` can contain any type (integer, string, etc.)
* All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
* `x` represents the number of elements to access in `my_list`
* `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
* Returns the real number of integers printed
* You have to use `try: / except:`
* You have to use `"{:d}".format()` to print an integer
* You are not allowed to import any module
* You are not allowed to use `len()`

**File**: [2-safe_print_list_integers.py](./2-safe_print_list_integers.py)

### 3. Integers division with debug
A function that divides 2 integers and prints the result.
* Prototype: `def safe_print_division(a, b):`
* You can assume that `a` and `b` are integers
* The result of the division should print on the `finally:` section preceded by `Inside result:`
* Returns the value of the division, otherwise: `None`
* You have to use `try: / except: / finally:`
* You have to use `"{}".format()` to print the result
* You are not allowed to import any module

**FIle**: [3-safe_print_division.py](./3-safe_print_division.py)

### 4. Divide a list
A function that divides element by element 2 lists.
* Prototype: `def list_division(my_list_1, my_list_2, list_length):`
* `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
* `list_length` can be bigger than the length of both lists
* Returns a new list (length = `list_length`) with all divisions
* If 2 elements can’t be divided, the division result should be equal to `0`
* If an element is not an integer or float: print: `wrong type`
* If the division can’t be done (`/0`): print: `division by 0`
* If `my_list_1` or `my_list_2` is too short, print: `out of range`
* You have to use `try: / except: / finally:`
* You are not allowed to import any module

**File**: [4-list_division.py](./4-list_division.py)

### 5. Raise exception
A function that raises a type exception.
* Prototype: `def raise_exception():`
* You are not allowed to import any module

**File**: [5-raise_exception.py](./5-raise_exception.py)

### 6. Raise a message
A function that raises a name exception with a message.
* Prototype: `def raise_exception_msg(message=""):`
* You are not allowed to import any module

**File**: [6-raise_exception_msg.py](./6-raise_exception_msg.py)