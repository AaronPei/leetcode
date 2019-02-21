class Solution:
    def binarySearch(self,array,key):
        start = 0
        end = len(array)-1
        while  start < end :
            mid = (end - start)/2+start
            if array[mid] > key:
                end = mid - 1
            elif array[mid] < key:
                start = mid + 1
            else:
                return mid
        return -1
if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8]
    S = Solution()
    print(S.binarySearch(list,6))