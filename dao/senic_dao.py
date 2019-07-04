from dao import BaseDao
from logger import api_logger

class ScenicDao(BaseDao):

    @classmethod
    def baselist(cls, sql):
        dao = BaseDao()
        with dao.db as c:
            c.execute(sql)
            items = c.fetchall()
            api_logger.info('select %s ok!' % sql)
        return items


    def scenic_homepage(self,num):
        sql = "select * from scenics where type=%s"%(num)
        items = ScenicDao.baselist(sql)
        return items


    def s_detail(self,id):
        sql = """
                 select scenic.img,scenic.name,scenic.price,scenic.satisfaction,scenic_detail.pro_code,
                 scenic_detail.pro_cha,scenic_detail.expense_exp,scenic_detail.id
                 from scenic
                 inner join scenic_detail
                 on scenic.id = scenic_detail.scenic_id
                 where scenic.id=%s
                 """ %(id,)
        items = ScenicDao.baselist(sql)
        return items