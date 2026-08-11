class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsidx={n:i for i,n in enumerate(nums1)}
        res=[-1]*len(nums1)
        stack=[]
        for i in range(len(nums2)):
            curr=nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx=numsidx[val]
                res[idx]=curr
            if curr in numsidx:
                stack.append(curr)
        return res

        