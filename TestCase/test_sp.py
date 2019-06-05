from Common import Request,login,Assert,read_excel,Shell
import allure
import pytest



idds=[]
shell=Shell.Shell()

assertion = Assert.Assertions()
lg=login.Test_login()
request = Request.Request()
head={}
lists=[]
excel_list = read_excel.read_excel_list('../table/tianjia.xlsx')
for i in range(len(excel_list)):
    lists.append(excel_list[i].pop())



@allure.feature('商品管理')
class Test_shangping():
    @allure.story('获取商品分类')
    def test_huoqu(self):
        global head
        head=lg.test_login()
        resp = request.get_request(url='http://192.168.60.132:8080/productCategory/list/0',
                                          params={'pageNum': 1, 'pageSize': 5}, headers=head)
        json_dict = resp.json()
        assertion.assert_in_text(json_dict['message'],'成功')
        assertion.assert_code(resp.status_code,200)



        data=json_dict['data']
        list=data['list']
        idd=list[0]
        global idds
        idds=idd['id']


    @allure.story('删除商品')
    def test_delet(self):

        resp=request.post_request(url='http://192.168.60.132:8080/productCategory/delete/'+str(idds),headers=head)
        resp_dict=resp.json()
        assertion.assert_in_text(resp_dict['message'],'成功')
        assertion.assert_code(resp.status_code,200)

    @allure.story('添加商品')
    @pytest.mark.parametrize('name,keyw,msg',excel_list,ids=lists)
    def test_add(self,name,keyw,msg):
        resp=request.post_request(url='http://192.168.60.132:8080/productCategory/create',
                                  json={"name":name,"description":"","icon":"","keywords":keyw,"navStatus":0,"parentId":0,"productUnit":"",
                                  "showStatus":0,"sort":0,"productAttributeIdList":[]},headers=head)
        resp_dict = resp.json()
        assertion.assert_code(resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],msg)


pytest.main(['-s','-q','--alluredir','../Report/xml/','../TestCase'])
cmd="allure generate ../Report/xml/ -o ../Report/html/ --clean"
try:
    shell.invoke(cmd)
except Exception:

    print('html错误')
