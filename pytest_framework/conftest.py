import  pytest

from commons.request_util import  logger
from commons.yaml_util import clean_yaml

@pytest.fixture(scope='session', autouse=True)
def clean_extract_value():
    clean_yaml()
    logger.info("清空了中间变量~~~~~~~~~~~~~")