class Solution:
    def countDigits(self, num: int) -> int:
        n=num
        count =0

        while n>0:
            #Now extract digits one by one using:
            digit=n%10 
            #Check whether the digit divides the original number:
            if num % digit==0: 
                count+=1
            #Then remove the last digit:
            n=n//10
        return count

        