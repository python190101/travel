from dao import BaseDao
from logger import api_logger


class DeleteOrderDao(BaseDao):

    @classmethod
    def baselist(cls, sql):
        dao = BaseDao()
        with dao.db as c:
            c.execute(sql)
            items = c.fetchall()
            api_logger.info('select %s ok!' % sql)
        return items

    def delete_order(self,p_num):
        dao = BaseDao()
        sql1 = "select id from tn_user  where p_num=%s"%p_num
        with dao.db as c:
            c.execute(sql1)
            user_id = c.fetchone()[0]["id"]
        sql2 = "delete tn_order from tn_order,tn_user where tn_order.user_id=%s"% user_id
        with dao.db as c:
            c.execute(sql2)