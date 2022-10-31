cha = int(input('So tuoi cua cha: '))
con = int(input('So tuoi cua con: '))

while con<0 or (con*2>=cha) or (con+15>cha):
    print('Tuoi cha va tuoi con khong dung voi yeu cau de bai')
    print('Nhap lai!')
    cha = int(input('So tuoi cua cha: '))
    con = int(input('So tuoi cua con: '))

print(f'Sau {cha-con*2} nam nua thi tuoi cha gap doi tuoi con')
