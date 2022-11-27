n=int(input('n='))
k=int(input('k='))
a=[]
for i in range(n):
    val=int(input('nhap phan tu: '))
    a.append(val)
print('A=', a)
x=0
for i in a:
    if i>k:
        x+=1
print(f'co {x} phan tu > k (>{k})')
shown = []
for i in a:
    a1 = [x for x in a if x != i]
    for j in a1:
        if i + j == k and {i, j} not in shown:
            shown.append({i, j})
            print([i, j], end='   ')
        a2 = [x for x in a1 if x != j]
        for l in a2:
            if i + j + l == k and {i, j, l} not in shown:
                shown.append({i, j, l})
                print([i, j, l], end='   ')