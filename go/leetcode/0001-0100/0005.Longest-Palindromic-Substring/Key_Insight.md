### Core Algorithmic Pattern:

The core algorithmic pattern used in this solution is **Expand Around Center**.

### Key Insight (The "Aha!" Moment):

The key insight is recognizing that **every palindrome has a center**, and the longest palindrome can be found by expanding outwards from this center. There are two types of centers for palindromes:

1. **Odd-length palindromes** have a single center character.
2. **Even-length palindromes** have a center between two characters.

By iterating through each possible center and expanding outwards, we can efficiently find the longest palindrome.

### Explanation:

* **Expand Around Center**: The idea is to treat each character (and each pair of adjacent characters) as a potential center of a palindrome. For each potential center, we expand outwards (by decrementing `left` and incrementing `right`) as long as the characters on both sides match. This gives the largest palindrome that can be formed with the current center.

  * For each index `i`, we consider two cases:

    * **Odd-length palindromes**: The center is `s[i]`, so we expand with `left = right = i`.
    * **Even-length palindromes**: The center is between `s[i]` and `s[i + 1]`, so we expand with `left = i` and `right = i + 1`.

* **Updating the Result**: Each time a palindrome is found, we compare its length to the current longest palindrome (`res`). If the new palindrome is longer, we update `res` with the new palindrome.

* **Efficient Comparison**: By expanding from the center, we avoid the need for checking all possible substrings (which would require (O(n^2)) time). Instead, the palindrome is found in a linear scan, and the center is expanded in (O(n)) time for each index, resulting in an overall time complexity of (O(n^2)) for the worst case (which is still more efficient than brute force substring checking).

### Why Efficient:

* **Time Complexity**: The time complexity is (O(n^2)), where (n) is the length of the string. For each index, we expand outwards in both directions (which is linear), and we do this for each index. Although this is quadratic in nature, it is much more efficient than trying to generate all substrings and check each one.

* **Space Complexity**: The space complexity is (O(1)), apart from the space needed for the output string, because we only need a few variables to track the left and right indices and the longest palindrome found so far.

This solution is efficient and easy to understand because it avoids the complexity of dynamic programming or brute force while leveraging the center-expansion method, which directly finds palindromes by expanding outward from potential centers.
