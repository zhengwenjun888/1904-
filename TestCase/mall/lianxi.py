import allure
import pytest
from Common import Assert,Request
assertion=Assert.Assertions()
request=Request.Request()
head=[]
@allure.feature('退货原因')
class Test_return():

    @allure.story('登录')
    def test_login(self):
        resp=request.post_request(url='http://qa.yansl.com:8080/admin/login',
                                  json={"username":"admin","password":"123456"})
        resp_dict=resp.json()
        assertion.assert_code(resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],'成功')

        data=resp_dict['data']
        a=data['tokenHead']
        b=data['token']
        global head
        head={'Authorization':a+b}

    @allure.story('添加原因')
    def test_add_reason(self):
        resp=request.post_request(url='http://qa.yansl.com:8080/returnReason/create',
                                  json={"name":"不好","sort":0,"status":1,"createTime":''},headers=head)
        resp_json = resp.json()
        assertion.assert_code(resp.status_code,200)
        assertion.assert_in_text(resp_json['message'],'成功')








