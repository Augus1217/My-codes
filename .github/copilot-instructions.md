# Copilot Instructions for My-codes

## Project Overview

This is a competitive programming practice repository containing solutions to APCS (Advanced Placement Computer Science) and ZeroJudge (ZJ) problems in both Python and C++.

## Directory Structure

```
cpp/
  apcs/      # APCS problems in C++
  zj/        # ZeroJudge problems in C++
python/
  apcs/      # APCS problems in Python (organized by difficulty/category)
    1/       # Primary APCS solutions
    2/       # Secondary APCS solutions
  apcs-simu/ # APCS simulation contest problems
```

## Coding Conventions

### Problem Naming
- Files are named by problem ID (e.g., `b964.cpp`, `c462.py`, `a001.cpp`)
- Each problem has its own directory: `<problem-id>/<problem-id>.<ext>`
- Both languages may have solutions to the same problem (e.g., `apcs/b964/b964.cpp` and `apcs/1/b964.py`)

### Python Style
- **Compact, competition-focused code**: prioritize brevity over readability
- **List comprehensions**: heavily used for input parsing and transformations
  - Example: `l=[int(x) for x in input().split()]`
- **No imports unless necessary**: most solutions use built-in functions only
- **Direct I/O**: use `input()` and `print()` without wrapper functions
- **Variable names**: short names (`l`, `n`, `k`, `s`) are standard

### C++ Style
- **Always include**: `#include<iostream>` and `using namespace std;`
- **STL usage**: `vector`, `algorithm` (sort, min_element, max_element, lower_bound)
- **Short types**: prefer `short int` or `int` for memory efficiency
- **Direct I/O**: use `cin` and `cout` without buffering optimizations

### Common Patterns

**Python input parsing**:
```python
n = int(input())                          # Single integer
l = [int(x) for x in input().split()]     # List of integers
a, b, c = map(int, input().split())       # Multiple variables
l = [int(x) for x in input()]             # Digit-by-digit parsing
```

**C++ problem structure**:
```cpp
#include<iostream>
using namespace std;
int main(){
    // Variable declarations
    // Input reading with cin
    // Logic
    // Output with cout
    return 0;
}
```

## Build & Run

### C++
Use the configured VS Code task: "C/C++: g++ build active file"
- Compiles with: `g++ -fdiagnostics-color=always -g <file> -o <output>`
- Working directory: same as source file
- Run: `./<filename>` in the same directory

### Python
- No build step required
- Run directly: `python3 <filename>.py`

## Testing Approach
- No automated tests; solutions are verified by submitting to online judges
- Test with sample inputs provided in problem descriptions
- Use `test.py` and `test.cpp` for quick experimentation

## Notes
- `.ilk` files are compiler artifacts, can be ignored
- `python/apcs/1/others/Gemini.py`: experimental/fun code, not a problem solution
- Solutions prioritize correctness and speed for online judge submission, not production code quality
