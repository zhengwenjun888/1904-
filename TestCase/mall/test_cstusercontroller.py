from Common import Tools1,read_excel,Assert,Request
import pytest
request = Request.Request()
assertion = Assert.Assertions()
phone=Tools1.phone_num()
pwd= Tools1.random_str_abc(2) + Tools1.random_123(4)
pwd1= Tools1.random_str_abc(2) + Tools1.random_123(5)
userName= Tools1.random_str_abc(3) + Tools1.random_123(2)
import allure
head={}
url='http://192.168.60.132:1811'

lists=[]
excel_list = read_excel.read_excel_list('./table/zhuce.xlsx')
for i in range(len(excel_list)):
    lists.append(excel_list[i].pop())

@allure.feature('用户')
class Test_order():

    @allure.story('注册2')
    @pytest.mark.parametrize('phones,pwdd,rePwdd,userNamee,cod',excel_list,ids=lists)
    def test_singup2(self,phones,pwdd,rePwdd,userNamee,cod):
        post_resp = request.post_request(url=url + '/user/signup',
                                         json={"phone": phones, "pwd": pwdd, "rePwd": pwdd, "userName": userNamee})
        post_resp_dict = post_resp.json()
        assertion.assert_code(post_resp.status_code, 200)

        assertion.assert_in_text(post_resp_dict['respCode'], cod)


    @allure.story('注册')
    def test_singup(self):
        post_resp = request.post_request(url=url + '/user/signup',
                                            json={"phone": phone, "pwd": pwd, "rePwd": pwd, "userName": userName})
        post_resp_dict = post_resp.json()
        assertion.assert_code(post_resp.status_code,200)
        assertion.assert_in_text(post_resp_dict['respBase'],'注册成功')


    @allure.story('登录')
    def test_login(self):
        post_resp = request.post_request(url=url + '/user/login',
                                            json={"pwd": pwd,"userName":userName})
        post_resp_dict = post_resp.json()
        assertion.assert_code(post_resp.status_code,200)
        assertion.assert_in_text(post_resp_dict['respDesc'],'登录成功')



    @allure.story('修改密码')
    def test_changepwd (self):
        post_resp = request.post_request(url=url + '/user/changepwd',
                                         json={"newPwd": pwd1,"oldPwd": pwd,"reNewPwd": pwd1,"userName": userName})
        post_resp_dict = post_resp.json()
        assertion.assert_code(post_resp.status_code, 200)
        assertion.assert_in_text(post_resp_dict['respDesc'], '成功')

    @allure.story('冻结用户')
    def test_lock(self):
        post_resp = request.post_request(url=url + '/user/lock', params={"userName":userName},
                                         headers ={"Content-Type": "application/x-www-form-urlencoded"})
        post_resp_dict = post_resp.json()
        assertion.assert_code(post_resp.status_code, 200)
        assertion.assert_in_text(post_resp_dict['respDesc'], '成功') 

    @allure.story('结冻用户')
    def test_unLock(self):
        post_resp = request.post_request(url=url + '/user/unLock', params={"userName": userName},
                                         headers={"Content-Type": "application/x-www-form-urlencoded"})
        post_resp_dict = post_resp.json()
        assertion.assert_code(post_resp.status_code, 200)
        assertion.assert_in_text(post_resp_dict['respDesc'], '成功')












