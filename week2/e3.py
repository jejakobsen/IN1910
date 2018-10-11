# Exercise 3 a) 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1    
    else:
        return fibonacci(n-1)+fibonacci(n-2)    

for i in range(10): 
    print(fibonacci(i))
     
#b) 

class Fibonacci:
    def __init__(self):
        self.memory = {0: 1, 1: 1}
        
    def __call__(self, n):
        memory = self.memory
        for i in range(n):
            if i in memory:
                print(memory[i])
            if i not in memory:
                elem = memory[i-1] + memory[i-2]
                memory.update({i:elem})
                print(memory[i])
        pass      

# c) + d)
fib = Fibonacci()
print(fib(1000))   
# e)
class Factorial:
    def __init__(self):
        self.memory = {0: 1}
        
    def __call__(self, n):
        memory = self.memory
        for i in range(n):
            if i in memory:
                print(memory[i])
            if i not in memory:
                elem = i*memory[i-1]
                memory.update({i:elem})
                print(memory[i])
        pass    

fact = Factorial()        
print(fact(100))