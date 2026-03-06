The core algorithmic pattern used in this solution is **Hash Map (or Hash Table)**.

### Key Insight (The "Aha!" Moment):

The core insight here is using a hash map (dictionary in Python) to store the indices of the elements as we iterate through the list. This allows for **constant time lookups** for the difference between the target and the current number, which makes this solution more efficient than a brute force approach.

* **Efficient Lookup**: As you iterate through the array, for each number, you calculate the difference between the target and the current number (`diff = target - num`). If this difference has already been seen in the array (i.e., it exists as a key in the hash map), then you have found the two numbers that sum up to the target, and you can return their indices immediately.

* **Avoiding Nested Loops**: Instead of using nested loops to check every pair of numbers, which would take (O(n^2)) time, the hash map approach only requires one pass through the array, giving you an (O(n)) time complexity. The space complexity is (O(n)) due to the hash map storing up to (n) elements.

### Explanation:

* `map` is used to store each number's value as a key and its index as the corresponding value.
* For each element in the list, you compute the `diff` (i.e., the number needed to complement the current number to reach the target sum).
* If this `diff` is already in `map`, it means you have already encountered the other number, and the pair that sums to `target` is found.
* If `diff` isn't found in the map, the current number is added to `map`, storing its index for future reference.

This approach avoids the brute force (O(n^2)) time complexity and achieves (O(n)) time complexity with the tradeoff of (O(n)) space complexity, making it both time-efficient and easy to implement.
