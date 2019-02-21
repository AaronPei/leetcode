#-*-coding:utf-8-*-
'''
@Description: 121. Best Time to Buy and Sell Stock
@Author: AaronPei
@Date: 2019-02-01 19:01:18
@LastEditTime: 2019-02-01 19:19:10
@LastEditors: Please set LastEditors
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :desc: 强制条件是只能进行一次transcation：一次买进卖出的机会获取最大收益
               已知每天只有两种状态：buy or sell
               buy的话，收益即为当天价格的负数： -prices[i]
               sell的话，收益为buy值加上当天价格：buy+prices[i]
               动态规划的思路解决：遍历每天的股票价格，比较最高的买入收益和卖出收益
               考虑初始值：第1天，数组index=0，这一天buy即为-prices[i]，sell为0（买入卖出）
               最后返回max(sell, 0)，可以考虑下如果任何交易都不做的话。
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return None
        buy, sell, len_prices = -prices[0], 0, len(prices)
        for i in range(1, len_prices):
            buy = max(buy, -prices[i])
            sell = max(sell, buy+prices[i])
        return max(sell, 0) 
