import asyncio
import threading


#此方法将会被弃用

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again! (%s)" % threading.currentThread())

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()