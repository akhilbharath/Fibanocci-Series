# Fibanocci-Series
x=0
y=1
i=0
l=int (input('enter length = ' ))
while i<l:
    print(x)
    z=x+y
    x=y
    y=z
    i=i+1

if l<=0:
    print('try again')
