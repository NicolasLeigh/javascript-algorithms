### Core Algorithmic Pattern

**Sorting + Two Pointers (Greedy Optimization)**

This solution uses the same structural idea as **3Sum**, but with a different optimization goal. After sorting, it applies the **two-pointer technique** to efficiently search the space of possible triplets.

---

### The “Aha!” Moment 🧠

The key insight is:

> **After sorting, moving pointers deterministically moves the sum closer to the target.**

Even though we’re not looking for an exact zero, the monotonic behavior of the sum still holds—and that’s what makes this efficient.

---

### Why This Works

#### 1. Sorting creates a monotonic search space

```python
nums.sort()
```

Once sorted:

* Increasing `left` → increases the sum
* Decreasing `right` → decreases the sum

This guarantees that every pointer move is *directionally meaningful*.

---

#### 2. Fix one number, optimize the remaining two

```python
for i in range(n - 2):
```

Just like 3Sum:

* Fix `nums[i]`
* Use two pointers to find the best pair for this fixed value

This reduces a 3D search into a sequence of 1D scans.

---

#### 3. Track the best answer greedily

```python
if diff < min_diff:
    min_diff = diff
    closest_sum = total
```

**Aha insight:**
You don’t need to store all candidates.
Just keep the **closest one so far**, updating it greedily whenever you find a better match.

---

#### 4. Early exit on perfect match

```python
if total == target:
    return total
```

You can’t do better than exact—so the algorithm stops immediately.

---

### Mental Model

Think of this as:

* Slide two pointers inward
* Measure how close you are
* Remember the best result
* Move in the direction that reduces the error

It’s like **binary search intuition applied in two dimensions**.

---

### Efficiency

* **Time Complexity:** `O(n²)`

  * `O(n log n)` sorting
  * `O(n²)` pointer scanning
* **Space Complexity:** `O(1)`

---

### Summary

**Pattern:**

> Sorting + Two Pointers with Greedy Tracking

**Aha Moment:**

> Even when you’re optimizing “closeness” instead of exact equality, sorted order guarantees that pointer movements systematically reduce the error.

This insight lets you reuse the 3Sum structure and turn a brute-force search into a clean, efficient solution.
