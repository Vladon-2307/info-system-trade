import datetime
import os
import json

from pymysql import Connect
from sqlalchemy import create_engine, MetaData, Column, String, DateTime, Integer, Table, select, null
from sqlalchemy.orm import Session

# connectUrl = "mysql+pymysql://crmtrade:00crmtrade00@localhost:3306/crm_trade"
# basePath = "\\\\Vlad-asup2\клиенты\\"

connectUrl = ""
basePath = ""

with open('config.json', 'r', encoding='utf-8') as file:
    config = json.loads(str(file.read()))
    connectUrl = config.get("connectUrl")
    basePath = config.get("basePath")


engine = create_engine(connectUrl)
metadata = MetaData()



Counterparties = Table(
    'counterparties',
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("account_number", String(255), nullable=True),
    Column("bank_name", String(255), nullable=True),
    Column("code_bank", String(255), nullable=True),
    Column("legal_address", String(255), nullable=True),
    Column("mailing_address", String(255), nullable=True),
    Column("phone", String(255), nullable=True),
    Column("email", String(255), nullable=True),
    Column("unn", String(255), nullable=True),
    Column("okpo", String(255), nullable=True),
    Column("last_call_date", DateTime, nullable=True),
    Column("dir_name", String(255), nullable=True),
)

def getById(id: int):
    with Session(engine) as connection:
        query = Counterparties.select().where(Counterparties.c.id == id)
        res = connection.execute(query).first()
        return res

def getData(search: str = '', sort: bool = False):

    base = Counterparties.select().with_only_columns([Counterparties.c.id, Counterparties.c.name, Counterparties.c.phone, Counterparties.c.email, Counterparties.c.last_call_date])
    query = base.order_by(Counterparties.c.name)
    with Session(engine) as connection:
        if search != '' and sort==False:
            query = base.where(Counterparties.c.name.like("%"+search+"%")).order_by(Counterparties.c.name)
        elif search != '' and sort == True:
            query = base.where(Counterparties.c.name.like("%" + search + "%"), Counterparties.c.last_call_date.is_not(null())).order_by(
                Counterparties.c.last_call_date)
        elif search == '' and sort == True:
            query = base.where(Counterparties.c.last_call_date.is_not(null())).order_by(
                Counterparties.c.last_call_date)

        res = connection.execute(query).all()
        return res

def delete(id: int):
    with Session(engine) as connection:
        query = Counterparties.delete().where(Counterparties.c.id == id)
        connection.execute(query)
        connection.commit()
        return True

def create(name, account_number, bank_name, code_bank, legal_address, mailing_address, phone, email, unn, okpo):
    with Session(engine) as connection:
        query = Counterparties.select(Counterparties.c.id).where(Counterparties.c.name == name, Counterparties.c.unn == unn)
        res = connection.execute(query).all()
        if len(res) != 0:
            return (False, 'Контрагент с таким названием и УНН уже существует')

        insert_query = Counterparties.insert().values(name=name, account_number=account_number,
                                               bank_name=bank_name, code_bank=code_bank, legal_address=legal_address,
                                               mailing_address=mailing_address, phone=phone, email=email,
                                               unn=unn, okpo=okpo)
        connection.execute(insert_query)
        connection.commit()
        return (True, '')

def update(id, name, account_number, bank_name, code_bank, legal_address, mailing_address, phone, email, unn, okpo):
    with Session(engine) as connection:
        query = Counterparties.select(Counterparties.c.id).where(Counterparties.c.name == name,
                                                                 Counterparties.c.unn == unn,
                                                                 Counterparties.c.id != id)
        res = connection.execute(query).all()
        if len(res) != 0:
            return (False, 'Контрагент с таким названием и УНН уже существует')

        update_query = Counterparties.update().where(Counterparties.c.id == id).values(name=name, account_number=account_number,
                                                      bank_name=bank_name, code_bank=code_bank,
                                                      legal_address=legal_address,
                                                      mailing_address=mailing_address, phone=phone, email=email,
                                                      unn=unn, okpo=okpo)
        connection.execute(update_query)
        connection.commit()
        return (True, '')

def initDir(id: int, dir_name: str):
    with Session(engine) as connection:
        query = Counterparties.select().where(Counterparties.c.id == id)
        res = connection.execute(query).all()
        if res[0]["dir_name"] != '' and res[0]["dir_name"] != None:
            return (False, 'У контрагента уже существует дериктория')
        isDir = os.path.exists(basePath + dir_name)
        if isDir == True:
            return (False, 'Такая дериктория существует')
        os.mkdir(basePath + dir_name)
        update_query = Counterparties.update().where(Counterparties.c.id == id).values(dir_name = dir_name)
        connection.execute(update_query)
        connection.commit()
        return (True, '')


def getFiles(dirName):
    files = os.listdir(basePath + dirName)
    return files

def updateCallDate(id: int):
    with Session(engine) as connection:
        date = datetime.datetime.now()
        update_query = Counterparties.update().where(Counterparties.c.id == id).values(last_call_date=date)
        connection.execute(update_query)
        connection.commit()
        return True