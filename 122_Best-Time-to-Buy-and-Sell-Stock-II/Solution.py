# -*-coding:utf-8-*-
# 122. 买卖股票的最佳时机 II


class Solution:
    def maxProfit1(self, prices):
        """
        :des: 贪心算法（Greedy）,遍历每一天的价格，默认当天买入，
              如果第二天价格低于当天则当天卖出(也相当于不买入)；
              如果第二天价格大于当天则第二天卖出，锁定收益（相当于今天买入明天卖出）。
              这种贪心算法的适用性比较少，也就类似的问题吧。
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for i in range(len(prices)-1):  # 必须减1，不然就会越界的。
            if prices[i] < prices[i+1]:
                maxProfit += prices[i+1]-prices[i]
        return maxProfit

    def maxProfit2(self, prices):
        """
        :des: DFS 深度优先遍历·
        :type prices: List[int]
        :rtype: int
        """
        pass

    def maxProfit3(self, prices):
        '''
        @description: 动态规划,dymaic planing：
        @param {type} 
        @return: 
        '''
        hold = float('-inf')  # 买入后收益剩余
        profit = 0  # 可用现金流，总收益
        for p in prices: 
            hold = max(hold, profit-p)  # 比较当前持有和继续买入那个收益大
            profit = max(profit, hold+p) # 比较现有收益和卖出收益那个大，锁定最大收益
        return profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    s = Solution()
    print(s.maxProfit3(prices))
