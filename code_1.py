canh = int(input("nhap chieu dai canh"))
for i in range(canh):
    if i == 0 or i == canh-1:
#in hang dau
        for k in range(canh):
            print("# ", end="")
        print()
        
    else:
        print("#", end="")
        for n in range(2 * canh -3):
            print(" ", end="")
        print("#")

        