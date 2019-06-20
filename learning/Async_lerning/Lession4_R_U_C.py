import time
import asyncio

start = time.time()


async def get_page(site_name):
    if site_name == "API ":
        await asyncio.sleep(0.1)
    else:
        await asyncio.sleep(0.5)
    print("Get pages for {}".format(site_name))
    return range(1, 4)


async def get_page_data(site_name, page):
    await asyncio.sleep(1)
    return "Data from page {} ({})".format(page, site_name)


async def spider(site_name):  # добавив async перед def получаем асинхронную ф-ю (сопрограмма или корутин)
    all_data = []
    pages = await get_page(site_name)
    for page in pages:
        data = await get_page_data(site_name, page)
        all_data.append(data)
    return all_data


spiders = [
    asyncio.ensure_future(spider("Blog ")),  # ensure_future - гарантировать выполнение в будущем
    asyncio.ensure_future(spider("News ")),
    asyncio.ensure_future(spider("Forum ")),
    asyncio.ensure_future(spider("API "))
]
event_loop = asyncio.get_event_loop()  # диспетчер событий
result = event_loop.run_until_complete(asyncio.gather(*spiders))
print(result)
event_loop.close()

print(time.time() - start)
