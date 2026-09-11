### Core Algorithmic Pattern

**Sorting + Two Pointers (Search Space Reduction)**

This solution combines **sorting** with the **two-pointer technique**, wrapped in a loop. It’s a classic pattern for “k-sum” problems (especially 3Sum).

---

### The “Aha!” Moment 🧠

The key insight is:

> **Once the array is sorted, fixing one number turns 3Sum into a 2Sum problem with two pointers.**

That single realization collapses the problem from cubic to quadratic time.

---

### Why This Works

#### 1. Sorting unlocks structure

```python
nums.sort()
```

After sorting:

* Values are ordered
* Pointer movement becomes meaningful
* Duplicate handling becomes trivial

Sorting is what makes everything else possible.

---

#### 2. Fix one number, solve the rest with two pointers

```python
for i in range(n - 2):
```

You fix `nums[i]`, then search for:

```text
nums[left] + nums[right] == -nums[i]
```

This is exactly the **two-sum in a sorted array** problem.

---

#### 3. Greedy pointer movement

```python
if total < 0:
    left += 1
else:
    right -= 1
```

**Aha insight:**
Because the array is sorted:

* Moving `left` increases the sum
* Moving `right` decreases the sum

So every move is guaranteed to push the sum closer to zero—no guessing, no backtracking.

---

#### 4. Early termination is safe

```python
if nums[i] > 0:
    break
```

Once the smallest fixed number is positive:

* All remaining numbers are ≥ it
* The sum can never be zero

This cuts off unnecessary iterations.

---

#### 5. Duplicate skipping prevents redundant work

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

And after finding a valid triplet:

```python
while left < right and nums[left] == nums[left + 1]:
    left += 1
while left < right and nums[right] == nums[right - 1]:
    right -= 1
```

This ensures:

* No duplicate triplets
* No wasted pointer moves

---

### Mental Model

Think of it as:

1. Sort the array
2. Pick a fixed number
3. Shrink a window from both sides to balance the sum
4. Skip everything you’ve already seen

---

### Efficiency

* **Time Complexity:** `O(n²)`

  * `O(n log n)` for sorting
  * `O(n²)` for the two-pointer scan
* **Space Complexity:** `O(1)` (excluding output)

---

### Summary

**Pattern:**

> Sorting + Two Pointers

**Aha Moment:**

> Sorting lets you reduce 3Sum to repeated 2Sum searches, where pointer movement deterministically adjusts the sum.

This is the canonical example of how **ordering + greedy pointer movement** turns a brute-force problem into an elegant optimal solution.
