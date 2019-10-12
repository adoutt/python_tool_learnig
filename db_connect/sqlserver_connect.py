import pymssql
import sqlalchemy
import pandas as pd

"""
simple example
"""
def simple_example():
    db_informations = {'ip': 'xxx.xxx.xxx.xxx', 'username': 'xxxx', 'passwd': 'xxxxxx', 'port': 1433, 'db': 'xxx'}
    ''' pymysql '''

    conn = pymssql.connect(host=db_informations['ip'], user =db_informations['username'], password =db_informations['passwd'], database =db_informations['db'],port=db_informations['port'], charset ='utf8')
    # conn.close()
    ''' sqlalchemy '''
    connstr = "mssql+pymssql://%s:%s@%s:%s/%s?charset=utf8" % (db_informations['username'],db_informations['passwd'],db_informations['ip'],db_informations['port'],db_informations['db'])
    print(connstr)
    db = sqlalchemy.create_engine(connstr, pool_size=20, max_overflow=100, pool_recycle=7200, echo=False)
    #db.close
    return conn,db