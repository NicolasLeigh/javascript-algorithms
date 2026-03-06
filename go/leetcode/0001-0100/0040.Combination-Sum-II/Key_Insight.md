### 1. The Core Algorithmic Pattern: **Backtracking**

The solution uses **Backtracking (Depth-First Search)**.

Since the problem asks for all possible combinations that meet a specific criteria, we are essentially exploring a **state-space tree**. We "make a choice" (add a number), "explore" (recurse), and then "undo the choice" (pop the number) to try a different path.

### 2. The "Aha!" Moment: **Horizontal vs. Vertical Duplicate Management**

The true brilliance of this solution isn't just the recursion; it’s the combination of **sorting** and the **`if i > start`** condition.

The "Aha!" insight is realizing the difference between using a duplicate number in a **single combination** versus starting a **new combination** with that same duplicate.

* **Vertical Movement (Depth):** By calling `backtrack(i + 1)`, we allow the algorithm to move to the next index. If the input is `[1, 1, 2]`, it's perfectly fine to have a combination like `[1, 1]` because those are two different "1"s from different positions in the array.
* **Horizontal Movement (Breadth):** The loop `for i in range(start, len(candidates))` represents choices at the *same* position in the combination. If we just finished exploring a combination starting with the first `1`, we don't want to start an entirely new branch with the second `1`. It would lead to the exact same results.

> **The Logic:** The condition `if i > start and candidates[i] == candidates[i - 1]: continue` says: "If I am at the same level of the tree and this number is the same as the one I just tried, skip it."

---

### Why this is efficient

1. **Sorting ($O(N \log N)$):** This is a small price to pay to enable $O(1)$ duplicate detection.
2. **Early Pruning:** The check `if sum_val > target: return` stops the algorithm from wasting time on paths that will never work, significantly cutting down the search space.
3. **No Extra Memory for Uniqueness:** Many beginners use a `Set` to store results to handle duplicates, which is slow and memory-intensive. This "skip" logic ensures the results are unique by design.
