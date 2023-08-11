class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        comb = [0] * (amount+1)
        comb[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                comb[i] += comb[i - coin]
        return comb[amount]