
from Common import Request,Assert

url='http://192.168.1.137:8080/'

request = Request.Request()

assertion = Assert.Assertions()


class Test_login:

    def test_login(self):
        login_resp=request.post_request(url=url+'admin/login',
                                        json={"username": "admin", "password": "123456"})
        resp_text = login_resp.text
        resp_dict = login_resp.json()
        assertion.assert_code(login_resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],'成功')

        # 提取token
        dict_data = resp_dict['data']
        token=dict_data['token']
        tokenhead=dict_data['tokenHead']

        head={'Authorization':tokenhead+token}
        return head

