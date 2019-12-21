

# 从代理池中随机取出一个代理
from mongo import MongoDB

mon = MongoDB()

count = mon.get_count()

get_ip = True

while get_ip:

    ip_url = mon.get(count)

    if ip_url:
        get_ip = False

    count = mon.get_count()

mon.close_mongo()


print(ip_url)
