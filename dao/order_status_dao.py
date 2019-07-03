from dao import BaseDao
from logger import api_logger


class OrderStateDao(BaseDao):

    @classmethod
    def query(cls,sql):
        dao = BaseDao()
        with dao.db as c:
            c.execute(sql)
            items = c.fetchall()
            api_logger.info('select %s ok!' % sql)
        return items

    def order_status(self):
        sql = 'update tn_order set order_status=1'

        items = OrderStateDao.query(sql)
        return "下单成功"