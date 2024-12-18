import yaml





def read_test_case(yaml_file_path:str) -> dict:
    """
    分为三种类型：
        1.单接口用例
        2.数据驱动用例
        3.流程用例
    :param yaml_file_path:  测试用例文件的路径
    :return:
    """
    with open(yaml_file_path, encoding='utf-8') as f:
        case_lists = yaml.safe_load(f)
        if len(case_lists) > 2:
            # 流程用例
            return [case_lists]
        else:
            if "parametrize" in dict(*case_lists).keys():
                return change_case_list(*case_lists)
                #数据驱动用例
                pass
            else:
                # 单接口用例
                return case_lists
def change_case_list(case_lists: dict) -> list:
    # 即将拆分的驱动数据
    data_list = case_lists["parametrize"]
    x, y = len(data_list[0]), len(data_list)
    copy_single_case = yaml.safe_dump(case_lists)
    new_cae_lists = []
    for j in range(1, y):
        single_case = copy_single_case
        for i in range(x):
            if isinstance(data_list[j][i], str) and data_list[j][i].isdigit():
                data_list[j][i] = "'" + data_list[j][i] + "'"
            single_case = single_case.replace("$ddt{"+ data_list[0][i] + "}", data_list[j][i])
        single_case = yaml.safe_load(single_case)
        single_case.pop("parametrize")
        new_cae_lists.append(single_case)
    return new_cae_lists

if __name__ == '__main__':
    print(read_test_case())