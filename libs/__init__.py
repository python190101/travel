from redis import Redis


# 121.199.63.71


r = Redis(host="localhost",port=6379,db=1)

def save_token(token, user_id):
    # 保存token
    r.set(token, user_id)
    r.expire(token, 12*3600)  # 有效时间： 12小时

def check_token(token):
    # 验证token
    return r.exists(token)

