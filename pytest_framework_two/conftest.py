import pytest

from yaml_util import clean_yaml

@pytest.fixture(scope='session',autouse=True)
def clean_extract_yaml():
    clean_yaml()