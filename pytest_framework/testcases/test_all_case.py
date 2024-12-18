
import pytest
import  allure
from pathlib import Path

from commons.main_util import standard_case_flow
from commons.template import  verify_yaml
from commons.ddts import  read_test_case

class TestAllCase:
    pass
def create_testcase(yaml_file_path:str):
    @pytest.mark.parametrize("case_info", read_test_case(yaml_file_path))
    def inner_function(self, case_info):

        #用例校验
        case_obj = verify_yaml(case_info)

        #生成美观的测试报告
        allure.dynamic.feature(case_obj.feature)
        allure.dynamic.story(case_obj.story)
        allure.dynamic.title(case_obj.title)

        #执行标准化流程
        standard_case_flow(case_obj)

    return inner_function


#读取到所有的yaml测试用例
testcase_path = Path(__file__).parent
yaml_case_list = testcase_path.glob("**/*.yaml")
for yaml_case in yaml_case_list:
    setattr(TestAllCase,'test_' + yaml_case.stem , create_testcase(yaml_case))


