import threading
import asyncio
 
async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(4)
    print('Hello again! (%s)' % threading.currentThread())
 
loop = asyncio.get_event_loop()
#tasks = [hello(), hello()]
tasks = [hello() for i in range(2)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()