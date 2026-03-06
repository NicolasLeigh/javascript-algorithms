### Core Algorithmic Pattern

**Stack (LIFO) + Greedy Matching**

This is a classic **stack-based parsing** problem where you validate properly nested structures using **Last-In–First-Out** behavior.

---

### The “Aha!” Moment 🧠

The key insight is this line of thinking:

> **Instead of pushing opening brackets, push the *expected closing bracket*.**

That single idea makes the solution:

* Simpler
* More readable
* Less error-prone

---

### Why This Works

#### 1. Push expectations, not symbols

```python
if ch == '(':
    stack.append(')')
```

**Aha insight:**
When you see `'('`, you already know what must come next eventually: `')'`.

So you push **what you expect**, not what you saw.

This avoids mapping lookups later and makes the comparison trivial.

---

#### 2. Validate immediately on closing brackets

```python
if not stack or stack.pop() != ch:
    return False
```

Two critical checks in one:

* **`not stack`** → closing bracket with no opener
* **mismatch** → wrong nesting order

This enforces **correct order**, not just matching counts.

---

#### 3. Stack must be empty at the end

```python
return len(stack) == 0
```

**Aha insight:**
If anything remains in the stack, it means:

* An opening bracket was never closed

---

### Mental Model

Think of the stack as a **contract list**:

* Each opening bracket signs a contract for a specific closing bracket
* Each closing bracket must fulfill the most recent contract
* Any violation → invalid

---

### Efficiency

* **Time Complexity:** `O(n)` — single pass through the string
* **Space Complexity:** `O(n)` — worst case all opening brackets

---

### Summary

**Pattern:**

> Stack (LIFO) for structured validation

**Aha Moment:**

> Push the *expected closing bracket* onto the stack so validation becomes a simple equality check.

This is one of the cleanest stack tricks—and once you see it, it’s hard to unsee 😄
