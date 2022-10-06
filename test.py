def main():
    m = int(input('nhap vao so m: '))
    n = int(input('nhap vao so n: '))
    a = n//m    #phan nguyen phep chia
    b = n%m     #phan du cua phep chia
    c = n-m+1   #so luong so trong doan
    d = c*(m+n)/2   #tong cac so nguyen trong doan
    if m < n :
        print('phan nguyen cua phep chia',n, 'cho',m,'la:',a)
        print('phan du cua phep chia',n,'cho',m,'la:',b)
        print('so luong so trong doan [',m,';',n,'] la:',c)
        print('tong cac so nguyen trong doan [',m,';',n,'] la:', d)
    else :
        print('Nhap lai m va n, sao cho m < n')
        main();
main();
