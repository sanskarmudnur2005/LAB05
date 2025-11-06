# LAB05
NAME : SANSKAR M. MUDNUR <BR>
SRN : PES1UG24CS829 <BR>
SEC: G <BR>



### **Known Issue Table**

| **Issue** | **Type** | **Line(s)** | **Description** | **Fix Approach** |
|------------|-----------|-------------|------------------|------------------|
| Mutable default argument | Bug | 8 | `items=[]` used as default argument — shared across calls | Change default to `None` and initialize inside the function |
| Bare except | Bug | 19 | Bare `except:` hides all errors and makes debugging hard | Catch specific exception types (e.g., `except KeyError:`) |
| Use of eval() | Security | 59 | Insecure use of `eval()` can lead to code injection | Replace with `ast.literal_eval()` or safer parsing method |
| Unused import | Code Smell | 2 | `logging` imported but never used | Remove unused import statement |
| Missing docstrings | Maintainability | 1, 8, 14, 22, 25, 31, 36, 41, 48 | No docstrings for module and functions | Add appropriate docstrings for readability and maintainability |
| Naming convention | Style | Multiple | Function names like `addItem`, `removeItem` don’t follow `snake_case` | Rename to `add_item`, `remove_item`, etc. |
| Open without encoding | Bug | 26, 32 | `open()` used without specifying encoding | Use `open(filename, 'r', encoding='utf-8')` |
| Use of global variable | Code Smell | 27 | `global` keyword used, making code harder to maintain | Refactor to avoid global variables; return values instead |
| Missing blank lines | Style | 8, 14, 22, 25, 31, 36, 41, 48 | Function definitions not separated by two blank lines | Add required blank lines for PEP8 compliance |
| Missing module docstring | Style | 1 | File lacks a top-level description | Add a descriptive module-level docstring |
| Use of `%` formatting | Refactor | 12 | Regular string formatting instead of f-string | Use f-string for readability and efficiency |
| Low code rating | Metric | — | Pylint score: 4.80 / 10 | Address above issues to improve code quality |


<br>


### **Static Analysis Reflection**

#### 1. Which issues were the easiest to fix, and which were the hardest? Why?
- **Easiest:** Unused import, missing blank lines, line length, and `%`-formatting issues were simple syntax or style edits that didn’t affect logic.  
- **Hardest:** Mutable default argument (`logs=[]`), `bare except:`, and `eval()` were harder because they required changing how data and exceptions are handled while preserving the original functionality.

#### 2. Did the static analysis tools report any false positives? If so, describe one example.
- Yes. The **naming convention** warnings (`C0103`) for functions like `addItem` and `removeItem` were stylistic, not actual bugs.  
  Since the project specification required keeping original function names, these were treated as **false positives** and suppressed.

#### 3. How would you integrate static analysis tools into your actual software development workflow?
- **Local Development:** Use pre-commit hooks to run `flake8`, `pylint`, and `bandit` automatically before committing.  
- **Continuous Integration (CI):** Integrate static analysis checks into the CI pipeline to block merges if security or high-severity issues are found.  
- **Maintenance:** Use auto-formatters like `black` or `isort` for style consistency and allow justified rule suppressions when needed.

#### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
- **Security:** Removed dangerous use of `eval()` and replaced `bare except` with explicit exception handling.  
- **Robustness:** Added type checks, used `with open(..., encoding='utf-8')`, and ensured safe default arguments.  
- **Maintainability:** Added docstrings, consistent logging, and better error handling.  
- **Readability:** Code structure and spacing now follow PEP8, making it easier to understand and extend.

