def main():
    cha = int(input('So tuoi cua cha: '))
    con = int(input('So tuoi cua con: '))
    if con<0 or (con*2>=cha) or (con+15>cha):
        print('Tuoi cha va tuoi con khong dung voi de bai')
        print('Nhap lai!')
        main();
    else:
        print('Sau', cha-con*2, 'nam nua thi tuoi cha gap doi tuoi con')
main();