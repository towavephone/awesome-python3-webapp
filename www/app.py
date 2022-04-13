#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
import asyncio
from models import User
async def test(loop):                      
    await orm.create_pool(loop=loop, user='root', password='123456', db='awesome')
    u = User(name='Test1', email='test2@qq.com', passwd='1234567890', image='about:blank')
    await u.save()
    orm.__pool.close()
    await orm.__pool.wait_closed()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()