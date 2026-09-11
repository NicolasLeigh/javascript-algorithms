### Core Algorithmic Pattern

**Two Pointers / Symmetric Comparison**

This solution uses the **two-pointer pattern**, applied to a string representation of the number. One pointer starts from the **left**, the other from the **right**, and they move inward comparing mirrored characters.

---

### The “Aha!” Moment 🧠

The key insight is:

> **A number is a palindrome if and only if its left half mirrors its right half.**

Instead of reversing the number or dealing with tricky math edge cases, converting the integer to a string lets you directly compare symmetric positions with minimal logic.

---

### Why This Solution Is Efficient

#### 1. Early elimination of impossible cases

```python
if x < 0:
    return False
```

Negative numbers can never be palindromes because of the `-` sign—this instantly removes half the search space.

```python
if x < 10:
    return True
```

Single-digit numbers are always palindromes—another fast exit.

---

#### 2. Symmetry check instead of full reversal

```python
for i in range(length // 2 + 1):
    if s[i] != s[length - 1 - i]:
        return False
```

**Aha insight:**
You only need to check **half** the digits.

* First digit ↔ last digit
* Second ↔ second-last
* … and so on

The moment one pair doesn’t match, you can stop immediately.

---

#### 3. Early termination saves work

As soon as a mismatch is found, the function returns `False`. There’s no need to process the rest of the digits.

---

### Mental Model

Think of folding the number in half:

```
12321
^   ^
```

If every mirrored pair matches, it’s a palindrome.

---

### Efficiency

* **Time Complexity:** `O(n)` where `n` is the number of digits
  (Only half the digits are compared, but asymptotically still linear)
* **Space Complexity:** `O(n)` due to string conversion

---

### Summary

**Pattern:**

> Two Pointers (symmetric comparison)

**Aha Moment:**

> You don’t need to reverse the number—just compare mirrored digits from the outside in, and stop early on mismatch.

This keeps the solution clean, readable, and efficient.
