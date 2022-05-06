whole=[]
for i in range(1,10001):
    whole.append(i)
for i in range(1,10001):
    a=i//10000
    b=(i//1000)%10
    c=(i//100)%10
    d=(i//10)%10
    e=i%10

    new_num=i+a+b+c+d+e

    if new_num<=10000:
        if new_num in whole:
            whole.remove(new_num)
for new in whole:
    print(new)