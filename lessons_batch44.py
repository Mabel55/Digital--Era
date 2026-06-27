"""
Batch 44: Expanding C Programming Curriculum (Operators, Strings, Function Pointers, Bit Manipulation, Sockets)
"""
import json, os

NEW_COURSES_BATCH44 = {
    "Operators & Expressions": {
        "tier": "Beginner",
        "aiRubric": "Assess basic C operators",
        "lessons": [
            {"title": "Arithmetic & Modulo", "theory": "## Math in C\\nC supports standard arithmetic operators (`+`, `-`, `*`, `/`). The modulo operator (`%`) gives the remainder of integer division.", "instructions": "## Task: Calculate Remainder\\nUse the modulo operator to find the remainder when 10 is divided by 3.", "starterCode": "#include <stdio.h>\\n\\nint main() {\\n    int remainder = 10 ___ 3;\\n    printf(\"%d\", remainder);\\n    return 0;\\n}", "solution": "#include <stdio.h>\\n\\nint main() {\\n    int remainder = 10 % 3;\\n    printf(\"%d\", remainder);\\n    return 0;\\n}", "hint": "Use the % operator", "rubric": "Correctly uses the % operator."},
            {"title": "Increment & Decrement", "theory": "## Shortcuts\\nThe `++` and `--` operators add or subtract 1 from a variable. Be careful with prefix (`++x`) vs postfix (`x++`) notation.", "instructions": "## Task: Postfix Increment\\nIncrement the variable `count` by 1 using the postfix operator.", "starterCode": "int count = 5;\\n___;", "solution": "int count = 5;\\ncount++;", "hint": "Use count++", "rubric": "Uses count++."}
        ]
    },
    "Strings in C": {
        "tier": "Intermediate",
        "aiRubric": "Assess C string manipulation",
        "lessons": [
            {"title": "Null-Terminated Arrays", "theory": "## Character Arrays\\nIn C, there is no `String` type. A string is just an array of characters ending with a null terminator (`'\\0'`).", "instructions": "## Task: Define a String\\nDefine a character array that stores the string \"Hello\" (remember the implicit null terminator).", "starterCode": "char greeting[] = \"___\";", "solution": "char greeting[] = \"Hello\";", "hint": "Hello", "rubric": "Assigns \"Hello\" to greeting."},
            {"title": "String Functions", "theory": "## string.h\\nThe `<string.h>` library provides functions to manipulate strings, such as `strlen` for length and `strcpy` for copying.", "instructions": "## Task: String Length\\nUse the standard library function to find the length of the string.", "starterCode": "#include <string.h>\\n\\nint len = ___(greeting);", "solution": "#include <string.h>\\n\\nint len = strlen(greeting);", "hint": "Use strlen", "rubric": "Uses strlen()."}
        ]
    },
    "Function Pointers": {
        "tier": "Intermediate",
        "aiRubric": "Assess function pointers",
        "lessons": [
            {"title": "Pointers to Code", "theory": "## Storing Functions\\nJust as pointers can store the address of a variable, they can store the address of a function, allowing you to pass functions as arguments (callbacks).", "instructions": "## Task: Declare Function Pointer\\nDeclare a function pointer named `operation` that takes two `int` parameters and returns an `int`.", "starterCode": "int (___operation)(int, int);", "solution": "int (*operation)(int, int);", "hint": "Use an asterisk inside the parentheses (*operation)", "rubric": "Correctly declares (*operation)."},
            {"title": "Using Callbacks", "theory": "## Dynamic Execution\\nYou can assign a function address to a pointer and then call it.", "instructions": "## Task: Assign and Call\\nAssign the `add` function to the pointer and call it.", "starterCode": "operation = ___;\\nint result = operation(5, 3);", "solution": "operation = add;\\nint result = operation(5, 3);", "hint": "Just use the name of the function: add", "rubric": "Assigns add without parentheses."}
        ]
    },
    "Bit Manipulation": {
        "tier": "Advanced",
        "aiRubric": "Assess bitwise operations",
        "lessons": [
            {"title": "Bitwise AND, OR, XOR", "theory": "## Twiddling Bits\\nBitwise operators (`&`, `|`, `^`, `~`) operate on numbers at the binary level. They are extremely fast and commonly used in embedded systems.", "instructions": "## Task: Bitwise OR\\nUse the Bitwise OR operator to combine flags `A` and `B`.", "starterCode": "int FLAG_A = 1; // 0001\\nint FLAG_B = 2; // 0010\\nint combined = FLAG_A ___ FLAG_B;", "solution": "int FLAG_A = 1; // 0001\\nint FLAG_B = 2; // 0010\\nint combined = FLAG_A | FLAG_B;", "hint": "Use the | operator", "rubric": "Uses |."},
            {"title": "Bit Shifting", "theory": "## Fast Multiplication\\nShifting bits left (`<<`) effectively multiplies by 2, and shifting right (`>>`) divides by 2.", "instructions": "## Task: Multiply by 4\\nUse the left shift operator to multiply the value by 4 (which is 2 to the power of 2).", "starterCode": "int value = 5;\\nint result = value ___ 2;", "solution": "int value = 5;\\nint result = value << 2;", "hint": "Use <<", "rubric": "Uses << 2."}
        ]
    },
    "Socket Programming": {
        "tier": "Advanced",
        "aiRubric": "Assess basic network sockets in C",
        "lessons": [
            {"title": "Creating a Socket", "theory": "## The Network Endpoint\\nIn Linux, a socket is just a file descriptor. You create one using the `socket()` system call, specifying the domain (IPv4) and type (TCP).", "instructions": "## Task: socket() Call\\nCreate a TCP socket using `AF_INET` and `SOCK_STREAM`.", "starterCode": "#include <sys/socket.h>\\n\\nint server_fd = socket(AF_INET, ___, 0);", "solution": "#include <sys/socket.h>\\n\\nint server_fd = socket(AF_INET, SOCK_STREAM, 0);", "hint": "Use SOCK_STREAM", "rubric": "Correctly uses SOCK_STREAM."},
            {"title": "Bind and Listen", "theory": "## Waiting for Connections\\nAfter creating a socket, a server must `bind()` it to a port and then `listen()` for incoming client connections.", "instructions": "## Task: Listen Call\\nWrite the function call to make the socket listen, allowing a backlog of 3 connections.", "starterCode": "___(server_fd, 3);", "solution": "listen(server_fd, 3);", "hint": "Use listen", "rubric": "Calls listen(server_fd, 3)."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'c_programming.json')
    
    # 1. Update c_programming.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH44.items():
            if new_course_name not in track_data:
                track_data[new_course_name] = {
                    "aiRubric": course_info["aiRubric"],
                    "lessons": course_info["lessons"]
                }
                updated = True
                total += len(course_info["lessons"])
                
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(track_data, f, indent=2, ensure_ascii=False)
                
    # 2. Update index.json
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH44.items():
            tier = course_info["tier"]
            if "C Programming" in index_data and tier in index_data["C Programming"]:
                if new_course_name not in index_data["C Programming"][tier]:
                    index_data["C Programming"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 44: Added {total} lessons to C Programming track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
