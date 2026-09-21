#  Based on https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit_buy_day = dict()
        max_profit_sell_day = dict()

        def compute_future_profit_considering_buy_on_day(day):
            if day >= n:
                return 0  # no future profit possible since last day is n-1

            if day in max_profit_buy_day:
                return max_profit_buy_day[day]

            # Consider two cases:
            #   1) buy today (and pay price) and then sell in the future
            #   2) don't buy today but consider buying starting tomorrow
            highest_profit_if_buy_today = compute_future_profit_considering_sell_on_day(day+1) - prices[day]
            highest_profit_if_nobuy_today = compute_future_profit_considering_buy_on_day(day+1)
            result = max(highest_profit_if_buy_today, highest_profit_if_nobuy_today)
            max_profit_buy_day[day] = result
            return result

        def compute_future_profit_considering_sell_on_day(day):
            if day == n:
                return 0  # no future profit possible since last day is n

            if day in max_profit_sell_day:
                return max_profit_sell_day[day]

            # Consider two cases:
            #   1) sell today (and receive price) and buy after cooldown
            #   2) don't sell today but consider selling starting tomorrow
            highest_profit_if_sell_today = prices[day] + compute_future_profit_considering_buy_on_day(day+2)
            highest_profit_if_nosell_today = compute_future_profit_considering_sell_on_day(day+1)
            result = max(highest_profit_if_sell_today, highest_profit_if_nosell_today)
            max_profit_sell_day[day] = result
            return result

        # Compute result by considering buying on day 0 (cannot consider selling at day 0).
        return compute_future_profit_considering_buy_on_day(0)


if __name__ == '__main__':
    sol = Solution()
    series = [1, 2, 3, 0, 2]
    print(sol.maxProfit(series))
