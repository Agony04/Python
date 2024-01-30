class polygon:
    def __init__(self,no_of_sides):
        self.n=no_of_sides
        self.sides=[0 for i in range(no_of_sides)]
    def inputsides(self):
        self.sides=[float(input("enter side"+str(i+1)+":"))
        for i in range (self.n)]
    def dispsides(self):
        for i in range(self.n):
            print("Side:",i+1,self.sides[i])


class triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
    def findarea(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))*0.5
        print("the area of triangle is %0.2f " %area)
        t=triangel()
        t.inputsides()
        t.dispsides()
        t.findarea()
