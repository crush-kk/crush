from dataclasses import  dataclass
from commons.request_util import logger
@dataclass
class CaseInfo:
    """用来规范yaml测试用例"""
    # 必填字段
    # allure定制
    feature: str
    story: str
    title: str

    # 请求
    request: dict
    # 断言
    validate: dict

    # 选填字段
    # 提取
    extract: dict = None
    parametrize: list = None
def verify_yaml(case_info: dict) -> CaseInfo:
    try:
        return CaseInfo(**case_info)
    except Exception as e:
        logger.error(f"yaml用例书写不规范!，请规范书写!{str(e)}")
        raise  Exception("yaml用例书写不规范!，请规范书写!") from e

