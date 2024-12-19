import requests
from jsonpath import jsonpath

HOST = 'https://cloud.seafile.com'
sess = requests.Session()
class TestSeafileInterface:

    """


2.查看所有资料库(library中的list libraries)
curl -H 'Authorization: Token {{token}}' {{host}}/api2/repos/
URL:	{{host}}/api2/repos/
请求方法：get
header:	Authorization:Token {{token}}
json响应：json格式，该用户的所有库，数组类型，元素是每个库
需要检查资料库数组的长度>0

3.新建资料库(library中的create library)
curl -d "name={{repo_name}}&passwd={{password}}" -H 'Authorization: Token token值' {{host}}/api2/repos/
URL:	{{host}}/api2/repos/
请求方法：post
header:	Authorization:Token {{token}}
传参方式：x-www-form-urlencoded
参数：
name={{repo_name}}
passwd={{password}}，选填
desc={{desc}}，选填
需要断言新建资料库是否成功，以及passwd空时encrypted值为空，passwd非空时encrypted=1
json响应：关于该库的json，其中有repo_id
说明：如果不传passwd，则创建的资料库为不加密资料库，返回Json中节点encrypted=""，传passwd则创建加密资料库，返回Json中节点encrypted=1
需要断言资料库创建是否成功；需要断言是否加密；需要提取repo_id

4.查看资料库文件和查看目录下文件(directory中的list directory entries)
curl -H 'Authorization: Token {{token}}' {{host}}/api2/repos/{{repo_id}}/dir/?p=/{{dirpath}}
URL:	{{host}}/api2/repos/{{repo_id}}/dir/?p=/{{dirpath}}
请求方法：get
URL参数：p=/{{dirpath}}
header:	Authorization:Token {{token}}
json响应：目录下的文件信息，数组类型，元素为文件的json
说明：查看资料库文件用的就是查看目录下文件的请求，只不过p参数传递的是根目录/
需要断言返回文件列表是否正确，如空资料库则返回空，如已建立文件夹和文件，则需要返回这些文件夹和文件
文件和文件夹通过节点中type=file或者type=dir来区分。

5.资料库解密(library中的decrypt library)
curl -d "password={{librarypwd}}" -H 'Authorization: Token {{token}}' {{host}}/api2/repos/{{repo_id}}/
URL:	{{host}}/api2/repos/{{repo_id}}/
请求方法：post
header:	Authorization:Token {{token}}
传参方式：x-www-form-urlencoded
参数：
password={{librarypwd}}
文字响应：解密成功则返回"success"，否则返回带有error_msg节点的json数据
需要断言响应内容是否正确

6.重命名资料库(接口文档缺失)
curl -d "repo_name={{new_repo_name}}" -H 'Authorization: Token {{token}}' {{host}}/api2/repos/{{repo_id}}/?op=rename
URL:	{{host}}/api2/repos/{{repo_id}}/?op=rename
                {{host}}/api2/repos/{{repo_id}}/?op=rename
URL参数：op=rename
请求方法：post
header:	Authorization:Token {{token}}
传参方式：x-www-form-urlencoded
body参数：
repo_name={{new_repo_name}}
响应："success"
需要断言响应内容是否正确

7.新建文件夹(directory的Create New Directory)
curl -d 'operation=mkdir' -H 'Authorization: Token {{token}}' {{host}}/api2/repos/{{repo_id}}/dir/?p=/{{new_dirpath}}
URL:	{{host}}/api2/repos/{{repo_id}}/dir/?p=/{{new_dirpath}}
URL参数：p=/{{new_dirpath}}
请求方法：post
header:	Authorization:Token {{token}}
传参方式：x-www-form-urlencoded
body参数：
operation=mkdir
纯文字响应：如果创建成功则"success"，失败返回"failure..."
断言响应内容是否正确

8.新建文件(file的Create File)
curl -d 'operation=create' -H 'Authorization: Token {{token}}' {{host}}/api2/repos/{{repo_id}}/file/?p=/{{new_filepath}}
URL:	{{host}}/api2/repos/{{repo_id}}/file/?p=/{{new_filepath}}
URL参数：p=/{{new_filepath}}
请求方法：post
header:	Authorization:Token {{token}}
传参方式：x-www-form-urlencoded
body参数：
operation=create
纯文字响应：如果创建成功则"success"，失败返回"failure..."
断言响应内容是否正确

9.1.上传文件-获取网址(File的Upload File，分为2个请求完成上传文件)
curl -H "Authorization: Token {{token}}" {{host}}/api2/repos/{{repo_id}}/upload-link/
URL:	{{host}}/api2/repos/{{repo_id}}/upload-link/
请求方法：get
header:	Authorization:Token {{token}}
响应：网址
需要提取网址

9.2.上传文件-实施文件上传
URL:	{{upload_url}}，就是获取网址接口返回响应中的网址
请求方法：post
header:	Authorization:Token {{token}}
传参方式：form-data
参数
file=@{{filename}}
parent_dir=/
响应：一串字符串

10.重命名文件夹(Directory的Rename Directory)
URL:	{{host}}/api2/repos/{{repo_id}}/dir/?p=/{{old_dir}}
请求方法：post
URL参数：p=/{{old_dir}}
header:	Authorization:Token {{token}}
传参方式：x-www-form-urlencoded
参数
operation=rename
newname={{new_name}}
纯文字响应：如果创建成功则"success"，失败返回"failure..."
测试要求：断言是否成功

11.重命名文件(File的Rename File)
URL:	{{host}}/api2/repos/{{repo_id}}/file/?p=/{{old_file}}
请求方法：post
URL参数：p=/{{old_file}}
header:	Authorization:Token {{token}}
传参方式：x-www-form-urlencoded
参数:
operation=rename
newname={{new_name}}
纯文字响应：如果创建成功则"success"，失败返回"failure..."
测试要求：断言是否成功

12.13.复制文件夹和文件(File的Copy File)
URL:	{{host}}/api2/repos/{{repo_id}}/fileops/copy/?p=/{{parent_folder}}
请求方法：post
URL参数：p=/{{parent_folder}}
header:	Authorization:Token {{token}}
传参方式：x-www-form-urlencoded
参数
dst_repo={{dst_repo_id}}
dst_dir={{dst_dir}}
file_names={{copy_file}}
json响应：如果成功则返回字符串"success"
测试要求：断言是否成功

14.15.移动文件夹和文件(File的Move File)
URL:	{{host}}/api2/repos/{{repo_id}}/file/?p={{move_file}}
请求方法：post
URL参数：p={{move_file}}
header:	Authorization:Token {{token}}
传参方式：x-www-form-urlencoded
参数
operation=move
dst_repo={{dst_repo_id}}
dst_dir={{dst_dir}}
文字响应：如果成功则返回文本"success"
测试要求：断言是否成功

16.下载文件
URL：{{host}}/api2/repos/{{repo_id}}/file/?op=download&p=/{{download_file}}
请求方法：get
header:	Authorization:Token {{token}}
纯文字响应：网址


16.删除文件(File的Delete File)
URL:	{{host}}/api2/repos/{{repo_id}}/file/?p=/{{del_file}}
请求方法：delete
URL参数：p=/{{del_file}}
header:	Authorization:Token {{token}}
纯文字响应：如果创建成功则"success"，失败返回"failure..."
测试要求：断言是否成功

17.删除文件夹(Directory的Delete Directory)
URL:	{{host}}/api2/repos/{{repo_id}}/dir/?p=/{{del_dir}}
请求方法：delete
URL参数：p=/{{del_dir}}
header:	Authorization:Token {{token}}
纯文字响应：如果创建成功则"success"，失败返回"failure..."
测试要求：断言是否成功

18.删除资料库(Library的Delete Library)
URL:	{{host}}/api2/repos/{{repo_id}}/
请求方法：delete
header:	Authorization:Token {{token}}
纯文字响应：如果创建成功则"success"，失败返回"failure..."
测试要求：断言是否成功
    """
    def test_follow_main(self):
        username, password = 'admin666@qq.com', 'admin666'
        """
        1.登录接口(quick start的第2个接口)
        curl -d "username={{email}}&password={{userpwd}}"  {{host}}/api2/auth-token/
        URL:	{{host}}/api2/auth-token/
        请求方法：post
        传参方式：x-www-form-urlencoded
        参数：
        username={{email}}
        password={{userpwd}}
        json响应：
        需要断言登录是否成功，成功返回token节点的json，状态码200；失败则返回non_field_errors节点的json，状态码400
        成功则需要提取token值，保存为集合变量token，如果登录失败，后续接口调用都不执行
        :return:
        """
        request = {
            'url': HOST + '/api2/auth-token/',
            'method': 'POST',
            'data': {
                'username': username,
                'password': password
            }
        }
        resp = sess.request(**request)
        assert resp.status_code == 200
        token = jsonpath(resp.json(), '$.token')[0]
        print(token)

