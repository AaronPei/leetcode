# -*-coding:utf-8-*-
# 50.实现 pow(x, n) ，即计算 x 的 n 次幂函数。-100<n<100
# 采用分支思想来解决,即：先求2个x的n/2次方相乘，再分解成4个n/4相乘，如此类推直到x的1次方和0次方


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2:
            # 如果n为基数，那么将n-1
            return x*self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

    def myPow2(self, x, n):
        """
        :desc: 位运算解决，非递归形式
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        pow = 1
        while n:
            if n & 1:
                # 与运算符，相当于判断n是否等于1
                pow *= x
            x *= x
            n >>= 1 # n除以2
        return pow


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(10, 2))
