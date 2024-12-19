import  openpyxl
import json
import  yaml

from commons.reload_and_replace_util import reload_and_replace_util
def read_xlsx_file(xlsx_file:str):
    # 创建表对象
    xlsx_table = openpyxl.load_workbook(xlsx_file)
    # 获取sheet1对象
    sheet1 = xlsx_table["flow"]
    # 创建一个流程用例对象
    flow_testcase = []
    #读取每一行
    for row in sheet1.iter_rows(min_row = 2):
        # 读取表头
        row_key = map(lambda cell: cell.value, sheet1[1])
        row_value = map(lambda cell: cell.value, row)
        testcase = dict(zip(row_key, row_value))
        testcase["request"] = json.loads(testcase["request"])
        testcase["validate"] = json.loads(testcase["validate"])
        testcase["extract"] = json.loads(testcase["extract"])
        print(testcase)
        testcase_str = reload_and_replace_util(yaml.safe_dump(testcase))
        flow_testcase.append(yaml.safe_load(testcase_str))
    print(flow_testcase)
    return flow_testcase
if __name__ == '__main__':
    read_xlsx_file(r"D:\testing\crush\pytest_framework_two\testcases\data\flow.xlsx")




