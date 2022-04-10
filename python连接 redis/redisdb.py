import redis


def main():
    r = redis.StrictRedis(host="127.0.0.1",decode_responses="UTF-8")
    r.set("键值对","这是一个普通的值")
    print(r.get("键值对"))

    print("从前有一个hash名叫小哈,他走在放学的路上")
    r.hmset("hash",{"姓名":"小哈","类型":"hash",'状态':"疲惫ing","金钱":0})
    print(r.hgetall("hash"))
    print("突然,小哈捡到了50元钱,Lucky~")
    r.hincrby("hash","金钱",amount=50)
    r.hset("hash","状态","狂喜ing")
    print(r.hgetall("hash"))

    print("小哈有一个同学叫小李,他很富有")
    r.delete("list")
    r.rpush("list",'小李','有','钱')
    print(r.lrange("list",0,-1))
    print("有一天,小李做了点生意,于是")
    r.linsert("list","before","钱","很多")
    print(r.lrange("list",0,-1))
    print("后来,小李买彩票中了两个亿,于是他富有得只剩下钱了")
    r.ltrim("list",3,3)
    print(r.lrange("list",0,-1))
    print("最后,小李过于装B,被人发现彩票中奖是通过非法攻击获得的,最终什么也没有了")
    r.lrem("list", 0, "钱")
    print(r.lrange("list", 0, -1))


    print("小哈和小李的班里面,有一个很随便的人,叫小赛")
    r.delete("sadd")
    r.sadd("set",'小赛','非常','的','随便')
    print(r.smembers("set"))

    print("不过他们三人有一个共识,就是要好好学习,多读书,少睡觉,不要玩游戏")
    r.zadd("zset",mapping={"读书":10,"睡觉":5,"打游戏":1})
    for i in r.zscan_iter("zset"):
        print(i)

    print("当小李有钱的时候,他的zset就堕落了")
    r.zincrby("zset",amount=-9,value="读书")
    r.zincrby("zset", amount=9,value="打游戏")

    for i in r.zscan_iter("zset"):
        print(i)
if __name__ == '__main__':
    main()