class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        all_trnsactions = []
        last_sell = 0
        maximum_index = len(prices)
        for i, p in enumerate(prices):
            sell = [0]
            buy = p
            for j in range(i+1, len(prices)):
                if p >= prices[j]:
                    continue
                else:
                    sell.append(prices[j])
            all_trnsactions.append(max(sell) - buy)
            # print((buy, sell[-1], all_trnsactions))

        last_sell = max(all_trnsactions)
        return last_sell if last_sell > 0 else 0