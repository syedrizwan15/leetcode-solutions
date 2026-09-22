class Solution {
    public int maxSubArray(int[] nums) {
        
       int max=Integer.MIN_VALUE;
       int cur=0;
       int i=0;
       while(i<nums.length){
           cur+=nums[i];    
           max=Math.max(cur,max);
           if(cur<0)cur=0;
           i++;
       }
       return max;

    }
}
    
