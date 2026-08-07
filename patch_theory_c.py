import json

with open("curriculum/tracks/c_programming.json", "r", encoding="utf-8") as f:
    data = json.load(f)

theories = {
    ("C Syntax", "Hello World in C"): """## The Anatomy of a C Program

C is a compiled, procedural programming language that serves as the foundation for modern computing. Operating systems (Linux, Windows, macOS), databases (PostgreSQL), and interpreters for other languages (Python, Ruby) are written in C.

Unlike Python, C is not executed directly. It must be translated into raw machine code (binary) by a **Compiler** (like `gcc` or `clang`) before it can run.

### The Standard Template

Every executable C program has a specific, rigid structure:

```c
#include <stdio.h> // 1. Preprocessor Directive

int main() {       // 2. The Main Function (Entry Point)
    
    // 3. Statements
    printf("Hello, World!\\n");
    
    return 0;      // 4. Return Statement
}
```

### Breaking It Down

**1. `#include <stdio.h>`**
This is a preprocessor directive. Before the compiler even looks at your code, the preprocessor finds the file `stdio.h` (Standard Input/Output) and literally copies its contents into your file. Without this, your program wouldn't know what `printf` is.

**2. `int main()`**
This is where execution begins. The Operating System calls this function when you run the program. 
- `int` means this function will return an integer to the OS when it finishes.
- `{}` (curly braces) define the start and end of the function's block. Indentation is optional in C, but braces are mandatory.

**3. `printf("Hello, World!\\n");`**
- `printf` (print formatted) writes text to the standard output (the console).
- `\\n` is the newline character. C does not automatically add newlines like Python's `print()` does.
- `;` (semicolon). **Every statement in C must end with a semicolon.** Forgetting this is the most common syntax error for beginners.

**4. `return 0;`**
When `main()` finishes, it must return a status code to the Operating System. By convention, returning `0` means "Success" (the program ran without errors). Returning any non-zero number (like `1` or `-1`) indicates that a fatal error occurred.""",

    ("C Syntax", "Variables & Types"): """## Statically Typed Memory

C is a **statically typed** language. This means you cannot just write `age = 25`. You must explicitly tell the compiler exactly what type of data the variable will hold *before* you use it. Once a variable is declared as an `int`, it can never hold a decimal or a string.

Why? Because C requires you to manage memory precisely. The compiler needs to know exactly how many bytes of RAM to reserve for that variable.

### Core Data Types

1. **`int` (Integer)**
   - Whole numbers (e.g., `-10`, `0`, `42`).
   - Usually takes 4 bytes of memory.
   - Range: roughly -2 billion to +2 billion.

2. **`float` (Floating Point)**
   - Decimal numbers (e.g., `3.14`, `-0.01`).
   - Takes 4 bytes of memory (single precision).
   - Accurate to about 6-7 decimal places.

3. **`double` (Double Precision)**
   - Decimal numbers, but takes 8 bytes of memory.
   - Accurate to about 15 decimal places. Used for precise scientific or financial math.

4. **`char` (Character)**
   - A single letter or symbol (e.g., `'A'`, `'?'`, `'7'`).
   - Enclosed in **single quotes** (double quotes are for strings).
   - Takes exactly 1 byte of memory.

### Formatting Output with `printf`

Because C variables are strictly typed, you cannot simply concatenate them with text like `print("Age: " + age)`. 

Instead, you use **Format Specifiers** inside `printf`. These act as placeholders, telling C what type of data to inject into the string.

```c
int age = 25;
float height = 1.75;
char grade = 'A';

// %d is for int (decimal/base-10)
printf("I am %d years old.\\n", age);

// %f is for float/double. .2 limits to 2 decimal places.
printf("My height is %.2f meters.\\n", height);

// %c is for char
printf("I got an %c on the test.\\n", grade);
```

**Common Specifiers:**
- `%d` or `%i`: `int`
- `%f`: `float`
- `%lf`: `double` (long float)
- `%c`: `char`
- `%s`: string (character array)
- `%p`: pointer (memory address)""",

    ("C Syntax", "Arithmetic Operations"): """## The Mechanics of C Arithmetic

Math in C works mostly as you would expect from standard algebra, but with a few critical caveats related to how the CPU handles data types.

The basic operators are:
- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division)
- `%` (Modulo / Remainder)

### The Integer Division Trap

The most common source of logic bugs in C is integer division.

If you divide two integers, the CPU performs *integer division*. It calculates the result and **truncates** (drops) any decimal remainder. It does not round up; it simply deletes the fraction.

```c
int total_apples = 10;
int people = 3;

// 10 / 3 is 3.333..., but because both are ints, C truncates it.
int apples_per_person = total_apples / people; 

printf("%d", apples_per_person); // Outputs: 3
```

### Type Casting (Forcing Floats)

To get a true decimal result from dividing two integers, you must temporarily convert (or "cast") at least one of the integers into a `float` before the division happens. 

You do this by placing the new type in parentheses `(float)` immediately before the variable.

```c
int total = 10;
int people = 3;

// Cast 'total' to a float. 10.0 / 3 = 3.333...
float exact = (float)total / people; 

printf("%.2f", exact); // Outputs: 3.33
```

### Modulo (`%`)

The modulo operator is incredibly useful in algorithms. It returns the integer remainder of a division. It only works on integers.

```c
int remainder = 10 % 3; // 10 divided by 3 is 3, remainder 1.
printf("%d", remainder); // Outputs: 1
```

**Common uses for modulo:**
- Finding even/odd numbers (`if (num % 2 == 0)`)
- Clock arithmetic (keeping hours between 0 and 23)
- Hash table indexing""",

    ("C Syntax", "If/Else in C"): """## Control Flow: Conditional Logic

An `if` statement allows a program to make decisions and execute specific blocks of code only when a condition evaluates to True.

In C, the concept of "True" and "False" is fundamentally tied to integers:
- **`0`** is strictly **False**.
- **Any non-zero number** (usually `1`) is **True**.

*Note: C did not originally have a boolean type. While modern C includes `<stdbool.h>`, at the machine level, booleans are still just integers.*

### The Structure of If/Else

Conditions must be enclosed in parentheses `()`. The code to execute must be enclosed in curly braces `{}`.

```c
int score = 85;

if (score >= 90) {
    printf("Grade: A\\n");
} else if (score >= 80) {
    printf("Grade: B\\n");
} else {
    printf("Study harder.\\n");
}
```

### Comparison and Logical Operators

To build conditions, you use relational operators:
- `==` (Equal to. *Do not confuse with `=` which is assignment!*)
- `!=` (Not equal to)
- `>` and `<` (Greater than / Less than)
- `>=` and `<=` (Greater than or equal / Less than or equal)

To combine multiple conditions, use logical operators:
- `&&` (Logical AND): True only if *both* sides are true.
- `||` (Logical OR): True if *at least one* side is true.
- `!` (Logical NOT): Inverts true to false, and false to true.

```c
int age = 25;
int has_license = 1; // 1 means true

// AND Example
if (age >= 18 && has_license == 1) {
    printf("You can drive.\\n");
}

// OR Example
if (age < 12 || age > 65) {
    printf("You get a discount.\\n");
}
```

### The Dangling Else and Braces

If an `if` block contains only a single line of code, the curly braces are technically optional. However, omitting them is a notorious source of bugs (e.g., Apple's "goto fail" SSL bug). **Always use curly braces, even for single lines.**""",

    ("C Syntax", "Loops in C"): """## Iteration: Automating Repetition

Loops allow you to execute a block of code multiple times without rewriting it. C provides three types of loops: `while`, `do-while`, and `for`.

### The `while` Loop

Use a `while` loop when you don't know exactly how many times the loop will run, but you know the condition that should stop it.

```c
int count = 5;

// Checks the condition BEFORE running the block
while (count > 0) {
    printf("%d... ", count);
    count--; // Decrement by 1
}
printf("Liftoff!\\n");
```

### The `do-while` Loop

A `do-while` loop is similar, but it checks the condition AFTER running the block. This guarantees the code will execute **at least once**, regardless of the condition. Often used for menus or user input validation.

```c
int choice;
do {
    printf("Press 1 to exit: ");
    scanf("%d", &choice); // Get input from user
} while (choice != 1);
```

### The `for` Loop

Use a `for` loop when you know exactly how many times you want to iterate (e.g., looping through an array, or counting from 1 to 10). It consolidates the setup, condition, and increment into a single, clean line.

```c
// 1. Initialize: int i = 0 (Runs once)
// 2. Condition: i < 5 (Checked before every iteration)
// 3. Increment: i++ (Runs after every iteration completes)

for (int i = 0; i < 5; i++) {
    printf("Iteration %d\\n", i);
}
```

### Break and Continue

You can manually control the flow inside any loop:
- `break`: Instantly kills the loop and jumps out of it.
- `continue`: Instantly skips the rest of the current iteration and jumps back to the top to evaluate the condition again.

```c
for (int i = 1; i <= 10; i++) {
    if (i == 3) {
        continue; // Skip printing 3
    }
    if (i == 8) {
        break; // Stop completely when we hit 8
    }
    printf("%d ", i); 
}
// Output: 1 2 4 5 6 7
```""",

    ("C Syntax", "Functions in C"): """## Modularity and Prototypes

As programs grow larger than a few dozen lines, putting everything inside `main()` becomes unreadable and impossible to maintain. **Functions** allow you to break your code into reusable, isolated blocks.

### The Anatomy of a Function

A function definition has a return type, a name, parameters, and a body.

```c
// ReturnType Name(Parameters)
int add_numbers(int a, int b) {
    int sum = a + b;
    return sum; // Must return an int
}
```

If a function does not return any data (e.g., it just prints to the screen), its return type must be `void`.

```c
void print_warning() {
    printf("WARNING: Disk Space Low!\\n");
    // No return statement needed
}
```

### The Compilation Order Problem

The C compiler reads your file strictly from top to bottom, line by line. 

If you try to call a function inside `main()` before you have defined that function further down in the file, the compiler will panic and throw an "implicit declaration" error because it hasn't seen it yet.

**Bad Example:**
```c
int main() {
    int x = square(5); // ERROR: What is 'square'? I haven't seen it!
    return 0;
}

int square(int n) {
    return n * n;
}
```

### The Solution: Function Prototypes

To solve this, you use **Function Prototypes** (also called declarations). A prototype is just the function's header ending with a semicolon, placed at the top of the file. It acts as a promise to the compiler: *"I promise a function with this signature exists somewhere, don't worry about it yet."*

**Good Example:**
```c
#include <stdio.h>

// 1. Prototype (Declaration)
int square(int n); 

int main() {
    // 2. The compiler knows 'square' takes an int and returns an int.
    int x = square(5); 
    return 0;
}

// 3. Actual Implementation (Definition)
int square(int n) {
    return n * n;
}
```
This separation between *declaration* (interfaces) and *definition* (implementation) is a core philosophy of C architecture.""",

    ("Pointers Basics", "What are Pointers?"): """## The Fundamental Concept of C: Memory Addresses

Every variable you create in C is stored somewhere in your computer's Random Access Memory (RAM). 

Think of RAM as a massive neighborhood of mailboxes. Each mailbox can hold a piece of data (like the integer `42`), and every single mailbox has a unique, sequential house number (the **Memory Address**), usually represented in hexadecimal (e.g., `0x7fffc08b`).

A **Pointer** is simply a variable that stores a memory address instead of regular data. It *points* to where the data lives.

### The Two Pointer Operators

To master pointers, you must understand two symbols: `&` and `*`.

**1. The "Address-of" Operator (`&`)**
When placed before a regular variable, `&` asks the computer, *"What is the memory address of this variable?"*

```c
int age = 25;
// Read as: "pointer-to-int ptr gets the address of age"
int *ptr = &age; 

printf("Value: %d\\n", age);         // Outputs: 25
printf("Address: %p\\n", &age);      // Outputs: 0x7ffe... (the address)
printf("Pointer holds: %p\\n", ptr); // Outputs: 0x7ffe... (same address)
```

**2. The Dereference Operator (`*`)**
When placed before a pointer variable, `*` asks the computer, *"Go to the address stored in this pointer, and give me the actual data sitting inside that mailbox."*

```c
int age = 25;
int *ptr = &age;

// Read as: "print the integer located AT the address in ptr"
printf("Value via pointer: %d\\n", *ptr); // Outputs: 25

// We can also change the value remotely!
*ptr = 100; // "Go to the address in ptr, and overwrite the data with 100"

printf("New age: %d\\n", age); // Outputs: 100
```

### Why Do Pointers Exist?

1. **Performance**: Passing a massive 50-megabyte image structure to a function would require the CPU to copy all 50MB. Passing a pointer to that image only requires copying 8 bytes (the address).
2. **Hardware Access**: C allows you to point directly to specific memory addresses used by hardware, which is how device drivers control graphics cards and network chips.
3. **Dynamic Memory**: Pointers are the only way to manage memory allocated on the heap during runtime.""",

    ("Pointers Basics", "Pointers & Functions"): """## Pass-by-Value vs. Pass-by-Reference

A fundamental rule of C is that **all function arguments are passed by value.**

When you pass a variable to a function, the compiler makes a complete, isolated copy of that variable and gives it to the function. The function cannot modify the original variable.

### The Problem (Pass-by-Value)

```c
void add_ten(int x) {
    x = x + 10; // This modifies the local COPY of x
}

int main() {
    int health = 50;
    add_ten(health);
    printf("%d", health); // Outputs: 50. The original was untouched!
    return 0;
}
```

### The Solution: Pass-by-Reference (Using Pointers)

If you want a function to modify a variable declared in `main()`, you cannot pass the value of the variable. You must pass the **address** of the variable. The function then receives a pointer to the original memory location, allowing it to reach out and modify the original data.

```c
// 1. Function parameter is a POINTER to an int
void add_ten(int *x) {
    // 3. Dereference the pointer to modify the actual data
    *x = *x + 10; 
}

int main() {
    int health = 50;
    // 2. Pass the ADDRESS of the variable using &
    add_ten(&health); 
    
    printf("%d", health); // Outputs: 60. Success!
    return 0;
}
```

### The Classic 'Swap' Interview Question

A classic C programming task is writing a function to swap the values of two variables. It is impossible without pointers.

```c
// Incorrect (Pass-by-value)
void bad_swap(int a, int b) {
    int temp = a; a = b; b = temp; // Only swaps local copies
}

// Correct (Pass-by-reference)
void good_swap(int *a, int *b) {
    int temp = *a; // Store the value AT address a
    *a = *b;       // Put the value AT address b into address a
    *b = temp;     // Put the original value into address b
}

int main() {
    int x = 1, y = 2;
    good_swap(&x, &y); // Must pass addresses!
}
```
Whenever a C function needs to modify an input parameter or "return" more than one value, it uses pointers.""",

    ("Pointers Basics", "Pointer Arithmetic"): """## Moving Through Memory

Because pointers hold numerical memory addresses, you can actually perform math on them (addition and subtraction). However, pointer arithmetic does not work like normal math.

When you add `1` to a pointer, it does not add 1 byte to the address. It adds **1 unit of the underlying data type's size.**

### How the Math Works

Assume an `int` takes 4 bytes of memory.
If `int *ptr` holds the address `1000`:
- `ptr + 1` evaluates to `1004` (moves forward 1 integer).
- `ptr + 2` evaluates to `1008` (moves forward 2 integers).

If `char *c_ptr` holds the address `1000` (and chars are 1 byte):
- `c_ptr + 1` evaluates to `1001` (moves forward 1 character).

### The Secret Truth: Arrays are just Pointers

In C, an array is not an object. The name of an array is actually just a pointer to the first element in memory. 

When you write `arr[3]`, the compiler actually translates this into pointer arithmetic under the hood: `*(arr + 3)`. It means: "Take the starting address of `arr`, jump forward 3 memory slots, and dereference it."

```c
int numbers[] = {10, 20, 30, 40};
int *ptr = numbers; // ptr now points to the '10'

printf("%d\\n", *ptr);       // Outputs 10
printf("%d\\n", *(ptr + 1)); // Outputs 20
printf("%d\\n", *(ptr + 2)); // Outputs 30

// You can also increment the pointer variable itself
ptr++; 
printf("%d\\n", *ptr); // Outputs 20
```

### Iterating with Pointers

Pointer arithmetic allows for highly optimized loops, which is how the standard library processes strings and memory buffers.

```c
int arr[] = {5, 10, 15, 20};
int *ptr = arr;

for (int i = 0; i < 4; i++) {
    printf("%d ", *ptr);
    ptr++; // Move the pointer to the next integer in memory
}
// Outputs: 5 10 15 20
```

**Warning:** C does not check boundaries. If you keep doing `ptr++` past the end of your array, you will start reading (or overwriting!) random memory belonging to other variables, leading to catastrophic bugs and security vulnerabilities.""",

    ("Pointers Basics", "NULL Pointers"): """## The Danger of Uninitialized Pointers

When you declare a regular variable like `int age;` without initializing it, C fills it with whatever "garbage" data happens to be left over in that memory slot from a previous program.

When you declare a pointer like `int *ptr;` without initializing it, it contains a garbage memory address. This is called a **Wild Pointer**. If you attempt to dereference a wild pointer (`*ptr = 100;`), you are commanding the CPU to write data to a completely random location in RAM. 
- If you're lucky, the OS will block you, resulting in a **Segmentation Fault** (a crash).
- If you're unlucky, you overwrite critical data in your own program silently.

### The Concept of NULL

To prevent wild pointers, you should always initialize pointers to point to "nothing" if they aren't ready to point to something specific. In C, "nothing" is represented by the macro `NULL`.

At the machine level, `NULL` is usually just the memory address `0` (an address the OS guarantees you are never allowed to access).

```c
#include <stdio.h>

int main() {
    int *ptr = NULL; // Safe initialization
    
    // We can safely check if the pointer is valid before using it
    if (ptr != NULL) {
        printf("%d\\n", *ptr);
    } else {
        printf("Pointer is uninitialized, cannot dereference!\\n");
    }
    
    return 0;
}
```

### Dangling Pointers

Another massive source of bugs is the **Dangling Pointer**. This occurs when a pointer is pointing to valid memory, but then that memory is freed or destroyed (e.g., when a function returns and its local variables are destroyed).

```c
int* get_dangling() {
    int local_var = 10;
    return &local_var; 
    // DANGER! local_var is destroyed when the function ends.
    // The returned pointer now points to invalid, dead memory.
}
```

**Best Practice:**
1. Always initialize pointers to `NULL` or a valid address immediately.
2. After freeing dynamic memory, immediately set the pointer to `NULL` so you don't accidentally try to use it again.""",

    ("Pointers Basics", "Double Pointers"): """## Pointers to Pointers

If a pointer is a variable that stores the address of a standard variable, a **Double Pointer** (`**`) is a variable that stores the address of another pointer. 

```c
int value = 42;
int *ptr = &value;      // Pointer to int
int **double_ptr = &ptr; // Pointer to pointer to int

// Dereferencing
printf("%d", *ptr);         // 42
printf("%p", *double_ptr);  // The address of 'ptr'
printf("%d", **double_ptr); // 42 (Dereferenced twice)
```

### Why Do We Need Double Pointers?

Recall that C is strictly **pass-by-value**. If you want a function to modify an integer in `main`, you must pass a pointer to that integer (`int *`).

But what if you want a function to modify a *pointer* in `main`? Specifically, what if you want a function to point a pointer at a newly allocated block of memory? You must pass a pointer *to the pointer* (`int **`).

### Example: Modifying a Pointer Inside a Function

```c
#include <stdio.h>
#include <stdlib.h>

// Incorrect: This only modifies the local copy of the pointer
void bad_allocate(int *p) {
    p = malloc(sizeof(int)); // Memory leak! The original pointer is unchanged.
}

// Correct: Pass a double pointer
void good_allocate(int **p) {
    // Dereference once to access the original pointer in main
    *p = malloc(sizeof(int));
}

int main() {
    int *my_ptr = NULL;
    
    // bad_allocate(my_ptr); // Fails
    
    // Pass the ADDRESS of the pointer
    good_allocate(&my_ptr);
    
    if (my_ptr != NULL) {
        *my_ptr = 100;
        printf("Allocated and set to: %d\\n", *my_ptr);
        free(my_ptr);
    }
    return 0;
}
```

Double pointers are incredibly common in C for building complex data structures (like linked lists or trees) where functions need to physically re-wire the pointers connecting the nodes, or when creating 2D arrays dynamically.""",

    ("Arrays & Strings", "C Arrays"): """## Fixed Memory Blocks

In higher-level languages like Python, lists can grow, shrink, and hold mixed data types dynamically. In C, an array is a rigid, contiguous block of memory. 

- All elements must be the exact same data type.
- The size must be defined when the array is created, and it **cannot change** (unless you use dynamic allocation on the heap).
- C does not store the size of the array internally.

### Declaration and Initialization

```c
// Declare an array of 5 integers (contains garbage data initially)
int scores[5];

// Initialize index by index
scores[0] = 90;
scores[1] = 85;

// Declare and initialize simultaneously (size is inferred)
int ages[] = {25, 30, 35, 40};
```

### The `sizeof` Trick

Because C arrays don't have a `.length` property, you have to calculate the size yourself using the `sizeof()` operator, which returns the size of an object in bytes.

To find the number of elements in an array, you take the total bytes of the array and divide by the bytes of a single element.

```c
int numbers[] = {10, 20, 30, 40, 50};

int total_bytes = sizeof(numbers); // e.g., 20 bytes (5 elements * 4 bytes/int)
int element_bytes = sizeof(numbers[0]); // e.g., 4 bytes

int length = total_bytes / element_bytes; // 20 / 4 = 5 elements

for (int i = 0; i < length; i++) {
    printf("%d\\n", numbers[i]);
}
```

### The Out-of-Bounds Danger

C does not check if you are accessing a valid index. If you declare an array of size 5 (`arr[0]` to `arr[4]`) and attempt to write to `arr[10] = 99;`, the compiler will not stop you. 

The program will blindly jump to the memory address where the 11th element *would* be and overwrite whatever data happens to live there. This is called a **Buffer Overflow** and is one of the most common causes of security vulnerabilities and system crashes in software history.""",

    ("Arrays & Strings", "String Functions"): """## The `<string.h>` Library

Because strings in C are just arrays of characters ending in a null-terminator (`\\0`), standard operators like `=` or `==` do not work on them. 

```c
char str1[10] = "Apple";
char str2[10];

// str2 = str1;          // ERROR: Cannot assign arrays!
// if (str1 == "Apple")  // ERROR: Compares pointer addresses, not string contents!
```

To manipulate strings, you must include the standard `<string.h>` library, which provides functions that iterate through the arrays byte by byte.

### Core String Functions

**1. `strlen(string)` (String Length)**
Returns the number of characters before the null-terminator.
```c
char text[] = "Hello";
int length = strlen(text); // Returns 5 (does not count the \0)
```

**2. `strcpy(destination, source)` (String Copy)**
Copies the contents of `source` into `destination`, including the null-terminator.
```c
char dest[20];
strcpy(dest, "World"); // dest now contains "World\0"
```
*Warning:* If the destination array is too small to hold the source string, `strcpy` will cause a buffer overflow. Safe modern C often uses `strncpy`.

**3. `strcat(destination, source)` (String Concatenate)**
Appends the `source` string to the end of the `destination` string.
```c
char greeting[20] = "Hello ";
strcat(greeting, "Alice"); // greeting is now "Hello Alice\0"
```

**4. `strcmp(string1, string2)` (String Compare)**
Compares two strings character by character based on their ASCII values.
- Returns `0` if the strings are exactly identical.
- Returns `< 0` if string1 comes before string2 alphabetically.
- Returns `> 0` if string1 comes after string2 alphabetically.

```c
if (strcmp("Apple", "Apple") == 0) {
    printf("Strings match!\\n");
}
```

These functions highlight the low-level nature of C: you are responsible for ensuring your destination arrays are large enough to hold the results of copies and concatenations.""",

    ("Arrays & Strings", "2D Arrays"): """## Matrices and Tables

A two-dimensional array in C is essentially an array of arrays. It represents data in a grid format (rows and columns), making it ideal for matrices, game boards, or tabular data.

### Declaration and Initialization

When declaring a 2D array, you must specify the size of both dimensions: `array[rows][columns]`.

```c
// A 3x4 grid (3 rows, 4 columns)
int grid[3][4] = {
    { 1,  2,  3,  4},  // Row 0
    { 5,  6,  7,  8},  // Row 1
    { 9, 10, 11, 12}   // Row 2
};
```
*Note: In memory, this grid is not actually a rectangle. It is flattened into a single contiguous block of 12 integers. The compiler uses the row/col sizes to calculate the correct memory offset under the hood.*

### Accessing Elements

You access elements using double brackets: `[row][column]`. Remember, C is 0-indexed.

```c
printf("%d", grid[0][0]); // Outputs 1 (Top left)
printf("%d", grid[1][2]); // Outputs 7 (Row 1, Column 2)

grid[2][3] = 99; // Modifies the bottom-right element (was 12)
```

### Iterating over 2D Arrays

To process every element in a 2D array, you use **nested loops**. The outer loop iterates over the rows, and the inner loop iterates over the columns of that specific row.

```c
#define ROWS 3
#define COLS 4

for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
        // Print the element, padded to 3 spaces for alignment
        printf("%3d ", grid[i][j]); 
    }
    printf("\\n"); // Newline after every row completes
}
```

### Passing 2D Arrays to Functions

When passing a 2D array to a function, you **must** specify the number of columns in the function parameter. This is because the compiler needs to know exactly how wide a row is in order to jump to the next row in memory.

```c
// The row size can be empty [], but the column size [4] is mandatory
void print_matrix(int matrix[][4], int rows) {
    // ...
}
```""",

    ("Arrays & Strings", "String Manipulation"): """## Parsing and Modifying Characters

In Python, manipulating strings is trivial (e.g., `text.upper().replace('a', 'b')`). In C, because strings are just raw character arrays, you have to build these functionalities yourself by iterating through the array and manipulating the underlying ASCII values.

### The Null Terminator Loop

The standard way to process a string manually is to loop through it until you hit the null terminator (`\\0`).

```c
char text[] = "Hello";
int i = 0;

// The loop continues as long as text[i] is not '\0' (which evaluates to 0/False)
while (text[i] != '\\0') {
    printf("%c", text[i]);
    i++;
}
```

### Manipulating via Pointers

Professional C programmers rarely use integer indexes (`i`) for strings. Instead, they use pointer arithmetic, which is slightly faster and more idiomatic.

```c
char text[] = "Hello";
char *ptr = text;

// *ptr dereferences the character. If it hits '\0', the loop stops.
while (*ptr) {
    printf("%c", *ptr);
    ptr++; // Move the pointer to the next character
}
```

### ASCII Math (Case Conversion)

Under the hood, characters are just integers mapped to the ASCII table. 
- `'A'` is `65`, `'B'` is `66`...
- `'a'` is `97`, `'b'` is `98`...

Notice that the difference between an uppercase and lowercase letter is exactly **32**. You can convert cases by simply doing math on the characters!

```c
void to_uppercase(char *str) {
    while (*str) {
        // If the character is between lowercase 'a' and 'z'
        if (*str >= 'a' && *str <= 'z') {
            *str = *str - 32; // Convert to uppercase
        }
        str++;
    }
}

int main() {
    char name[] = "mabel";
    to_uppercase(name);
    printf("%s", name); // Outputs: MABEL
}
```

### Reversing a String (In-Place)

To reverse a string without allocating new memory, you use a "two-pointer" approach. One index starts at the beginning, one at the end, and you swap the characters, moving inward until they meet in the middle. This is a fundamental algorithm interview question.""",

    ("Arrays & Strings", "Command Line Arguments"): """## Interacting with the Outside World

Up to this point, our `main` function has always looked like this: `int main()`. 

However, command-line applications (like `ls`, `grep`, or `git`) take arguments from the user when they are launched (e.g., `git commit -m "Fix bug"`). To receive these inputs in C, you must use the full signature of the main function:

```c
int main(int argc, char *argv[])
```

### Understanding `argc` and `argv`

1. **`argc` (Argument Count)**: An integer representing the total number of arguments passed to the program, **including the name of the program itself.**
2. **`argv` (Argument Vector)**: An array of strings (specifically, an array of character pointers). Each string is one argument separated by a space.

**Example execution:**
`./my_program -v file.txt`

In this case:
- `argc` = 3
- `argv[0]` = `"./my_program"`
- `argv[1]` = `"-v"`
- `argv[2]` = `"file.txt"`

### Parsing Arguments

A common pattern is looping through `argv` to configure the program based on user flags.

```c
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <filename> [--verbose]\\n", argv[0]);
        return 1; // Return error code
    }
    
    char *filename = argv[1];
    int verbose_mode = 0;
    
    // Check remaining arguments for flags
    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "--verbose") == 0) {
            verbose_mode = 1;
        }
    }
    
    if (verbose_mode) {
        printf("Verbose mode enabled.\\n");
    }
    printf("Processing file: %s\\n", filename);
    
    return 0;
}
```

### Converting Strings to Numbers

Command-line arguments are always passed as strings, even if the user types a number (e.g., `./calc 10 20`). 

To use these as integers, you must convert them using the `<stdlib.h>` functions like `atoi()` (ASCII to Integer) or `atof()` (ASCII to Float).

```c
#include <stdlib.h>

// If argv[1] is "42"
int value = atoi(argv[1]); // value is now the integer 42
```""",

    ("Dynamic Memory", "malloc and free"): """## Heap vs. Stack Memory

In C, memory is divided into two primary regions: the **Stack** and the **Heap**.

1. **The Stack**: Used for local variables inside functions (e.g., `int x = 5;`). Stack memory is fast, automatically managed, but strictly limited in size. Crucially, stack memory is destroyed the moment the function returns.
2. **The Heap**: A massive pool of memory used for dynamic allocation. Heap memory survives until you explicitly destroy it. You use the heap when you don't know how much memory you need until the program is running (e.g., loading a variable-sized file into memory).

### `malloc` (Memory Allocation)

To request memory from the heap, use `malloc()` from `<stdlib.h>`. You must tell it exactly how many bytes you need.

```c
#include <stdlib.h>

// Allocate memory for an array of 100 integers
// sizeof(int) ensures it works across different CPU architectures
int *arr = (int *)malloc(100 * sizeof(int));

if (arr == NULL) {
    // malloc returns NULL if the system is out of memory!
    printf("Memory allocation failed.\\n");
    return 1;
}

// You can use 'arr' exactly like a normal array
arr[0] = 42;
```

### `free` (Preventing Memory Leaks)

Unlike Python or Java, C has no Garbage Collector. If you `malloc` memory, it belongs to your program forever. If your program runs in a loop and keeps `malloc`ing without releasing the memory, the OS will eventually run out of RAM and kill your application. This is a **Memory Leak**.

To return memory to the OS, you must pass the pointer to `free()`.

```c
free(arr);
arr = NULL; // Best practice: prevent dangling pointers
```

### Other Allocation Functions

- **`calloc(count, size)`**: Similar to `malloc`, but it automatically zeros out (clears) the memory. `malloc` leaves garbage data in the memory blocks.
- **`realloc(pointer, new_size)`**: Resizes an existing heap block. If you allocated an array of 100 ints, but need 200, `realloc` will attempt to expand the block. If it can't, it finds a new block, copies the data over, and frees the old block.""",

    ("Structs & Unions", "Custom Data Types"): """## Grouping Data with `struct`

Arrays group elements of the *same* type. But what if you want to group a string (name), an int (age), and a float (salary) into a single logical unit? In object-oriented languages, you use a Class. In C, you use a **struct** (structure).

A `struct` creates a custom, composite data type. It does not contain functions (methods), only variables (members).

### Defining and Using a Struct

```c
// Define the blueprint (usually placed outside main)
struct Player {
    char name[50];
    int hp;
    float speed;
};

int main() {
    // Declare a variable of type 'struct Player'
    struct Player p1;
    
    // Access members using the dot (.) operator
    p1.hp = 100;
    p1.speed = 4.5;
    strcpy(p1.name, "Hero"); // Strings must be copied!
    
    printf("%s has %d HP.\\n", p1.name, p1.hp);
    return 0;
}
```

### `typedef` for Cleaner Code

Typing `struct Player` every time gets tedious. C allows you to alias the type using `typedef`, allowing you to use it just like a native type like `int`.

```c
typedef struct {
    int x;
    int y;
} Point;

int main() {
    Point p = {10, 20}; // Much cleaner!
}
```

### Structs and Pointers (The `->` Operator)

When you pass a large struct to a function, you should pass it by pointer to avoid copying a massive amount of memory. 

When accessing a struct's members *through a pointer*, you do not use the dot (`.`). You use the **arrow operator** (`->`).

```c
void take_damage(struct Player *p, int damage) {
    // Because p is a pointer, we must use ->
    p->hp = p->hp - damage;
    
    // (p->hp is syntactic sugar for (*p).hp)
}

int main() {
    struct Player p1 = {"Hero", 100, 4.5};
    take_damage(&p1, 25);
}
```

Structs combined with pointers to other structs form the basis of dynamic data structures like Linked Lists, Trees, and Graphs.""",

    ("File Handling", "Reading Files in C"): """## The File Pointer

To interact with files on the hard drive, C uses a special data type called a `FILE` pointer. Reading and writing files in C follows a strict lifecycle: Open → Process → Close.

### 1. Opening a File (`fopen`)

`fopen` takes a file path and a mode (e.g., `"r"` for read, `"w"` for write, `"a"` for append).

```c
FILE *file = fopen("data.txt", "r");

if (file == NULL) {
    printf("Failed to open file. Does it exist?\\n");
    return 1;
}
```

### 2. Reading from a File

There are three primary ways to read a file, depending on the data structure:

**A. Reading Character by Character (`fgetc`)**
```c
char c;
// Read until EOF (End Of File) is reached
while ((c = fgetc(file)) != EOF) {
    printf("%c", c);
}
```

**B. Reading Line by Line (`fgets`)**
Safest way to read text files. It reads until a newline or the buffer size is met.
```c
char buffer[256];
// Read up to 255 chars into buffer, stop at newline
while (fgets(buffer, sizeof(buffer), file) != NULL) {
    printf("%s", buffer);
}
```

**C. Reading Formatted Data (`fscanf`)**
Useful if the file has structured data (like CSV).
```c
int id;
char name[50];
// File format: 123 Alice
while (fscanf(file, "%d %s", &id, name) == 2) {
    printf("ID: %d, Name: %s\\n", id, name);
}
```

### 3. Closing a File (`fclose`)

Just like `malloc`, if you open a file, you have claimed a resource from the Operating System (a File Descriptor). If you do not close it, the OS may prevent other programs from accessing the file, and you may leak memory or lose data that wasn't flushed to the disk.

```c
fclose(file);
file = NULL; // Prevent dangling file pointer
```

**Writing to Files:**
If you open a file in `"w"` mode, you can write to it using `fprintf`, which works exactly like `printf` but takes the file pointer as its first argument:
`fprintf(file, "Score: %d\\n", score);`""",

    ("Data Structures in C", "Linked Lists"): """## Beyond Contiguous Memory

An array requires a single, continuous block of memory. If you want an array of 1,000,000 integers, you need 4MB of *uninterrupted* RAM. Furthermore, resizing arrays requires copying all the data to a new block.

A **Linked List** solves this by scattering data across the heap. Each piece of data is stored in a "Node". A Node is a struct that contains two things:
1. The actual data.
2. A pointer to the next Node in memory.

### Defining a Node

```c
typedef struct Node {
    int data;
    struct Node *next; // Pointer to the same struct type
} Node;
```

### Traversing a Linked List

Because the nodes are scattered, you cannot use an index like `list[3]`. You must start at the very first node (the `head`) and follow the pointers one by one until you reach a node whose `next` pointer is `NULL` (the end of the list).

```c
void print_list(Node *head) {
    Node *current = head; // Start at the beginning
    
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next; // Move to the next node
    }
    printf("NULL\\n");
}
```

### The Cost of Flexibility

**Advantages of Linked Lists:**
- **O(1) Insertions**: Inserting a new node at the beginning of the list is instant. You just create the node and point it at the old head. You don't have to shift a million elements down like you do in an array.
- **Dynamic Size**: The list can grow indefinitely until the computer literally runs out of RAM.

**Disadvantages:**
- **O(N) Search**: To find the 100th element, you must visit the first 99 elements. There is no random access.
- **Memory Overhead**: Every piece of data now requires an extra 8 bytes to store the pointer to the next node.

Linked lists form the structural foundation for more complex data structures like Stacks, Queues, Hash Table collision chains, and Binary Trees.""",

    ("Bit Manipulation", "Bitwise Operators"): """## Talking to the Machine

At the lowest level, all computer data is just binary—a series of 1s and 0s (bits). Usually, programmers work with bytes (8 bits) or integers (32 bits). But sometimes—particularly in embedded systems, cryptography, or writing network protocols—you need to manipulate individual bits.

C provides **Bitwise Operators** that manipulate data at the bit level.

### The Core Operators

Assume `A = 5` (Binary: `0101`) and `B = 3` (Binary: `0011`).

**1. AND (`&`)**: 1 if BOTH bits are 1.
- `0101 & 0011` = `0001` (Decimal 1)
- *Use: "Masking" (turning off specific bits).*

**2. OR (`|`)**: 1 if EITHER bit is 1.
- `0101 | 0011` = `0111` (Decimal 7)
- *Use: Turning on specific bits.*

**3. XOR (`^`)**: 1 if bits are DIFFERENT.
- `0101 ^ 0011` = `0110` (Decimal 6)
- *Use: Flipping bits, cryptography.*

**4. NOT (`~`)**: Flips all bits.
- `~0101` = `1010`

### Bit Shifting

Bit shifting literally slides the binary digits left or right.

**Left Shift (`<<`)**: Shifts bits to the left, adding 0s on the right. 
Mathematically, shifting left by 1 is the same as **multiplying by 2**, but it executes significantly faster in the CPU hardware than standard multiplication.
- `5` (`00000101`) `<< 1` = `10` (`00001010`)
- `5 << 2` = `20` (Multiplied by 4)

**Right Shift (`>>`)**: Shifts bits to the right. Mathematically equivalent to **integer division by 2**.
- `20` (`00010100`) `>> 1` = `10` (`00001010`)

### Practical Use: Bit Flags

Instead of having 8 boolean variables (taking 8 bytes of memory), you can store 8 true/false states in a single 1-byte `char` using bits.

```c
#define FLAG_A (1 << 0) // 00000001
#define FLAG_B (1 << 1) // 00000010
#define FLAG_C (1 << 2) // 00000100

unsigned char status = 0;

status |= FLAG_B; // Turn ON Flag B (OR)
status &= ~FLAG_B; // Turn OFF Flag B (AND NOT)

// Check if Flag B is ON
if (status & FLAG_B) {
    // ...
}
```""",

    ("System Calls", "Talking to the OS"): """## The OS Boundary: User Mode vs Kernel Mode

When you write a C program, it runs in **User Mode**. This is an unprivileged state. Your program is strictly confined to a sandbox: it is not allowed to read the keyboard, write to the hard drive, or send packets over the network. If User Mode programs could do this, a malicious script could easily format your hard drive or read passwords belonging to other applications.

The **Operating System Kernel** (Linux, Windows, macOS) runs in **Kernel Mode**, with total god-like control over the hardware.

### What is a System Call?

If your User Mode program wants to open a file on the hard drive, it must politely ask the Kernel to do it on its behalf. It does this via a **System Call** (syscall).

When you write `printf("Hello");` in C, the standard library formats the string, and then it invokes the `write()` system call.

**The Workflow:**
1. The User program puts the arguments (e.g., the string "Hello") into specific CPU registers.
2. The program triggers a software interrupt (a "trap").
3. The CPU immediately halts the User program and switches hardware privileges to Kernel Mode.
4. The Kernel executes the `write()` function, commanding the hardware to display pixels on the screen.
5. The Kernel switches the hardware back to User Mode and hands control back to your program.

### The Cost of Syscalls (Context Switching)

Switching between User Mode and Kernel Mode is computationally expensive. It takes thousands of CPU cycles. 

This is why **Buffering** is crucial in software engineering.

If you want to write 1,000 characters to a file:
- **Bad Way**: Call the `write()` syscall 1,000 times, once for each character. This causes 1,000 slow context switches.
- **Good Way (How C does it)**: Store the characters in a memory array (a buffer). When the buffer is full (e.g., 4096 bytes), make exactly ONE syscall to write the entire block of data to the disk at once. 

Understanding system calls bridges the gap between C programming and Operating Systems architecture.""",

    ("Operators & Expressions", "Arithmetic & Modulo"): """## Math in C

C supports standard arithmetic operators (`+`, `-`, `*`, `/`). The modulo operator (`%`) gives the remainder of integer division.

It is important to remember that C does integer division when both operands are integers. For example, `10 / 3` is `3`, not `3.33`.

The modulo operator `%` only works with integers. `10 % 3` returns `1`. It's very useful for checking divisibility or keeping numbers within a certain range.""",

    ("Operators & Expressions", "Increment & Decrement"): """## Shortcuts

The `++` and `--` operators add or subtract 1 from a variable. 

Be careful with prefix (`++x`) vs postfix (`x++`) notation.
- `++x` (Prefix) increments the value, and *then* returns the new value to the expression.
- `x++` (Postfix) returns the current value to the expression, and *then* increments the variable.

```c
int a = 5;
int b = a++; // b gets 5, then a becomes 6
int c = ++a; // a becomes 7, then c gets 7
```""",

    ("Strings in C", "Null-Terminated Arrays"): """## Character Arrays

In C, there is no `String` type. A string is just an array of characters ending with a null terminator (`'\\0'`).

This means the string `"Hello"` actually requires an array of 6 characters: `['H', 'e', 'l', 'l', 'o', '\\0']`.

When C functions print or copy a string, they simply process characters one by one until they hit that `\\0`. If you forget the null terminator, C will keep reading memory into adjacent variables until it crashes.""",

    ("Strings in C", "String Functions"): """## string.h

The `<string.h>` library provides functions to manipulate strings, such as `strlen` for length and `strcpy` for copying.

Because strings are arrays, you cannot reassign them directly like `string1 = string2`. You must use `strcpy(string1, string2)` to copy the contents of memory.

Similarly, you cannot compare strings with `==`, as that only compares their memory addresses. You must use `strcmp(string1, string2)`.

*Note: This is the second iteration of string fundamentals, cementing the use of standard library functions.*""",

    ("Function Pointers", "Pointers to Code"): """## Storing Functions

Just as pointers can store the address of a variable, they can store the address of a function, allowing you to pass functions as arguments (callbacks).

In memory, compiled code lives in a read-only segment. A function's name acts as a pointer to the start of its machine code in that segment.

### The Syntax

Declaring a function pointer looks intimidating because you have to specify the return type and parameter types of the function it will point to.

```c
// Declares a pointer named 'operation' 
// It points to any function that takes (int, int) and returns an int
int (*operation)(int, int);
```
The parentheses around `(*operation)` are mandatory, otherwise the compiler thinks you are declaring a function that returns an `int *`.""",

    ("Function Pointers", "Using Callbacks"): """## Dynamic Execution

You can assign a function address to a pointer and then call it.

```c
int add(int a, int b) { return a + b; }
int multiply(int a, int b) { return a * b; }

int main() {
    int (*operation)(int, int);
    
    // Point to the add function
    operation = add; 
    printf("%d\\n", operation(5, 3)); // Outputs 8
    
    // Change the pointer at runtime!
    operation = multiply;
    printf("%d\\n", operation(5, 3)); // Outputs 15
}
```

This is the foundation of "Callbacks" in C (like passing a custom comparison function to `qsort`) and the basis for implementing Object-Oriented Polymorphism in C using structures of function pointers.""",

    ("Socket Programming", "Creating a Socket"): """## The Network Endpoint

In Linux, a socket is just a file descriptor. You create one using the `socket()` system call.

To communicate over the internet, you typically create an IPv4 TCP socket.
- `AF_INET`: Specifies the IPv4 address family.
- `SOCK_STREAM`: Specifies TCP (a reliable, connection-oriented stream). `SOCK_DGRAM` would specify UDP.

```c
#include <sys/socket.h>

// Returns a file descriptor (an integer). -1 on error.
int server_fd = socket(AF_INET, SOCK_STREAM, 0);
```
Once created, this socket is just an empty endpoint. It is not connected to anything and doesn't have a port assigned to it yet.""",

    ("Socket Programming", "Bind and Listen"): """## Waiting for Connections

After creating a socket, a server must `bind()` it to a specific network interface and port on the machine (e.g., Port 8080).

After binding, the socket is still not ready to accept traffic. You must call `listen()`, which tells the OS, "Make this an active listening socket that accepts incoming connections."

```c
// The '3' is the backlog: the maximum number of pending 
// connections the OS will queue up before rejecting new ones.
listen(server_fd, 3);
```

After `listen()`, the server typically enters an infinite `while` loop calling `accept()`, which blocks the thread until a client actually connects.""",

    ("Multi-threading & Concurrency Masterclass", "POSIX Threads (pthreads)"): """## True Concurrency

Unlike async/await in high-level languages (which usually multiplexes tasks on a single thread), POSIX threads (pthreads) in C provide true OS-level concurrency. 

When you spawn a pthread, the Operating System creates a new execution context that can run simultaneously on a completely different CPU core.

### The `<pthread.h>` Library

To use threading in C on UNIX/Linux systems, you include `<pthread.h>`.

To create a thread, you use `pthread_create()`. It requires four arguments:
1. A pointer to a thread identifier (`pthread_t`).
2. Thread attributes (usually `NULL` for default).
3. A function pointer to the code the thread will execute (must return `void *` and take `void *`).
4. An argument to pass to that function (or `NULL`).

```c
#include <pthread.h>
#include <stdio.h>

void* print_hello(void* arg) {
    printf("Hello from thread!\\n");
    return NULL;
}

int main() {
    pthread_t my_thread;
    pthread_create(&my_thread, NULL, print_hello, NULL);
    // Main thread continues while my_thread runs concurrently
}
```""",

    ("Multi-threading & Concurrency Masterclass", "Thread Joining and Detaching"): """## Waiting for Completion

When a C program starts, the `main()` function is executed by the "main thread". 

If the main thread finishes and `main()` returns 0, the Operating System terminates the entire process immediately, **killing all other threads** instantly, even if they were in the middle of important work.

### Joining Threads

To prevent this, the main thread must wait for its worker threads to finish. You do this with `pthread_join()`. It acts as a roadblock; the calling thread will sleep until the specified thread completes.

```c
pthread_t worker;
pthread_create(&worker, NULL, do_work, NULL);

// Main thread pauses here until 'worker' finishes.
pthread_join(worker, NULL); 
printf("Worker is done, program can safely exit.\\n");
```

### Detaching Threads

Sometimes you spawn a "background task" (like a logging thread) and you don't care when it finishes, nor do you want to wait for it. You can call `pthread_detach(worker)`. This tells the OS, "Let this thread run independently, and automatically clean up its resources when it finishes." A detached thread cannot be joined.""",

    ("Multi-threading & Concurrency Masterclass", "Race Conditions"): """## Shared Memory Chaos

Threads share the same memory space. If Thread A and Thread B both have pointers to the same global variable, they can both read and write to it.

A **Race Condition** occurs when multiple threads attempt to read, modify, and write to the same memory location simultaneously. 

### The `counter++` Illusion

Consider a global `int counter = 0;`. Thread A and Thread B both execute `counter++;`. You expect the counter to be 2.

But `counter++` is not a single atomic operation. At the hardware level, it is three steps:
1. **READ**: Load counter from RAM into CPU register.
2. **MODIFY**: Add 1 to the register.
3. **WRITE**: Save register back to RAM.

**The Race (Interleaving):**
- Thread A reads `0` into its register.
- *OS Context Switch! Thread A pauses.*
- Thread B reads `0` into its register.
- Thread B adds 1, writes `1` to RAM.
- *OS Context Switch! Thread A resumes.*
- Thread A adds 1 to its register (which was 0), writes `1` to RAM.

Both threads completed `counter++`, but the final value in RAM is `1`, not `2`. Data is corrupted. The solution is **Mutual Exclusion** (ensuring only one thread can execute those three steps at a time).""",

    ("Multi-threading & Concurrency Masterclass", "Mutexes"): """## The Lock

To prevent race conditions, we use a **Mutex** (Mutual Exclusion object). Think of a mutex as a physical key to a bathroom. Only the person holding the key can enter the room.

### Locking and Unlocking

A `pthread_mutex_t` is the lock. 
Before a thread accesses a shared variable (the "Critical Section"), it calls `pthread_mutex_lock(&lock)`. 
- If the lock is available, the thread takes it and proceeds.
- If another thread already has the lock, the calling thread is put to sleep by the OS until the lock is released.

Once the thread finishes modifying the variable, it MUST call `pthread_mutex_unlock(&lock)`.

```c
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
int shared_counter = 0;

void* worker(void* arg) {
    // Acquire the lock
    pthread_mutex_lock(&lock);
    
    // CRITICAL SECTION: Safe to modify
    shared_counter++; 
    
    // Release the lock so other threads can proceed
    pthread_mutex_unlock(&lock);
    
    return NULL;
}
```

If you lock a mutex but forget to unlock it (or if the thread crashes while holding the lock), any other thread waiting for that lock will sleep forever. This is a fatal bug.""",

    ("Multi-threading & Concurrency Masterclass", "Condition Variables"): """## Waiting for State

Mutexes protect data. But what if a thread needs to wait for a specific *condition* to become true? 

Example: A consumer thread wants to read data from a queue, but the queue is empty.
It could use a `while` loop to constantly lock the mutex, check the queue, unlock, and repeat. This is called "Busy Waiting" and it consumes 100% of the CPU doing absolutely nothing.

### `pthread_cond_t`

A **Condition Variable** solves this. It allows a thread to safely go to sleep until another thread signals that the condition has changed.

**The Consumer (Waiting):**
```c
pthread_mutex_lock(&lock);
while (queue_is_empty) {
    // Atomically releases the lock and puts thread to sleep!
    // When woken up, it re-acquires the lock automatically.
    pthread_cond_wait(&cond, &lock);
}
// Read from queue...
pthread_mutex_unlock(&lock);
```

**The Producer (Signaling):**
```c
pthread_mutex_lock(&lock);
// Add item to queue...
queue_is_empty = 0;

// Wake up at least one sleeping consumer thread!
pthread_cond_signal(&cond); 
// Or pthread_cond_broadcast() to wake ALL sleeping threads

pthread_mutex_unlock(&lock);
```
Condition variables are the backbone of the Producer/Consumer design pattern.""",

    ("Multi-threading & Concurrency Masterclass", "Semaphores"): """## Counting Resources

A Mutex is binary: Locked (0) or Unlocked (1). It allows exactly ONE thread in.

A **Semaphore** (`sem_t`) is a generalized lock that maintains an internal counter. It allows exactly N threads in. Think of it like a parking garage with 50 spots. A semaphore initialized to 50 will let 50 cars in before the barrier closes; any subsequent cars must wait in line until someone leaves.

### Semaphores in POSIX (`<semaphore.h>`)

- **`sem_wait(&sem)` (Decrement / P-operation)**: 
  Checks the counter. If > 0, decrements the counter and proceeds. If == 0, the thread is put to sleep until the counter is > 0.
  
- **`sem_post(&sem)` (Increment / V-operation)**:
  Increments the counter. If threads are sleeping waiting for the semaphore, one is woken up.

**Classic Use Case: Bounded Buffer**
If you have a queue that can only hold 10 items, you initialize an `empty_slots` semaphore to 10.
When a producer wants to add an item, it calls `sem_wait(&empty_slots)`. 
When the 11th producer arrives, the counter is 0, so it sleeps, preventing a buffer overflow.""",

    ("Multi-threading & Concurrency Masterclass", "Deadlocks"): """## The Deadly Embrace

A **Deadlock** occurs when two or more threads are permanently blocked, waiting on each other to release resources. The system grinds to a halt and must be manually restarted.

### How it Happens (Coffman Conditions)

Imagine Thread A and Thread B both need Mutex 1 and Mutex 2 to proceed.
1. Thread A locks Mutex 1.
2. *Context switch.*
3. Thread B locks Mutex 2.
4. *Context switch.*
5. Thread A tries to lock Mutex 2. It's held by B, so A sleeps.
6. Thread B tries to lock Mutex 1. It's held by A, so B sleeps.

Both threads will wait for eternity.

### Preventing Deadlocks

The most robust and common strategy for preventing deadlocks in a complex system is **Strict Lock Ordering**.

If the system design mandates that *every* thread in the program must ALWAYS acquire Mutex 1 before attempting to acquire Mutex 2, the deadlock scenario becomes impossible. Thread B would never be allowed to grab Mutex 2 because it wouldn't have Mutex 1 yet. 

Other prevention strategies include:
- Avoid holding locks during slow I/O operations.
- Use `pthread_mutex_trylock()`, which returns an error instead of sleeping if the lock is held, allowing the thread to back off, release its current locks, and try again later.""",

    ("Multi-threading & Concurrency Masterclass", "Atomic Operations"): """## Lock-Free Concurrency

Mutexes are safe, but they are incredibly slow. Putting a thread to sleep and waking it up via the OS kernel takes thousands of CPU cycles. 

If all you need to do is increment a shared counter or flip a boolean flag, a Mutex is extreme overkill.

### Hardware-Level Atomicity

Modern CPUs provide specialized machine instructions (like Compare-And-Swap) that can read, modify, and write a variable in a single, uninterruptible hardware cycle. This is an **Atomic Operation**.

Because it happens at the hardware level, no OS context switching is required, making atomic operations vastly faster than mutexes.

### C11 Atomics (`<stdatomic.h>`)

Modern C (C11) provides built-in support for atomic types. If you declare a variable as `_Atomic`, the compiler guarantees that any operations on it are thread-safe without needing a mutex.

```c
#include <stdatomic.h>
#include <pthread.h>

// This integer is hardware-protected from race conditions
_Atomic int shared_counter = 0;

void* worker(void* arg) {
    for (int i = 0; i < 100000; i++) {
        // Safe concurrent increment! No mutex needed.
        shared_counter++; 
    }
    return NULL;
}
```
Atomics are the foundation for building high-performance, lock-free data structures used in modern real-time systems and game engines."""
}

patched = 0
for category_name, category_data in data.items():
    for lesson in category_data.get("lessons", []):
        title = lesson["title"]
        key = (category_name, title)
        if key in theories and theories[key] is not None:
            old_len = len(lesson.get("theory", ""))
            lesson["theory"] = theories[key]
            new_len = len(lesson["theory"])
            print(f"  OK [{category_name}] {title}: {old_len} -> {new_len} chars")
            patched += 1

with open("curriculum/tracks/c_programming.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nPatched {patched} lessons in c_programming.json")
