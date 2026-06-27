"""
Batch 37: Expanding Systems Programming Curriculum (C++, Multithreading, Syscalls, Embedded, Kernel)
"""
import json, os

NEW_COURSES_BATCH37 = {
    "C++ Fundamentals": {
        "tier": "Beginner",
        "aiRubric": "Assess C++ fundamentals",
        "lessons": [
            {"title": "Pointers and References", "theory": "## Memory Access\\nIn C++, pointers hold the memory address of a variable, while references act as an alias to an existing variable. Both are crucial for systems programming.", "instructions": "## Task: Pass by Reference\\nWrite a function signature that takes an integer reference so the function can modify the original variable.", "starterCode": "void increment(int___ value) {\\n    value++;\\n}", "solution": "void increment(int& value) {\\n    value++;\\n}", "hint": "Use the & operator.", "rubric": "Correctly uses the reference operator &."},
            {"title": "RAII Paradigm", "theory": "## Resource Acquisition Is Initialization\\nRAII is a C++ programming technique which binds the life cycle of a resource that must be acquired before use to the lifetime of an object.", "instructions": "## Task: Destructor Cleanup\\nImplement a destructor for a `FileHandler` class that prints 'Closing file'.", "starterCode": "class FileHandler {\\npublic:\\n    FileHandler() { cout << \"Opening file\"; }\\n    ___FileHandler() { cout << \"___\"; }\\n};", "solution": "class FileHandler {\\npublic:\\n    FileHandler() { cout << \"Opening file\"; }\\n    ~FileHandler() { cout << \"Closing file\"; }\\n};", "hint": "Use ~ for destructor and print 'Closing file'", "rubric": "Correctly defines the destructor using ~ and prints the required string."}
        ]
    },
    "Multithreading & Mutexes": {
        "tier": "Intermediate",
        "aiRubric": "Assess multithreading concepts",
        "lessons": [
            {"title": "Spawning Threads", "theory": "## Concurrent Execution\\nSystems programming often requires doing multiple things at once. In C++ or Rust, you can spawn threads to execute functions concurrently.", "instructions": "## Task: C++ std::thread\\nCreate a thread that runs the `workerFunction`.", "starterCode": "#include <thread>\\n\\nvoid workerFunction() { }\\n\\nint main() {\\n    std::___ t(___);\\n    t.join();\\n    return 0;\\n}", "solution": "#include <thread>\\n\\nvoid workerFunction() { }\\n\\nint main() {\\n    std::thread t(workerFunction);\\n    t.join();\\n    return 0;\\n}", "hint": "Use thread and workerFunction", "rubric": "Correctly instantiates a std::thread with the function."},
            {"title": "Data Races and Mutexes", "theory": "## Protecting Shared Data\\nWhen multiple threads access the same memory concurrently and at least one is writing, a data race occurs. Mutexes (Mutual Exclusion) prevent this.", "instructions": "## Task: Lock Guard\\nUse `std::lock_guard` to safely lock the mutex inside the critical section.", "starterCode": "#include <mutex>\\nstd::mutex mtx;\\nint counter = 0;\\n\\nvoid increment() {\\n    std::___<std::mutex> lock(___);\\n    counter++;\\n}", "solution": "#include <mutex>\\nstd::mutex mtx;\\nint counter = 0;\\n\\nvoid increment() {\\n    std::lock_guard<std::mutex> lock(mtx);\\n    counter++;\\n}", "hint": "Use lock_guard and mtx", "rubric": "Correctly applies std::lock_guard to the mutex."}
        ]
    },
    "System Calls in C": {
        "tier": "Intermediate",
        "aiRubric": "Assess POSIX syscalls",
        "lessons": [
            {"title": "The open() Syscall", "theory": "## Interacting with the Kernel\\nSystem calls are how a program requests a service from the operating system's kernel. The `open()` syscall opens a file descriptor.", "instructions": "## Task: Open for Writing\\nUse the `open()` syscall to open a file 'log.txt' for writing only, creating it if it doesn't exist.", "starterCode": "#include <fcntl.h>\\n\\nint main() {\\n    int fd = open(\"log.txt\", ___ | ___);\\n    return 0;\\n}", "solution": "#include <fcntl.h>\\n\\nint main() {\\n    int fd = open(\"log.txt\", O_WRONLY | O_CREAT);\\n    return 0;\\n}", "hint": "Use O_WRONLY and O_CREAT", "rubric": "Correctly uses the O_WRONLY and O_CREAT flags."},
            {"title": "Forking Processes", "theory": "## Process Creation\\nThe `fork()` system call creates a new process by duplicating the calling process. The new process is called the child process.", "instructions": "## Task: Detect Child Process\\nWrite the standard check to determine if the current executing code is the child process.", "starterCode": "#include <unistd.h>\\n\\nint main() {\\n    pid_t pid = fork();\\n    if (pid ___ ___) {\\n        // I am the child process\\n    }\\n    return 0;\\n}", "solution": "#include <unistd.h>\\n\\nint main() {\\n    pid_t pid = fork();\\n    if (pid == 0) {\\n        // I am the child process\\n    }\\n    return 0;\\n}", "hint": "Check if pid == 0", "rubric": "Correctly checks if pid equals 0."}
        ]
    },
    "Embedded Systems Basics": {
        "tier": "Advanced",
        "aiRubric": "Assess embedded systems knowledge",
        "lessons": [
            {"title": "Bitwise Operations", "theory": "## Manipulating Registers\\nIn embedded systems, you often need to manipulate individual bits in hardware registers using bitwise operators like AND (&), OR (|), and XOR (^).", "instructions": "## Task: Set a Bit\\nWrite the bitwise operation to set the 3rd bit of an 8-bit register (assuming 0-indexed) without changing other bits.", "starterCode": "unsigned char reg = 0x00;\\n// Set the 3rd bit (bit mask 0x08 or 1 << 3)\\nreg = reg ___ (1 ___ 3);", "solution": "unsigned char reg = 0x00;\\n// Set the 3rd bit (bit mask 0x08 or 1 << 3)\\nreg = reg | (1 << 3);", "hint": "Use | and <<", "rubric": "Correctly uses bitwise OR and left shift to set the bit."},
            {"title": "Volatile Keyword", "theory": "## Memory Mapped I/O\\nThe `volatile` keyword tells the compiler not to optimize read/write operations for a variable because its value may change outside the program's control (e.g. by hardware).", "instructions": "## Task: Volatile Pointer\\nDeclare a pointer to an integer memory address (0x4000) that should not be optimized.", "starterCode": "___ int *hardware_register = (___ int *)0x4000;", "solution": "volatile int *hardware_register = (volatile int *)0x4000;", "hint": "Use the volatile keyword", "rubric": "Correctly uses the volatile keyword for the pointer."}
        ]
    },
    "Writing Kernel Modules": {
        "tier": "Advanced",
        "aiRubric": "Assess kernel module basics",
        "lessons": [
            {"title": "Module Initialization", "theory": "## Loading Code into the Kernel\\nLinux kernel modules allow you to extend the kernel's capabilities dynamically. Every module needs an initialization function.", "instructions": "## Task: module_init\\nRegister the `hello_init` function as the initialization entry point for the module.", "starterCode": "#include <linux/module.h>\\n\\nstatic int __init hello_init(void) {\\n    return 0;\\n}\\n\\n___(hello_init);", "solution": "#include <linux/module.h>\\n\\nstatic int __init hello_init(void) {\\n    return 0;\\n}\\n\\nmodule_init(hello_init);", "hint": "Use the module_init macro", "rubric": "Correctly invokes the module_init macro."},
            {"title": "Printing to Kernel Log", "theory": "## printk\\nYou cannot use `printf` inside the Linux kernel because the standard C library is not available. Instead, you use `printk`.", "instructions": "## Task: Kernel Info Log\\nUse `printk` to log an informational message (KERN_INFO).", "starterCode": "#include <linux/kernel.h>\\n\\nvoid log_msg(void) {\\n    ___(___ \"Module loaded successfully\\n\");\\n}", "solution": "#include <linux/kernel.h>\\n\\nvoid log_msg(void) {\\n    printk(KERN_INFO \"Module loaded successfully\\n\");\\n}", "hint": "Use printk and KERN_INFO", "rubric": "Correctly uses printk and the KERN_INFO log level."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'systems_programming.json')
    
    # 1. Update systems_programming.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH37.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH37.items():
            tier = course_info["tier"]
            if "Systems Programming" in index_data and tier in index_data["Systems Programming"]:
                if new_course_name not in index_data["Systems Programming"][tier]:
                    index_data["Systems Programming"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 37: Added {total} lessons to Systems Programming track')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
