### Core Algorithmic Pattern

**Sorting + Two Pointers (Generalized K-Sum Pattern)**

This solution is the natural extension of **3Sum** to **4Sum**. It uses:

* **Sorting** to impose order
* **Nested fixing of elements**
* **Two pointers** to efficiently search the remaining space

This is the canonical **K-Sum reduction pattern**.

---

### The “Aha!” Moment 🧠

The key insight is:

> **After sorting, fixing `k-2` numbers reduces K-Sum to a 2-Sum problem solvable with two pointers.**

For 4Sum:

* Fix 2 numbers (`i`, `j`)
* Solve the remaining 2Sum using `left` and `right`

That insight collapses a brute-force `O(n⁴)` problem into `O(n³)`.

---

### Why This Works

#### 1. Sorting enables structure and pruning

```python
nums.sort()
```

After sorting:

* Pointer movement is meaningful
* Duplicate handling is easy
* The sum changes monotonically with pointer movement

Sorting is what makes the greedy pointer logic correct.

---

#### 2. Fix two numbers, search the rest

```python
for i in range(n - 3):
    for j in range(i + 1, n - 2):
```

At this point, the problem becomes:

```text
nums[left] + nums[right] = target - nums[i] - nums[j]
```

Which is exactly **2Sum on a sorted array**.

---

#### 3. Deterministic pointer movement

```python
if total < target:
    left += 1
else:
    right -= 1
```

**Aha insight:**
Because the array is sorted:

* Moving `left` increases the sum
* Moving `right` decreases the sum

Every move strictly shrinks the search space—no backtracking.

---

#### 4. Duplicate skipping avoids redundant work

```python
if nums[i] == nums[i - 1]: continue
if nums[j] == nums[j - 1]: continue
```

And after finding a valid quadruplet:

```python
while nums[left] == nums[left + 1]: left += 1
while nums[right] == nums[right - 1]: right -= 1
```

This guarantees:

* No duplicate results
* No repeated exploration of the same values

---

### Mental Model

Think of this as:

1. Sort the array
2. Lock two positions
3. Slide two pointers to balance the remaining sum
4. Skip everything you’ve already seen

This is **3Sum with one extra fixed layer**.

---

### Efficiency

* **Time Complexity:** `O(n³)`

  * Sorting: `O(n log n)`
  * Triple nested scan
* **Space Complexity:** `O(1)` (excluding output)

---

### Summary

**Pattern:**

> Sorting + Two Pointers (K-Sum Reduction)

**Aha Moment:**

> Sorting lets you reduce 4Sum into repeated 2Sum searches by fixing values and greedily shrinking the search space with pointers.

This insight scales cleanly to **K-Sum** problems and is one of the most important patterns in array algorithm interviews.
