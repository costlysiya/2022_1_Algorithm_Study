example=int(input())
frac=[1,1]
i=0
total=0
while total<example:
    total=total+i
    i=i+1
k=((i-2)*(i-1))//2
num=example-k
frac[1]=i-1
for j in range(num-1):
    frac[0]=frac[0]+1
    frac[1]=frac[1]-1

if (i-1)%2==1:
    frac.reverse()

print(frac[0],end="/")
print(frac[1])


