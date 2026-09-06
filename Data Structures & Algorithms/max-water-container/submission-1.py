class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0

        while l < r:
            h1 = heights[l]
            h2 = heights[r]
            height = min(h1, h2)
            width = r - l
            if area < width * height:
                area = width * height
            if h1 > h2:
                r -= 1
            else:
                l += 1
        
        return area