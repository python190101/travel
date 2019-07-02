from dao import BaseDao
from logger import api_logger

class OrderDao(BaseDao):

    @classmethod
    def baselist(cls, sql):
        dao = BaseDao()
        with dao.db as c:
            c.execute(sql)
            items = c.fetchall()
            api_logger.info('select %s ok!' % sql)
        return items

    def price_list(self,table_name,scenicid):
        sql = "select date,price from %s where scenic_id=%s" % (table_name,scenicid)
        items = OrderDao.baselist(sql)
        return items

    def scenic_list(self,table_name,scenicid):
        sql = "select name from %s where id=%s" % (table_name,scenicid)
        items = OrderDao.baselist(sql)
        return items

    def ticket_list(self):
        sql = "select start_time,end_time,start_point,end_point from tickets where ticket_type=1"
        items = OrderDao.baselist(sql)
        return items
