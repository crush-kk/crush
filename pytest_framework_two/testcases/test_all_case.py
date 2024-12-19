from pathlib import Path

import pytest
import  allure
from commons.template import verify_xlsx
from commons.xlsx_util import read_xlsx_file
from commons.main_util import  standard_flow


class TestAllCase:
    pass
def create_testcase(xlsx_path:str):
    @pytest.mark.parametrize("case_info", read_xlsx_file(xlsx_path))
    def inner_function(self, case_info):
        """
        :param case_info:
        :return:
        """
        # 1、数据校验
        case_obj = verify_xlsx(case_info)
        # 2、配置allure
        allure.dynamic.feature(case_obj.feature)
        allure.dynamic.story(case_obj.story)
        allure.dynamic.title(case_obj.title)
        # 3.执行标准测试流程
        standard_flow(case_obj)
    return  inner_function


testcase_path = Path(__file__).parent
print(testcase_path)
xlsx_case_list = testcase_path.glob("**/*.xlsx")
for xlsx_case in xlsx_case_list:
    setattr(TestAllCase, 'test_'+ xlsx_case.stem, create_testcase(xlsx_case))

