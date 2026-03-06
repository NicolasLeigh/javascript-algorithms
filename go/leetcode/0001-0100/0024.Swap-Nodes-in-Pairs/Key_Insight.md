### Core Algorithmic Pattern

**Iterative Linked List Manipulation with a Dummy (Sentinel) Node**

This solution uses **pointer re-wiring in a singly linked list**, driven by an **iterative two-node window**, with a **dummy head** to unify edge cases.

---

### The “Aha!” Moment 🧠

The key insight is:

> **Don’t try to swap nodes by value or handle the head separately.
> Introduce a dummy node so *every* pair looks the same, including the first one.**

Once you realize that swapping a pair only requires changing **three `next` pointers**, the problem becomes mechanical and safe.

---

### Why This Works Efficiently

#### 1. Dummy node eliminates special cases

```python
dummyHead = ListNode(0)
dummyHead.next = head
cur = dummyHead
```

**Aha insight:**
Without a dummy node, swapping the first pair would require extra logic to update `head`.
With a dummy node, the pointer **before every pair always exists**.

---

#### 2. Fixed two-node sliding window

```python
while cur.next and cur.next.next:
```

* `cur.next` → first node of the pair (`t1`)
* `cur.next.next` → second node of the pair (`t2`)

This acts like a **window of size 2** over the linked list.

---

#### 3. Swapping nodes via pointer re-wiring

```python
t1 = cur.next
t2 = cur.next.next

cur.next = t2
t1.next = t2.next
t2.next = t1
```

Visually:

```
cur → t1 → t2 → next
```

After swap:

```
cur → t2 → t1 → next
```

**Aha insight:**
You’re not swapping values—just redirecting pointers.
Exactly **three assignments** complete the swap.

---

#### 4. Advance to the next pair

```python
cur = cur.next.next
```

After swapping, `cur.next` is `t2`, and `cur.next.next` is `t1`, so moving two steps lands you right before the next pair.

---

### Efficiency

* **Time Complexity:** `O(n)` — each node visited once
* **Space Complexity:** `O(1)` — in-place pointer manipulation

---

### Summary

**Pattern:**

> Iterative linked list pointer manipulation + dummy (sentinel) node

**Aha Moment:**

> Add a dummy node so every swap is identical, then swap pairs by rewiring three pointers—no value swapping, no edge cases.

This is a classic linked-list trick that shows up again and again in interview problems.
