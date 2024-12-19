from copy import  deepcopy

class AssertUtil:

    def assert_result(self,resp, assert_type, assert_content):
        copy_resp = deepcopy(resp)
        try:
             copy_resp.json = copy_resp.json()
        except :
            copy_resp.json = {"msg": "response has not such data"}
        msg, expect_value, real_value = assert_content.split(",")
        expect_value = int(expect_value)
        #根据反射得到real_value
        real_value = getattr(copy_resp, real_value)
        match assert_type:
            case "equals":
                assert real_value == expect_value, print(f"断言失败{msg}, 期望值{expect_value}, 实际值{real_value}")
                print(f"断言成功{msg}, 期望值{expect_value}, 实际值{real_value}")
            case "contains":
                assert expect_value in real_value, print(f"断言失败{msg}, 期望值{expect_value}, 实际值{real_value}")
                print(f"断言成功{msg}, 期望值{expect_value}, 实际值{real_value}")

