from time import sleep

import pytest

from Common.Baseui import baseUI

class Test_mall():

    # def test_login(self,driver):
    #     base = baseUI(driver)
    #     base.driver.get('http://192.168.60.132/#/login')
    #     base.send_keys("输入用户名","//input[@name='username']",'')
    #     base.send_keys("输入密码", "//input[@name='password']", '')
    #     base.click('点击登录','//span[contains(text(),"登录")]')
    #     sleep(2)
    @pytest.mark.Ship
    def test_order(self,base):
        # base = baseUI(driver)
        base.click('点击订单列表',"(//span[contains(text(),'订单列表')])")
        base.click('点击订单状态','//label[contains(text(),"订单状态：")]/following-sibling::div//input')
        base.click('点击待发货',"//span[contains(text(),'待发货')]")
        base.click('点击搜索',"//span[contains(text(),'查询搜索')]")
        base.click('点击订单发货',"(//span[contains(text(),'订单发货')])[1]")
        base.click('选择物流公司','//input[@placeholder="请选择物流公司"]')
        base.click('选择物流公司','//span[contains(text(),"圆通快递")]')
        base.click('点击确定',"(//span[contains(text(),'确定')])[1]")
        base.click('点击确定',"(//span[contains(text(),'确定')])[2]")
        text=base.get_text('获取页面文本','''//div[@role="alert"]//p''')
        assert '成功'in text

    @pytest.mark.Return
    def test_return(self,base):
        base.click('点击退货原因设置','''//span[contains(text(),'退货原因设置')]''')
        # 点击添加
        base.click('点击添加', '(//button[@type="button"])[1]')
        # 输入原因类型
        base.send_keys('输入原因类型','''//*[contains(text(),'原因类型：')]/following-sibling::div//input''','不好看')
        # 点击确定
        base.click('点击确定','//div[@class="el-dialog__footer"]//span//button[2]/span')
        # 获取成功提示
        assert '成功'in base.driver.page_source

    @pytest.mark.reasons_for_return
    def test_teturn_do(self,base):
        # base=baseUI(driver)
        base.driver.get('http://192.168.60.132/#/oms/returnApply')
        # 点击处理状态
        base.click('点击处理状态','''//label[contains(text(),'处理状态：')]/following-sibling::div//input''')
        # 点击待处理
        base.click('点击待处理',"//span[contains(text(),'待处理')]")
        # 点击查询搜索
        base.click('点击查询搜索',"//span[contains(text(),'查询搜索')]")
        # 点击第一列信息
        base.click('点击第一列信息',"(//span[contains(text(),'查看详情')])[1]")
        # 下拉滚动
        base.scroll_screen('下拉滚动')
        # 获取金额
        money=base.get_text('获取金额','''//div[contains(text(),'订单金额')]/following-sibling::div''')
        money=money[1:]
        print(money)
        # 输入金额
        base.send_keys('输入金额','''//div[contains(text(),'确认退款金额')]/following-sibling::div//input''',str(money))
        base.click('点击选择','//div[contains(text(),"选择收货点")]/following-sibling::div//input')
        base.click('选择发货地址','''//span[contains(text(),'北京发货点')]''')
        base.send_keys('处理备注','//div[contains(text(),"处理备注")]/following-sibling::div//input','已处理')
        base.click('点击确认退货','''//span[contains(text(),'确认退货')]''')
        base.click('点击确定',"//span[contains(text(),'确定')]")
        text=base.get_text('获取页面文本', '''//div[@role="alert"]//p''')
        assert '成功' in text





        sleep(5)










