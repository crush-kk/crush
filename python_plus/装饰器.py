import  time


def timer(threshold):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if end_time - start_time > threshold:
                print(f'{func.__name__} took longer than {threshold}s.')
            return result
        return wrapper
    return decorator
# 第一种写法 @timer(0.2)
# @timer(0.2)
def sleep_04():
    time.sleep(0.4)
# 第二种写法
sleep_04 = timer(0.2)(sleep_04)


if __name__ == '__main__':
    sleep_04()