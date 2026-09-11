### Core Algorithmic Pattern

**Greedy Algorithm (Value Decomposition)**

This solution is a classic **greedy** approach: at every step, it takes the **largest possible Roman value** that does not exceed the remaining number.

---

### The “Aha!” Moment 🧠

The key insight is:

> **Roman numerals are not positional—they’re subtractive and additive, and their valid symbols form a fixed, ordered set.**

Once you realize this, the problem becomes:

* Repeatedly subtract the **largest valid Roman value ≤ current number**
* Append its corresponding symbol
* Repeat until the number is reduced to zero

No backtracking. No DP. Just greedily consume the number.

---

### Why This Works

#### 1. Pre-encoding subtractive cases

```python
values = [1000, 900, 500, 400, 100, 90, ...]
symbols = ["M", "CM", "D", "CD", "C", "XC", ...]
```

**Aha insight:**
Roman numerals like `IV`, `IX`, `XL`, `CM` are **special cases**, not rules you derive dynamically.

By explicitly listing them:

* You avoid conditional logic
* You guarantee correctness
* The greedy choice is always safe

---

#### 2. Always take the largest possible value

```python
while values[i] > num:
    i += 1
num -= values[i]
res += symbols[i]
```

At each step:

* You choose the largest symbol that fits
* This choice is **locally optimal and globally correct**

There’s no scenario where taking a smaller symbol first leads to a better or more valid Roman numeral.

---

#### 3. Deterministic and bounded

* The values list is fixed (13 elements)
* The loop runs a small, predictable number of times
* This is effectively **O(1)** in practice

---

### Mental Model

Think of making change with special coins:

* Roman symbols are coins
* You always give the biggest coin you can
* Some coins are “special” (like 900 = `CM`)
* Repeat until change is exact

---

### Efficiency

* **Time Complexity:** `O(1)` (bounded by fixed Roman symbols)
* **Space Complexity:** `O(1)`

---

### Summary

**Pattern:**

> Greedy Algorithm with Predefined Mapping

**Aha Moment:**

> Once you treat Roman numerals as a fixed descending set of values (including subtractive cases), you can greedily subtract and append symbols without ever reconsidering a choice.

That insight turns what feels like a rule-heavy problem into a clean, elegant loop.
