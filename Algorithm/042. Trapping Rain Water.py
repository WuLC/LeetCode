# encoding:utf-8
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0
        leftMax = []
        rightMax = {}
        # leftMax Array
        max = height[0]
        for i in range(len(height)):
            if height[i] > max :
                max = height[i]
            leftMax.append(max)

        #rightMax Array
        right = len(height)-1
        max = height[right]
        rightMax[right] = max
        while right >=0:
            right-=1;
            if height[right] > max:
                max = height[right]
            rightMax[right] = max

        sum = 0
        for i in range(1,len(height)-1):
            miniHeight = min(leftMax[i-1],rightMax[i+1])
            # 没有这个判断输入数据为[0,2,0]时会出错
            if miniHeight > height[i]:
                 sum += miniHeight-height[i]
        return sum
 

# 另外一种解法，可以不开辟rightMax数组
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0
        
        leftMax = []
        # leftMax Array
        max = height[0]
        for i in range(len(height)):
            if height[i] > max :
                max = height[i]
            leftMax.append(max)
        
        sum = 0
        rightMax = height[len(height)-1]
        for i in reversed(range(1,len(height)-1)):
            miniHeight = min(leftMax[i-1],rightMax)
            if miniHeight > height[i]:
                sum += miniHeight - height[i]

            if height[i] > rightMax:
                rightMax = height[i]
        return sum 


        
        


