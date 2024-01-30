class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return"({0},{1})".format(self.x,self.y)
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)
p1=Point(1,2)
p2=Point(3,4)
print(p1+p2)

#x+y __add__ -> x.__add__(y)
#x-y __sub__ -> x.__sub__(y)
#x*y __mul__ -> x.__mul__(y)
#x**y __pow__ -> x.__pow__(y)
#x/y __turediv -> x.__turediv__(y)
#x//y __floordiv__ ->x.__floordiv__(y)
#__mod__
#less than __lt__ 
#less or equal __le__ 
#equal __eq__ 
#not equal __ne__
