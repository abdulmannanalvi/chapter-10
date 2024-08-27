class Calculator:
    def __init__(self, num):
        self.num =num
        print(num)

    def sqr(self):
        print(f"The No of Square is: {self.num*self.num}")
    
    def cube(self):
        print(f"The No of Cube is: {self.num*self.num*self.num}")
    
    def sqr_root(self):
        print(f"The No of Cube is: {self.num**1/2}")

No=Calculator(5)
No.sqr()
No.cube()
No.sqr_root()