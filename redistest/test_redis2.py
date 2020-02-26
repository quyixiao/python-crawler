import redis

r = redis.Redis(host='172.16.157.238', password='Hello1234', port=6379, db=9)

r.zadd('mboard', 'yellow', 1, 'rolling in the deep')

r.zadd('mboard', 'eye of the tiger', 1, 'billie jean', 1, 'say you say me', 1, 'payphone', 1)
r.zadd('mboard', 'my heart will go on', 1, 'when you believe', 1, 'hero', 1)
r.zincrby('mboard', 'yellow', 50)
r.zincrby('mboard', 'rolling in the deep', 60)
r.zincrby('mboard', 'my heart will go on', 68.8)
r.zincrby('mboard', 'when you believe', 70)
# 所有元素
allmusic = r.zrange('mboard', 0, -1, withscores=True)
print(type(allmusic))
for m in allmusic:
    print(m)
print('-' * 30)
# 排行榜
musicboard = r.zrevrange('mboard', 0, 9, True)
print('欧美热曲榜')
for i, m in enumerate(musicboard):
    print(i, *m)
