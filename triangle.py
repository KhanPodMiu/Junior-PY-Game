canh = int(input("Nhap chieu danh canh"))
k = 0
for i in range(canh):
    for w in range((canh-i-1)*2):
        print(" ",end="")
    for a in range(i+1):
        print(a+1,"",end="")
        if a == i:
            for q in range(a):
                print(a-q,"",end="")
    print("")