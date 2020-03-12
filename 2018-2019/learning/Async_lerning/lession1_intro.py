import time
import asyncio

start = time.time()


async def spider(site_name):  # добавив async перед def получаем асинхронную ф-ю (сопрограмма или корутин)
    for page in range(1, 4):
        #        time.sleep(1) заменяем на асинхронную ф-ю
        await asyncio.sleep(1)  # ждем пока пройдет секунда
        print(site_name, page)


# spider("Blog ")
# spider("News ")
# spider("Forum ")

spiders = [
    asyncio.ensure_future(spider("Blog ")),  # ensure_future - гарантировать выполнение в будущем
    asyncio.ensure_future(spider("News ")),
    asyncio.ensure_future(spider("Forum "))
]
event_loop = asyncio.get_event_loop()  # диспетчер событий
event_loop.run_until_complete(asyncio.gather(*spiders))  # R-U-C - выполнение всех программ из списка спайдерс
event_loop.close()  # gather нужен, чтобы посместить все сопрограммы вместе и
# поместить их разом в R-U-C

print(time.time() - start)
