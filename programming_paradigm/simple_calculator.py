class SimpleCalculator:
    """A simple claculator class that supports basic arithmetic operations"""
    
    def add(self, a, b):
        #Return the addition of a and b.
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        #Return division of a by b and Returns None if b is zero
        if b == 0:
            return None
        return a / b 