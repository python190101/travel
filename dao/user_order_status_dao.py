from dao import BaseDao
from logger import api_logger

class UserStatusOrderDao(BaseDao):

    @classmethod
    def baselist(cls, sql):
        dao = BaseDao()
        with dao.db as c:
            c.execute(sql)
            items = c.fetchall()
            api_logger.info('select %s ok!' % sql)
        return items

    def all_order(self,p_num):
        sql = """
               select tn_user.p_num,tn_order.code,tn_order.price,
               tn_order.start_time,tn_order.order_time,tn_order.order_status,
               tn_order.scenic_id
               from tn_user
               inner join tn_order
               on tn_user.id = tn_order.user_id
               where tn_user.p_num=%s
               """ % p_num
        items = UserStatusOrderDao.baselist(sql)
        return items

    def check_oreder1(self,p_num):
        sql = """ 
                select tn_user.p_num,tn_order.code,tn_order.price,
                tn_order.start_time,tn_order.order_time,tn_order.scenic_id
                from tn_user
                inner join tn_order
                on tn_user.id = tn_order.user_id
                where tn_user.p_num=%s and tn_order.order_status=1
                """ % p_num
        items = UserStatusOrderDao.baselist(sql)
        return items

    def check_oreder2(self,p_num):
        sql = """ 
                select tn_user.p_num,tn_order.code,tn_order.price,
                tn_order.start_time,tn_order.order_time,tn_order.scenic_id
                from tn_user
                inner join tn_order
                on tn_user.id = tn_order.user_id
                where tn_user.p_num=%s and tn_order.order_status=0
                """ % p_num
        items = UserStatusOrderDao.baselist(sql)
        return items