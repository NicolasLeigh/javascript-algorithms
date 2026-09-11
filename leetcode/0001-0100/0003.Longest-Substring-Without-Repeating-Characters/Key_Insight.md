### Core Algorithmic Pattern:

The core algorithmic pattern used in this solution is **Sliding Window** with a **Hash Set (or Bit Set) for Tracking Characters**.

### Key Insight (The "Aha!" Moment):

The key insight is using the **sliding window technique** combined with a **bitset (or hash set)** to efficiently track characters in the current window without needing to revisit characters. The sliding window ensures that we are examining each character only once, and the bitset ensures that we can quickly check if a character has already been seen in the current window.

* **Sliding Window**: The sliding window technique allows us to examine substrings without repeatedly checking every possible substring. We maintain two pointers, `l` and `r`, which represent the left and right bounds of the current substring. As we move the `r` pointer to the right, we extend the window, and as soon as we encounter a duplicate character, we move the `l` pointer to shrink the window until the duplicate is removed.

* **Efficient Character Tracking**: The `bitSet` array acts as a simple way to track whether a character has appeared in the current window. By using the ASCII value of characters (via `ord(s[r])`), we can directly mark a position in the array to indicate whether the character is currently in the window. This allows us to check for duplicates in constant time.

### Explanation:

* **Sliding Window**: The right pointer (`r`) is used to expand the window. If a character is already in the window (as tracked by `bitSet`), we move the left pointer (`l`) forward to shrink the window, effectively removing the duplicate.
* **Bitset Tracking**: The bitset (`bitSet[ord(s[r])]`) is used to track the presence of characters in the current window. If `bitSet[ord(s[r])]` is `True`, it means that the character `s[r]` has been seen before in the current window, so we need to move `l` to the right until the duplicate is removed.
* **Window Calculation**: Each time we move `r` and add a character to the window, we calculate the size of the current window (`r - l`) and update `res` if it's the longest substring found so far.
* **Early Exit Condition**: The `if r >= len(s): break` condition ensures that the loop terminates once we have scanned the entire string.

### Why Efficient:

* **Time Complexity**: The algorithm runs in (O(n)), where (n) is the length of the string. This is because each character is processed at most twice—once when `r` moves to the right and once when `l` moves to the right to remove duplicates.

* **Constant Time Operations**: Both the `bitSet` array lookup and the operations to move `l` and `r` are constant time (O(1)), so the time complexity is dominated by the linear scan of the string.

* **Space Complexity**: The space complexity is (O(1)) in terms of input size because the bitset only stores information for a fixed number of characters (128 for ASCII characters), which is constant. This ensures the solution is space-efficient.

This combination of the sliding window with a bitset makes this solution both time-efficient and space-efficient for the problem.
