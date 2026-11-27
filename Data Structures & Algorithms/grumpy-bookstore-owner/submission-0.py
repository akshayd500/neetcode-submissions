from typing import List


class Solution:

  def maxSatisfied(
      self, customers: List[int], grumpy: List[int], minutes: int
  ) -> int:
    base_satisfied = 0
    window_gain = 0
    max_gain = 0

    for i in range(len(customers)):
      if grumpy[i] == 0:
        base_satisfied += customers[i]
      else:
        window_gain += customers[i]

      if i >= minutes and grumpy[i - minutes] == 1:
        window_gain -= customers[i - minutes]

      if window_gain > max_gain:
        max_gain = window_gain

    return base_satisfied + max_gain
