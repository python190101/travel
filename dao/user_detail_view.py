from dao import BaseDao
from logger import api_logger


class UserDaoDetail(BaseDao):

    def save(self, **values):
        api_logger.info('db insert user_detail: <%s>' % values['real_name', 'birth',])
        super(UserDaoDetail, self).save('user_detail', **values)

    def get_c(self, p_num):
        # 获取用户的详细信息
        sql = """
                select user.p_num,user_detail.birth,user_detail.real_name,user_detail.sex,user_detail.job
                from user
                inner join user_detail
                on user.id = user_detail.user_id
                where user.p_num=%s
                """ % p_num

        with self.db as c:
            c.execute(sql)
            user_detail = c.fetchall()
            return user_detail

    def update_c(self, **values):
        # sql1 = "update user_detail set birth= '%s',real_name='%s'"%(values['birth'],values['real_name'])
        # sql2 = "update  user  set email='%s' where p_num='%s'  "%(values['email'],values['p_num'])
        sql3 = """
                      update  user
                      inner join user_detail
                      on user.id = user_detail.user_id
                      set user.email='%s',user_detail.birth='%s',user_detail.real_name='%s'
                      where user.p_num=%s
                      """ % (values['email'], values['birth'], values['real_name'], values['p_num'])
        with self.db as c:
            c.execute(sql3)

        return "更新数据成功"

"""
                'p_num': p_num,
                 'photo': photo,

                 'sex': sex,
                 'marriage': marriage,
                 'education': education,
                 'job': job,
                 'address': address,
"""