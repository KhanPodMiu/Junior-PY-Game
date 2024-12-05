import random   

sothu1= random.randint(1,10)
sothu2= random.randint(1,10)
print("lan 1",sothu1)
print("lan 2",sothu2)
if sothu1 >= sothu2:
    i = sothu1
    sothu1= random.randint(1,10)
    print(sothu1)
    if sothu1 >= sothu2:
        k = sothu1
    else:
        k = sothu2
else:
    i = sothu2
    sothu2= random.randint(1,10)
    print(sothu2)
    if sothu1 >= sothu2:
        k = sothu1
    else:
        k = sothu2
print("so lon nhat lan 1:",i)
print("so lon nhat lan 2:",k)
print("tong",i+k)
