def area():
    print("the area of square")
    area(side1)
def area(side1):
    area = side1 * side1
    print("the area of the square is :",area)
    area(l,b)
def area(l,b):
    area = l*b
    print("the area of a rectangle is :",area)
class area:
    def area(self):
        print("the area of square")
    def area(self,side):
        area = side * side
        print("the area of the square is :",area)
    def area(self,l,b):
        area = l*b
        print("the area of a rectangle is :",area)
a=area()
l=int(input("enter length :"))
b=int(input("enter breadth: "))
side1 = int(input("Enter side value : "))
a.area(side1,side1)
a.area(l,b)




