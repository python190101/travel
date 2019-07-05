from dao import BaseDao
from logger import api_logger


class UserDetailDao(BaseDao):


    def get_c(self, p_num):
        # 获取用户的详细信息
        sql = """
                select tn_user.p_num,
                from tn_user
                inner join user_detail
                on tn_user.id = user_detail.user_id
                where tn_user.p_num=%s
                """ % p_num
        with self.db as c:
            c.execute(sql)
            user_detail = c.fetchall()
            return user_detail
