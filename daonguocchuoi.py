def dao_nguoc_chuoi(chuoi):

    return chuoi[::-1]

# Thử nghiệm hàm với một chuỗi

chuoi_can_dao_nguoc = input()

ket_qua = dao_nguoc_chuoi(chuoi_can_dao_nguoc)

print("Chuỗi ban đầu:", chuoi_can_dao_nguoc)

print("daoChuỗi sau khi đảo ngược:", ket_qua)