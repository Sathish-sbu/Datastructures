"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.
"""

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sortedA = sorted(A)
        c = 1
        for j in range(len(sortedA)-1):
            if sortedA[j] == sortedA[j+1]:
                c += 1
                if c == len(A)/2:
                    return sortedA[j]
            else:
                c = 1
                
        return None
            
