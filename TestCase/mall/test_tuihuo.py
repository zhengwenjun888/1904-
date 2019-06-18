from Common import Request,login,Assert,read_excel
import pytest
import allure

request=Request.Request()
assertion =Assert.Assertions()
head={}
idd=0
list=[]
excel_list = read_excel.read_excel_list('./table/tuihuo.xlsx')
for i in range(len(excel_list)):
    list.append(excel_list[i].pop())


@allure.feature('退货')
class Test_tuihuo():
    @allure.story('获取退货')
    def test_huoqu(self):
        global head
        head=login.Test_login().test_login()
        response = request.get_request(url='http://192.168.60.132:8080/returnReason/list',
                                          params={'pageNum': 1, 'pageSize': 5},headers=head)
        json_dict = response.json()
        assertion.assert_code(response.status_code,200)
        assertion.assert_in_text(json_dict['message'],'成功')

        data = json_dict['data']
        list = data['list']
        listt = list[0]
        global idd
        idd = listt['id']

    @allure.story('添加退货原因')
    def test_yuanying(self):
        response = request.post_request(url='http://192.168.60.132:8080/returnReason/create',
                                            json={"name": "nihao", "sort": 0, "status": 1, "createTime": ""},
                                            headers=head)
        json_dict = response.json()
        assertion.assert_code(response.status_code,200)
        assertion.assert_in_text(json_dict['message'],'成功')


    @allure.story('添加退货原因参数化')
    @pytest.mark.parametrize('name,msg',excel_list,ids=list)
    def test_yuanying(self,name,msg):
        response = request.post_request(url='http://192.168.60.132:8080/returnReason/create',
                                            json={"name": name, "sort": 0, "status": 1, "createTime": ""},
                                            headers=head)
        json_dict = response.json()
        assertion.assert_code(response.status_code,200)
        assertion.assert_in_text(json_dict['message'],msg)


    @allure.story('删除')
    def test_delete(self):
        response = request.post_request(url='http://192.168.60.132:8080/returnReason/delete',
                                        params={'ids':idd},headers=head)
        json_dict = response.json()
        assertion.assert_code(response.status_code, 200)
        assertion.assert_in_text(json_dict['message'], '成功')


