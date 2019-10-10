import cx_Oracle as cx
import sqlalchemy
import  pandas as pd
"""
simple example
"""

def simle_example():
   db_informations={'ip':'xxx.xxx.xxx.xxx','username':'yiwu','passwd':'yiwu','port':1521,'orcl':'ora11g'}
   '''cx_oracle connect'''
   Connection_string='192.168.239.8:1521/ora11g'.format(db_informations['ip'],db_informations['port'],db_informations['orcl'])
   conn=cx.connect(db_informations['username'],db_informations['passwd'],Connection_string)
   '''sqlalchemy connect'''
   connstr = "oracle+cx_oracle://%s:%s@%s:%s/%s" % ( db_informations['username'], db_informations['passwd'], db_informations['ip'], db_informations['port'], db_informations['orcl'])
   db = sqlalchemy.create_engine(connstr, echo=False)#true will echo executing sql
   return conn,db
"""
tns example
"""
def tns_services():
    db_informations = {'ip': 'xxx.xxx.xxx.xxx', 'username': 'yiwu', 'passwd': 'yiwu', 'port': 1521, 'orcl': 'ora11g'}
    oracle_tns = cx.makedsn(db_informations['ip'],db_informations['port'],db_informations['orcl'])
    '''cx_oracle connect'''
    conn = cx.connect(db_informations['username'],db_informations['passwd'],oracle_tns)
    '''sqlalchemy connect'''
    connstr = 'oracle://{user}:{password}@{sid}'.format(
        user=db_informations['username'],
        password=db_informations['passwd'],
        sid=oracle_tns)
    db = sqlalchemy.create_engine(connstr, echo=False)  # true will echo executing sql
    return conn, db
