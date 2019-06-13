# 字典是无序的
import json

adict={'password': '123456','username': 'admin'}
# 访问
print(adict['password'])
# 删除
print(adict.pop('username'))
# 修改
adict['password']='6666'
print(adict)
# 追加

adict['benzhu']='登录'
print(adict)
# 合并1
bdict={'kjlasjd':45555}
adict.update(bdict)
# 合并2成一个新字典,字典与列表元祖合并时放在最后前面加**,元祖放字典前加*
jkj = dict(adict, **bdict)
print(jkj)
# 字典转换字符串格式
lo = json.dumps(adict)
print(type(lo))
# 字符转字典
json_loads = json.loads(lo)
print(type(json_loads))


