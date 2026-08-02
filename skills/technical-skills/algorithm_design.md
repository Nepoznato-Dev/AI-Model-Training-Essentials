# Algorithm Design

## Overview

Algorithm design is the process of creating step-by-step procedures for solving computational problems efficiently. Well-designed algorithms optimize for time complexity, space complexity, and readability while correctly solving the problem at hand.

This skill covers fundamental algorithmic paradigms, analysis techniques, and practical strategies for designing efficient solutions to common programming challenges.

## Core Competencies

- **Complexity Analysis**: Big O notation, time and space trade-offs
- **Divide and Conquer**: Breaking problems into smaller subproblems
- **Greedy Algorithms**: Making locally optimal choices
- **Dynamic Programming**: Solving overlapping subproblems
- **Backtracking**: Systematic exploration of solution spaces
- **Graph Algorithms**: Traversal, shortest paths, minimum spanning trees
- **String Algorithms**: Pattern matching, text processing
- **Sorting and Searching**: Efficient data organization and retrieval

## When to Use

Algorithm design skills are essential when:
- ✅ Solving complex computational problems
- ✅ Optimizing performance-critical code
- ✅ Processing large datasets efficiently
- ✅ Building foundational software components
- ✅ Preparing for technical interviews
- ✅ Evaluating trade-offs between different approaches
- ✅ Designing scalable systems

**Not ideal for:**
- ❌ Simple CRUD operations (use standard patterns)
- ❌ Problems with existing well-tested library solutions
- ❌ Prototyping where performance isn't critical

## Algorithmic Paradigms

### Divide and Conquer

Break a problem into smaller subproblems, solve each independently, then combine results.

```python
def merge_sort(arr):
    """Sort array using divide and conquer approach."""
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer and Combine
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Time Complexity: O(n log n)
# Space Complexity: O(n)
```

### Greedy Algorithms

Make the locally optimal choice at each step hoping to find the global optimum.

```python
def activity_selection(activities):
    """
    Select maximum number of non-overlapping activities.
    Each activity has (start, finish) times.
    """
    # Sort by finish time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_finish = activities[0][1]
    
    for start, finish in activities[1:]:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    
    return selected

# Time Complexity: O(n log n) for sorting
# Space Complexity: O(1) excluding output
```

### Dynamic Programming

Solve complex problems by breaking them into overlapping subproblems and storing results.

```python
def longest_common_subsequence(text1, text2):
    """Find length of longest common subsequence."""
    m, n = len(text1), len(text2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
```

### Backtracking

Systematically explore all possible solutions, abandoning paths that fail constraints.

```python
def solve_n_queens(n):
    """Solve N-Queens problem using backtracking."""
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
        
        # Check diagonals
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False
        
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    
    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions

# Time Complexity: O(N!)
# Space Complexity: O(N)
```

## Graph Algorithms

### Breadth-First Search (BFS)

```python
from collections import deque

def bfs(graph, start):
    """Breadth-first search traversal."""
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Time Complexity: O(V + E)
# Space Complexity: O(V)
```

### Depth-First Search (DFS)

```python
def dfs(graph, start, visited=None):
    """Depth-first search traversal."""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# Time Complexity: O(V + E)
# Space Complexity: O(V)
```

### Dijkstra's Shortest Path

```python
import heapq

def dijkstra(graph, start):
    """Find shortest paths from start to all vertices."""
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Time Complexity: O((V + E) log V)
# Space Complexity: O(V)
```

## String Algorithms

### KMP Pattern Matching

```python
def kmp_search(text, pattern):
    """Knuth-Morris-Pratt string matching algorithm."""
    def compute_lps(pattern):
        """Compute Longest Proper Prefix which is also Suffix array."""
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    
    i = j = 0
    occurrences = []
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
            if j == m:
                occurrences.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return occurrences

# Time Complexity: O(n + m)
# Space Complexity: O(m)
```

## Sorting Algorithms Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable |
|-----------|-----------|--------------|------------|-------|--------|
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Counting Sort** | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |

## Practical Templates

### Binary Search Template

```python
def binary_search(arr, target):
    """Standard binary search implementation."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_leftmost(arr, target):
    """Find leftmost occurrence of target."""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] >= target:
            if arr[mid] == target:
                result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result
```

### Sliding Window Template

```python
def sliding_window_max(arr, k):
    """Find maximum in each sliding window of size k."""
    from collections import deque
    
    if not arr or k <= 0:
        return []
    
    result = []
    dq = deque()
    
    for i in range(len(arr)):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum for current window
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result
```

### Two Pointers Template

```python
def two_sum_sorted(arr, target):
    """Find two numbers that sum to target in sorted array."""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]
```

## Common Pitfalls

### 🚫 Off-by-One Errors

**Problem:** Incorrect loop boundaries or index calculations.

**Solution:**
```python
# ❌ Bad: May access out of bounds
for i in range(len(arr)):
    if arr[i] == arr[i+1]:  # Error when i = len(arr) - 1
        pass

# ✅ Good: Proper boundary check
for i in range(len(arr) - 1):
    if arr[i] == arr[i+1]:
        pass
```

