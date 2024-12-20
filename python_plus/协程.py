import  asyncio
"""事件循环 1、检查协程 2、让出控制 3、等待协程"""
"""
1.定义协程函数
2.把协程保证为任务
3.建立时间循环
"""
async def fetch_url():
    print("Fetching url")
    await asyncio.sleep(2)
    print("Finsh fetching ")
    return "url_content"
async def read_file():
    print("Reading  the url")
    await asyncio.sleep(2)
    print("Finsh Reading ")
    return "file_content"

# 返回一个协程对象
async def main():
    task1 = asyncio.create_task(fetch_url())
    task2 = asyncio.create_task(read_file())
    fetch_result = await task1
    read_result = await task2



if __name__ == '__main__':
    asyncio.run(main())