### Core Algorithmic Pattern

**Single Pass / Greedy with Reverse Traversal**

This solution uses a **greedy accumulation strategy** combined with a **right-to-left scan**. It’s essentially linear parsing with a very clever direction choice.

---

### The “Aha!” Moment 🧠

The key insight is:

> **Roman numerals only subtract when a smaller value appears *before* a larger one.**

By scanning the string **from right to left**, that rule becomes incredibly simple to implement.

---

### Why Scanning Backwards Is the Trick

Roman numeral rules:

* Normally, values are added: `VI = 5 + 1`
* Subtraction only happens in cases like `IV`, `IX`, `XL`, etc.

When scanning **left → right**, you need to look *ahead* to detect subtraction.

But when scanning **right → left**:

* You already know the value of the symbol to the right
* So subtraction becomes a simple comparison

```python
if num < last_num:
    total -= num
else:
    total += num
```

That’s the entire rule.

---

### Why This Is Efficient

#### 1. No special cases needed

You don’t need to explicitly check:

* `IV`, `IX`, `XL`, `CM`, etc.

The comparison with `last_num` handles *all* subtractive cases naturally.

---

#### 2. One pass, constant state

* One loop
* Two integers (`total`, `last_num`)
* No extra data structures

This keeps the solution clean and fast.

---

#### 3. Greedy accumulation works safely

At each step, you make a local decision:

* Add if current ≥ last
* Subtract if current < last

This greedy choice is always correct because Roman numerals are **locally determined** by adjacent symbols.

---

### Mental Model

Think of reading Roman numerals as:

> “Does this symbol weaken or strengthen the number to its right?”

* If weaker → subtract
* If stronger or equal → add

Scanning from right to left makes that question trivial.

---

### Efficiency

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

### Summary

**Pattern:**

> Greedy parsing with reverse traversal

**Aha Moment:**

> By reading the Roman numeral from right to left, subtraction reduces to a simple comparison with the previous value—no special rules required.

This insight turns a rule-heavy problem into one of the cleanest parsing solutions on LeetCode.