### 🚫 Ignoring Edge Cases

**Problem:** Not handling empty inputs, single elements, or extreme values.

**Solution:**
```python
def find_max(arr):
    # Handle edge cases first
    if not arr:
        raise ValueError("Array cannot be empty")
    
    if len(arr) == 1:
        return arr[0]
    
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    
    return max_val
```

### 🚫 Inefficient Nested Loops

**Problem:** Using O(n²) when O(n) or O(n log n) is possible.

**Solution:**
```python
# ❌ Bad: O(n²)
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# ✅ Good: O(n) with hash set
def has_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### 🚫 Recursion Without Base Case

**Problem:** Infinite recursion leading to stack overflow.

**Solution:**
```python
# ❌ Bad: Missing base case
def factorial(n):
    return n * factorial(n - 1)

# ✅ Good: With proper base case
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

## Best Practices

### ✅ Do

- Analyze time and space complexity before implementing
- Consider edge cases (empty, single element, duplicates)
- Choose appropriate data structures for the problem
- Write tests for boundary conditions
- Document algorithm assumptions and constraints
- Optimize only after profiling identifies bottlenecks
- Use built-in functions when they're optimized
- Break complex problems into smaller subproblems

### ❌ Don't

- Prematurely optimize without measuring
- Reinvent the wheel for standard problems
- Ignore memory constraints
- Use recursion for deep call stacks (use iteration)
- Overlook integer overflow possibilities
- Forget to validate input parameters
- Sacrifice readability for cleverness
- Skip testing with large inputs

## Tools & Resources

### Visualization Tools

| Tool | Purpose |
|------|---------|
| **VisuAlgo** | Algorithm visualizations |
| **Algorithm Visualizer** | Interactive algorithm animations |
| **USFCA Data Structures** | Data structure visualizations |

### Practice Platforms

| Platform | Focus |
|----------|-------|
| **LeetCode** | Interview preparation |
| **HackerRank** | Skill-building challenges |
| **Codeforces** | Competitive programming |
| **AtCoder** | Algorithm contests |
| **Project Euler** | Mathematical problems |

### Learning Resources

- 📚 ["Introduction to Algorithms" by Cormen et al.](https://mitpress.mit.edu/books/introduction-algorithms)
- 📚 ["Algorithms" by Sedgewick and Wayne](https://algs4.cs.princeton.edu/)
- 📚 ["The Algorithm Design Manual" by Skiena](http://www.algorist.com/)
- 🎥 [MIT OpenCourseWare: Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
- 🌐 [GeeksforGeeks Algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/)

## Examples

### Example 1: Finding Maximum Subarray Sum

```python
def max_subarray_sum(arr):
    """
    Kadane's Algorithm - Find maximum sum contiguous subarray.
    
    Example:
    >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6  # [4, -1, 2, 1]
    """
    if not arr:
        return 0
    
    max_current = max_global = arr[0]
    
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)
    
    return max_global

# Time Complexity: O(n)
# Space Complexity: O(1)
```

### Example 2: Merge Intervals

```python
def merge_intervals(intervals):
    """
    Merge overlapping intervals.
    
    Example:
    >>> merge_intervals([[1,3],[2,6],[8,10],[15,18]])
    [[1,6],[8,10],[15,18]]
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:
            # Overlapping intervals - merge
            last[1] = max(last[1], current[1])
        else:
            # Non-overlapping - add to result
            merged.append(current)
    
    return merged

# Time Complexity: O(n log n) for sorting
# Space Complexity: O(1) excluding output
```

### Example 3: Top K Frequent Elements

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    """
    Find k most frequent elements.
    
    Example:
    >>> top_k_frequent([1,1,1,2,2,3], 2)
    [1, 2]
    """
    # Count frequencies
    freq = Counter(nums)
    
    # Use heap to find top k
    return heapq.nlargest(k, freq.keys(), key=freq.get)

# Time Complexity: O(n log k)
# Space Complexity: O(n)
```

## Success Indicators

### Proficiency Levels

- **Beginner:** Can implement basic sorting, searching, and simple graph algorithms
- **Intermediate:** Applies dynamic programming, greedy approaches, and analyzes complexity
- **Advanced:** Designs novel algorithms for complex problems, optimizes for specific constraints
- **Expert:** Contributes new algorithmic techniques, teaches others, publishes research

### Quality Metrics

- Correctly solves problems on first attempt > 70% of time
- Accurately predicts time/space complexity before implementation
- Identifies optimal algorithm for given constraints
- Can explain trade-offs between different approaches
- Writes clean, maintainable algorithm implementations

## Related Skills

- [Programming Fundamentals](programming_fundamentals.md) - Core coding skills
- [Data Structures](data_structures.md) - Choosing appropriate structures
- [System Design](system_design.md) - Large-scale algorithm integration
- [Mathematics for CS](mathematics_for_cs.md) - Theoretical foundations

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Technical Skills Team
next_review: 2026-07-15
---
