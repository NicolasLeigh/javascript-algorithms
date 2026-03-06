### Core Algorithmic Pattern

**Two Pointers (Iterative Merge) + Dummy Node**

This solution uses the **two-pointer technique** to merge two sorted linked lists in a single pass. A **dummy node** is used to simplify pointer handling.

---

### The “Aha!” Moment 🧠

The key insight is:

> **At any point, the smallest next element must be at the head of one of the two lists.**

Because both lists are already sorted, you never need to look ahead—just compare the current heads and take the smaller one.

---

### Why This Works Efficiently

#### 1. Dummy node removes edge cases

```python
dummy = ListNode(-1)
current = dummy
```

**Aha insight:**
By starting with a dummy node:

* You don’t need special handling for the head
* The merge logic is identical for all nodes

This keeps the code clean and bug-resistant.

---

#### 2. Two pointers advance monotonically

```python
while l1 and l2:
```

Each iteration:

* Picks exactly one node
* Advances one pointer
* Never revisits nodes

No backtracking, no extra memory.

---

#### 3. Local greedy choice is always correct

```python
if l1.val < l2.val:
    current.next = l1
```

**Aha insight:**
Choosing the smaller head is a **globally optimal decision** because:

* Both lists are sorted
* Any later node is guaranteed to be ≥ the current head

---

#### 4. Append the remainder in O(1)

```python
current.next = l1 if l1 else l2
```

Once one list is exhausted:

* The rest of the other list is already sorted
* No further comparisons are needed

---

### Mental Model

This is exactly the **merge step of merge sort**, but applied to linked lists instead of arrays.

---

### Efficiency

* **Time Complexity:** `O(n + m)`
* **Space Complexity:** `O(1)`

---

### Summary

**Pattern:**

> Two Pointers + Dummy Node (Iterative Merge)

**Aha Moment:**

> Since both lists are sorted, the smallest remaining node is always at one of the two heads—just pick it and move on.

This is a foundational pattern that shows up everywhere in linked list and sorting problems.
