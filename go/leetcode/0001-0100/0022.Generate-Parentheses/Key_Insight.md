### Core Algorithmic Pattern

**Backtracking (DFS with Pruning / Constraint-guided Generation)**

This solution uses **backtracking** to systematically build all valid parentheses strings while **pruning invalid paths early**.

---

### The “Aha!” Moment 🧠

The key insight is:

> **You never need to generate all `2^(2n)` strings and then validate them.
> Instead, only build strings that are guaranteed to stay valid at every step.**

Validity is enforced *during construction*, not checked afterward.

---

### Why This Works Efficiently

#### 1. Track remaining parentheses, not the string’s validity

```python
backtrack(left, right, current_str)
```

* `left`: number of `(` still available
* `right`: number of `)` still available

**Aha insight:**
You don’t need a stack or a final validation pass.
If these two counts obey the rules, the string is automatically valid.

---

#### 2. Only two legal moves exist

```python
if left > 0:
    backtrack(left - 1, right, current_str + "(")
```

You can always place `(` if you still have some left.

```python
if right > 0 and left < right:
    backtrack(left, right - 1, current_str + ")")
```

You can place `)` **only if** there are more `(` already placed than `)`.

**Aha insight:**
The condition `left < right` enforces:

> “You can’t close more parentheses than you’ve opened.”

This single inequality eliminates **all invalid prefixes**.

---

#### 3. Base case guarantees correctness

```python
if left == 0 and right == 0:
    res.append(current_str)
```

Reaching `(0, 0)` means:

* Exactly `n` pairs used
* Every prefix was valid
* The final string must be valid

No further checks required.

---

### Mental Model

Think of this as walking a path:

* `(` moves you **up**
* `)` moves you **down**
* You’re never allowed to go below ground level
* You must end exactly at ground level

Backtracking explores all such valid paths.

---

### Efficiency

* **Time Complexity:** `O(Cn)` (Catalan number, optimal)
* **Space Complexity:** `O(n)` recursion depth

This is asymptotically optimal—you generate *only* valid results.

---

### Summary

**Pattern:**

> Backtracking with constraints (DFS + pruning)

**Aha Moment:**

> Enforce parentheses validity while building the string, using `left` and `right` counts—never generate invalid states.

This problem is a textbook example of **“generate valid states only”**, which is the essence of great backtracking solutions.
