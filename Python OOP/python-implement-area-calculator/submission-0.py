import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, x, y=0):
        if y != 0:
            return x*y
        else:
            return round(math.pi * x**2,2)

    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
