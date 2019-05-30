# 乘法口诀表
for i in range (1,10):
    for j in range (1,i+1):
        print('%s*%s=%2s'%(i,j,i*j),end='  ')
    print(' ')
# 冒泡排序
list=[8,1,2,5,3,6,4,7,9,]
for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        m=list[j]
        n=list[j+1]
        if m < n :
            continue
        num=list[j]
        list[j]=list[j+1]
        list[j+1]=num
print(list)


# 排正序
list.sort()
print(list)
# 排倒序
list.reverse()
print(list)

# 水仙花
# for n in range(100,1000):
#     i=n/100
#     j=n/10%10
#     k=n%10
#     print(i)
#     if n==i**3+j**3+k**3:
#         print(n)
