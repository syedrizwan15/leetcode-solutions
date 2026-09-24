class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d=int(''.join(map(str,digits)))

        num = d+1
        return list(map(int,str(num)))