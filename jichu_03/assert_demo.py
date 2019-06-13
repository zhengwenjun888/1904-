try:
    assert 5==6
except:
    print('断言失败')
try:
    assert '成功'not in '操作成功'
except:
    print('断言失败')
try:
    assert '成功'in '操作成功'
except:
    print('断言成功')