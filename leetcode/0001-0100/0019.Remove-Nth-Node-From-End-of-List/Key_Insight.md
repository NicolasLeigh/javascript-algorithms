### Core Algorithmic Pattern

**Two Pointers (Fast & Slow) / One-Pass Linked List Traversal**

This solution uses the **two-pointer technique** to locate the N-th node from the end in **a single traversal** of the linked list.

---

### The “Aha!” Moment 🧠

The key insight is:

> **If two pointers are `n` nodes apart, when the faster one reaches the end, the slower one is exactly at the node *before* the target.**

That insight eliminates the need to:

* Compute the list length
* Traverse the list twice

---

### Why This Works

#### 1. Dummy node simplifies edge cases

```python
dummy = ListNode(0)
dummy.next = head
```

**Aha insight:**
Using a dummy node means:

* Removing the head node needs no special handling
* The logic works uniformly for all cases

---

#### 2. Create a fixed distance between pointers

```python
while n > 0:
    fast = fast.next
```

After this:

* `fast` is exactly `n` nodes ahead of `slow`

That distance is preserved throughout the traversal.

---

#### 3. Move both pointers together

```python
while fast.next:
    slow = slow.next
    fast = fast.next
```

When `fast` reaches the end:

* `slow` is right before the node to remove

This is the heart of the trick.

---

#### 4. Remove in constant time

```python
slow.next = slow.next.next
```

No searching. No counting. Just a pointer rewrite.

---

### Mental Model

Picture two runners on a track:

* Runner A (fast) starts `n` steps ahead
* Both run at the same speed
* When A hits the finish line, B is exactly where you need to act

---

### Efficiency

* **Time Complexity:** `O(L)` where `L` is the length of the list
* **Space Complexity:** `O(1)`

Only one pass, constant memory.

---

### Summary

**Pattern:**

> Two Pointers (Fixed Gap / Runner Technique)

**Aha Moment:**

> Maintain a fixed `n`-node gap between two pointers so that reaching the end automatically locates the node to remove.

This is one of the most elegant linked-list tricks—and a must-know interview pattern.
