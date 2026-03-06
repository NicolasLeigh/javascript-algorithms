### Core Algorithmic Pattern

**Modified Binary Search (Divide & Conquer)**

This problem is still binary search at heart—but with a twist to handle the rotation.

---

### The “Aha!” Moment 🧠

The key insight is:

> **Even though the array is rotated, at least one half is always sorted.**

That single observation saves the problem.

Once you realize that **either the left half or the right half must be in sorted order**, you can:

* Identify the sorted half
* Check whether the target could lie inside it
* Discard the other half—just like normal binary search

So the rotation doesn’t break binary search; it just adds one extra decision.

---

### How the Logic Flows

#### 🔍 Step 1: Standard binary search setup

```python
mid = low + (high - low) // 2
```

Avoids overflow and keeps the search `O(log n)`.

---

#### 🧭 Step 2: Identify the sorted half

```python
if nums[low] <= nums[mid]:
    # Left half is sorted
else:
    # Right half is sorted
```

Because the array was originally sorted:

* One side of `mid` must still be ordered
* The rotation point can only be on one side

💡 This is the **core trick** of the problem.

---

#### 🎯 Step 3: Decide which half to keep

If the **left half is sorted**:

```python
if nums[low] <= target < nums[mid]:
    high = mid - 1
else:
    low = mid + 1
```

If the **right half is sorted**:

```python
if nums[mid] < target <= nums[high]:
    low = mid + 1
else:
    high = mid - 1
```

💡 You’re doing a normal binary-search range check—but only on the sorted half.

---

### Why This Is Efficient

* **Time Complexity:** `O(log n)`

  * Same as classic binary search
* **Space Complexity:** `O(1)`

  * No extra data structures

You never linearly scan the array, even though it’s rotated.

---

### Mental Model (Interview-Friendly)

> **“Rotation doesn’t destroy order—it just splits it.”**

At every step:

1. One half is sorted
2. Check if the target fits there
3. Throw away the other half

---

### Summary

* **Pattern:** Modified Binary Search
* **Key Insight:**

  > In a rotated sorted array, one side of `mid` is always sorted
* **Why it works:**
  You restore binary search by reasoning about which half is ordered

This is a textbook example of *not giving up on binary search just because the array looks messy*.
