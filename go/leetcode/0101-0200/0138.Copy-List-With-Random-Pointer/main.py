class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        original_to_clone = {}
        original_to_clone[None] = None

        # 第一次遍历：创建所有新节点
        cur = head

        while cur is not None:
            original_to_clone[cur] = Node(cur.val)
            cur = cur.next

        # 第二次遍历：复制 next 和 random
        cur = head

        while cur is not None:
            clone = original_to_clone[cur]

            clone.next = original_to_clone[cur.next]
            clone.random = original_to_clone[cur.random]

            cur = cur.next

        return original_to_clone[head]