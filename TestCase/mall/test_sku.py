from Common import Request,login,Assert,read_excel
request=Request.Request()
assertion =Assert.Assertions()
head={}
idd = 0
lists=[]
import pytest
import allure

excel_list = read_excel.read_excel_list('./table/youhuijuan.xlsx')
for i in range(len(excel_list)):
    lists.append(excel_list[i].pop())

@allure.feature('优惠卷')
class Test_sku():
    # @pytest.mark.zhixin
    @allure.story('获取优惠卷列表')
    def test_huoqu(self):
        global head
        head=login.Test_login().test_login()
        resp=request.get_request(url='http://192.168.60.132:8080/coupon/list',params={'pageNum':1,'pageSize':10},headers=head)
        resp_dict=resp.json()
        assertion.assert_code(resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],'成功')

        data=resp_dict['data']
        list=data['list']
        listt=list[0]
        global idd
        idd=listt['id']

    @allure.story('删除')
    # @pytest.mark.zhixin
    def test_delect(self):

        resp=request.post_request(url='http://192.168.60.132:8080/coupon/delete/'+str(idd),headers=head)
        resp_dict=resp.json()
        assertion.assert_in_text(resp_dict['message'],'成功')
        assertion.assert_code(resp.status_code,200)


    @allure.story('添加优惠卷')
    # @pytest.mark.zhixin
    @pytest.mark.parametrize('name,amount,perLimit,minPoint,msg',excel_list,ids=lists)
    def test_add(self,name,amount,perLimit,minPoint,msg):
        resp = request.post_request(url='http://192.168.60.132:8080/coupon/create',
                                    json={"type":0,"name":name,"platform":0,"amount":amount,"perLimit":perLimit,
                                           "minPoint":minPoint,"startTime":"","endTime":"","useType":0,"note":"","publishCount":4,"productRelationList":[],
                                           "productCategoryRelationList":[]},
                                   headers=head)
        resp_dict = resp.json()
        assertion.assert_in_text(resp_dict['message'], msg)
        assertion.assert_code(resp.status_code, 200)







