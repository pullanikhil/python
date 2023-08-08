nikhil=int(input('enter the fibonaci series'))
n1,n2=0,1
count=0
if nikhil<=0:
    print('enter the +ve numbers')
elif nikhil == 1:
    print('the first fibonaci series is ',n1)
else:
    print("fibonaci series")
    while count< nikhil:

        n=n1+n2
        n1=n2
        n2=n
        count+=1
        print(n1)
        
