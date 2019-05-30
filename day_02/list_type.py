alist=['nihao',12,'中国','abd','kjhkj','hhh']
blist=[78,'33',90]


#     索引访问
print(alist[0])
print(alist[0:1])
print(alist[-3])
print(alist[4:])
# 索引删除,删除的元素可以赋值给a
a=alist.pop()
alist.pop(3)
# 追加,两个列表的追加被追加的表会是第一个表的一个元素
alist.append(blist)
alist.append('ni')
print(alist)
# 合并两个列表,也可用于添加多个元素
alist.extend(blist)
print(alist)
# 更新列表元素,列表[索引]=值
alist[0]=11
alist[2]=200
# 获取长度
print(len(alist))
#去重
al=[1,2,3,4,5,1,2,3]
al=list(set(al))
print(al)

# 作业
dlist=['jjj','jk','ii','ss',55]
print(dlist[2])
print(dlist[1:4])
dlist.pop(3)
d=['dd',789]
dlist.extend(d)
print(dlist)
dlist[0]=5
print(len(dlist))










