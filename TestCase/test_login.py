import allure
import pytest

from Common import Shell ,read_excel,Assert,Request

request = Request.Request()
assertion = Assert.Assertions()
shell= Shell.Shell

idds=[]
excel_list = read_excel.read_excel_list('../table/demlu.xlsx')
for i in range(len(excel_list)):
    idds.append(excel_list[i].pop())


@allure.feature('测试')
class Test_Login():
    @allure.story('测试登录')
    def test_login(self):
        resp=request.post_request(url='http://192.168.60.132:8080/admin/login',
                           json={"password": "123456","username": "admin"})

        resp_dict = resp.json()
        assertion.assert_code(resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],'成功')


    @allure.story('测试登录2')
    @pytest.mark.parametrize('pwd,name,msg',excel_list,ids=idds)
    def test_login2(self, pwd,name,msg):
        resp = request.post_request(url='http://192.168.60.132:8080/admin/login',
                             json={"password": pwd, "username": name})
        resp_dict = resp.json()
        assertion.assert_code(resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],msg)


pytest.main(['-s','-q','--alluredir','../Report/xml/','../TestCase'])
cmd="allure generate ../Report/xml/ -o ../Report/html/ --clean"
try:
    shell.invoke(cmd)
except Exception:
    print('html错误')

