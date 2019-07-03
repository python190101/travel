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



    def s_all(self):
        all_dict = {
            "为您推荐": {"全部": [], "心动迪士尼": [], "出游正当时": [], "去玩海岛游": [], "亲子度假": [], "放假日本": [], "欧美澳新": [], "省心邮轮季": []},
            "出境游": {"东南亚": [], "海岛": [], "日本": [], "欧洲": [], "中东非": [], "美洲": [], "澳新 ": [], "港澳台": []},
            "境内游": {"海南": [], "云南": [], "西北": [], "广西": [], "福建": [], "北京": [], "陕西": [], "湖南": []},
            "周边游": {"精选": [], "踏青赏花": [], "名山胜水": [], "城市/乐园": [], "古镇": [], "高铁/动车": [], "巴士自由行": [], "酒店+景点": []}}
        a = 1
        for k, v in all_dict.items():
            for i, j in all_dict[k].items():
                a += 1
                sql = "select scenic_id,name,price,img from scenics where type=%s" % (str(a))
                itmes = ScenicDao.baselist(sql)
                all_dict[k][i] = itmes
        return all_dict

    def s_detail(self,id):
        sql = """
                 select scenic.img,scenic.name,scenic.price,scenic.satisfaction,scenic_detail.pro_code,
                 scenic_detail.pro_cha,scenic_detail.expense_exp,scenic_detail.id
                 from scenic
                 inner join scenic_detail
                 on scenic.id = scenic_detail.scenic_id
                 where scenic.id=%s
                 """ %(id)
        items = ScenicDao.baselist(sql)
        return items