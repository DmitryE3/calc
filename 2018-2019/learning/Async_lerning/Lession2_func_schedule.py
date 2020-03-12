import time
import asyncio


start=time.time()

def loader(url):
    print("Load {} at {}".format(url,time.time()-start))

async def spider(site_name): #добавив async перед def получаем асинхронную ф-ю (сопрограмма или корутин)
    for page in range(1,4):
        await asyncio.sleep(1) # ждем пока пройдет секунда
        print(site_name,page)

spiders=[
    asyncio.ensure_future(spider("Blog ")), #ensure_future - гарантировать выполнение в будущем
    asyncio.ensure_future(spider("News ")),
    asyncio.ensure_future(spider("Forum "))
]
event_loop=asyncio.get_event_loop() #диспетчер событий
now = event_loop.time() #Время старта цикла обработки событий
event_loop.call_soon(loader, "url1") #запуск в ближашее время, срабатывает, когда сопрограммы уходят в ожидание
#event_loop.call_later(2,loader, "url2") #отложенный вызов (первый аргумент - время задержки в секундах)
event_loop.call_at(now + 2,loader,"url 2") # выполнить в определенное время ()
event_loop.run_until_complete(asyncio.gather(*spiders))  #R-U-C - выполнение всех программ из списка спайдерс
                                                         #gather нужен, чтобы посместить все сопрограммы вместе и
event_loop.close()                                       #поместить их разом в R-U-C

print(time.time()-start)