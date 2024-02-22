# Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker.
# It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries.
# Redis has built-in replication, Lua scripting, LRU eviction, transactions and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.
# You can run atomic operations on these types, like appending to a string; incrementing the value in a hash; pushing to a list; computing set intersection, union and difference; or getting the member with highest ranking in a sorted set.

# Redis is written in C and runs on most POSIX systems such as Linux, OS X, and Solaris. It is not officially supported on Windows, but it can be run on Windows if necessary.

# Example 1: Redis Connection
import asyncio
import aioredis

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    await redis.set('my-key', 'value')
    value = await redis.get('my-key', encoding='utf-8')
    print(value)
    redis.close()
    await redis.wait_closed()

asyncio.run(main())

# Example 2: Redis Message Queue
# Redis can be used as a message queue.
# It is a simple and reliable way to send and receive messages between different processes or applications.
# The producer sends messages to a queue, and the consumer listens for messages on that queue.
import asyncio
import aioredis

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    channel = (await redis.subscribe('my-channel'))[0]
    while await channel.wait_message():
        message = await channel.get(encoding='utf-8')
        print(message)

asyncio.run(main())

# Example 3: Redis Pub/Sub
# It is used for real-time messaging between clients. 
# It is useful for chat rooms, real-time notifications, and other real-time messaging use cases.
# The publisher sends messages to a channel, and the subscriber listens for messages on that channel.
import asyncio
import aioredis

async def main():
    """Simple Redis Pub/Sub example."""
    redis = await aioredis.create_redis_pool('redis://localhost')
    channel = (await redis.subscribe('my-channel'))[0]
    await redis.publish_json('my-channel', {'key': 'value'})
    message = await channel.get_json()
    print(message)


asyncio.run(main())

# Example 4: Redis Lock
# Redis can be used to implement distributed locks.
# It is a simple and reliable way to coordinate access to a shared resource between different processes or applications.
# The lock is acquired by one process and released by another process.
import asyncio
import aioredis

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    lock = await redis.lock('my-lock')
    await lock.acquire()
    # Do something with the lock.
    await lock.release()

asyncio.run(main())

# Example 5: Redis Cache
# Redis can be used as a cache to store and retrieve data.
# It is a simple and reliable way to speed up access to frequently accessed data.
import asyncio
import aioredis

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    await redis.set('my-key', 'value')
    value = await redis.get('my-key', encoding='utf-8')
    print(value)

asyncio.run(main())

# Example 6: Redis Sorted Set
# Redis can be used to store and retrieve sorted sets of data.
# It is a simple and reliable way to store and retrieve data in a sorted order.
import asyncio
import aioredis

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    await redis.zadd('my-set', 1, 'one')
    await redis.zadd('my-set', 2, 'two')
    values = await redis.zrange('my-set', 0, -1, encoding='utf-8')
    print(values)

asyncio.run(main())

# Example 7: Redis HyperLogLog
# Redis can be used to store and retrieve hyperloglogs of data.
# It is a simple and reliable way to store and retrieve data in a hyperloglog data structure.
import asyncio
import aioredis

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    await redis.pfadd('my-hll', 'a', 'b', 'c')
    count = await redis.pfcount('my-hll')
    print(count)

asyncio.run(main())

# Example 8: Using varoious redis database instances
import asyncio
import aioredis

async def main():
    redis1 = await aioredis.create_redis_pool('redis://localhost', db=0)
    redis2 = await aioredis.create_redis_pool('redis://localhost', db=1)
    await redis1.set('my-key', 'value')
    value = await redis2.get('my-key', encoding='utf-8')
    print(value)
    redis1.close()
    redis2.close()
    await redis1.wait_closed()
    await redis2.wait_closed()

asyncio.run(main())


# Example 9: Using Redis as a cache
import asyncio
import aioredis

async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    await redis.set('my-key', 'value')
    value = await redis.get('my-key', encoding='utf-8')
    print(value)
    redis.close()

asyncio.run(main())


# Example 10: Common Redis Commands
import asyncio
import aioredis

redis =  aioredis.create_redis_pool('redis://localhost')

# Set a key
redis.set(  'my-key',   'value')

# Get a key
redis.get('my-key')

# Delete a key
redis.delete( 'my-key' )

# Set a key with a timeout
redis.hset('my-hash', 'field', 'value')

# Get a key from a hash
redis.hget('my-hash', 'field')

# Delete a key from a hash
redis.hdel('my-hash', 'field')

# Push a key to a list
redis.lpush('my-list', 'value')

# Get a key from a list
redis.lpop('my-list')

# Add a key to a set
redis.sadd('my-set', 'value')

# Get a key from a set
redis.spop('my-set')

# Add a key to a sorted set
redis.zadd('my-sorted-set', 1, 'one')

# Get a key from a sorted set
redis.zrange('my-sorted-set', 0, -1)

# Add a key to a hyperloglog
redis.pfadd('my-hll', 'a', 'b', 'c')

# Get the count of a hyperloglog
redis.pfcount('my-hll')

# Publish a message to a channel
redis.publish('my-channel', 'message')

# Subscribe to a channel
redis.subscribe('my-channel')

# Unsubscribe from a channel
redis.unsubscribe('my-channel')

# Acquire a lock
redis.lock('my-lock')

# Release a lock
redis.unlock('my-lock')

# Close the connection
redis.close()

# Wait for the connection to close
redis.wait_closed()



