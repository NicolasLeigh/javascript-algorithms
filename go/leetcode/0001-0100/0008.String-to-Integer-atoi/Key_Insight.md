### Core Algorithmic Pattern

**Single Pass / Finite-State Parsing (Greedy String Parsing)**

This solution follows a **linear scan with state transitions**, which is a classic pattern for parsing problems. You can think of it as a **very small state machine**:

1. Skipping whitespace
2. Reading an optional sign
3. Consuming digits
4. Stopping at the first invalid character

No backtracking, no extra data structures—just one pass.

---

### The “Aha!” Moment 🧠

The key insight is realizing that **you don’t need to parse the entire string or validate everything upfront**. Instead:

> **Process characters one by one, and stop the moment the rules say you should.**

This dramatically simplifies the problem.

---

### Why This Works So Well

#### 1. Build the number incrementally (like manual math)

```python
result = result * 10 + digit
```

This mirrors how humans construct numbers digit by digit. It avoids converting substrings or using expensive operations.

---

#### 2. Overflow is handled *during* construction

This is the real power move 👇

```python
if sign == 1 and result > 2**31 - 1:
    return 2**31 - 1
if sign == -1 and result > 2**31:
    return -2**31
```

**Aha insight:**
You don’t wait until the end to check overflow.
You **clamp early** as soon as it happens.

Why this matters:

* Prevents integer overflow
* Avoids unnecessary work
* Keeps logic clean and safe

---

#### 3. Early termination is intentional

```python
while i < n and '0' <= s[i] <= '9':
```

The moment a non-digit appears, parsing stops—exactly as the problem requires. No need to validate the rest of the string.

---

### Mental Model

Think of this as a **controlled scanner**:

* Consume only what’s allowed
* Maintain minimal state (`sign`, `result`)
* Stop immediately when rules are violated
* Clamp instead of erroring on overflow

---

### Efficiency

* **Time Complexity:** `O(n)` — one pass through the string
* **Space Complexity:** `O(1)` — constant extra space

---

### Summary

**Pattern:**

> Single-pass greedy parsing / finite-state parsing

**Aha Moment:**

> Build the integer digit-by-digit, apply sign once, and clamp overflow *while parsing*—not after.

That insight turns a messy edge-case-heavy problem into a clean, predictable solution.
