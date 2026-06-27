"""
Batch 63: Deep Dive into C Programming (Multi-threading & Concurrency Masterclass)
"""
import json, os

NEW_COURSES_BATCH63 = {
    "Multi-threading & Concurrency Masterclass": {
        "tier": "Advanced",
        "aiRubric": "Assess deep understanding of POSIX threads and concurrency in C",
        "lessons": [
            {"title": "POSIX Threads (pthreads)", "theory": "## True Concurrency\\nUnlike async/await in high-level languages, POSIX threads (pthreads) in C provide true OS-level concurrency. You spawn a new thread by calling `pthread_create()` and passing it a function pointer.", "instructions": "## Task: The Header\\nTo use the pthreads library in C, you must include a specific header file.", "starterCode": "#include <___>", "solution": "#include <pthread.h>", "hint": "Include pthread.h", "rubric": "Uses <pthread.h>."},
            {"title": "Thread Joining and Detaching", "theory": "## Waiting for Completion\\nIf your `main()` function returns before your threads finish, the OS will kill all running threads. You must use `pthread_join()` to block the main thread until the specified thread completes. Alternatively, `pthread_detach()` lets a thread run independently.", "instructions": "## Task: Join the Thread\\nBlock the current thread until `thread1` finishes execution.", "starterCode": "___(thread1, NULL);", "solution": "pthread_join(thread1, NULL);", "hint": "Use pthread_join", "rubric": "Uses pthread_join."},
            {"title": "Race Conditions", "theory": "## Shared Memory Chaos\\nA race condition occurs when multiple threads read and write to the same shared memory location simultaneously. The final value depends on the unpredictable timing (the 'race') of the OS scheduler.", "instructions": "## Task: The Solution\\nTo prevent a race condition, you must protect the shared resource. What is the fundamental mechanism used to ensure only one thread can access the resource at a time?", "starterCode": "# Options: A switch statement, Mutual Exclusion (Mutex), A detached thread\\nmechanism = '___'", "solution": "# Options: A switch statement, Mutual Exclusion (Mutex), A detached thread\\nmechanism = 'Mutual Exclusion (Mutex)'", "hint": "Mutual Exclusion (Mutex)", "rubric": "Identifies Mutual Exclusion (Mutex)."},
            {"title": "Mutexes", "theory": "## The Lock\\nA `pthread_mutex_t` is a lock. Before modifying a shared variable, a thread calls `pthread_mutex_lock()`. If another thread already holds the lock, the calling thread goes to sleep until it is unlocked with `pthread_mutex_unlock()`.", "instructions": "## Task: Release the Lock\\nAfter updating the global counter, you must release the lock so other threads can proceed.", "starterCode": "pthread_mutex_lock(&lock);\\ncounter++;\\n___(&lock);", "solution": "pthread_mutex_lock(&lock);\\ncounter++;\\npthread_mutex_unlock(&lock);", "hint": "Use pthread_mutex_unlock", "rubric": "Uses pthread_mutex_unlock."},
            {"title": "Condition Variables", "theory": "## Waiting for State\\nSometimes a thread needs to wait for a specific condition to become true (e.g., 'Wait until the queue is not empty'). Instead of spinning in a while loop (which wastes CPU), you use a `pthread_cond_t` to safely put the thread to sleep until another thread signals it.", "instructions": "## Task: The Signal\\nWhat function is called by a producing thread to wake up at least one thread that is waiting on a condition variable?", "starterCode": "pthread_cond____(&cond);", "solution": "pthread_cond_signal(&cond);", "hint": "Use signal", "rubric": "Uses pthread_cond_signal."},
            {"title": "Semaphores", "theory": "## Counting Resources\\nA Mutex allows exactly ONE thread in. A Semaphore (`sem_t`) maintains a counter and allows N threads in. It's often used to track the number of available slots in a bounded buffer.", "instructions": "## Task: Decrement the Semaphore\\nIn POSIX semaphores, what function is used to decrement the counter and wait if it is zero? (Often called the P operation).", "starterCode": "sem____(&my_semaphore);", "solution": "sem_wait(&my_semaphore);", "hint": "Use wait", "rubric": "Uses sem_wait."},
            {"title": "Deadlocks", "theory": "## The Deadly Embrace\\nA deadlock occurs when Thread A holds Lock 1 and is waiting for Lock 2, while Thread B holds Lock 2 and is waiting for Lock 1. Both sleep forever.", "instructions": "## Task: Prevention\\nWhat is the most common and robust strategy to prevent locking deadlocks in a complex system?", "starterCode": "# Options: Never use locks, Always acquire locks in the exact same strict order, Run on a single core\\nstrategy = '___'", "solution": "# Options: Never use locks, Always acquire locks in the exact same strict order, Run on a single core\\nstrategy = 'Always acquire locks in the exact same strict order'", "hint": "Always acquire locks in the exact same strict order", "rubric": "Identifies strict locking order."},
            {"title": "Atomic Operations", "theory": "## C11 Atomics\\nSince C11, the `<stdatomic.h>` header provides atomic types (like `atomic_int`). These use hardware-level instructions to guarantee that simple operations (like `counter++`) happen atomically, eliminating the need for slow mutexes for simple counters.", "instructions": "## Task: The Header\\nInclude the C11 header required to declare an `atomic_int`.", "starterCode": "#include <___>", "solution": "#include <stdatomic.h>", "hint": "Include stdatomic.h", "rubric": "Uses <stdatomic.h>."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'c_programming.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH63.items():
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
                
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH63.items():
            tier = course_info["tier"]
            if "C Programming" in index_data and tier in index_data["C Programming"]:
                if new_course_name not in index_data["C Programming"][tier]:
                    index_data["C Programming"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 63: Added {total} lessons to C Programming track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
