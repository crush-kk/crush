from commons.request_util import  RequestUtil
from commons.extract_util import ExtractUtil
from commons.assert_util import  AssertUtil
from commons.template import  CaseInfo
ru  = RequestUtil()
eu = ExtractUtil()
au = AssertUtil()
def standard_flow(case_obj: CaseInfo):
    """
    1、发送请求
    2.提取
    3.断言
    :param case_obj:
    :return:
    """
    print(case_obj)
    resp = ru.send_all_requests(**eu.use_extract(case_obj.request))
    # 如果提取字段有值
    if case_obj.extract:
        for k, v in case_obj.extract.items():
            v = v.split(',')
            eu.extract(resp, k, *v)
    #如果断言字段有值，进行断言
    if case_obj.validate:
        for assert_type,assert_content in case_obj.validate.items():
            au.assert_result(resp, assert_type, assert_content)

