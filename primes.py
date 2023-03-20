class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


def count_primes(head: ListNode) -> int:
  count = 0
  current = head
  while current:
    if is_prime(current.val):
      count += 1
    current = current.next
  return count


# Example usage
head = ListNode(
  1,
  ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))

num_primes = count_primes(head)

print(f"There are {num_primes} prime numbers in the linked list.")
