### Core Algorithmic Pattern

**Two Pointers (Slow–Fast Pointer Technique) + In-Place Array Modification**

This solution uses the classic **slow–fast pointer** pattern to process a **sorted array** in one pass while modifying it in place.

---

### The “Aha!” Moment 🧠

The key insight is:

> **Because the array is already sorted, all duplicates appear next to each other.
> You don’t need extra space—just overwrite duplicates as you go.**

Once you realize you only care about the **next unique value**, the problem becomes a simple pointer dance.

---

### How the Pattern Works

#### Pointer roles

* **`i` (slow pointer)**
  Tracks the **last position of a unique element**.
* **`j` (fast pointer)**
  Scans the array looking for **new unique values**.

```python
i = 0
for j in range(1, len(nums)):
```

---

#### Detecting a new unique element

```python
if nums[j] != nums[i]:
```

Because the array is sorted:

* `nums[j] == nums[i]` → duplicate → ignore
* `nums[j] != nums[i]` → new unique number found

---

#### Overwriting in place

```python
i += 1
nums[i] = nums[j]
```

**Aha insight:**
You’re not “removing” elements—
you’re **compacting all unique values toward the front** of the array.

The rest of the array doesn’t matter after that.

---

#### Final result

```python
return i + 1
```

* `i` ends at the index of the **last unique element**
* Length of unique portion = `i + 1`

---

### Why This Is Efficient

* **Single pass:** `O(n)`
* **No extra space:** `O(1)`
* **In-place modification:** exactly what the problem requires

---

### Mental Model (Easy to Remember)

> “`j` explores, `i` commits.”

* `j` finds new values
* `i` marks where the next unique value should go

---

### Summary

**Pattern:**

> Two Pointers (Slow–Fast) on a sorted array

**Aha Moment:**

> Sorting guarantees duplicates are adjacent, so you can overwrite them in place instead of deleting anything.

This pattern is foundational and reappears in problems like **Remove Element**, **Move Zeroes**, and **Deduplicate arrays**.
