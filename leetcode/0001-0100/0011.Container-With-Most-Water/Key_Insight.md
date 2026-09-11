### Core Algorithmic Pattern

**Two Pointers (Greedy Optimization)**

This solution uses the **two-pointer technique**, combined with a **greedy decision rule** to shrink the search space efficiently.

---

### The “Aha!” Moment 🧠

The key insight is this:

> **The area is limited by the shorter line — moving the taller line can never increase the area.**

That realization is what unlocks the linear-time solution.

---

### Why This Insight Changes Everything

The container area is:

```
area = width × min(height[left], height[right])
```

So at any step:

* The **width** shrinks when pointers move inward
* To compensate, the **height must increase**
* But the height is controlled by the **shorter wall**

👉 **Moving the taller wall does nothing** because:

* Width decreases
* Minimum height stays the same or decreases
* Area cannot improve

---

### Greedy Pointer Movement (The Core Trick)

```python
if height[start] < height[end]:
    start += 1
else:
    end -= 1
```

**Aha insight:**
Always move the pointer pointing to the **shorter line**, because:

* It’s the *only* move that might increase the limiting height
* All other moves are guaranteed to be worse

This greedy choice safely eliminates huge portions of the search space.

---

### Why This Is Efficient

#### 1. Linear scan instead of quadratic

* Brute force checks all pairs → **O(n²)**
* Two pointers eliminate one index each step → **O(n)**

#### 2. No missed optimal solution

* The greedy rule is mathematically sound
* Any container using the shorter wall cannot do better unless that wall is replaced

---

### Mental Model

Imagine squeezing the container inward:

* If one side is short, it’s the bottleneck
* You must try to find a taller wall on that side
* Shrinking from the taller side is pointless

---

### Efficiency

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

### Summary

**Pattern:**

> Two Pointers + Greedy Optimization

**Aha Moment:**

> Since area is limited by the shorter wall, only moving the shorter pointer can possibly improve the result.

This single insight turns an obvious brute-force problem into one of the cleanest and most elegant `O(n)` solutions on LeetCode.
