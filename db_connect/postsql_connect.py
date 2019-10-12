import psycopg2
import sqlalchemy
import pandas as pd

"""
simple example
"""
def simple_example():
    db_informations = {'ip': 'xxx.xxx.xxx.xxx', 'username': 'mdmp', 'passwd': 'mdmp', 'port': 5432, 'db': 'mdmp'}
    ''' pymysql '''
    conn = psycopg2.connect(host=db_informations['ip'], user =db_informations['username'], password =db_informations['passwd'], database =db_informations['db'],port=db_informations['port'])
    # conn.close()
    ''' sqlalchemy '''
    connstr = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (db_informations['username'],db_informations['passwd'],db_informations['ip'],db_informations['port'],db_informations['db'])
    print(connstr)
    db = sqlalchemy.create_engine(connstr, pool_size=20, max_overflow=100, pool_recycle=7200, echo=False)
    #db.close
    return conn,db
