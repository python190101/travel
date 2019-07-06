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
        sql = "select name,city_id from %s where id=%s" % (table_name,scenicid)
        items = OrderDao.baselist(sql)
        return items

    def travel_type(self,lat,lon,scenicid):
        sql = "SELECT distances(%s,%s, lat, lon) AS dis FROM scenics WHERE id=%s" % (lat,lon,scenicid)
        items = OrderDao.baselist(sql)
        return items

    def order_list(self,order_code):
        sql = "SELECT id FROM tn_order WHERE code=%s" % order_code
        order_id = OrderDao.baselist(sql)[0]["id"]
        return order_id

    def scenic_insert(self,lals,scenicid):
        sql = "insert into scenic(lat,lon) values(%s,%s) where id=%s" % (lals[1],lals[0],scenicid)
        OrderDao.baselist(sql)
        return "OK"
