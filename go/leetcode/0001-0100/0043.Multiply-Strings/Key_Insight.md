This is one of those problems that feels like it should be simple until you realize you can't just cast the strings to integers. The solution mimics the "long multiplication" we all learned in elementary school, but with a clever twist to handle the carries and positions programmatically.

---

### 1. The Core Algorithmic Pattern: **Elementary Manual Multiplication**

This pattern is essentially **Digit-by-Digit Simulation**. Instead of trying to multiply the whole numbers, we break the problem down into the smallest possible units (single-digit multiplications) and manage their placement in a pre-allocated result array.

### 2. The "Aha!" Moment: **The Index Mapping**

The real "Aha!" moment is the realization that the product of two digits at indices $i$ and $j$ (from `num1` and `num2` respectively) will **always** contribute to the positions $i+j$ and $i+j+1$ in the final result array.

Normally, when we do manual multiplication, we write out several intermediate rows, shift them with zeros, and then sum them up at the very end. This code skips all those intermediate steps by updating a single `result` array in real-time.

**Why this works:**

* **Space Efficiency:** By knowing that a number of length $M$ multiplied by a number of length $N$ will result in a product no longer than $M+N$, we can pre-allocate an array of that size.
* **Immediate Carry Management:** Instead of waiting until the end to handle carries, the code handles them locally.
* The product of `num1[i]` and `num2[j]` is added to `result[i + j + 1]`.
* Any overflow (the carry) is immediately added to the "tens" place at `result[i + j]`.



> **The Insight:** By iterating from right to left (end of the strings to the beginning) and using the $i+j$ / $i+j+1$ relationship, we eliminate the need for complex "shifting" logic or massive intermediate string storage.

---

### Efficiency Breakdown

* **Time Complexity:** $O(M \cdot N)$, where $M$ and $N$ are the lengths of the strings. We must visit every pair of digits once.
* **Space Complexity:** $O(M + N)$ to store the result array.
