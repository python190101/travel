from dao import BaseDao
from logger import api_logger

class UserDao(BaseDao):

    def save(self, **values):
        api_logger.info('db insert tn_user: <%s>' % values['p_num'])
        super(UserDao, self).save('tn_user', **values)

    def tn_list(self,*fields):
        api_logger.info('db insert tn_user: <%s>' % fields[0])
        sql = "select * from %s where p_num='%s' or email='%s' or user_name='%s'" % ('tn_user',fields[0],fields[0],fields[0])
        with self.db as c:
            c.execute(sql)
            item = c.fetchone()
            api_logger.info('select %s ok!' % sql)
        if item:
            if item["is_active"] == 1:
                if item["password"] == fields[1]:
                    return item
                else:
                    return 2
            else:
                return 4
        else:
            return 3


    def p_list(self,p_num):
        sql = "select p_num from tn_user where p_num='%s'" % p_num
        with self.db as c:
            c.execute(sql)
            number = c.fetchone()
        return number

    def user_id_list(self,p_num):
        sql = "select id from tn_user where p_num='%s'" % p_num
        with self.db as c:
            c.execute(sql)
            user_id = c.fetchone()[0]["id"]
            return user_id

    def update_pwd(self,password):
        sql = "update tn_user set password=%s" % password
        with self.db as c:
            c.execute(sql)
        api_logger.info('update %s ok!' % sql)

    def p_num_check(self, user_id):
        sql = "select p_num from tn_user where user_id=%s" % user_id
        with self.db as c:
            c.execute(sql)
            p_num = c.fetchone()[0]["p_num"]
            return p_num