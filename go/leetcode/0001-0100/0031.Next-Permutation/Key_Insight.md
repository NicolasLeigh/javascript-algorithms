### Core Algorithmic Pattern

**Greedy + Two Pointers (with In-Place Array Manipulation)**

This solution is a classic **greedy lexicographical algorithm**, combined with **two-pointer reversal** to finish the job efficiently and in-place.

---

### The “Aha!” Moment 🧠

The crucial insight is:

> **The next permutation is the smallest change that makes the number bigger.**

Once you see permutations as numbers in **lexicographical (dictionary) order**, the problem becomes:

1. Increase the number **as late as possible**
2. Increase it **by the smallest possible amount**

Everything in the algorithm follows directly from that idea.

---

### Step-by-Step Insight

#### 🔍 Step 1: Find the first decreasing element from the right

```python
while i >= 0 and nums[i] >= nums[i + 1]:
    i -= 1
```

* Scan from right to left
* This finds the **pivot** where we can still make the number larger
* The suffix to the right of `i` is already the **largest possible permutation**

💡 If no such `i` exists, the array is fully descending → already the largest permutation.

---

#### 🔁 Step 2: Swap with the smallest larger element

```python
while nums[j] <= nums[i]:
    j -= 1
swap(nums, i, j)
```

* Find the **smallest element greater than `nums[i]`** on the right
* This guarantees the **minimal increase**

💡 This is the greedy choice: *increase just enough, no more*.

---

#### 🔄 Step 3: Reverse the suffix

```python
reverse(nums, i + 1, end)
```

* After the swap, the suffix is still in descending order
* Reversing it makes it the **smallest possible arrangement**

💡 This ensures the final result is the **next**, not just *any larger*, permutation.

---

### Why This Is Efficient

* **Time:** `O(n)`

  * One backward scan
  * One forward scan
  * One reverse
* **Space:** `O(1)`

  * All operations are in-place

---

### Mental Model (Easy to Remember)

> **“Find where you can increase → increase minimally → reset the rest to smallest.”**

Or in one line:

> **Bump the rightmost digit you can, then clean up the tail.**

---

### Summary

* **Pattern:** Greedy + Two Pointers
* **Key Insight:**

  > Lexicographical order means *smallest possible increase at the latest position*
* **Why it works:**
  The suffix is already maximized, so reversing it guarantees the next permutation

This is one of those algorithms that feels magical—until the lexicographic insight clicks. Once it does, it’s unforgettable ✨
