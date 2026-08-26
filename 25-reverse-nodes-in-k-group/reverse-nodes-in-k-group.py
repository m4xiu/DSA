class Solution:
  def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
    if not head:
      return None

    tail = head

    for _ in range(k):
      if not tail:
        return head
      tail = tail.next

    newHead = self._reverse(head, tail)
    head.next = self.reverseKGroup(tail, k)
    return newHead

  def _reverse(
      self,
      head: ListNode | None,
      tail: ListNode | None,
  ) -> ListNode | None:
    prev = None
    curr = head
    while curr != tail:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    return prev