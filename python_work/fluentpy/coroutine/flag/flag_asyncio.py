"""Download flags of top 20 countries by population
asyncio + aiottp version
Sample run::
    $ python3 flags_asyncio.py
    EG VN IN TR RU ID US DE CN MX JP BD NG ET FR BR PH PK CD IR
    20 flags downloaded in 1.07s
"""
# BEGIN FLAGS_ASYNCIO
import asyncio

import aiohttp  # <1>

from fluentpy.coroutine.flag.flags_fl import BASE_URL, show, main, save_flag


@asyncio.coroutine  # <3>
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    # <4> 阻塞的操作通过协程实现，客户代码通过yield from 把职责委托给协程，以便异步运行协程

    image = yield from resp.read()  # <5> 读取响应内容是异步操作
    return image


@asyncio.coroutine
def download_one(cc):  # <6>
    image = yield from get_flag(cc)  # <7>
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    to_do = [download_one(cc) for cc in sorted(cc_list)]  # <9> 调用download_one 构建一个生成器对象列表
    wait_coro = asyncio.wait(to_do)  # <10> wait 是一个协程，等待传给它的所有协程运行完毕后结束
    # wait协程的参数是一个由期望或者协程构成的可迭代对象
    # wait 会把各个协程分别包装进一个Task对象，
    # wait是协程函数，返回的是一个协程或生成器对象

    loop = asyncio.get_event_loop()  # <8>
    res, _ = loop.run_until_complete(wait_coro)  # <11>
    loop.close()  # <12>

    return len(res)


if __name__ == '__main__':
    main(download_many)
# END FLAGS_ASYNCIO
