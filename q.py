n=int(input('enter a number'))
n1=0
n2=1
count=0
if n<0:
    print ("please enter valid number")
elif n==0:
    print ("fibonacci number ",n)
else:
    while count<n:
        print (n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
