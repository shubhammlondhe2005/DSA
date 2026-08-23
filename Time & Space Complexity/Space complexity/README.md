# 💾 Space Complexity

> **Space Complexity measures how much memory an algorithm requires as the input size grows.**

Space Complexity is one of the two fundamental parts of algorithm analysis:

```text
Time Complexity  → How much computation/work is performed?
Space Complexity → How much memory is required?
```

This section covers **Space Complexity from the fundamentals to practical Python examples**, including auxiliary space, recursion stack, data structures, time-space trade-offs, and common mistakes.

---

## 📚 Table of Contents

- [1. What is Space Complexity?](#1-what-is-space-complexity)
- [2. Why Space Complexity Matters](#2-why-space-complexity-matters)
- [3. Understanding `n`](#3-understanding-n)
- [4. Input Space vs Auxiliary Space](#4-input-space-vs-auxiliary-space)
- [5. Big-O for Space Complexity](#5-big-o-for-space-complexity)
- [6. O(1) — Constant Space](#6-o1--constant-space)
- [7. O(log n) — Logarithmic Space](#7-olog-n--logarithmic-space)
- [8. O(n) — Linear Space](#8-on--linear-space)
- [9. O(n²) — Quadratic Space](#9-on²--quadratic-space)
- [10. O(n³) — Cubic Space](#10-on³--cubic-space)
- [11. O(2ⁿ) — Exponential Space](#11-o2ⁿ--exponential-space)
- [12. O(n!) — Factorial Space](#12-on--factorial-space)
- [13. Recursion Stack](#13-recursion-stack)
- [14. Space Complexity of Python Data Structures](#14-space-complexity-of-python-data-structures)
- [15. Time-Space Trade-Off](#15-time-space-trade-off)
- [16. Rules for Calculating Space Complexity](#16-rules-for-calculating-space-complexity)
- [17. Common Mistakes](#17-common-mistakes)
- [18. Space Complexity Hierarchy](#18-space-complexity-hierarchy)
- [19. Quick Reference](#19-quick-reference)
- [20. Practice](#20-practice)

---

# 1. What is Space Complexity?

**Space Complexity** describes how the memory requirements of an algorithm grow as the size of its input increases.

In simple terms:

> **Space Complexity tells us how much memory an algorithm needs to solve a problem.**

Consider:

```python
def add(a, b):
    result = a + b
    return result
```

Only a fixed number of variables are created.

Therefore:

```text
Space Complexity = O(1)
```

The memory requirement does not grow with `n`.

---

# 2. Why Space Complexity Matters

An algorithm may be fast but use a large amount of memory.

For example:

| Approach | Time | Extra Space |
|---|---:|---:|
| Approach A | `O(n²)` | `O(1)` |
| Approach B | `O(n)` | `O(n)` |

Approach B is faster, but it requires additional memory.

Understanding Space Complexity helps us:

- Reduce unnecessary memory usage
- Prevent memory-related problems
- Choose appropriate data structures
- Optimize algorithms
- Understand recursion
- Design scalable solutions
- Analyze interview problems
- Make better time-space trade-offs

---

# 3. Understanding `n`

In DSA, `n` usually represents the **size of the input**.

Example:

```python
arr = [10, 20, 30, 40, 50]
```

There are 5 elements:

```text
n = 5
```

If the array contains 1,000 elements:

```text
n = 1000
```

Space Complexity asks:

> **As `n` increases, how does the memory required by the algorithm grow?**

---

# 4. Input Space vs Auxiliary Space

This distinction is extremely important.

## Input Space

The memory required to store the input itself.

Example:

```python
arr = [10, 20, 30, 40, 50]
```

An array containing `n` elements requires:

```text
Input Space = O(n)
```

---

## Auxiliary Space

The **additional memory used by the algorithm**, excluding the input.

Example:

```python
def find_max(arr):
    maximum = arr[0]

    for x in arr:
        if x > maximum:
            maximum = x

    return maximum
```

The input array already exists.

The algorithm only uses a few variables:

```text
maximum
x
```

Therefore:

```text
Auxiliary Space = O(1)
```

### ⭐ Important Interview Rule

When an interviewer asks:

> "What is the space complexity?"

They often mean:

> **What is the auxiliary space complexity?**

Always understand whether the input storage is being counted.

---

# 5. Big-O for Space Complexity

Big-O describes how memory usage grows as `n` increases.

The commonly encountered space complexities are:

| Complexity | Name |
|---|---|
| `O(1)` | Constant |
| `O(log n)` | Logarithmic |
| `O(n)` | Linear |
| `O(n²)` | Quadratic |
| `O(n³)` | Cubic |
| `O(2ⁿ)` | Exponential |
| `O(n!)` | Factorial |

For most DSA problems, the most important are:

```text
O(1)
O(log n)
O(n)
O(n²)
```

---

# 6. O(1) — Constant Space

## 📌 Definition

`O(1)` means the algorithm uses a **constant amount of extra memory**, regardless of the input size.

### Example

```python
def calculate_sum(a, b):
    result = a + b
    return result
```

Only a fixed number of variables are used.

```text
Space = O(1)
```

### Another Example

```python
def find_max(arr):
    maximum = arr[0]

    for x in arr:
        if x > maximum:
            maximum = x

    return maximum
```

Even if:

```text
n = 10
n = 1,000
n = 1,000,000
```

the algorithm still uses only a constant number of extra variables.

Therefore:

```text
Auxiliary Space = O(1)
```

### Common Examples

- Swapping two variables
- Finding maximum/minimum
- Calculating a sum
- Iterative traversal without extra storage
- Using a fixed number of variables

---

# 7. O(log n) — Logarithmic Space

## 📌 Definition

`O(log n)` space usually occurs when recursion repeatedly reduces the problem size by a constant factor.

### Example: Recursive Binary Search

```python
def binary_search(arr, left, right, target):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search(arr, mid + 1, right, target)

    return binary_search(arr, left, mid - 1, target)
```

At each recursive call, the search space is approximately halved:

```text
n
↓
n/2
↓
n/4
↓
n/8
↓
...
```

The recursion depth is:

```text
log n
```

Therefore:

```text
Time  = O(log n)
Space = O(log n)
```

### Iterative Binary Search

```python
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

There is no recursive call stack.

Therefore:

```text
Time  = O(log n)
Space = O(1)
```

### ⭐ Key Lesson

Two algorithms can have the same time complexity but different space complexities:

```text
Recursive Binary Search
Time  → O(log n)
Space → O(log n)

Iterative Binary Search
Time  → O(log n)
Space → O(1)
```

---

# 8. O(n) — Linear Space

## 📌 Definition

`O(n)` means the extra memory grows linearly with the input size.

### Example

```python
def create_array(n):

    result = []

    for i in range(n):
        result.append(i)

    return result
```

If:

```text
n = 10
```

we store 10 elements.

If:

```text
n = 1000
```

we store 1,000 elements.

Therefore:

```text
Space = O(n)
```

---

## Copying an Array

```python
def copy_array(arr):

    result = []

    for x in arr:
        result.append(x)

    return result
```

If the input contains `n` elements, the new array also contains `n` elements.

Therefore:

```text
Auxiliary Space = O(n)
```

### Common Examples

- Creating a new array
- Copying an array
- HashMap with `n` elements
- HashSet with `n` elements
- Queue containing `n` elements
- Stack containing `n` elements
- Recursion depth of `n`

---

# 9. O(n²) — Quadratic Space

## 📌 Definition

`O(n²)` space occurs when the algorithm stores approximately `n × n` elements.

The most common example is an `n × n` matrix.

```python
def create_matrix(n):

    matrix = []

    for i in range(n):

        row = []

        for j in range(n):
            row.append(0)

        matrix.append(row)

    return matrix
```

The matrix contains:

```text
n × n = n²
```

elements.

Therefore:

```text
Space = O(n²)
```

### Example

For:

```text
n = 3
```

we store:

```text
3 × 3 = 9
```

elements.

For:

```text
n = 100
```

we store:

```text
100 × 100 = 10,000
```

elements.

---

# 10. O(n³) — Cubic Space

`O(n³)` space can occur when storing a 3-dimensional structure.

Example:

```python
def create_3d_array(n):

    cube = [
        [
            [0 for _ in range(n)]
            for _ in range(n)
        ]
        for _ in range(n)
    ]

    return cube
```

Number of stored elements:

```text
n × n × n = n³
```

Therefore:

```text
Space = O(n³)
```

This is less common in basic DSA but is important to recognize.

---

# 11. O(2ⁿ) — Exponential Space

A set containing `n` elements has:

```text
2ⁿ
```

possible subsets.

For example:

```text
n = 3
```

Number of subsets:

```text
2³ = 8
```

If an algorithm explicitly stores all subsets, the storage can become exponential.

Therefore, depending on what is being stored:

```text
Space ≈ O(2ⁿ)
```

> **Note:** If each subset is explicitly stored, the total memory can be larger because each subset contains multiple elements. The exact bound depends on the implementation and what is counted.

---

# 12. O(n!) — Factorial Space

A collection of `n` elements has:

```text
n!
```

possible permutations.

Examples:

```text
3! = 6
4! = 24
5! = 120
6! = 720
10! = 3,628,800
```

If all permutations are explicitly stored:

```text
Space ≈ O(n!)
```

Again, if the actual elements inside every permutation are counted, the total memory can be larger than just the number of permutations.

---

# 13. Recursion Stack

## 📌 Why does recursion use memory?

Every recursive function call must be stored in the **call stack** until it returns.

Consider:

```python
def countdown(n):

    if n == 0:
        return

    print(n)
    countdown(n - 1)
```

For:

```text
n = 5
```

the call stack becomes:

```text
countdown(5)
     ↓
countdown(4)
     ↓
countdown(3)
     ↓
countdown(2)
     ↓
countdown(1)
     ↓
countdown(0)
```

There can be `n` active calls.

Therefore:

```text
Time  = O(n)
Space = O(n)
```

### ⭐ Important

Even if you don't create an array or list, recursion can still consume significant memory.

---

# 14. Space Complexity of Python Data Structures

Understanding Python's built-in data structures is important for DSA.

| Data Structure | Space for `n` Elements |
|---|---:|
| List | `O(n)` |
| Dictionary | `O(n)` |
| Set | `O(n)` |
| Stack | `O(n)` |
| Queue | `O(n)` |
| `n × n` Matrix | `O(n²)` |

### Example — List

```python
arr = [1, 2, 3, 4, 5]
```

For `n` elements:

```text
Space = O(n)
```

### Example — Dictionary

```python
frequency = {}

for x in arr:
    frequency[x] = frequency.get(x, 0) + 1
```

In the worst case, all `n` elements are different.

Therefore:

```text
Space = O(n)
```

### Example — Set

```python
seen = set()

for x in arr:
    seen.add(x)
```

In the worst case:

```text
Space = O(n)
```

---

# 15. Time-Space Trade-Off

Sometimes we use additional memory to make an algorithm faster.

## Example: Two Sum

### Brute Force

Check every pair:

```text
Time  = O(n²)
Space = O(1)
```

### HashMap

Store previously seen values:

```text
Time  = O(n) average
Space = O(n)
```

Comparison:

| Approach | Time | Space |
|---|---:|---:|
| Brute Force | `O(n²)` | `O(1)` |
| HashMap | `O(n)` average | `O(n)` |

The HashMap solution uses more memory but significantly improves the time complexity.

This is called a:

> **Time-Space Trade-Off**

---

# 16. Rules for Calculating Space Complexity

Use this process whenever you analyze an algorithm.

### Step 1 — Identify the input

Determine the input size:

```text
n = input size
```

### Step 2 — Find additional variables

Example:

```python
x = 10
y = 20
```

A fixed number of variables:

```text
O(1)
```

### Step 3 — Find additional data structures

Look for:

```text
List
Array
Dictionary
Set
Stack
Queue
Matrix
Tree
Graph
```

Ask:

> How large can this structure become?

### Step 4 — Check recursion

Ask:

> How many recursive calls can exist simultaneously?

This determines the recursion stack space.

### Step 5 — Calculate memory growth

Examples:

```text
n elements       → O(n)

n × n elements   → O(n²)

n × n × n        → O(n³)

log n calls      → O(log n)
```

### Step 6 — Keep the dominant term

Example:

```text
O(n + n²)
```

becomes:

```text
O(n²)
```

Similarly:

```text
O(n + n³)
```

becomes:

```text
O(n³)
```

---

# 17. Common Mistakes

## ❌ Mistake 1 — Counting Input Space as Auxiliary Space

```python
def find_max(arr):

    maximum = arr[0]

    for x in arr:
        maximum = max(maximum, x)

    return maximum
```

The input array already exists.

Therefore:

```text
Auxiliary Space = O(1)
```

Not `O(n)`.

---

## ❌ Mistake 2 — Forgetting Recursion Stack

```python
def f(n):

    if n == 0:
        return

    f(n - 1)
```

The recursive calls consume stack memory.

Therefore:

```text
Space = O(n)
```

---

## ❌ Mistake 3 — Assuming Time and Space Are the Same

```python
def print_array(arr):

    for x in arr:
        print(x)
```

Time:

```text
O(n)
```

Auxiliary Space:

```text
O(1)
```

Therefore:

```text
Time ≠ Space
```

They must be analyzed separately.

---

## ❌ Mistake 4 — Forgetting HashMap / Set Storage

```python
seen = set()

for x in arr:
    seen.add(x)
```

The set can contain up to `n` elements.

Therefore:

```text
Space = O(n)
```

---

## ❌ Mistake 5 — Ignoring Stored Results

If an algorithm creates and stores `n` results:

```text
Space = O(n)
```

The returned data itself may require memory.

---

# 18. Space Complexity Hierarchy

From lower growth to higher growth:

```text
O(1)
  ↓
O(log n)
  ↓
O(n)
  ↓
O(n²)
  ↓
O(n³)
  ↓
O(2ⁿ)
  ↓
O(n!)
```

For most DSA problems, you will frequently encounter:

```text
O(1)
O(log n)
O(n)
O(n²)
```

---

# 19. Quick Reference

| Space Complexity | Meaning | Typical Example |
|---|---|---|
| `O(1)` | Constant memory | Fixed variables |
| `O(log n)` | Logarithmic memory | Recursive binary search |
| `O(n)` | Linear memory | Extra array / HashMap |
| `O(n²)` | Quadratic memory | `n × n` matrix |
| `O(n³)` | Cubic memory | 3D structure |
| `O(2ⁿ)` | Exponential memory | Explicitly stored subsets |
| `O(n!)` | Factorial memory | Explicitly stored permutations |

---

# 20. Practice

Try to determine the **auxiliary space complexity** of each problem before checking the solution.

### Problem 1

```python
def example(n):

    x = 10
    y = 20
    z = x + y

    return z
```

<details>
<summary>Answer</summary>

```text
O(1)
```

Only a fixed number of variables are created.

</details>

---

### Problem 2

```python
def example(n):

    arr = [0] * n

    return arr
```

<details>
<summary>Answer</summary>

```text
O(n)
```

The new list contains `n` elements.

</details>

---

### Problem 3

```python
def example(arr):

    total = 0

    for x in arr:
        total += x

    return total
```

<details>
<summary>Answer</summary>

```text
O(1)
```

Only a fixed number of extra variables are used.

</details>

---

### Problem 4

```python
def example(arr):

    result = []

    for x in arr:
        result.append(x)

    return result
```

<details>
<summary>Answer</summary>

```text
O(n)
```

The new list contains up to `n` elements.

</details>

---

### Problem 5

```python
def example(n):

    matrix = []

    for i in range(n):
        row = [0] * n
        matrix.append(row)

    return matrix
```

<details>
<summary>Answer</summary>

```text
O(n²)
```

The matrix contains `n × n` elements.

</details>

---

### Problem 6

```python
def example(arr):

    seen = set()

    for x in arr:
        seen.add(x)

    return seen
```

<details>
<summary>Answer</summary>

Worst-case:

```text
O(n)
```

The set can contain `n` unique elements.

</details>

---

### Problem 7

```python
def example(n):

    if n == 0:
        return

    example(n - 1)
```

<details>
<summary>Answer</summary>

```text
O(n)
```

The recursion depth is `n`.

</details>

---

### Problem 8

```python
def example(n):

    if n <= 1:
        return

    example(n // 2)
```

<details>
<summary>Answer</summary>

```text
O(log n)
```

The input is divided by 2 at each recursive call.

</details>

---

### Problem 9

```python
def example(n):

    arr = [0] * n
    matrix = [[0] * n for _ in range(n)]

    return arr, matrix
```

<details>
<summary>Answer</summary>

```text
O(n) + O(n²)
```

Dominant term:

```text
O(n²)
```

</details>

---

### Problem 10

```python
def example(arr):

    frequency = {}

    for x in arr:
        frequency[x] = frequency.get(x, 0) + 1

    return frequency
```

<details>
<summary>Answer</summary>

Worst-case:

```text
O(n)
```

The dictionary can contain up to `n` unique keys.

</details>

---

# 🎯 Key Takeaways

Remember these core concepts:

```text
┌─────────────────────────────────────────────┐
│             SPACE COMPLEXITY                │
├─────────────────────────────────────────────┤
│                                             │
│ O(1)      → Fixed amount of extra memory    │
│                                             │
│ O(log n)  → Logarithmic recursion depth     │
│                                             │
│ O(n)      → Extra storage proportional to n │
│                                             │
│ O(n²)     → n × n storage                   │
│                                             │
│ Recursion → Uses call-stack memory          │
│                                             │
│ HashMap   → Can require O(n) extra space    │
│                                             │
│ Set       → Can require O(n) extra space    │
│                                             │
└─────────────────────────────────────────────┘
```

### ⭐ Core Rule

> **Count the extra memory created by the algorithm and determine how that memory grows with `n`.**

Always analyze:

```text
Time Complexity
       +
Space Complexity
       ↓
Complete Algorithm Analysis
```

---

## 🚀 Next Step

After understanding Space Complexity, continue with:

```text
Time Complexity
```

Start with:

```text
O(1)
 ↓
O(log n)
 ↓
O(√n)
 ↓
O(n)
 ↓
O(n log n)
 ↓
O(n²)
 ↓
O(n³)
 ↓
O(2ⁿ)
 ↓
O(n!)
```

---

## 📌 Repository Structure

```text
DSA/
│
├── README.md
│
└── 01_Time_and_Space_Complexity/
    │
    ├── README.md
    │
    ├── Space_Complexity/
    │   └── README.md
    │
    └── Time_Complexity/
        └── README.md
```

**Current Topic → Space Complexity** 💾
