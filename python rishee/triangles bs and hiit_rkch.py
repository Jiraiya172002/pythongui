import math
def area(a,b):
    ar=a*1/2*b
    print("The area of given triangle is===",ar)
def perimetr(a,b):
    o=math.sqrt(math.pow(a,2)+math.pow(b,2))
    p=a+b+o
    print("perimeter of the give triangle is===",p)
c=int(input("you want to give the base and height only then press_1 \n or you want to exit press_2",))
if(c==1):
      d=int(input("enter the base side of tringle"))
      e=int(input("enter the height side of tringle"))
      print("1: do you want to find the area of triangle")
      print("2:do you want to find the perimeter of triangle")
      print("3: do you want to exit")
      print("\n","=======================================================================================================================================================","\n")
      ch="y"
      while(ch=="y"):
          n=int(input("What do you want"))
          if(n==1):
              area(d,e)
          elif(n==2):
              perimetr(d,e)
          elif(n==3):
              print("Please press the above X button to exit----------")

elif(c==2):
    print("Please press the above X button to exit----------")



                  
else:
      print("Sorry....Please enter only the above no.----------???????????")
