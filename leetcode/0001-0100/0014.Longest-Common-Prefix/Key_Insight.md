### Core Algorithmic Pattern

**Horizontal Scanning (Prefix Expansion) + Greedy Early Termination**

This solution uses the **horizontal scanning** pattern: build the common prefix character by character and check it against all strings. It’s paired with a **greedy early-exit strategy** to stop as soon as the prefix becomes invalid.

---

### The “Aha!” Moment 🧠

The key insight is:

> **The longest common prefix cannot be longer than the shortest string.**

Once you lock onto the shortest string, every possible prefix must come from it. That immediately bounds the problem and avoids unnecessary checks.

---

### Why This Works Efficiently

#### 1. Sort by length to cap the search space

```python
strs.sort(key=len)
```

**Aha insight:**
If the shortest string has length `k`, the answer can’t exceed `k`.
Sorting once simplifies the rest of the logic.

---

#### 2. Grow the prefix one character at a time

```python
prefix = strs[0][:i + 1]
```

This incremental approach:

* Avoids recomputation
* Makes each step easy to verify
* Allows immediate failure detection

---

#### 3. Early termination on first mismatch

```python
if not strs[j].startswith(prefix):
    return prefix[:-1]
```

The moment **any** string fails to match:

* No longer prefix can ever work
* You return immediately

This greedy exit saves a lot of unnecessary comparisons.

---

### Mental Model

Imagine lining up all strings vertically:

```
flower
flow
flight
```

You scan column by column:

* As long as all characters match → keep going
* First mismatch → stop forever

---

### Efficiency

Let:

* `n` = number of strings

* `m` = length of the shortest string

* **Time Complexity:** `O(n × m)`

* **Space Complexity:** `O(1)` (ignoring sort cost)

> Note: Sorting costs `O(n log n)`, but the prefix check dominates for typical inputs.

---

### Summary

**Pattern:**

> Horizontal Scanning with Greedy Early Exit

**Aha Moment:**

> Once you limit the prefix to the shortest string and stop at the first mismatch, you never do unnecessary work.

This turns a potentially messy comparison problem into a clean, predictable scan.
