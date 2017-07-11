import www.orm
from www.models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()

async def insert():
    await www.orm.create_pool(loop, user='root', password='andy123', db='aywebblog')
    u = User(name='Test', email='test3@example.com', passwd='123456', image='about:blank')
    await u.save()

    r = await User.findAll()
    print(r)

loop.run_until_complete(insert())
loop.close()
