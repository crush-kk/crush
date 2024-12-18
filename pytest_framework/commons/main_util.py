from commons.request_util import  RequestUtil
from commons.assert_util import AssertUtil
from commons.extract_util import  ExtractUtil
from commons.template import  CaseInfo

ru = RequestUtil()
eu = ExtractUtil()
au = AssertUtil()
def standard_case_flow(case_obj: CaseInfo):
    """
    1.发送请求
    2.提取数据作为中间变量
    3.对结果进行断言
    :param case_obj: CaseInfo对象
    :return:
    """
    # 发送请求
    resp =  ru.send_all_requests(**eu.use_extract(case_obj.request))
    print(case_obj)
    #如果字段不为空，则说明需要提取值作为中间变量
    if case_obj.extract :
        for key, value in case_obj.extract.items():
            eu.extract(resp, key, *value)
    #如果断言字段不为空，对结果进行断言
    if case_obj.validate:
        for assert_type, assert_content in case_obj.validate.items():
            au.assert_result(resp, assert_type, assert_content)

