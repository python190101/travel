from dao import BaseDao
from logger import api_logger


class UserDaoDetail(BaseDao):

    def save(self, **values):
        api_logger.info('db insert user_detail: <%s>' % values['real_name', 'birth',])
        super(UserDaoDetail, self).save('user_detail', **values)

    def get_c(self, p_num):
        # 获取用户的详细信息
        sql = """
                select tn_user.p_num,
                from tn_user
                inner join user_detail
                on tn_user.id = user_detail.user_id
                where tn_user.p_num=%s
                """ % p_num
        with self.db as c:
            c.execute(sql)
            user_detail = c.fetchall()
            return user_detail

    def update_c(self, **values):
        sql3 = """
                      update  user_detail.birth,user_detail.real_name,user_detail.sex,
                user_detail.job,tn_user_email,user_detail.address
                      inner join user_detail
                      on tn_user.id = user_detail.user_id
                      set tn_user.email='%s',user_detail.birth='%s',user_detail.real_name='%s'
                      where tn_user.p_num=%s
                      """ % (values['email'], values['birth'], values['real_name'], values['p_num'])
        with self.db as c:
            c.execute(sql3)

        return "更新数据成功"
