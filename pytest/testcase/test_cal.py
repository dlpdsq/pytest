import pytest
from testcase.calculate import Calculate
from utils.yaml_operation import yaml_open
#import allure

class TestCalculate():
    print("--------------------------用例开始执行----------------------------")
    @pytest.mark.parametrize("test_data", yaml_open.read_yaml("./data/data.yaml", 'test_data'))
    @pytest.mark.run(order=1)
    def test_calculate(self,test_data):
        res=Calculate.cal(self,test_data["a"],test_data["b"],test_data["c"])
        print(res)
        #通过判断返回的是不是list来确定是否执行成功
        assert isinstance(res,list)
        print('------------------------------用例'+str(test_data["index"])+'执行结束------------------------------------')
    #测试用
    @pytest.mark.run(order=2)
    #@allure.severity("blocker")
    def test_calculate2(self,test_data):
        res=Calculate.cal(self,test_data["a"],test_data["b"],test_data["c"])
        print(res)
        #通过判断返回的是不是list来确定是否执行成功
        assert isinstance(res,list)
        print("------------------------------执行结束------------------------------------")




