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
        nol_city = {}
        for i in range(1, 27):
            i = i + 96
            nol_list = []
            for item in items:
                if item["city_code"].startswith(chr(i)):
                    nol_list.append(item["name"])
                if item["is_popular"] == 1 and item["country_id"] == 1:
                    if item["name"] not in pop_city:
                        pop_city.append(item["name"])
            if nol_list:
                nol_city[chr(i-32)] = (nol_list)
        return pop_city,nol_city

    def dim_list(self,cityname):
        api_logger.info('db insert tn_user: <%s>' % cityname)
        data = []
        sql = "select name from cities where name like '%%{}%%'".format(cityname,)
        items = CityDao.baselist(sql)

        if items:
            for item in items:
                data.append(item["name"])
            return data
        else:
            sql = "select name from cities where city_code like '{}%%'".format(cityname)
            items = CityDao.baselist(sql)
            if items:
                for item in items:
                    data.append(item["name"])
                return data

    def city_name(self,cityid):
        api_logger.info('db insert tn_user: <%s>' % "查询城市名字")
        sql = "select name from cities where id=%s" % cityid
        items = CityDao.baselist(sql)
        return items

    def elegant_city(self):
        dao = BaseDao()
        city_list = ["当季精选", "海岛精选", "热门目的地"]
        city_dict = {}

        for i in range(len(city_list)):
            sql = "select name,img from cities where is_popular='%s'" % (str(i + 2),)
            with dao.db as c:
                c.execute(sql)
                items = c.fetchall()
                city_dict[city_list[i]] = items
        return city_dict