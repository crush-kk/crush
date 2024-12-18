from copy import  deepcopy

from commons.request_util import  logger
class AssertUtil:

    def assert_result(self,resp, assert_type, assert_content):
        """
        对响应结果进行断言
        :param resp: 响应
        :param assert_type: 断言类型
        :param assert_content: 断言内容
        :return:
        """
        copy_resp = deepcopy(resp)
        try:
             copy_resp.json = copy_resp.json()
        except Exception:
            copy_resp.json = {"msg": "response has not such data"}
        for msg, data_list in assert_content.items():
            expect_value, real_value = data_list
            #根据反射得到real_value
            real_value = getattr(copy_resp, real_value)
            match assert_type:
                case "equals":
                    assert real_value == expect_value, logger.error(f"断言失败{msg}, 期望值{expect_value}, 实际值{real_value}")
                    logger.info(f"断言成功{msg}, 期望值{expect_value}, 实际值{real_value}")
                case "contains":
                    assert expect_value in real_value, logger.error(f"断言失败{msg}, 期望值{expect_value}, 实际值{real_value}")
                    logger.info(f"断言成功{msg}, 期望值{expect_value}, 实际值{real_value}")

