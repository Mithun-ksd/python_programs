def rec(x,y):
    area=x*y
    return area
def cir(r):
    PI=3.14
    area=PI*r**2
    return area
def sqar(a):
    area=a*a
    return area
def tri(b,h):
    area=1/2*(b*h)
    return area

i=0
while i<5:
    print("1.Find area of a Rectangle: ")
    print("2.Find area of a Circle: ")
    print("3.Find area of a Sqaure: ")
    print("4.Find area of a Triangle: ")
    print("5.Exit")
    i=int(input("Enter the choices: "))
    if(i==1):
        w=float(input("Enter width of a rectangle: "))
        h=float(input("Enter the height of rectangle: "))
        rec1=float(rec(w,h))
        print("The area of the rectangle is: ",rec1)
    elif(i==2):
        r=int(input("Enter the radius of a circle: "))
        a=cir(r)
        print("The area of the circle is: ",a)
    elif(i==3):
        a=int(input("Enter thr first sides of a square: "))
        sq=sqar(a)
        print("The area of the square is: ",sq)
    elif(i==4):
        b=int(input("Enter the base length: "))
        h=int(input("Enter the height : "))
        tr=tri(b,h)
        print("The area of the triangle is: ",tr)
    elif(i==5):
        print(exit(0))
    else:
        print("Please enter correct choice")
