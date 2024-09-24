class Calculator:
    def sum(self, a,b):
        return a+b
    
    def sub(self, a,b):
        return a-b
    
    def mul(self, a,b):
        return a*b
    
    def div(self, a,b):
        if (b==0):
            raise ArithmeticError("на ноль делить нельзя")
        return a/b
    
    def pow(self, a, b=2):
        return a**b

    # pow(2,3)
    # pow(5) -> 25  

    # [1,2,3,4]
    def avg(self, nums):
        if (len(nums)==0):
            return 0
        
        s = 0
        for num in nums:
            s = self.sum(s,num)
        l = len(nums)

        return self.div(s,l)
    