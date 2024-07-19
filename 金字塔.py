
for i in range(1,6):
    print(" "*(5-i),end='' )
    for j in range(1,i+1):
        print(j,end='')
    for s in range(i-1, 0, -1):
            print(s, end='')
    print()
for ii in range(4,0,-1):
    print(' '*(5-ii),end='')
    for jj in range(1,ii+1):
        print(jj,end='')
    for ss in range(ii-1,0,-1):
        print(ss,end='')
    print()
