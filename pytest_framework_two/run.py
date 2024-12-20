import pytest
import os
if __name__ == '__main__':


    pytest.main()
    os.system("allure generate ./temps -o ./reports --clean")
    os.system("allure open ./reports")