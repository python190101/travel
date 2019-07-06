from redis import Redis


# 121.199.63.71


r = Redis(host="121.199.63.71", port=6370,db=1)

def save_token(token, p_num):
    # 保存token
    r.set(token, p_num)
    r.expire(token, 12*3600)  # 有效时间： 12小时

def check_token(token):
    # 验证token
    return r.exists(token)

