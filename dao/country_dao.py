from dao import BaseDao
from logger import api_logger

class CountryDao(BaseDao):

    def tn_list(self, table_name,
             *fields, where=None, args=None,
             page=1, page_size=20):
        api_logger.info('db insert tn_user: <%s>' % table_name)
        items = super(CountryDao, self).tn_list(table_name)
        return items

    def type_list(self,countryid):
        api_logger.info('db insert tn_user: <%s>' % "类型查询")
        sql = "select * from cities where country_id=%s and is_popular=1" % countryid
        with self.db as c:
            c.execute(sql)
            items = c.fetchall()
        return items