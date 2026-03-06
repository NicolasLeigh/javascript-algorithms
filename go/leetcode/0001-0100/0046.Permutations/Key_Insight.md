### 1. The Core Algorithmic Pattern: **Backtracking (State-Space Search)**

The solution uses **Backtracking**. In this pattern, we treat the problem as filling $N$ empty slots. At each step, we make a decision, dive deeper into the consequences of that decision (recursion), and then undo the decision (backtrack) to try the next available option.

### 2. The "Aha!" Moment: **Selection Without Replacement**

The "Aha!" insight here is the use of the **`used_set`** to manage "Selection Without Replacement."

In many backtracking problems (like Subsets), you only look forward to avoid duplicates. In Permutations, you are allowed to look "backward" at the whole array for every slot—**except** for the numbers you've already picked for the current path.

**The Logic:**

* **The "Used" Filter:** By checking `if num in used_set`, you are essentially saying: "I have $N$ numbers available, but for this specific slot in my permutation, I can only use what hasn't been placed yet."
* **Global vs. Local State:** The `used_set` acts as a global "memo" of the current path. When you `add` a number, you're locking it for all recursive calls below it. When you `remove` it, you're unlocking it so it can be used in a different position in a later permutation.

> **The Insight:** A permutation is just a path from the root to a leaf in a tree where each level reduces the "available pool" by exactly one. The `used_set` is the most efficient way to keep track of that shrinking pool without physically modifying the input array.

---

### Why this is efficient

* **Time Complexity:** $O(N \cdot N!)$. There are $N!$ permutations, and it takes $O(N)$ time to copy each one into the result list. This is technically the "best" possible time because you have to generate every single permutation.
* **Space Complexity:** $O(N)$. The recursion depth is $N$, and the `used_set` stores at most $N$ elements, making it very memory-efficient compared to creating new sliced arrays at every step.
