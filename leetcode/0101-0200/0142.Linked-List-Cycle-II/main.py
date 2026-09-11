class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # 第一阶段：判断是否存在环
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                # 第二阶段：寻找环的入口
                entry = head

                while entry is not slow:
                    entry = entry.next
                    slow = slow.next

                return entry

        # 不存在环
        return None