class Solution:
    def fizzBuzz(self,n):
        coll = []
        for i in range(1,n+1):
            set = ""
            if i %3 == 0 and i % 5 == 0:
                set+="FizzBuzz"
            elif i %3 == 0:
                set+="Fizz"
            elif i %5 == 0:
                set+="Buzz"
            elif i %3 != 0 and i % 5 != 0:
                set+=str(i)
            coll.append(set)
        return coll 
        
