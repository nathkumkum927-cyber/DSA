class Solution(object):
    def maxArea(self, height):
      max_area = 0
      for i in range(len(height)):
          for j in range(i+1,len(height)):
              h = min(height[i],height[j])
              w = j-i
              area = h*w
              max_area = max(max_area, area)

      return max_area