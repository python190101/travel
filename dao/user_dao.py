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
    def p_num_check(self,user_id):
        sql = "select p_num from tn_user where user_id='%s'" % user_id
        with self.db as c:
            c.execute(sql)
            p_num = c.fetchone()
            return p_num