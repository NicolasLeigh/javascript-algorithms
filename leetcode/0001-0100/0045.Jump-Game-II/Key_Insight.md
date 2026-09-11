### 1. The Core Algorithmic Pattern: **Greedy Algorithm**

The solution uses a Greedy strategy by always looking for the **farthest possible horizon** reachable from the current set of choices. Instead of calculating every possible jump sequence (which would be exponential or $O(N^2)$ with Dynamic Programming), it makes a single pass through the array.

### 2. The "Aha!" Moment: **Lazy Jumping (The "Horizon" Logic)**

The "Aha!" insight is realizing that you don't need to know *which* specific index you jumped from; you only need to know the *range* of indices reachable within $N$ jumps.

**The logic works like this:**
Imagine you are standing at index 0. Your "current jump" gives you a specific range (from `i` to `needChoose`). While you are walking through this range, you aren't jumping yet. Instead, you are "scouting" ahead to see what the farthest point (`canReach`) is that you *could* get to if you took your next jump from any of the spots in your current range.

* **Scouting:** As you move, you constantly update `canReach`.
* **Committing:** You only increment `steps` when you physically reach the end of your current range (`i == needChoose`). At that moment, you "commit" to the best jump you found during your scouting phase, and your new "horizon" becomes that `canReach` value.

> **The Insight:** You treat the problem as a series of **cascading ranges**. You only increment your jump counter when you've exhausted all possibilities within your current "tier" of reach.

---

### Why this is efficient

* **Time Complexity:** $O(N)$. We visit each element exactly once.
* **Space Complexity:** $O(1)$. We only store three variables (`steps`, `canReach`, `needChoose`) regardless of the input size.
* **No Redundancy:** Unlike BFS or DP, we don't store multiple paths or re-calculate the same jump multiple times.
