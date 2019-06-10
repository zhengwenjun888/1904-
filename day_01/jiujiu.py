alist=[2,5,6,3,4,17]
for i in range(len(alist)-1):
    for j in range(len(alist)-i-1):

        if alist[j]>alist[j+1]:
            mm=alist[j]
            alist[j]=alist[j+1]
            alist[j + 1]=mm
print(alist)