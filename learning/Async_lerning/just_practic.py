import asyncio
import random

def test_soon():
    print("запустимся как только так сразу")

async def async_rand(count):
    print("{} запуск рандома".format(count))
    x=random.randint(0,10)
    if x>=5:
        print('Выпал {} Ждем 5 сек'.format(x))
        await asyncio.sleep(5)
    else:
        print('Выпал {} Ждем 1 сек'.format(x))
        await asyncio.sleep(1)
    print(x)

funcs=[asyncio.ensure_future(async_rand('Первый')),
       asyncio.ensure_future(async_rand('Второй')),
       asyncio.ensure_future(async_rand('Третий'))]

event_loop=asyncio.get_event_loop()
event_loop.call_soon(test_soon)
event_loop.run_until_complete(asyncio.gather(*funcs))
event_loop.close()