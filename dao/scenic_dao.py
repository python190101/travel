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


    def s_detail(self,id):
        sql = """
                 select scenics.img,scenics.name,scenics.price,scenics.satisfaction,scenic_detail.pro_code,
                 scenic_detail.pro_cha,scenic_detail.expense_exp,scenic_detail.id
                 from scenics
                 inner join scenic_detail
                 on scenics.id = scenic_detail.scenic_id
                 where scenics.id=%s
                 """ % (id,)
        items = ScenicDao.baselist(sql)
        return items


    def scenic_city_list(self,city_id,scenic_type):
        sql = "select id,name,img,people_num,price,satisfaction from scenics" \
              "where city_id=%s and scenic_type=%s" % (city_id,scenic_type)
        items = ScenicDao.baselist(sql)
        return items

    def sort_list(self,city_id,scenic_type,code):
        if code == 1:  # 销量排序
            sql = "select id,name,img,people_num,price,satisfaction from scenics" \
                  "where city_id=%s and scenic_type=%s order by people_num" % (city_id,scenic_type)
        elif code == 2:  # 满意度
            sql = "select id,name,img,people_num,price,satisfaction from scenics" \
                  "where city_id=%s and scenic_type=%s order by satisfaction" % (city_id,scenic_type)
        elif code == 3:  # 价格从高到低
            sql = "select id,name,img,people_num,price,satisfaction from scenics" \
                  "where city_id=%s and scenic_type=%s order by price desc" % (city_id,scenic_type)
        elif code == 4:  # 价格从低到高
            sql = "select id,name,img,people_num,price,satisfaction from scenics" \
                  "where city_id=%s and scenic_type=%s order by price" % (city_id,scenic_type)
        else:  # 默认排序
            sql = "select id,name,img,people_num,price,satisfaction from scenics" \
                  "where city_id=%s and scenic_type=%s" % (city_id,scenic_type)
        items = ScenicDao.baselist(sql)
        return items

    def scenic_homepage(self, num1, num2):
        sql = "select * from scenics where type=%s and code =%s" % (num1, num2)
        items = ScenicDao.baselist(sql)
        return items