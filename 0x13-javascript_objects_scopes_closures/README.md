# JavaScript - Objects, Scopes and Closures

[![js-semistandard-style](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg)](https://github.com/standard/semistandard)

## Resources
* [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
* [Object-oriented JavaScript (read all examples!)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
* [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
* [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
* [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
* [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
* [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
* [this/self](https://alistapart.com/article/getoutbindingsituations/)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

***

## Tasks
### 0. Rectangle #0
an empty class `Rectangle` that defines a rectangle:

File: [0-rectangle.js](./0-rectangle.js)

### 1. Rectangle #1
a class Rectangle that defines a rectangle:
* You must use the `class` notation for defining your class
* The constructor must take 2 arguments `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`

File: [1-rectangle.js](./1-rectangle.js)

### 2. Rectangle #2
a class `Rectangle` that defines a rectangle:
* You must use the `class` notation for defining your class
* The constructor must take 2 arguments `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object

File: [2-rectangle.js](./2-rectangle.js)

### 3. Rectangle #3
a class `Rectangle` that defines a rectangle:
* You must use the `class` notation for defining your class
* The constructor must take 2 arguments: `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
* Create an instance method called `print()` that prints the rectangle using the character X

File: [3-rectangle.js](./3-rectangle.js)

### 4. Rectangle #4
a class `Rectangle` that defines a rectangle:
* You must use the `class` notation for defining your class
* The constructor must take 2 arguments: `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
* Create an instance method called `print()` that prints the rectangle using the character `X`
* Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
* Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

File: [4-rectangle.js](./4-rectangle.js)

### 5. Square #0
a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:
* You must use the `class` notation for defining your class and `extends`
* The constructor must take 1 argument: `size`
* The constructor of `Rectangle` must be called (by using `super()`)

File: [5-square.js](./5-square.js)

### 6. Square #1
a class `Square` that defines a square and inherits from `Square` of `5-square.js`:
* You must use the `class` notation for defining your class and `extends`
* Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
  * If c is undefined, use the character X

File: [6-square.js](./6-square.js)

### 7. Occurrences
a function that returns the number of occurrences in a list:
* Prototype: `exports.nbOccurences = function (list, searchElement)`

File: [7-occurrences.js](./7-occurrences.js)

### 8. Esrever
a function that returns the reversed version of a list:
* Prototype: `exports.esrever = function (list)`
* You are not allow to use the built-in method `reverse`

File: [8-esrever.js](./8-esrever.js)

### 9. Log me
a function that prints the number of arguments already printed and the new argument value. (see example below)
* Prototype: `exports.logMe = function (item)`
* Output format: `<number arguments already printed>: <current argument value>`

File: [9-logme.js](./9-logme.js)

### 10. Number Conversion
a function that converts a number from base 10 to another base passed as argument:
* Prototype: `exports.converter = function (base)`
* You are not allowed to import any file
* You are not allowed to declare any new variable (`var`, `let`, etc..)

File: [10-converter.js](./10-converter.js)

### 11. Factor index
a script that imports an array and computes a new array.
* Your script must import `list` from the file `100-data.js`
* You must use a `map`. [Tips](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?v=control)
* A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
* Print both the initial list and the new list

File: [100-map.js](./100-map.js)

### 12. Sorted occurrences
a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
* Your script must import `dict` from the file `101-data.js`
* In the new dictionary:
  * A key is a number of occurrences
  * A value is the list of user ids
* Print the new dictionary at the end

File: [101-sorted.js](./101-sorted.js)

### 13. Concat files
a script that concats 2 files.
* The first argument is the file path of the first source file
* The second argument is the file path of the second source file
* The third argument is the file path of the destination

File: [102-concat.js](./102-concat.js)
