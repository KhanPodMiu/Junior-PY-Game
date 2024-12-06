import random 
la_bai = [1,2,3,4,5,6,7,8,9,10]


print("Chao Mung Ban Den Voi Game Bai Cao")

print("May:")
may_la_1 = random.choice(la_bai)
may_la_2 = random.choice(la_bai)
print(may_la_1,end="")
print("?")


#nguoi choi
print("Nguoi choi:")
nguoi_choi_la_1 = random.choice(la_bai)
nguoi_choi_la_2 = random.choice(la_bai)
print(nguoi_choi_la_1)
print(nguoi_choi_la_2)
#rut lan thu 1



rut_lan_1 = input("Ban co muon rut:")
if rut_lan_1 == 'n':
    print("Tong cua ban:", nguoi_choi_la_1+nguoi_choi_la_2)
    tong_nguoi_choi = nguoi_choi_la_1+nguoi_choi_la_2
if rut_lan_1  == 'y':
    nguoi_choi_la_3 = random.choice(la_bai)
    print(nguoi_choi_la_3)
    print("Tong hien tai:", nguoi_choi_la_3 + nguoi_choi_la_2 + nguoi_choi_la_1)
    
    #thua o lan rut thu 1
    if nguoi_choi_la_3 + nguoi_choi_la_2 + nguoi_choi_la_1 > 21:
        print("Ban da thua")
    else:
        # rut lan 2
        rut_lan_2 = input("Ban co muon rut:")
        if rut_lan_2 == 'n':
           print("Tong cua ban:", nguoi_choi_la_1+nguoi_choi_la_2 + nguoi_choi_la_3)
           tong_nguoi_choi = nguoi_choi_la_1 +nguoi_choi_la_2 + nguoi_choi_la_3
        
        if rut_lan_2  == 'y':
            nguoi_choi_la_4 = random.choice(la_bai)
            print(nguoi_choi_la_4)
            print("Tong hien tai:", nguoi_choi_la_3 + nguoi_choi_la_2 + nguoi_choi_la_1 + nguoi_choi_la_4)
            #thua o lan rut thu 2
            if nguoi_choi_la_3 + nguoi_choi_la_2 + nguoi_choi_la_1 + nguoi_choi_la_4 > 21 :
                print("Ban da thua")

            if nguoi_choi_la_3 + nguoi_choi_la_2 + nguoi_choi_la_1 + nguoi_choi_la_4 <= 21:
        #rut lan 3
                rut_lan_3 = input("Ban co muon rut:")
                if rut_lan_3 == 'n':
                    print("Tong cua ban:", nguoi_choi_la_1+nguoi_choi_la_2 + nguoi_choi_la_3 + nguoi_choi_la_4)
                    tong_nguoi_choi = nguoi_choi_la_1+nguoi_choi_la_2 + nguoi_choi_la_3 + nguoi_choi_la_4
                if rut_lan_3  == 'y':
                    nguoi_choi_la_5 = random.choice(la_bai)
                    print(nguoi_choi_la_5)
                    print("Tong hien tai:", nguoi_choi_la_3 + nguoi_choi_la_2 + nguoi_choi_la_1 + nguoi_choi_la_4 + nguoi_choi_la_5)
    
            #thua o lan rut thu 3
                    if nguoi_choi_la_3 + nguoi_choi_la_2 + nguoi_choi_la_1 + nguoi_choi_la_4 + nguoi_choi_la_5> 21:
                        print("Ban da thua")


#may rut
if may_la_1 +may_la_2 <=17:
    may_la_3 = random.choice(la_bai)
    tong_may = may_la_1 +may_la_2 + may_la_3
    if tong_may > tong_nguoi_choi:
        print("May thang")
        print("Tong may la:", tong_may)
    else:
        if may_la_1 +may_la_2 + may_la_3<=17:
            may_la_4 = random.choice(la_bai)
            tong_may = may_la_1 +may_la_2 + may_la_3 + may_la_4
            if tong_may > tong_nguoi_choi:
                print("May thang")
                print("Tong may la:", tong_may)
            else:
                if may_la_1 +may_la_2 +may_la_4 + may_la_3 <=17:
                    may_la_5 = random.choice(la_bai)
                    tong_may = may_la_1 +may_la_2 + may_la_3 + may_la_5 + may_la_4
                    if tong_may > tong_nguoi_choi:
                        print("May thang")
                        print("Tong may la:", tong_may)
                
        
                if may_la_1 +may_la_2 + may_la_3 > 21:
                    print("May da thua")
        
            if may_la_1 +may_la_2 + may_la_3 + may_la_4> 21:
                print("May da thua")
    if may_la_1 +may_la_2 + may_la_3 > 21:
        print("May da thua")



    

