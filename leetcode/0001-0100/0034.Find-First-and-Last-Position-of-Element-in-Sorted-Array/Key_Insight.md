### Core Algorithmic Pattern:

The core algorithmic pattern used in this solution is **Binary Search**.

### Key Insight (The "Aha!" Moment):

The key insight is that we can leverage binary search to find both the **first occurrence** and the **last occurrence** of a target element in a **sorted array**. Rather than performing a linear scan for both operations, which would take (O(n)) time, binary search allows us to find these positions in **logarithmic time** ((O(\log n))) by carefully adjusting the search conditions.

* **Binary Search for First Occurrence**: When a match is found, instead of returning the index immediately, we continue searching in the left half of the array to check if there are earlier occurrences of the target.

* **Binary Search for Last Occurrence**: When a match is found, we continue searching in the right half of the array to check if there are later occurrences of the target.

### Explanation:

* **Finding the First Occurrence**: In the `searchFirstEqualElement` function, the key is to adjust the search bounds after finding a match. If the current element equals the target, we check if it is the first occurrence by ensuring either it is at the start of the array or the previous element is not the same. If not, we continue searching in the left half (`high = mid - 1`).

* **Finding the Last Occurrence**: Similarly, in the `searchLastEqualElement` function, after finding a match, we check if it is the last occurrence by ensuring either it is at the end of the array or the next element is not the same. If not, we continue searching in the right half (`low = mid + 1`).

* **Efficient Search**: By using binary search, we reduce the time complexity of each search to (O(\log n)) rather than (O(n)), making this approach very efficient for large sorted arrays.

### Why Efficient:

* **Time Complexity**: Each search (for the first and last occurrences) runs in (O(\log n)), where (n) is the length of the array. Thus, the total time complexity for finding both occurrences is (O(\log n)), which is significantly more efficient than the naive linear scan approach.

* **Space Complexity**: The space complexity is (O(1)), as we are only using a few variables (`low`, `high`, `mid`) and not using any extra space proportional to the size of the input array.

This solution is efficient because it avoids the need for a linear scan and leverages the sorted nature of the array to perform logarithmic searches. By separately handling the first and last occurrences with binary search, we ensure that the solution works in optimal time.
