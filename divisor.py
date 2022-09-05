class divisor:
    
       
    def __init__(self,input):
        self.input=input
        self.output=[]
        self.sum=0
        for x in range(1,input+1):
          
                if input%x==0:
                    self.output.append(x)
                    self.sum=self.sum+input
                    
try:                  
   input=int(input("enter a number:")) 
         
except ValueError:
         print("invalid input")  
except Exception:
         print("something went wrong")               
obj=divisor(input)
         

if input>1:
 print(obj.output)
 print("The sum of the output is",obj.sum)
 
else:
    print("input number should be greater than 1")