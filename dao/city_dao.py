from dao import BaseDao
from logger import api_logger

class CityDao(BaseDao):

    @classmethod
    def baselist(cls,sql):
        dao = BaseDao()
        with dao.db as c:
            c.execute(sql)
            items = c.fetchall()
            api_logger.info('select %s ok!' % sql)
        return items


    def city_list(self):

        api_logger.info('db insert tn_user: <%s>' % "查询城市")
        sql = "select * from cities"
        items = CityDao.baselist(sql)
        pop_city = []
        nol_city = []
        for i in range(1, 27):
            i = i + 96
            nol_list = []
            for item in items:
                if item["code"].startswith(chr(i)):
                    nol_list.append(item["name"])
                if item["is_popular"] == 1:
                    if item["name"] not in pop_city:
                        pop_city.append(item["name"])
            if nol_list:
                nol_city.append(nol_list)
        return pop_city,nol_city

    def dim_list(self,cityname):
        api_logger.info('db insert tn_user: <%s>' % cityname)
        sql = "select name from cities where name like '%%{}%%'".format(cityname,)
        items = CityDao.baselist(sql)
        data = []
        if items:
            for item in items:
                data.append(item["name"])
            return data
        else:
            sql = "select name from cities where code like '{}%%'".format(cityname)
            items = CityDao.baselist(sql)
            if items:
                for item in items:
                    data.append(item["name"])
                return data

