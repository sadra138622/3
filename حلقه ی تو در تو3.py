a= int(input())
for i in range (a):
    m=0
    b=int(input())
    for j in range (2,b):
        if(b%j==0):
            m=1
    if m!=1 :
        print(b)
