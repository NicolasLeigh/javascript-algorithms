### Core Algorithmic Pattern

**Two Pointers (Write Pointer / In-Place Filtering)**

This is a clean variant of the **slow–fast pointer** pattern, often described as **in-place filtering**.

---

### The “Aha!” Moment 🧠

The key realization is:

> **You don’t need to delete elements at all.
> Just overwrite the array with the elements you want to keep.**

Once you stop thinking in terms of “removal” and instead think **“copy valid elements forward”**, the solution becomes both simple and optimal.

---

### How the Pattern Works

#### Pointer roles

* **`insertPos` (slow / write pointer)**
  Indicates where the **next valid element** should be written.
* **Loop variable `num` (fast / read pointer)**
  Iterates through every element in the array.

---

#### Filtering logic

```python
if num != val:
    nums[insertPos] = num
    insertPos += 1
```

* If the element should be **kept**, write it at `insertPos`
* Move `insertPos` forward
* If the element equals `val`, **skip it** (do nothing)

💡 No shifting, no popping, no extra memory.

---

#### Final result

```python
return insertPos
```

* The **first `insertPos` elements** of `nums` contain the filtered array
* Everything after that is irrelevant

---

### Why This Is Efficient

* **Time:** `O(n)` — single pass
* **Space:** `O(1)` — in-place
* **Stable order:** relative order of kept elements is preserved

---

### Mental Model (Easy to Remember)

> “Read everything, write only what you keep.”

Or even shorter:

> **Filter in place.**

---

### Comparison with Problem #26

| Problem           | Key Difference             |
| ----------------- | -------------------------- |
| Remove Duplicates | Relies on **sorted array** |
| Remove Element    | Works on **any order**     |

But both share the same **Two Pointers / Write Pointer** core idea.

---

### Summary

**Pattern:**

> Two Pointers – In-Place Filtering

**Aha Moment:**

> Removing elements is just copying the ones you want to keep to the front.

This technique shows up everywhere—array compression, filtering, partitioning—and mastering it pays off fast 🚀
