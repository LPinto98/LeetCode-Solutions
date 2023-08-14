class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickSelect(left, k):
            pvt = random.choice(left)
            L, R = [i for i in left if i < pvt], [j for j in left if j > pvt]
            if len(R) >= k:
                return quickSelect(R, k)
            elif len(left)-len(L) >= k:
                return pvt
            else:
                return quickSelect(L, k - (len(left) - len(L)))

        return quickSelect(nums, k)
